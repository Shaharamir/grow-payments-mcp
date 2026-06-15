---
title: "getTokenTransactionsByExternalIdentifiers"
slug: post_api-light-server-1-0-gettokentransactionsbyexternalidentifiers-1
type: endpoint
section: reference
source_url: https://grow-il.readme.io/reference/post_api-light-server-1-0-gettokentransactionsbyexternalidentifiers-1
---

# getTokenTransactionsByExternalIdentifiers

> Each business has its own unique identifiers - the identifiers on this documentation are for example only.  To integrate with the API, please contact Grow support to obtain the necessary permissions and your unique identifiers.

## `POST /api/light/server/1.0/getTokenTransactionsByExternalIdentifiers/`

**Servers:**
- https://sandbox.meshulam.co.il

**Summary:** getTokenTransactionsByExternalIdentifiers

Each business has its own unique identifiers - the identifiers on this documentation are for example only.  To integrate with the API, please contact Grow support to obtain the necessary permissions and your unique identifiers.


**Request body** (`multipart/form-data`):

| Field | Type | Required | Description |
|---|---|---|---|
| userId | string | False | Required field - Unique identifier refers to every business that is connected and uses Grow payments solutions. |
| cardToken | string | False | Required field - credit card token . |
| transactionGroupIdentifier | integer | False | optional -Group identifier for the payment- if you send a value in this field, then a check will be made if there is a succesful payment with this value, then the request will be rejected . |
| transactionUniqueIdentifier | integer | False | Required field - Unique identifier for the request - if we send a value in this field, then a check will be made that this is the first time we see this value for the business. If it finds that a request has been sent with this ID, then the current request will be rejected outright regardless of the status of the first request with this ID. |

**Responses:**

- `200` — Successful response

> 📘
>
> ### Important note :
>
> - **All requests must be sent exclusively from your server’s back end. Client-side (browser-based) requests are not supported and will be blocked.**
> - **Do not include any special characters in any parameter of the API request.**
