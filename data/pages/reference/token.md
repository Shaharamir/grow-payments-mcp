---
title: "Token"
slug: token
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/token
---

# Token

Grow Tokenization allows businesses to securely save a customer’s card as a token and use it for future credit card charges.

It is needed when payments repeat over time, amounts may change, or the customer should not re-enter payment details for every transaction.

The customer pays once and the payment method is securely saved as a token for future use.
After that, one-time or recurring charges can be made with the token, without asking the customer to enter card details again.

### Charging with Tokens

Customers that are authorized to make transactions by using a token would be able to make a transaction by using a credit card token.  
credit card token would be received after making the transaction via payment form (Server to Server update),**cardToken field.**  
You will need to send the transaction’s details such as paymentType, paymentNum, sum, etc.

You will need to send the transaction’s details such as paymentType, paymentNum, sum, etc.

paymentType Parameter Codes Table

| Code | Description |
| --- | --- |
| 1 | Recurring Payments |
| 2 | Regular |
| 4 | Payments |

Token Management with Grow: Empowering Seamless Transactions  
Effortlessly manage your customers' transactions with tokenization, providing a secure and efficient way to handle ongoing charges.  
Here's what you can achieve with Grow's token feature:

**Key Features:**  
● Save Token :  
Save credit card tokens for your customers securely, eliminating the need for entering credit card details with each charge.

● Manage Your Charging:  
Charge customers independently using saved tokens, streamlining ongoing transaction management.

> 📘
>
> ### Important Note:
>
> You must not reveal any inner transaction’s identification details to the paying customer such as transactionId and token.  
> You may reveal the asmachta value in order to make a unique identification of the transaction.

## Tokenization - recurring payments

● **recurring payment with Tokens:**

1. ```
   Managed By Us:
   ```We will automatically charge the customer every month according to the defined amount and number of charges sent in the creation of the recurring payment.
   ```
2. Managed Your Charging:  
   Implement and manage recurring payment independently using a saved token for monthly billing.

● **Payment Options:**

1. Recurring Payment with Token
2. Premium Recurring Payment with Token

This section is for the companies or systems who wish to manage their own billing system.

> 📘
>
> ### Note:
>
> ● Permission Requirement: Working with tokens requires permission from Grow.
>
> ● Payment or Token-only Option: Choose whether the customer will make a payment and save the token or only save the token without immediate payment (not applicable to Bit, Apple Pay, or Google Pay).
>
> ● Billing Management: Token usage puts billing system management in your hands, utilizing your database, etc.

> ❗️
>
> ### Importent:
>
> Handling Tokenized Charge Errors:  
> If a tokenized charge encounters a final error (e.g., card expired, stolen card), cease charging the token, delete it, and update the customer's new card number.

### you can make recurring payment with token , you have 3 options

for more information about the different about manging the billing - [press here](https://grow-il.readme.io/reference/recurring-vs-token)

1+2- **Recurring payment that managed by Grow** -( if you have the primum service the recurring will be premium if don't it will be regular)

![](https://files.readme.io/d7a20b4-image.png)

3**Managed by You: Independently manage recurring payments.**

![](https://files.readme.io/3f79fdc-image.png)
  
  
> 📘
>
> ### Additional Insights:
>
> ● Token Duration: Tokens can be saved for up to 180 payments, offering flexibility in transaction planning.

## Optional Error Details:

JSON

```
{  
    "err": {  
        "id": 103,  
        "message": "כרטיס גנוב - עסקה לא מאושרת"  
    },  
    "status": 0,  
    "data": ""  
}
```

פירוט שגיאות אופציונליות לחיוב טוקן לא תקין.

|  |  |  |
| --- | --- | --- |
| [message] => כרטיס פג תוקף. | [id] => 103 | סופי |
| [message] => כרטיס גנוב - עסקה לא מאושרת | [id] => 103 | סופי |
| [message] => כרטיס חסום - עסקה לא מאושרת | [id] => 103 | סופי |
| [message] => חברת האשראי לא אשרה את העסקה | [id] => 103 | לא סופי |
| [message] =>כרטיס האשראי אינו פעיל/פג תוקף, נא לפנות ללקוח לקבלת כרטיס חדש | [id] =>451 | סופי |
| [message] => חסימת מערכת | [id] =>453 | סופי |
| [message] =>חברת האשראי חסמה את הכרטיס, נא לפנות ללקוח לבדיקה | [id] =>452 | סופי |

[Try it yourself](https://grow-il.readme.io/reference/overview-4)

● For advanced recurring payment services (premium), request specific permissions from Grow.  
● For detailed error codes and handling, refer to the optional error details. Experience the convenience and control of seamless transactions with Grow's token management, ensuring secure and efficient recurring payments.


## Images

- https://files.readme.io/d7a20b4-image.png
- https://files.readme.io/3f79fdc-image.png