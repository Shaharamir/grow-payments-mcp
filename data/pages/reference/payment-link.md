---
title: "Overview"
slug: payment-link
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/payment-link
---

# Overview

> Payment Link

Payment Link enables a business to create a flexible payment page for different real-world payment scenarios.

It can be used as a standalone checkout page, an embedded payment component on a website, or an offline payment request sent to a customer.

The page supports rich customization, including logo, background color, button color, button text, and visual assets.
Beyond design, it also supports dynamic products and custom fields, making each payment request fit the business need

**Effortless Dynamic Payment Requests with Grow**  
Easily initiate dynamic payment requests using the [createPaymentLink](https://grow-il.readme.io/reference/post_api-light-server-1-0-createpaymentlink)  API call. This feature enables you to send secure payment links to your customers via SMS or email, allowing them to complete payments using various supported methods, including Apple Pay, Google Pay, Bit, bank transfer, and more.

**How It Works:**  
● Use the [createPaymentLink](https://grow-il.readme.io/reference/post_api-light-server-1-0-createpaymentlink)  API to generate a unique payment link for each customer.  
● The customer receives the link via SMS or email.  
● By clicking the link, the customer is directed to a secure payment page where they can complete the transaction using their preferred payment method.  
Available payment methods include Apple Pay, Google Pay, Bit, bank transfer, and others.  
● Upon successful payment, your server receives a real-time notification via a webhook confirming the transaction status.

![](https://files.readme.io/22ddf0e08ec4234bcbc6ae7250e87efe29cff2df96f086e0c80d389e27336aac-_.png)


## Images

- https://files.readme.io/22ddf0e08ec4234bcbc6ae7250e87efe29cff2df96f086e0c80d389e27336aac-_.png