---
title: "Update Payment Link "
slug: post_api-light-server-1-0-updatepaymentlink-1
type: endpoint
section: reference
source_url: https://grow-il.readme.io/reference/post_api-light-server-1-0-updatepaymentlink-1
---

# Update Payment Link 

> Each business has its own unique identifiers - the identifiers on this documentation are for example only. To integrate with the API, please contact Grow support to obtain the necessary permissions and your unique identifiers.

## `POST /api/light/server/1.0/UpdatePaymentLink`

**Servers:**
- https://sandboxapi.grow.link

**Summary:** Update Payment Link 

Each business has its own unique identifiers - the identifiers on this documentation are for example only. To integrate with the API, please contact Grow support to obtain the necessary permissions and your unique identifiers.


**Parameters:**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| x-api-key | header | string | False |  |

**Request body** (`multipart/form-data`):

| Field | Type | Required | Description |
|---|---|---|---|
| pageCode | string | False | Required field - Unique identifier refers for this payment mathod  |
| isActive | integer | False | Required field - Link is active = 1 inactive =0 |
| paymentLinkProcessId | string | False | Required field - process identifier  |
| paymentLinkProcessToken | string | False | Required field - process identifier  |

**Responses:**

- `200` — Successful response

> 📘
>
> ## Important note:
>
> - The x-api-key header is mandatory and must be included in every request.
> - All requests must be sent exclusively from your server’s back end. Client-side (browser-based) requests are not supported and will be blocked.
> - Do not include any special characters in any parameter of the API request.
