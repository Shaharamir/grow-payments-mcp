---
title: "Server-to-Server Callback"
slug: server-response-copy
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/server-response-copy
---

# Server-to-Server Callback

> Transaction Status Update via Webhook for CreatePaymentProcess

An HTTPS callback will be sent to your server to notify the completion of the transaction.  
The method takes in parameters as an HTTP POST, the same way as you would send the data to the CreatePaymentProcess method and NOT as JSON.

The callback will be made to the endpoint URL specified in the **notifyUrl** parameter of the [createPaymentProcess](https://grow-il.readme.io/reference/post_api-light-server-1-0-createpaymentprocess-5)  API request.

JSON

```
{
    "err": "",
    "status": "1",
    "data": {
        "cardSuffix": "3253",
        "cardType": "Local",
        "cardTypeCode": 1,
        "cardBrand": "Visa",
        "cardBrandCode": 3,
        "cardExp": "0524",
        "firstPaymentSum": 0,
        "periodicalPaymentSum": 0,
        "status": "עסקה מושהית",
        "statusCode": 11,
        "transactionTypeId": 1,
        "paymentType": 2,
        "sum": 1,
        "paymentsNum": 1,
        "allPaymentsNum": 1,
        "paymentDate": "09/1/24",
        "description": "description",
        "fullName": "TEST TEST",
        "payerPhone": "0500000000",
        "payerEmail": "test@test.co.il",
        "customFields": [],
        "transactionId": 301770,
        "transactionToken": "62aec6d32197fbb654152eee5c41728f",
        "processId": 477278,
        "processToken": "b350a1924f8cbd7ae2d31fc9ae3304b0"
    }
```

# Testing the Server-to-Server Callback

You can test the server-to-server callback using the [updateMyUrl](https://sandbox.meshulam.co.il/api/light/server/1.0/updateMyUrl/?url=MySiteURL)  endpoint.

This GET request simulates the callback notification by sending an HTTP request to the URL you specify.

Replace **MySiteURL** with your server's endpoint to test how it handles incoming callback data.

This tool allows you to debug the integration and verify your server’s handling of incoming notifications, including any logging as needed.

<https://sandbox.meshulam.co.il/api/light/server/1.0/updateMyUrl/?url=MySiteURL>
