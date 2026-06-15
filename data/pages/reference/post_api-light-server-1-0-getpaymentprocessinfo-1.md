---
title: "Get Payment Process Info"
slug: post_api-light-server-1-0-getpaymentprocessinfo-1
type: endpoint
section: reference
source_url: https://grow-il.readme.io/reference/post_api-light-server-1-0-getpaymentprocessinfo-1
---

# Get Payment Process Info

> Each business has its own unique identifiers  (userId + pageCode) - the identifiers on this documentation are for example only. To integrate with the API, please contact Grow support to obtain the necessary permissions and your unique identifiers.

## `POST /api/light/server/1.0/getPaymentProcessInfo`

**Servers:**
- https://sandbox.meshulam.co.il

**Summary:** Get Payment Process Info Copy

**Request body** (`multipart/form-data`):

| Field | Type | Required | Description |
|---|---|---|---|
| pageCode | string | False | Required field - Unique identifier refers to payment mathod |
| processId | integer | False | Required field - process identifier |
| processToken | string | False | Required field - process identifier |

**Responses:**

- `200` — Successful response

> 📘
>
> ### Important note :
>
> - **All requests must be sent exclusively from your server’s back end. Client-side (browser-based) requests are not supported and will be blocked.**
> - **Do not include any special characters in any parameter of the API request.**
