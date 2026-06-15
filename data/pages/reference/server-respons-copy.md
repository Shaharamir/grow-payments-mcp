---
title: "Server-to-Server Callback"
slug: server-respons-copy
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/server-respons-copy
---

# Server-to-Server Callback

> Transaction Status Update via Webhook for CreatePaymentLink

An HTTPS callback will be sent to your server to notify the completion of the transaction.

The callback will be made to the endpoint URL specified in the **notifyUrl** parameter of the [CreatePaymentLink](https://grow-il.readme.io/reference/post_api-light-server-1-0-createpaymentlink)  API request.

Upon receiving the update, you are required to execute the [ApproveTransaction](https://grow-il.readme.io/reference/post_api-light-server-1-0-approvetransaction-1)  API call.  
This call serves as an acknowledgment that your system has received the server notification and is aware of the transaction status.

**Please note:** The transaction will be processed even if the [ApproveTransaction](https://grow-il.readme.io/reference/post_api-light-server-1-0-approvetransaction-1)  request is not executed or fails.

  

JSON

```
{
    "err": "",
    "status": "1",
    "data": {
        "status": "שולם",
            "statusCode": "2",
            "transactionTypeId": "1",
            "paymentType": "2",
            "sum": "100",
            "paymentsNum": "0",
            "allPaymentsNum": "1",
            "paymentDate": " 05/6/25",
            "description": " דרישת תשלום  טיפול יופי",
            "fullName": "ישראל ישראלי",
            "payerPhone": " 0500000000",
            "payerEmail": "test@test.com",
            "transactionId": "421100",
            "transactionToken": "29d52adf037112121ea99be5c3ce90b9",
            "paymentLinkProcessId": "12128",
            "paymentLinkProcessToken": "0e515e412128b401f56c791b068b7f77e",
            "asmachta": "117128222",
        "cardSuffix": "4880",
        "cardType": "Foreign",
        "cardTypeCode": "2",
        "cardBrand": "Visa",
        "cardBrandCode": "3",
        "cardExp": "1127",
        "firstPaymentSum": "0",
        "periodicalPaymentSum": "0",
        "payerBankAccountDetails": "",
        "productData": [{
                             "product_id": "9767",
                             "name" : "חבילת טיפול יופי",
                             "catalog_number": "1",
                             "vat": "1",
                             "quantity": "1",
                             "price": "100",
                            "sum": "100",
                            "price_mark": "0"
        }
        ],
        "processId": " 512895",
        "processToken": " 3e747881212e6dd36d43e6f0072dc7049",
        "customFields": " Array"
    }
}
```

  
  

# Testing the Server-to-Server Callback

You can test the server-to-server callback using the [updateMyUrl](https://sandbox.meshulam.co.il/api/light/server/1.0/updateMyUrl/?url=MySiteURL)  endpoint.

This GET request simulates the callback notification by sending an HTTP request to the URL you specify.

Replace **MySiteURL** with your server's endpoint to test how it handles incoming callback data.

This tool allows you to debug the integration and verify your server’s handling of incoming notifications, including any logging as needed.

<https://sandbox.meshulam.co.il/api/light/server/1.0/updateMyUrl/?url=MySiteURL>
