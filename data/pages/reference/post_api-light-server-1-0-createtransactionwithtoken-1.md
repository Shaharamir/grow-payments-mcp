---
title: "Further Payment -Premium Recurring By Token"
slug: post_api-light-server-1-0-createtransactionwithtoken-1
type: endpoint
section: reference
source_url: https://grow-il.readme.io/reference/post_api-light-server-1-0-createtransactionwithtoken-1
---

# Further Payment -Premium Recurring By Token

## `POST /api/light/server/1.0/createTransactionWithToken`

**Servers:**
- https://sandbox.meshulam.co.il
- https://sandboxapi.grow.link

**Summary:** Further Payment -Premium Recurring By Token

**Request body** (`multipart/form-data`):

| Field | Type | Required | Description |
|---|---|---|---|
| cardToken | string | False | Required field - credit card token . |
| userId | string | False | Required field - Will be provided by Meshulam for each clearing business Example: 41deb6f1347ee8b2. |
| sum | integer | False | Required field - Total amount for payment Example: 10.99. |
| description | string | False | Required field - Description of the product to be charged (will appear in the details of the transaction as well) Example: Payment for a monthly subscription. |
| paymentType | integer | False | Required field - 2-Regular   |
| paymentNum | integer | False | Determine payments number. 1-12 |
| pageField[fullName] | string | False | Required field - Full name must consist of at least two names. |
| pageField[phone] | string | False | Required field - A valid israeli mobile phone numebr Example: 0500000000  |
| pageField[email] | string | False | A valid email address |
| cField1 | string | False | Custom field, you may add up to 9 fields. |
| cField2 | string | False | Custom field, you may add up to 9 fields. |
| recurringDebitId | integer | False | Required field - the given value in the param "recurringDebitId" from the respons of the first premiume recurring payment  payment  |
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
