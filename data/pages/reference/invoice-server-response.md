---
title: "Invoice Server Response"
slug: invoice-server-response
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/invoice-server-response
---

# Invoice Server Response

## **Invoice Callback**

When using the [createPaymentProcess](https://grow-il.readme.io/reference/post_api-light-server-1-0-createpaymentprocess) API, you can provide the optional parameter invoiceNotifyUrl.

This parameter defines a server callback URL that will be triggered once an invoice is successfully generated for the corresponding transaction.

To enable invoice notifications, include the invoiceNotifyUrl parameter in your [createPaymentProcess](https://grow-il.readme.io/reference/post_api-light-server-1-0-createpaymentprocess) request.  
Once the invoice is generated, Grow will send a server-to-server POST request to the URL you provided.

**Example – Invoice Callback**:

JSON

```
[
  {
    "transactionId": "6111677",
    "processId": "211111",
    "invoiceNumber": "4111",
    "invoiceUrl": "https://meshulam.co.il/s/9aaa8395-1111-bd6b-2df2-2d41354814b1"
  }
]
```

For a detailed example of the API request, please see the API Request Example [Server-to-Server Callback](https://grow-il.readme.io/reference/server-response)
