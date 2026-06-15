---
title: "Overview"
slug: overview-6
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/overview-6
---

# Overview

This page outlines how to launch a standard online payment flow by generating a secure payment form for customers.

It is designed to ensure smooth checkout experiences while maintaining security and real-time transaction updates for the business.

The process includes creating a payment form, displaying it in an iFrame or new tab, receiving the customer payment indication and server update, and then completing the flow with the ApproveTransaction request.

This API initiates a standard payment process and returns a secure URL for the transaction form.

The **userId and pageCode** parameters are provided by Grow during the onboarding process

![](https://files.readme.io/07c2514-image.png)

The flow:

  
![](https://files.readme.io/a7a0c5cbfc534415368373aa2f3e06fd47635c21483f6d1c3c5c2019d345b1ba-_.png)

# Important Notes

1. The URL will be valid for 10 min.
2. The transaction will be processed even if the [Approve Transaction](https://grow-il.readme.io/reference/post_api-light-server-1-0-approvetransaction) request is not executed or fails.
3. Due to URL length restrictions in the browser, restricted to 2000 characters, it is possible that not all Optional fields would return on requesting the Thank You page. ( On a request made to the server all fields will return).
4. The successUrl and the optional fields must contain valid characters. In case you are interested in sending different parameters, it is recommended that you would use encryption of base64 or a similar one to it.
5. In case of using Post Message, the successUrl and cancelUrl are not required.
6. In case of using iFrame, please see iFrame section. [iframe info](https://grow-il.readme.io/reference/iframe-vs-redirect)
7. To receive the invoice via webhook, set the invoiceNotifyUrl parameter with your endpoint.
8. The successUrl and cancelUrl must point to external URLs. localhost is not allowed.
9. When using an iFrame, ensure that the URL uses HTTPS rather than HTTP.

  
> 📘
>
> ### Important
>
> Only server-side requests are allowed. Any client-side (browser-based) requests will be blocked.


## Images

- https://files.readme.io/07c2514-image.png
- https://files.readme.io/a7a0c5cbfc534415368373aa2f3e06fd47635c21483f6d1c3c5c2019d345b1ba-_.png