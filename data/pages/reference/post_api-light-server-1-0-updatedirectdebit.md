---
title: "Update Recurring Payment"
slug: post_api-light-server-1-0-updatedirectdebit
type: endpoint
section: reference
source_url: https://grow-il.readme.io/reference/post_api-light-server-1-0-updatedirectdebit
---

# Update Recurring Payment

> This method is for updating an existing direct debit payment .   Each business has its own unique identifiers - the identifiers on this documentation are for example only.  To integrate with the API, please contact Grow support to obtain the necessary permissions and your unique identifiers.

## `POST /api/light/server/1.0/updateDirectDebit`

**Servers:**
- https://sandbox.meshulam.co.il

**Summary:** Update Recurring Payment

**Request body** (`multipart/form-data`):

| Field | Type | Required | Description |
|---|---|---|---|
| userId | string | False | Required field -Unique identifier refers to every business that is connected and uses Grow payments solutions. |
| transactionToken | string | False | Required field -transaction identifier  |
| transactionId | integer | False | Required field -transaction identifier |
| asmachta | integer | False | Required field - An approval from the credit card company for the payment |
| fullName | string | False | optional-Full name must consist of at least two names. |
| phone | string | False | optional -A valid israeli mobile phone numebr Example: 0500000000  |
| chargeDay | integer | False | optional - 1-31 |
| sum | integer | False | optional - Total amount for payment Example: 10.99. |
| paymentNum | integer | False | optional - 1-48 |
| email | string | False | optional -A valid email address |
| changeStatus | integer | False | optional - 1= active 2= canceled |
| updateCard | integer | False | optional - 0= no update 1=update |

**Responses:**

- `200` — Successful response

> 📘
>
> ### Important note :
>
> - **All requests must be sent exclusively from your server’s back end. Client-side (browser-based) requests are not supported and will be blocked.**
> - **Do not include any special characters in any parameter of the API request.**
