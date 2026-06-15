---
title: "Create Transaction With Token"
slug: post_api-light-server-1-0-createtransactionwithtoken-4
type: endpoint
section: reference
source_url: https://grow-il.readme.io/reference/post_api-light-server-1-0-createtransactionwithtoken-4
---

# Create Transaction With Token

> Each business has its own unique identifiers - the identifiers on this documentation are for example only.  To integrate with the API, please contact Grow support to obtain the necessary permissions and your unique identifiers.

## `POST /api/light/server/1.0/createTransactionWithToken`

**Servers:**
- https://sandbox.meshulam.co.il

**Summary:** Create Transaction With Token Copy

**Request body** (`multipart/form-data`):

| Field | Type | Required | Description |
|---|---|---|---|
| cardToken | string | False | Required field - credit card token . |
| userId | string | False | Required field - Will be provided by Meshulam for each clearing business Example: 41deb6f1347ee8b2. |
| sum | integer | False | Required field - Total amount for payment Example: 10.99. |
| description | string | False | Required field - Description of the product to be charged (will appear in the details of the transaction as well) Example: Payment for a monthly subscription. |
| paymentType | integer | False | Required field - 1-Direct Debit, 2-Regular, 4-Payments |
| paymentNum | integer | False | optional -Determine payments number. 1-12 |
| pageField[invoiceName] | string | False | optional - the name for the invoice |
| pageField[invoiceLicenseNumber] | string | False | optional - Invoice License Number for invoice |
| pageField[fullName] | string | False | Required field - Full name must consist of at least two names. |
| pageField[phone] | integer | False | Required field - A valid israeli mobile phone numebr Example: 0500000000  |
| pageField[email] | string | False | optional -A valid email address |
| cField1 | string | False | optional -Custom field, you may add up to 9 fields. |
| cField2 | string | False | optional -Custom field, you may add up to 9 fields. |
| transactionGroupIdentifier | integer | False | optional - Group identifier for the payment- if you send a value in this field, then a check will be made if there is a succesful payment with this value,  then the request will be rejected . |
| transactionUniqueIdentifier | integer | False | Required field - Unique identifier for the request - if we send a value in this field, then a check will be made that this is the first time we see this value for the business. If it finds that a request has been sent with this ID, then the current request will be rejected outright regardless of the status of the first request with this ID. |

**Responses:**

- `200` — Successful response

> 📘
>
> ### Important note :
>
> - **All requests must be sent exclusively from your server’s back end. Client-side (browser-based) requests are not supported and will be blocked.**
> - **Do not include any special characters in any parameter of the API request.**
