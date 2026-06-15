---
title: "overview"
slug: overview-8
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/overview-8
---

# overview

Token Billing with Premium Recurring Payments  
Experience the ease of managing customer billing independently and unlock the benefits of premium recurring payment services through Grow Systems.

Follow these steps to create a premium recurring payment order with a token:

**Step 1: Save Token**  
● Save the token using the standard form createPaymentProcess.

**Step 2: Initiate First Recurring Payment**  
● When creating the initial recurring payment, call createTransactionWithToken with the parameter isRecurringDebitPayment=1.  
● Receive the recurring debit code (recurringDebitId) in the response and save it for future use.

**Step 3: Subsequent Recurring Payments**  
● For subsequent runs, send the recurring debit code in the call to createTransactionWithToken under the recurringDebitId parameter.

> 📘
>
> ### Very important!!
>
> ● When making regular non-recurring payments (recurring payment), do not send the direct debit code or the parameter defining premium recurring payments.
>
> Ensure a smooth billing process by adhering to these steps and guidelines. For more details or assistance, refer to our comprehensive documentation. Optimize your payment workflows with Grow Systems' premium recurring payment solutions.

The flow is as following:

![](https://files.readme.io/a6518e3-IMG-20230927-WA0035.jpg)


## Images

- https://files.readme.io/a6518e3-IMG-20230927-WA0035.jpg