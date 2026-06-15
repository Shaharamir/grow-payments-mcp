---
title: "Transition to Production Environment"
slug: live-environment
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/live-environment
---

# Transition to Production Environment

> Key Steps

This page explains how to move from Sandbox testing to Grow’s live Production environment.

It is needed before real payment processing can begin, because Grow must review the setup and issue production identifiers.
The transition covers live URLs, server updates, ApproveTransaction handling, token saving consent, webhooks, Apple Pay, and commercial approval.
Following these requirements helps reduce payment errors, protect customer data, and ensure the business is ready to accept real transactions through Grow.

To transition from the Sandbox environment to the Production environment, please contact us and request a production review.

**Contact Information:**
Email: [support@grow.business](mailto:support@grow.business)

Before production identifiers can be issued, Grow will review the integration and verify that the required API calls, server updates, and implementation steps were completed correctly.

The review process may take several business days.

---

## Production Approval Process

Once your development is complete, please contact us and request to move to Production.

As part of the review, Grow will check the integration logs and verify that:

- API requests are sent correctly
- Server update callbacks are handled properly
- Your server returns HTTP 200 for server updates
- The `ApproveTransaction` request is sent when required
- Customer-side validations are implemented correctly
- The integration does not create avoidable errors due to missing or invalid customer fields

Only after the integration review is completed successfully, Grow will provide the production identifiers required for live processing.

Production identifiers may include:

- `pageCode`
- `userId`
- `apiKey`, if required for your integration

---

## Production Environment URL

When moving to Production, make sure to update the API base URL from the Sandbox environment to the Production environment.

Production Environment URL:

<https://secure.meshulam.co.il/api/light/server/1.0>

---

## Growin Wallet SDK Configuration

If you are using the Growin Wallet SDK, make sure to update the SDK environment value in the `configureGrowSdk` function.

Change the environment from:

JavaScript

```
environment: "DEV"
```

To:

JavaScript

```
environment: "PRODUCTION"
```

  

## Server Update and ApproveTransaction

When handling Grow server updates, make sure your server:

- Receives the server update successfully
- Returns HTTP 200 for the server update
- Performs the required validations on your side
- Sends an `ApproveTransaction` request when required

For regular transactions, the `ApproveTransaction` request must be sent after receiving the server update.

For J4/J5 authorization flows, do not send an `ApproveTransaction` request.  
These flows should be handled according to the authorization and capture process.

You should also validate customer fields, such as customer name and phone number, before sending the request to Grow, in order to avoid preventable errors on your side.

## Token Saving Requirements

If your integration saves card tokens, the payment page must include a checkbox that allows the end customer to actively approve saving the card token.

The customer must clearly approve token saving before the token is stored.

## CreatePaymentLink API

If you are using the CreatePaymentLink API, make sure to update the X-API-KEY header to the following production value:

WqnMS3npu9IOxLc2lRfz8Ny9teEN87AACzSUma80

## Apple Pay

If your website supports Apple Pay, the live domain must be approved according to [the Apple Pay domain verification instructions.](https://grow-il.readme.io/update/reference/sdk-apple)

Make sure to complete the Apple Pay setup for the Production domain, even if the Sandbox domain was already configured.

## Webhooks

If you configured webhooks in the Sandbox environment, they must be configured again in the Production environment.

Sandbox webhook configuration does not automatically apply to Production.

## Commercial Approval

If the integration is for a system, platform, or partner integration, make sure that a signed commercial agreement is completed with the relevant commercial teams before moving to Production.

Production access cannot be provided before the required commercial approval is completed.

## Website Review Criteria for E-commerce Websites

If your integration is for an **e-commerce website**, the website must meet the following requirements before Production approval.

## Website Requirements:

1. **Active Website** - The website must be active, with a real or temporary domain, and it should include all the products or services that will be sold continuously on the site.
2. **Payment Page** - A payment page must appear on the website.  
   This should be a page that comes after clicking "Purchase" or "Shopping Cart" (not a credit card page but a page with customer details before proceeding to payment).
3. **Contact Phone Number** - A contact phone number must be clearly displayed on the website, either on the homepage or on a dedicated contact page.
4. **Business Address** - The business address must be present on the website itself or in the terms and conditions.
5. **Purchase Terms Approval** - On the payment page, there must be a checkbox (which can be marked) for approving the terms and conditions. Additionally, the approval must include a link to view the actual terms and conditions.
6. **Terms and Conditions** - In addition to the terms and conditions checkbox, there must be terms and conditions displayed on the website's homepage.  
   In every set of terms and conditions, the following clauses must be included:

- **Product/Service Delivery Policy** - (Including information about how long it takes from the purchase date for the product to be shipped to the customer, and how the product will be delivered, among other details.)
- **Business Liability Information** - (Stating that the company and/or its representatives will not be held responsible for any direct or indirect damages resulting from the use of the service or product purchased on the website.)
- **Age Restriction** - (Clearly specifying from what age purchases can be made on the website. Conditions for purchasing on the site, such as the purchaser being 18 years or older – for credit card purchases and use.)
- **Transaction Cancellation Terms** - (Outlining the conditions for canceling a transaction.)
- **Privacy Policy** - (Explaining whether or not user-provided information on the website will be used, and how user data is protected.)

By following these steps and completing the required review, you can transition smoothly to Grow's Production environment.
