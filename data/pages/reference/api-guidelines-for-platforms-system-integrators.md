---
title: "Platforms & Multi-Merchant Systems"
slug: api-guidelines-for-platforms-system-integrators
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/api-guidelines-for-platforms-system-integrators
---

# Platforms & Multi-Merchant Systems

# API Guidelines for Platform Partners and System Integrators

This section is intended for platform partners and system integrators that enable multiple businesses to process payments through their own system using Grow Payments.

The guidelines below include requirements and parameters that are relevant for platform-based integrations only.

---

## When Is a Platform Partner / System Integrator Setup Required?

A platform partner or system integrator setup is required when your system serves multiple businesses, merchants, or end customers that need to process payments through Grow.

This setup is relevant, for example, when:

- Your system allows multiple businesses to open or manage payment activity through the same platform.
- Your platform creates payment processes on behalf of different businesses.
- Your integration requires centralized API activity under one platform identifier.
- Your platform needs to route each transaction to the relevant business.

  

In these cases, Grow may create a dedicated platform partner or system integrator setup.

This setup allows Grow to associate the relevant API activity with your platform while still identifying the specific business related to each transaction.

---

## Merchant Onboarding Through Grow

An approved platform partner can implement Grow's registration form directly within their system.

This allows merchants to start the Grow registration process from inside the platform, creating a smoother and more direct onboarding experience.

The onboarding flow is relevant when a platform wants to allow its merchants to connect to Grow without leaving the platform's environment or going through a separate manual process.

Once the onboarding process is completed and approved, the business can be connected to Grow and start processing payments according to the approved integration setup.

This option is available only for approved platform partner integrations and requires coordination with Grow.

---

## API Key Requirement

For platform partner integrations, each API request must include your unique `apiKey`.

The `apiKey` identifies your platform and links the API activity to your system.

This parameter is mandatory for authentication and must be sent in every relevant API request.

You will receive your `apiKey` together with the additional identifiers required for your integration, such as `pageCode` and `userId`, if applicable.

---

## Business Identification

In platform partner integrations, each transaction must be associated with the relevant business that processes the payment.

Depending on the integration setup, Grow will provide the identifiers required to route the transaction to the correct business.

Make sure to use the correct identifiers provided by Grow for each business or payment flow.

---

## Company Commission

As a platform partner, you may define a commission amount per transaction.

The commission is automatically deducted from the transaction and allocated to your platform, according to the commercial agreement with Grow.

The commission amount is defined in ILS, excluding VAT.

---

## Implementation - Company Commission

To define a commission amount for a transaction, include the following parameter in your API request when creating the payment process.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `companyCommission` | Number | Optional | The commission amount to be allocated to the platform for the transaction. |

### Example

JSON

```
{
  "companyCommission": 2.5
}
```

> 📘
>
> **Important Notes**
>
> - The companyCommission value must be sent in ILS.
> - The amount is excluding VAT.
> - The value must be sent as a fixed amount and not as a percentage.
> - The commission is applied per transaction.
> - This parameter should be used only by approved platforms that have a commercial commission setup with Grow.
> - The use of this parameter is subject to the commercial agreement between the platform and Grow.
