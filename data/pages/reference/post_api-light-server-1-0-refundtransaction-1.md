---
title: "Refund Transaction"
slug: post_api-light-server-1-0-refundtransaction-1
type: endpoint
section: reference
source_url: https://grow-il.readme.io/reference/post_api-light-server-1-0-refundtransaction-1
---

# Refund Transaction

> Each business has its own unique identifiers  (userId + pageCode) - the identifiers on this documentation are for example only. To integrate with the API, please contact Grow support to obtain the necessary permissions and your unique identifiers.

## `POST /api/light/server/1.0/refundTransaction`

**Servers:**
- https://sandbox.meshulam.co.il

**Summary:** Refund Transaction Copy

**Request body** (`multipart/form-data`):

| Field | Type | Required | Description |
|---|---|---|---|
| transactionId | integer | False | Required field - transaction identifier |
| transactionToken | string | False | Required field - transaction identifier |
| refundSum | integer | False | Required field - total amount to refund |
| stopDirectDebit | integer | False | optional - in case this is a direct debit transaction you need to send the value of 1 to stop the upcoming payments |
| userId | string | False | Required field - Unique identifier refers to every business that is connected and uses Grow payments solutions. |
| pageCode | string | False | optional - Unique identifier refers to payment mathod   |

**Responses:**

- `200` — Successful response

> 📘
>
> ### Important note :
>
> - **All requests must be sent exclusively from your server’s back end. Client-side (browser-based) requests are not supported and will be blocked.**
> - **Do not include any special characters in any parameter of the API request**
