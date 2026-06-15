---
title: "New invoice features"
slug: new-development-invoice-items-in-api-call
type: none
section: changelog
source_url: https://grow-il.readme.io/changelog/new-development-invoice-items-in-api-call
---

# New invoice features

01.11.2022 New development of invoice items in API call

Using the new development, it is possible to edit items for the invoice within the call for payment in the API:  
**The new parameters for editing:**

1. productData[price] = product price
2. productData[quantity]= Product quantity
3. productData[0][itemDescription]= Product description
4. productData[0][catalogNumber]= barcode number
5. productData[0][vatType] = VAT Type:  
   Tax exemption = 3  
   Before VAT = 2  
   including VAT = 1 (dipulative)

In addition, you can also set the name for the invoice using parameter

pageField[invoiceName] = edit invoice name.
