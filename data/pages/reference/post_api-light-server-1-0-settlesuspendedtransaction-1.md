---
title: "Settle Suspended Transaction"
slug: post_api-light-server-1-0-settlesuspendedtransaction-1
type: endpoint
section: reference
source_url: https://grow-il.readme.io/reference/post_api-light-server-1-0-settlesuspendedtransaction-1
---

# Settle Suspended Transaction

> This method is used to perform a J4 operation, releasing a held transaction. It requires the transactionId and transactionToken to identify and settle the transaction. Please note that each business has its own unique identifiers — the values shown in this documentation are for demonstration purposes only. To integrate with the API, please contact Grow support to obtain the necessary permissions and your unique identifiers.

## `POST /api/light/server/1.0/settleSuspendedTransaction`

**Servers:**
- https://sandbox.meshulam.co.il

**Summary:** Settle Suspended Transaction Copy

**Request body** (`multipart/form-data`):

| Field | Type | Required | Description |
|---|---|---|---|
| userId | string | False | Required field -Unique identifier refers to payment mathod |
| transactionId | integer | False | Required field -transaction identifier  |
| transactionToken | string | False | Required field -transaction identifier  |
| sum | integer | False | Required field -Total amount for payment Example: 10.99. |
| productData[0][catalogNumber] | integer | False | optional -catalog number for an item in the Invoice  |
| productData[0][quantity] | integer | False | optional -quantity for an item in the Invoice  |
| productData[0][price] | integer | False | optional -price for an item in the Invoice  |
| productData[0][itemDescription] | string | False | optional -item description for an item in the Invoice  |
| pageField[invoiceName] | string | False | optional - the name for the invoice   |
| pageField[invoiceLicenseNumber] | string | False | optional - Invoice License Number for invoice |

**Responses:**

- `200` — Successful response

> 📘
>
> ### Important note :
>
> - **All requests must be sent exclusively from your server’s back end. Client-side (browser-based) requests are not supported and will be blocked.**
> - **Do not include any special characters in any parameter of the API request.**
