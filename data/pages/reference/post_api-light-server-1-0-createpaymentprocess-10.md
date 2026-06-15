---
title: "Delayed Payment J4J5"
slug: post_api-light-server-1-0-createpaymentprocess-10
type: endpoint
section: reference
source_url: https://grow-il.readme.io/reference/post_api-light-server-1-0-createpaymentprocess-10
---

# Delayed Payment J4J5

> Each business has its own unique identifiers  (userId + pageCode) - the identifiers on this documentation are for example only. To integrate with the API, please contact Grow support to obtain the necessary permissions and your unique identifiers.

## `POST /api/light/server/1.0/createPaymentProcess`

**Servers:**
- https://sandbox.meshulam.co.il

**Summary:** Delayed Payment J4J5 Copy

**Request body** (`multipart/form-data`):

| Field | Type | Required | Description |
|---|---|---|---|
| pageCode | string | False | Required field -Unique identifier refers to payment mathod |
| userId | string | False | Required field -Unique identifier refers to every business that is connected and uses Grow payments solutions. |
| chargeType | integer | False | Required field -  2 - Suspended Charge  |
| sum | integer | False | Required field -Total amount for payment Example: 10.99. |
| successUrl | string | False | Required field -An after payment "Thank you" URL. make sure to use HTTPS and not HTTP. Must use an external URL and not localhost. Example: https://mysite.co.il?success=true  Do not include special characters in this field. |
| cancelUrl | string | False | Required field -The page users will be redirected to if a payment is cancelled.  Do not include special characters in this field. |
| paymentNum | integer | False | optional -Determine payments number. 1-12 |
| maxPaymentNum | integer | False | optional -the customer can choose number of payments between 2- to the value that you choose in this parameter. The payments number must be minimum 2 Determine Restricting the number of payments |
| description | string | False | Required field -Description of the product to be charged (will appear in the details of the transaction as well) Example: Payment for a monthly subscription.  Do not include special characters in this field. |
| pageField[invoiceName] | string | False | optional - the name for the invoice |
| pageField[invoiceLicenseNumber] | string | False | optional - Invoice License Number for invoice |
| pageField[fullName] | string | False | Required field -Full name must consist of at least two names. |
| pageField[phone] | string | False | Required field -A valid israeli mobile phone numebr Example: 0500000000  |
| pageField[email] | string | False | optional -A valid email address |
| cField1 | string | False | optional -Custom field, you may add up to 9 fields.  Do not include special characters in this field. |
| cField2 | string | False | optional -Custom field, you may add up to 9 fields.  Do not include special characters in this field. |
| saveCardToken | integer | False | optional -if set to 1: the token of client credit card will be sent after payment for running future tokenization payments .  if you set 0 the token of client credit card wil not be saved . |
| productData[0][catalogNumber]
 | integer | False | optional -catalog number for an item in the Invoice  |
| productData[0][quantity] | integer | False | optional -quantity for an item in the Invoice  |
| productData[0][price] | integer | False | optional -price for an item in the Invoice  |
| productData[0][itemDescription] | string | False | optional -item description for an item in the Invoice  |
| notifyUrl | string | False | optional -Url for server to sever request  Do not include special characters in this field. |
| invoiceNotifyUrl | string | False | optional - Url for invoice  Do not include special characters in this field. |

**Responses:**

- `200` — Successful response

> 📘
>
> ### Important note :
>
> - **All requests must be sent exclusively from your server’s back end. Client-side (browser-based) requests are not supported and will be blocked.**
> - **Do not include any special characters in any parameter of the API request.**
