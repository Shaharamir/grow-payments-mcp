---
title: "Authentication"
slug: authentication
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/authentication
---

# Authentication

Authentication is required to keep payment processing secure and to separate test credentials from live payment credentials.

Each Grow payment request must include the relevant authentication parameters, according to the type of integration and the payment environment being used.

This ensures that every request is processed securely, using the correct credentials for the correct business, payment method, and environment.

## Authentication Flows

Grow supports two main authentication flows:

1. **Direct business payments**
   Used by a business that processes payments for itself.
2. **Multiple business payments**
   Used by companies or platforms that manage payments on behalf of multiple businesses.

## Direct Business Payments

For a regular business, each payment request should include:

- UserId
- PageCode

The **UserId** identifies the business, while the **PageCode** identifies the relevant payment page or payment method, such as credit card, Bit, or another supported payment type.

## Authentication Parameters

**UserId**

The **UserId** is a unique identifier assigned to each business connected to Grow Payment Solutions.

It is used to identify the business that owns the payment request.

**PageCode**

The **PageCode** identifies a specific payment page or payment method configured for the business.

Each payment type may have a different PageCode. For example:

- Credit card payments may use one PageCode.
- Bit payments may use a different PageCode.
- Additional payment flows may have their own dedicated PageCodes.

For more information about payment pages and PageCode options, please refer to the [Payment Page documentation](https://grow-il.readme.io/reference/payment-page)

![](https://files.readme.io/c41fcac-image.png)

## Supporting Multiple Businesses

If your company, platform, or system manages payments for multiple businesses, Grow supports a dedicated authentication flow for this structure.

This flow is relevant for companies such as accounting platforms, management systems, marketplaces, or other service providers that process payments on behalf of different businesses.

In this case, each request should include:

- **APIKey**
- **UserId** of the client business
- **PageCode** of the relevant payment method

The **APIKey** identifies your company or platform, while the **UserId** identifies the specific business for which the payment is being processed.

**APIKey**

The **APIKey** is a unique identifier assigned to your company or platform.

It is connected to the businesses you are authorized to process payments for.

Example

If your company provides services to multiple businesses and needs to create a payment for one of them, the request should include:

- Your company’s APIKey
- The client business’s UserId
- The relevant PageCode for the payment method

This allows Grow to securely identify both the company managing the payment flow and the specific business receiving the payment.


## Images

- https://files.readme.io/c41fcac-image.png