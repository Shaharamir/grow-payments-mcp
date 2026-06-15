---
title: "Server-to-Server Callback"
slug: server-to-server-callback
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/server-to-server-callback
---

# Server-to-Server Callback

> Transaction Status Update via Webhook for CreatePaymentProcess

An HTTPS callback will be sent to your server to notify the completion of the transaction.  
The method takes in parameters as an HTTP POST, the same way as you would send the data to the CreatePaymentProcess method and NOT as JSON.

The callback will be made to the endpoint URL specified in the **notifyUrl** parameter of the [CreatePaymentProcess](https://grow-il.readme.io/reference/post_api-light-server-1-0-createpaymentprocess)  API request.

Upon receiving the update, you are required to execute the [ApproveTransaction](https://grow-il.readme.io/reference/post_api-light-server-1-0-approvetransaction)  API call.  
This call serves as an acknowledgment that your system has received the server notification and is aware of the transaction status.

**Please note:** The transaction will be processed even if the [ApproveTransaction](https://grow-il.readme.io/reference/post_api-light-server-1-0-approvetransaction)  request is not executed or fails.

JSON

```
    {
        "err": "",
        "status": "1",
        "data": {
            "asmachta": "0289199",
            "cardSuffix": "1177",
            "cardType": "Local",
            "cardTypeCode": "1",
            "cardBrand": "Mastercard",
            "cardBrandCode": "2",
            "cardExp": "0126",
            "firstPaymentSum": "0",
            "periodicalPaymentSum": "0",
            "status": "שולם",
            "statusCode": "2",
            "transactionTypeId": "6",
            "paymentType": "2",
            "sum": "269",
            "paymentsNum": "0",
            "allPaymentsNum": "1",
            "paymentDate": "21/12/21",
            "description": "TEST TEST",
            "fullName": "John Smith",
            "payerPhone": "0541234567",
            "payerEmail": "email@gmail.com",
            "transactionId": "145111110",
            "transactionToken": "c68d98D4c3f19b30hgy7362e9g5g5g5862",
            "processId": "332002",
            "processToken": "f01644c3f19b30h825eg5g5g5g3b0",
          	"payerBankAccountDetails": {
								"bankNum":"",
								"branchNum":"",
								"accountNum":"",
								"accountName":""
		},
            "customFields": {
                "cField1": "3ba543214f1"
            }
        }
    }
```

# Testing the Server-to-Server Callback

You can test the server-to-server callback using the [updateMyUrl](https://sandbox.meshulam.co.il/api/light/server/1.0/updateMyUrl/?url=MySiteURL)  endpoint.

This GET request simulates the callback notification by sending an HTTP request to the URL you specify.

Replace **MySiteURL** with your server's endpoint to test how it handles incoming callback data.

This tool allows you to debug the integration and verify your server’s handling of incoming notifications, including any logging as needed.

Example request: <https://sandbox.meshulam.co.il/api/light/server/1.0/updateMyUrl/?url=MySiteURL>
