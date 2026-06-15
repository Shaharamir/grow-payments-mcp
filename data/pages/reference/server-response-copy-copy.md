---
title: "Server-to-Server Callback"
slug: server-response-copy-copy
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/server-response-copy-copy
---

# Server-to-Server Callback

> Transaction Status Update via Webhook for CreatePaymentProcess

An HTTPS callback will be sent to your server to notify the completion of the transaction.  
The method takes in parameters as an HTTP POST, the same way as you would send the data to the CreatePaymentProcess method and NOT as JSON

The callback will be made to the endpoint URL specified in the **notifyUrl** parameter of the [CreatePaymentProcess](https://grow-il.readme.io/reference/post_api-light-server-1-0-createpaymentprocess-3)  API request.

Upon receiving the update, you are required to execute the ApproveTransaction API call.  
This call serves as an acknowledgment that your system has received the server notification and is aware of the transaction status.

Please note: The transaction will be processed even if the ApproveTransaction request is not executed or fails.

  

JSON

```
{
"err": "",
"status": "1",
"data": {
		"status" :"שולם",
		"statusCode" :" 2",
		"transactionTypeId": "1",
		"paymentType":"1" ,
		"sum" :"1" ,
		"paymentsNum" :"0",
		"allPaymentsNum": "1",
		"paymentDate": "21/9/25" ,
		"description" :" תיאור עסקה",
		"fullName" :"ישראל ישראלי ",
		"payerPhone" :"0500000000",
		"payerEmail": "TEST@TEST.COM",
		"transactionId" :" 6121277",
		"transactionToken":"8a66bc017b12121209a3aeea840f8181",
		"directDebitId" :" 33333885",
		"recurringDebitId" :" 341742",
		"asmachta" :" 43221726",
		"cardSuffix": "3333",
		"cardType" : "Local",
		"cardTypeCode": "1",
		"cardBrand": "Visa",
		"cardBrandCode": "3",
		"cardExp" : "1125",
		"firstPaymentSum": "0",
    "periodicalPaymentSum": "0",
		"payerBankAccountDetails": "",
		"processId": "212121775",
		"processToken" : "17632617beb34343414b0bec684651d",
		"customFields": {
                "cField1": "3ba543214f1"
            }
        }
    }
```

  
  
  

# Testing the Server-to-Server Callback

You can test the server-to-server callback using the [updateMyUrl](https://sandbox.meshulam.co.il/api/light/server/1.0/updateMyUrl/?url=MySiteURL)  endpoint.

This GET request simulates the callback notification by sending an HTTP request to the URL you specify.

Replace MySiteURL with your server's endpoint to test how it handles incoming callback data.

This tool allows you to debug the integration and verify your server’s handling of incoming notifications, including any logging as needed.

<https://sandbox.meshulam.co.il/api/light/server/1.0/updateMyUrl/?url=MySiteURL>
