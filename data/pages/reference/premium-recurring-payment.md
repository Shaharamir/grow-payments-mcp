---
title: "Premium Recurring Payment"
slug: premium-recurring-payment
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/premium-recurring-payment
---

# Premium Recurring Payment

# Premium Recurring Payment:

For enhanced services, consider the premium recurring payment option that offers:

1. Updated Token: In case of credit card expiration, the existing token is seamlessly updated with the new expiration date.
2. In case the customer switched to a new credit card, he can confirm to the credit company to automatic transfer of the recurring payment to the new card.
3. Distinct Credit Card Charges: Charges appear as recurring payments in the customer's credit card company, providing clarity in monthly summaries.

> 📘
>
> ### Please note
>
> ● Permissions: Request permission from Grow to access the premium recurring payment service.  
> ● Monthly Charge Detail: When configuring billing, use the sum parameter to specify the monthly charge.

  

# Setting Up premium Recurring Payments

There are two ways to set up a premium recurring payments managed by Grow:

1. ### **Managed by GROW:**

- **CreateTransactionWithToken**:  
  This method allows you to set up a recurring charge using an existing token.
- **CreatePaymentProcess**:  
  This method sets up a recurring payment using an iframe via dedicated pageCode.

  

2. ### **Managed internally by your company:**

- If you prefer to manage recurring payments internally:  
  This involves saving a token and then managing the monthly charges independently.

  

# **How it Works:**

**premium recurring payment managed by Grow via dedicated page code :**

For this option,  
Ensure that the settings defined in GROW are configured according to the Premium recurring payment .  
You need to send a createPaymentProcess call with the dedicated pageCode for the recurring payment ,  
And specify the number of payments you want the recurring payment to run under the paymentNum parameter.

  

**premium recurring payment managed by Grow via token :**

For this option,  
Send the createTransactionWithToken call with the parameter paymentType = 1 and specify the desired number of runs under the paymentNum parameter.

See the following flow.

  
![](https://files.readme.io/db5aff2-image.png)
  
  
  

**premium recurring payment manage by you via token**

For this option,  
you need to perform two actions:  
The first action is to set up the recurring payment by sending the createTransactionWithToken call with the parameter isRecurringDebitId = 1.  
After executing the call, you will receive the recurring payment code in the server update under the recurringDebitId parameter.

For the next charge of the recurring payment ,  
Send the createTransactionWithToken call with the recurringDebitId parameter to link the current charge to the previous charges of the recurring payment .

See the following flow-

  
![](https://files.readme.io/4e1df04-image.png)
  
  

Experience the convenience of recurring payments with Grow, streamlining your billing processes for continuous and seamless transactions.


## Images

- https://files.readme.io/db5aff2-image.png
- https://files.readme.io/4e1df04-image.png