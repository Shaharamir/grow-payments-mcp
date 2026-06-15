---
title: "Growin SDK"
slug: page
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/page
---

# Growin SDK

Growin SDK adds a modern checkout experience that feels like a payment wallet, without redirects or separate payment pages.
It unifies payment methods like credit card, bit, Apple Pay, Google Pay, PayBox, and bank transfer in one flow.
The form adapts to the site design, helping create a smoother payment experience and improve conversion.
After the SDK is loaded, checkout starts with a wallet payment process, returns an authCode, and opens the payment options.
Real-time events keep the payment status clear from start to success, failure, cancellation, or form changes.

> 📘
>
> ### NOTE:
>
> 1. The SDK must be used together with the server-side [createPaymentProcess](https://grow-il.readme.io/reference/post_api-light-server-1-0-createpaymentprocess-1**)  method,  
>    configured with a **pageCode** that is set to Wallet SDK mode.
> 2. The wallet session becomes valid as soon as you call the backend [createPaymentProcess](https://grow-il.readme.io/reference/post_api-light-server-1-0-createpaymentprocess-1) API.  
>    To avoid timeouts during checkout, make this call only immediately before rendering the wallet.
> 3. All scripts must be embedded on the frontend of the checkout page.

### **Integration steps :**

1. Begin by loading the SDK into your webpage as shown below:

   HTML

   ```
   <script>
      (function () {
        var s = document.createElement('script');
        s.type = 'text/javascript';
        s.async = true;
        s.src = 'https://cdn.meshulam.co.il/sdk/gs.min.js';
        s.onload = configureGrowSdk; //replace with your callback function
        var x = document.getElementsByTagName('script')[0];
        x.parentNode.insertBefore(s, x);
      })();
    </script>
   ```
2. The scripts **'onload'** event should call a function that initializes and configures the wallet:

   JavaScript

   ```
   function configureGrowSdk() {
   	let config = {
   		environment: "DEV",
   		version: 1,
   		events: {
   			onSuccess: (response) => {},
   			onFailure: (response) => {},
   			onError: (response) => {},
   			onTimeout: (response) => {},
   			onWalletChange: (state) => {},
   			onPaymentStart: (response) => {},
   			onPaymentCancel: (response) => {},
          }
      };
   	growPayment.init(config);
   }
   ```

| Name | Type | Required | Options | Description | Response Examples |
| --- | --- | --- | --- | --- | --- |
| environment | String | required | “PRODUCTION”, “DEV” |  |  |
| version | String | required | Current stable version is 1 | Target the preferred base version |  |
| events | Object | optional | onSuccess: Gets triggered on payment success, receives a response with information about the payment (confirmation number, payment method, and more).  onFailure: Gets triggered on payment failure, receives a message describing what caused the failure.  onError: Gets triggered on payment error, receives a message describing what caused the error.  onWalletChange: Gets triggered on wallet state change, receives the current wallet state - open/closed.  Note: useful for changing your loaders state.  onPaymentStart: Gets triggered when a payment process starts, receives a response with the triggered `paymentType` and `paymentName`.  onPaymentCancel: Gets triggered when a payment process is cancelled, receives a response with the triggered `paymentType` and `paymentName`. | Attach callback functions to handle each event type | onSuccess:  {  "status": 1,  "data": {  "payment_sum": "1",  "full_name": "example example",  "payment_method": "credit",  "number_of_payments": 1,  "confirmation_number": "12345678"  }  }  onFailure:  {  "status": 0,  "message": "תשלום נכשל"  }  onError:  {  "status": 0,  "message": "לא ניתן לבצע עסקת תשלומים על כרטיס מסוג זה"  }  {  "status": 0,  "message": "התשלום סורב"  }  onWalletChange:  open  Close  onPaymentStart:  {  "paymentType": 15,  "paymentName": "bank_transfer"  }  onPaymentCancel:  {  "paymentType": 15,  "paymentName": "bank_transfer"  } |

onSuccess events:

| payment method | Response Examples |
| --- | --- |
| bit | {  "status": 1,  "data": {  "payment_sum": "1",  "full_name": "example example",  "payment_method": "bit",  "number_of_payments": 1,  "confirmation_number": "12345678"  } |
| Google Pay | {  "status": 1,  "data": {  "payment_sum": "1",  "full_name": "example example",  "payment_method": "google",  "number_of_payments": 1,  "confirmation_number": "12345678"  } |
| Apple Pay | "status": 1,  "data": {  "payment_sum": "1",  "full_name": "example example",  "payment_method": "apple",  "number_of_payments": 1,  "confirmation_number": "12345678"  } |
| Credit Card | {  "status": 1,  "data": {  "payment_sum": "1",  "full_name": "example example",  "payment_method": "credit",  "number_of_payments": 1,  "confirmation_number": "12345678"  } |
| Bank Transfer | {  "status": 1,  "data": {  "payment_sum": "1",  "full_name": "example example",  "payment_method": "bank_transfer",  "number_of_payments": 1,  "confirmation_number": "12345678"  } |
| Pay Box | {  "status": 1,  "data": {  "payment_sum": "1",  "full_name": "example example",  "payment_method": "paybox",  "number_of_payments": 1,  "confirmation_number": "12345678"  } |

**Note:** The init method can also be used to update the entire SDK configuration. However, this will reset all previously registered events and replace them with the new ones provided.

3. Once the user clicks the checkout button (or any other payment trigger), call [createPaymentProcess](https://grow-il.readme.io/reference/post_api-light-server-1-0-createpaymentprocess-1)  on your server.  
   You’ll receive an **authCode**, which you can pass into **renderPaymentOptions** to display the wallet.

Below is a sample response returned by [createPaymentProcess](https://grow-il.readme.io/reference/post_api-light-server-1-0-createpaymentprocess-1)  when called with the wallet-specific **pageCode**.  
As shown, the response contains an **authCode** that is required to open the wallet.

JSON

```
{
  "status": 1,
  "err": "",
  "data": {
    "processId": 413133,
    "processToken": "92ab69240c00aa073eb818dc646e2c32",
    "authCode": "beb1064aa495042a69c9c5e2dc384180%NDEzMTM0"
  }
}
```

Here’s how you can use the **authCode** from [createPaymentProcess](https://grow-il.readme.io/reference/post_api-light-server-1-0-createpaymentprocess-1)  to render the wallet:

JavaScript

```
// response - the response you received from 'createPaymentProcess'
if (response.status && growPayment) {
   growPayment.renderPaymentOptions(response.authCode);
}
```

> 📘
>
> ### NOTE:
>
> 1. When **renderPaymentOptions** is invoked, the SDK initiates a request to the Grow backend before rendering the wallet UI.  
>    To properly handle loading states, listen for the **onWalletChange** event, which indicates that the wallet is about to open.

After opening the wallet, track the events configured in **configureGrowSdk** and monitor the server update to keep the payment flow in sync.
