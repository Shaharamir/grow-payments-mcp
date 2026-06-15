---
title: "Iframe vs. Redirect"
slug: iframe-vs-redirect
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/iframe-vs-redirect
---

# Iframe vs. Redirect

Businesses can choose between Iframe and Redirect when setting up the Grow payment flow.
With Iframe, the payment page stays embedded inside the business website, creating a smoother and more continuous checkout experience.

With Redirect, the customer moves to a separate payment page, which can be simpler to manage and clearer for external payment actions.

The comparison is needed because each option affects the customer journey, trust, payment experience, and checkout flow differently.
For businesses using Apple Pay in an Iframe, domain verification is an important requirement for secure payment integration.

### The differences between Iframe and Redirect:

## Redirect:

Redirect is a process that involves transferring the user from one web page to another in an absolute manner. This method is commonly used in payment processing or identity verification scenarios. When a user clicks a button or submits required information, they are redirected to another page, often with a different URL, where necessary actions are performed, and results are displayed.

## Iframe:

Iframe is an HTML element that allows you to embed an entire web page or a specific portion of it within another web page. Typically, an iframe displays another page as a small, independent window while preserving the integrity of the main page. Iframes are commonly used when you need to display content from an external source within an existing page, such as external news or compact payment windows.

In summary, the key distinction between Redirect and Iframe lies in the user experience. In Redirect, the user is transferred to a new page, while in Iframe, the content is seamlessly displayed within the existing page.

**Using Apple Pay with Iframe:**  
If you intend to use Apple Pay with an iframe, domain verification is a prerequisite. This verification process ensures the secure integration of Apple Pay into your web page.

> 📘
>
> ### **Important Note:**
>
> When using an iframe, it's essential to employ post-messaging techniques to facilitate secure and efficient communication between different parts of the web page.
