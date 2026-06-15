---
title: "Overview"
slug: overview-4
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/overview-4
---

# Overview

Grow tokenization supports secure future payments, recurring payments, and token-based charges without storing card details directly.

It is needed when a business wants faster repeat checkout, subscription-style billing, and secure saved payment methods for credit cards and PayBox.

The solution gives the business more flexibility and control, with the ability to charge customers when needed, reduce payment friction to improve conversion rates, and issue invoices automatically.

Token work can begin by saving a token only, or by saving the token as part of a regular transaction after the customer completes the payment details.

Once saved, the token can be used to charge the customer again or to create Grow-managed recurring payments for future billing cycles.

### Flow for Token Save Process Only

1. Token Storage Only:  
   ● Execute a call to create Payment Process with sum= 1.  
   ● Set parameters: chargeType=3 and saveCardToken=1.  
   ● After the customer fills in credit card details, their token is saved.  
   ● Receive the token update from Grow Systems for future transactions.

![](https://files.readme.io/800a544-image.png)

### Regular Transaction with Token Save

Regular Transaction with Token Save:  
● Use create Payment Process for a standard transaction.  
● Simultaneously save the token by adding the parameter saveCardToken=1.  
● After the payment, the card token is saved, and you receive an update from Grow Systems.

![](https://files.readme.io/a0c98c2bc479e6407bbb7e8e3a037fbf0b5218375c4d87874623fa140ba64362-__.png)
  

### The flow for recurring payment with token

- To create a recurring payment that is managed by GROW using a token, the following parameters must be sent in the call -  
  paymentType = 1  
  paymentNum=1-48

![](https://files.readme.io/f60490c-image.png)

### The flow for charge token

● Execute a call to charge a saved token for a transaction. Flow for Charge Token:

![](https://files.readme.io/8c440aa-image.png)

Choose the token transaction flow that aligns with your business strategy. Grow Systems ensures seamless and secure token handling for efficient transactions. For further assistance or details, contact our support team. Elevate your payment processes with Grow Systems.


## Images

- https://files.readme.io/800a544-image.png
- https://files.readme.io/a0c98c2bc479e6407bbb7e8e3a037fbf0b5218375c4d87874623fa140ba64362-__.png
- https://files.readme.io/f60490c-image.png
- https://files.readme.io/8c440aa-image.png