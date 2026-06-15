---
title: "Server Response"
slug: server-response-1
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/server-response-1
---

# Server Response

After a transaction starts, Grow sends payment status updates to the business server.
It helps verify and record transaction details, payer information, card data, and custom fields
Grow sends an HTTPS POST update to the notifyUrl provided in CreatePaymentProcess.

After receiving the update, the business confirms receipt and calls ApproveTransaction.

This flow is unique because payment updates continue server-to-server, even if the customer leaves the payment page.

If no confirmation is received, Grow retries the update at 10, 20, and 30-minute intervals.

# Server To Server

Server-To-Server Communication:  
Our server-to-server service facilitates seamless communication with your server after a transaction is initiated. To ensure a smooth process, it is imperative that you send a response to Grow's server, confirming the receipt of our call. In the event that no response is received, our server will make additional attempts as follows:

● 1-3 times after 10 minutes.

● 4-5 times after 20 minutes.

● 6 times after 30 minutes.  
For example, the initial call occurs immediately after the transaction, followed by subsequent calls at 10-minute intervals.

Updating the server with the transaction's status and details would be performed by an HTTPS API method that you will be providing us when calling CreatePaymentProcess, in the notifyUrl param.

This URL is an endpoint in your site, which Grow's server will call to update you about the transaction. When received this call (you could save data to DB etc. and then) you should call ApproveTransaction.

The method takes in parameters as an HTTP POST, the same way as you would send the data to the CreatePaymentProcess method and NOT as JSON

# Parameter Details

| Field Name | Description | Type of Field | Example |  |
| --- | --- | --- | --- | --- |
| transactionId | Transaction Id | Int | 79755 |  |
| transactionToken | Transaction Token | String | f3f9598b42cb119980f07360a66482b3 |  |
| TransactionTypeId | Method of payment | Int | 1 |  |
| paymentType | payments method (regular, multiple payments or direct debit) | Int | 4 |  |
| sum | transaction total amount | Flot | 99 |  |
| firstPaymentSum | The first payment to pay in a multiple payments transaction | Float | 16.5 |  |
| periodicalPaymentSum | the amount of each payment after the first payment in a multiple payments transaction | Float | 16.5 |  |
| paymentsNum | current payment number | Int | 1 |  |
| allPaymentsNum | Total number of payments to be made | Int | 6 |  |
| paymentDate | payment date | String | 04/12/17 |  |
| asmachta | An approval from the credit card company for the payment | String | 7304783 |  |
| description | Transaction description | String | course registration |  |
| fullName | full name | String | John Doe |  |
| payerPhone | phone | String | 0500000000 |  |
| payerEmail | email | String | [customeremail@gmail.com](mailto:customeremail@gmail.com) |  |
| cardSuffix | last 4 credit card digits | String | 1121 |  |
| cardType | card type | String | Local |  |
| cardTypeCode | card-type code | Int | 1 |  |
| cardBrand | the card's brand | String | Visa |  |
| cardBrandCode | card brand code | Int | 3 |  |
| cardExp | expiration date | String | 0120 |  |
| processId | process id | Int |  |  |
| processToken | process token | String |  |  |
| cardToken | credit card token | String | 456456776vgfyvhjbsdkc87s8 |  |
| customFields | an array of optional fields | Array | {"cField1":"customer123","cField2":"product123"} |  |

  
> 📘
>
> ### Please note:
>
> No Localhost Support  
> Server updates cannot be sent to a localhost address. The update must be directed to a valid server address.

  
  
  

Server url for testing : )[[https://sandbox.meshulam.co.il/api/light/server/1.0/updateMyUrl/?url=](](https://sandbox.meshulam.co.il/api/light/server/1.0/updateMyUrl/?url=%5D()<https://sandbox.meshulam.co.il/api/light/server/1.0/updateMyUrl/?url=>

  

For a detailed example of the API request, please see the API Request Example [Server-to-Server Callback](https://grow-il.readme.io/reference/server-response)
