---
title: "Response"
slug: response-copy-3
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/response-copy-3
---

# Response

> CreatePaymentLink

## Response from createFarPaymentProcess example:

### *Success*:

JSON

```
{
    "status": 1,
    "err": "",
    "data": {
        "paymentLinkProcessId": 6652,
        "paymentLinkProcessToken": "ac3f4d3b656d3245454512c5ff33d7030",
        "url": "https://sandbox.meshulam.co.il/payment_link?l=a994875846565656199971473385ac5b3"
    }
}
```

### *Failure*:

JSON

```
{
    "err": {
        "id": 54,
        "message": "חסרים נתונים:pageCode"
    },
    "status": "0",
    "data": ""
}
```

- - **status** is referred to success or failure (1 or 0 respectively).
- **err** - in case of an error, would return as the error code and error message.
- **data** - all the details would return here.

## ***Important!***

*You must NOT reveal the process details such as the**processId** and the **processToken** to the paying customer. You may display the **asmachta** field for unique identification of the transaction.*
