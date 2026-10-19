---
title: "Webhook Field Mapping"
slug: webhook-field-mapping
type: basic
section: docs
source_url: https://developers.grow.business/docs/webhook-field-mapping
---

# Webhook Field Mapping

> This page lists the possible values of webhook fields and explains their meaning.

transactionType

The transactionType field indicates the payment method used for the transaction. The values below are shown exactly as returned in the webhook payload.

  

| Key | Value | Payment Method |
| --- | --- | --- |
| transactionType | אשראי | Credit Card |
| transactionType | Bit | Bit |
| transactionType | PayBox | PayBox |
| transactionType | Gpay | Google Pay |
| transactionType | ApplePay | Apple Pay |
| transactionType | העברה בנקאית | Bank Transfer |

Note: This mapping applies only to webhook payloads that contain the transactionType field.

  

Example

JSON

```
{ 
  "webhookKey":"ABC1234", 
  "transactionCode":"ABCD1234", 
  "transactionType":"אשראי",
  "paymentSum":2.00, 
  "paymentsNum":1, 
  "allPaymentNum":2, 
  "firstPaymentSum":1, 
  "periodicalPaymentSum":1, 
  "paymentType":"רגיל", 
  "paymentDate":"14/10/21",
  "asmachta":"123456789", 
  "paymentDesc":"Description",
  "fullName":"Full Name", 
  "payerPhone":"0500000000", 
  "payerEmail":"test@test.com", 
  "cardSuffix":"1234", 
  "cardBrand":"Mastercard", 
  "cardType":"Local", 
  "paymentSource":"מערכת חיצונית"
}
```

  

In this example, the payment was made using a credit card.
