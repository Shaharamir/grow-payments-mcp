---
title: "Create Payment Link"
slug: post_api-light-server-1-0-createpaymentlink
type: endpoint
section: reference
source_url: https://grow-il.readme.io/reference/post_api-light-server-1-0-createpaymentlink
---

# Create Payment Link

> Each business has its own unique identifiers  (userId + pageCode) - the identifiers on this documentation are for example only. To integrate with the API, please contact Grow support to obtain the necessary permissions and your unique identifiers.

## `POST /api/light/server/1.0/CreatePaymentLink`

**Servers:**
- http://sandboxapi.grow.link

**Summary:** Create Payment Link

Each business has its own unique identifiers  (userId + pageCode) - the identifiers on this documentation are for example only. To integrate with the API, please contact Grow support to obtain the necessary permissions and your unique identifiers.


**Parameters:**

| Name | In | Type | Required | Description |
|---|---|---|---|---|
| x-api-key | header | string | False |  |

**Request body** (`multipart/form-data`):

| Field | Type | Required | Description |
|---|---|---|---|
| userId | string | False | Required field - Unique identifier refers to every business that is connected and uses Grow payments solutions.  |
| pageCode | string | False | Required field - Unique identifier refers for this payment mathod  |
| paymentLinkType | integer | False | Required field -The link is closed for one payment |
| isActive | integer | False | Required field -Link is active = 1 |
| sendingMode | integer | False | Optional   - 1=SMS,2=Mail |
| messageText | string | False | Message text sent to user.   Required only in case the parameter "sendingMode" is send.    |
| chargeType | integer | False | Optional - 1 - Regular Charge 2- j4j5  |
| successUrl | string | False | Optional  -An after payment "Thank you" URL. make sure to use HTTPS and not HTTP. Must use an external URL and not localhost. Example: https://mysite.co.il?success=true  Do not include special characters in this field. |
| customText[thankPageTitle] | string | False | Optional -Thank you page title |
| customText[thankPageDescription] | string | False | Optional -Description to the thank you page |
| invoiceNotifyUrl | string | False | optional - Url for invoice  Do not include special characters in this field. |
| notifyUrl | string | False | Optional - A fixed server address can be set via GROW  Do not include special characters in this field. |
| title | string | False | Required field -Page title |
| paymentTypes[0][type] | string | False | Required field - payment method - payments |
| paymentTypes[0][payments][paymentsPaymentNum] | integer | False | Required field  - in case the parameter  paymentTypes[0][payments][paymentsMaxPaymentNum]  is not sent.  Determine payments number. 1-12 |
| paymentTypes[0][payments][paymentsMaxPaymentNum] | string | False | Required field  in case the  parameter  paymentTypes[0][payments][paymentsPaymentNum]  is not sent. -Determine payments number must be minimum 2 Restricting the number of payments. the customer can choose between 2- 12 |
| pageFieldSettings[fullName][value] | string | False | Required field -Full name must consist of at least two names. |
| pageFieldSettings[phone][value] | string | False | Required field -A valid israeli mobile phone numebr Example: 0500000000 |
| pageFieldSettings[email][value] | string | False | optional -A valid email address |
| pageFieldSettings[invoiceName][isRequired] | boolean | False | Optional - specifies whether the customer is required to complete the invoice name field. If set to true (or 1), the field becomes mandatory. If set to false (or 0), the field remains optional. |
| pageFieldSettings[invoiceLicenseNumber][isRequired] | boolean | False | Optional - specifies whether the customer is required to complete the invoice name field. If set to true (or 1), the field becomes mandatory. If set to false (or 0), the field remains optional. |
| products[data][0][catalogNumber] | integer | False | Optional - catalog number of the product |
| products[data][0][name] | string | False | Required field - product name |
| products[data][0][price] | integer | False | Required field - product amount |
| products[data][0][quantity] | integer | False | Optional - maximum units per product |
| products[data][0][minQuantity] | integer | False | Optional - minimum units per product |
| products[data][0][url] | string | False | Optional -URL image of the product |
| products[data][0][vatType] | integer | False | Required field-  Specifies the value based on the business VAT status:   if the business is subject to regular VAT setting=  1 if the business is VAT-exempt - VAT setting = 3  |
| transactionType[0] | integer | False | specify which payment method to display - Credit Card |
| transactionType[1] | integer | False | specify which payment method to display -bit |
| transactionType[2] | integer | False | specify which payment method to display -Apple Pay |
| transactionType[3] | integer | False | specify which payment method to display - Google Pay |
| transactionType[4] | integer | False | specify which payment method to display - bank transfer |
| transactionType[5] | integer | False | specify which payment method to display - Pay Box |
| cField1 | string | False | optional -Custom field, you may add up to 9 fields.  Do not include special characters in this field. |
| cField2 | string | False | optional -Custom field, you may add up to 9 fields.  Do not include special characters in this field. |
| backgroundColor | string | False | Optional - Defines the background color of the payment page.  Format: HEX color code (e.g. #FFFFFF)   |
| buttonColor | string | False | Optional - Defines the background color of the payment button.  Format: HEX color code (e.g. #0285AC)   |
| paymentButtonText | string | False | Optional - Sets the text that will appear on the payment button  Validation rules: Up to 20 characters - only letters  You can also configure a default business logo via the business management interface. |

**Responses:**

- `200` — Successful response

> 📘
>
> ### Important note:
>
> - **The x-api-key header is mandatory and must be included in every request.**
> - **All requests must be sent exclusively from your server’s back end. Client-side (browser-based) requests are not supported and will be blocked.**
> - **Do not include any special characters in any parameter of the API request.**
