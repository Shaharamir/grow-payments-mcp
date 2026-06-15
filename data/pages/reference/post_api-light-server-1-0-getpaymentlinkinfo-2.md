---
title: "Get Payment Link Info"
slug: post_api-light-server-1-0-getpaymentlinkinfo-2
type: endpoint
section: reference
source_url: https://grow-il.readme.io/reference/post_api-light-server-1-0-getpaymentlinkinfo-2
---

# Get Payment Link Info

> Each business has its own unique identifiers - the identifiers on this documentation are for example only. To integrate with the API, please contact Grow support to obtain the necessary permissions and your unique identifiers.

## `POST /api/light/server/1.0/getPaymentLinkInfo`

**Servers:**
- https://sandbox.meshulam.co.il
- http://sandboxapi.grow.link
- https://sandboxapi.grow.link
- https://growdevcms.inmanage.com

**Summary:** GetPaymentLinkInfo Copy

**Request body** (`multipart/form-data`):

| Field | Type | Required | Description |
|---|---|---|---|
| paymentLinkProcessToken | string | False | Required field - process identifier   |
| paymentLinkProcessId | string | False | Required field - process identifier   |
| pageCode | string | False | Required field - Unique identifier refers for this payment mathod  |

**Responses:**

- `200` — Successful response

> 📘
>
> ### Important note:
>
> - **All requests must be sent exclusively from your server’s back end. Client-side (browser-based) requests are not supported and will be blocked.**
> - **Do not include any special characters in any parameter of the API request.**
