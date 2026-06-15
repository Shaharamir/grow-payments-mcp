---
title: "Approve Transaction"
slug: post_api-light-server-1-0-approvetransaction-4
type: endpoint
section: reference
source_url: https://grow-il.readme.io/reference/post_api-light-server-1-0-approvetransaction-4
---

# Approve Transaction

> The ApproveTransaction call must be executed after each successful payment. It is the final step in the transaction flow and serves as confirmation that your system has received and acknowledged the transaction details. Note: The transaction will still be processed even if the ApproveTransaction request is not executed or fails.

## `POST /api/light/server/1.0/approveTransaction`

**Servers:**
- https://sandbox.meshulam.co.il
- http://sandboxapi.grow.link
- https://sandboxapi.grow.link
- https://growdevcms.inmanage.com

**Summary:** Approve Transaction Copy

**Request body** (`multipart/form-data`):

| Field | Type | Required | Description |
|---|---|---|---|
| pageCode | string | False | Required field -Unique identifier refers to payment mathod |
| transactionId | integer | False | Required field - transaction identifier  |
| transactionToken | string | False | Required field -transaction identifier  |
| transactionTypeId | integer | False | Required field -  Credit card=1 Bit=6 Google Pay=14 Apple Pay=13 |
| paymentType | integer | False | Required field -  1-Direct Debit 2-Regular 4-Payments |
| sum | integer | False | Required field - Sum from server notification   |
| firstPaymentSum | integer | False | Required field - The first payment to pay in a multiple payments transaction   |
| periodicalPaymentSum | integer | False | Required field - The amount of each payment after the first payment in a multiple payments transaction |
| paymentsNum | integer | False | Required field -Current payment number  |
| allPaymentsNum | integer | False | Required field -Total number of payments to be made  |
| paymentDate | string | False | Required field- Payment date  |
| asmachta | integer | False | Required field -An approval from the credit card company for the payment  |
| description | string | False | Required field- Description of the product to be charged (will appear in the details of the transaction as well) Example: Payment for a monthly subscription. |
| fullName | string | False | Required field -Full name must consist of at least two names. |
| payerPhone | integer | False | Required field -A valid israeli mobile phone numebr Example: 0500000000  |
| payerEmail | string | False | Required field -A valid email address |
| cardSuffix | integer | False | Required field -Last 4 credit card digits from server notification |
| cardType | string | False | Required field -CardType from server notification  |
| cardTypeCode | integer | False | Required field - 1-Local 2-Foreign 3-Fuel 4-Debit 5-Gift/Rechargeable |
| cardBrand | string | False | Required field -The card's brand from server notification   |
| cardBrandCode | integer | False | Required field - Mastercard=2 Visa=3 Isracard=5 Diners=8 Discover=7  |
| cardExp | integer | False | Required field -Card expiration date from server notification |
| processId | integer | False | Required field -process identifier  |
| processToken | string | False | Required field -process identifier  |

**Responses:**

- `200` — Successful response

> 📘
>
> ### Important note :
>
> - **All requests must be sent exclusively from your server’s back end. Client-side (browser-based) requests are not supported and will be blocked.**
> - **Do not include any special characters in any parameter of the API request.**
