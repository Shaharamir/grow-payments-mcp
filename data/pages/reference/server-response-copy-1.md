---
title: "Server response"
slug: server-response-copy-1
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/server-response-copy-1
---

# Server response

Updating the server with the transaction's status and details would be performed by an HTTPS API method that you will be providing us when calling to create a payment process, in the ***notifyUrl*** param.

This URL is an endpoint in your site, which Grow's server will call to update you about the transaction. When received this call (you could save data to DB etc. and then) you should call [ApproveTransaction](https://grow-il.readme.io/reference/post_api-light-server-1-0-approvetransaction-1).

The method takes in parameters as an **HTTP POST**, the same way as you would send the data to the [CreatePaymentProcess](https://grow-il.readme.io/reference/post_api-light-server-1-0-createpaymentprocess-1) method and ***NOT as JSON***.

**Please note:** *The payment will go through even if you did not[Approve Transaction](https://grow-il.readme.io/reference/post_api-light-server-1-0-approvetransaction).*

JSON

```
 {
        "err": "",
        "status": "1",
        "data": {
            "cardSuffix": "1234",
            "cardType": "Local",
            "cardTypeCode": "1",
            "cardBrand": "Visa",
            "cardBrandCode": "3",
            "cardExp": "1125",
            "firstPaymentSum": "0",
            "periodicalPaymentSum": "0",
            "status": "עסקה מושהית",
            "statusCode": "11",
            "transactionTypeId": "1",
            "paymentType": "2",
            "sum": "1",
            "paymentsNum": "1",
            "allPaymentsNum": "1",
            "paymentDate": "19/10/23",
            "description": "תיאור",
            "fullName": "בדיקה GROW",
            "payerPhone": "0500000000",
            "payerEmail": "",
            "cardToken": "9294decf1dg5g2g5g2g5g2g58fd286",
            "transactionId": "287377",
            "transactionToken": "4e6ca0b42e5ca8f35563cg2g517ed5e",
            "processId": "462950",
            "processToken": "e2202e3c9ffaaf65de1g2g53fbad5e9d"
        }
    }
```

JSON

```
"status": 0,
    "err": {
        "id": 701,
        "message": "פרמטר קוד זיהוי אינו תקין userId"
    },
    "data": ""
```

- **status** is referred to success or failure (1 or 0 respectively).
- **err** - in case of an error, would return as the error code and error message.
- **data** - all the details would return here.

# Test

If you wish to test this call you can use **updateMyUrl** function.

This is a *Get* function that simulates our server-to-server call. You need to insert your server address in the URL.

This will help you debug the service, and/or insert logs if necessary.

<https://sandbox.meshulam.co.il/api/light/server/1.0/updateMyUrl/?url=MySiteURL>
