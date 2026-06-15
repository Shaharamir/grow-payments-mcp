---
title: "NFC"
slug: nfc-1
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/nfc-1
---

# NFC

**Procedure for Setting Up the NFC Service:**

- Download the Grow application from Google Play Store.
- Purchase the service and notify us to receive the code for your device.
- Send this code as a parameter in the "createPaymentProcess" call under the name "deviceKey."
- In transaction broadcasts to the device, use the unique pageCode for this transaction provided by the Grow service.

**Steps to Perform a Transaction:**

1. Execute a "createPaymentProcess" call with the designated "pageCode" for the transaction and the "deviceKey" of the selected broadcasting device.
2. Open the URL sent after the call where transaction details will appear on the application screen.

**Opening the URL - Important Notes:**

1. Before making the call, ensure our application is open on the home page, in a waiting state.  
   For example

![](https://files.readme.io/88e3b2e-WhatsApp_Image_2023-11-05_at_13.15.21_cc4ca549.jpg)

2. After making the "createPaymentProcess" call, you will receive a URL in response.  
   This URL should be opened and not closed until the process is completed !  
   In other words, the link received from the call should be opened on a device separate from the one where the application is open and should remain open until the transaction is finished.  
   The next screen must remain open:

![](https://files.readme.io/ef84633-image.png)

3. Credit card pairing transactions (pairing a credit card to the back of the phone) are limited to an amount of up to 300 NIS. Digital wallet pairing transactions (phone-to-phone) have no amount limitations.
4. Business owners can broadcast to multiple devices, meaning they should be able to select from a list which device they want to broadcast to, with support for multiple device keys.

**The application screen during transmission:**

NOTE:

> 📘
>
> ### Important Note:
>
> 1. Broadcasting to an active device should only be done within the live environment.  
>    After Transaction:
> 2. Receive an update from the server confirming that the transaction was successfully completed.
> 3. Initiate a call to "approve" that updates you upon receiving the server's update, indicating awareness of the transaction.
> 4. For business owners, the ability to broadcast to multiple devices is supported. They can select from a list which device they want to broadcast to, with support for multiple device keys.


## Images

- https://files.readme.io/88e3b2e-WhatsApp_Image_2023-11-05_at_13.15.21_cc4ca549.jpg
- https://files.readme.io/ef84633-image.png