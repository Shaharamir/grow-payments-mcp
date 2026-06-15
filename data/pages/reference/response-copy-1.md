---
title: "Response"
slug: response-copy-1
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/response-copy-1
---

# Response

## *Response example:*

### *Success*:

JSON

```
{
    "status": 1,
    "err": "",
    "data": {
        "asmachta": "111111111",
        "cardSuffix": "1234",
        "cardType": "Local",
        "cardTypeCode": "1",
        "cardBrand": "Visa",
        "cardBrandCode": "3",
        "cardExp": "1123",
        "firstPaymentSum": "0",
        "periodicalPaymentSum": "0",
        "status": "שולם",
        "statusCode": "2",
        "transactionTypeId": "1",
        "paymentType": "2",
        "sum": "3",
        "paymentsNum": "0",
        "allPaymentsNum": "1",
        "paymentDate": "22/8/23",
        "description": "תיאור",
        "fullName": "לקוח לקוח",
        "payerPhone": "0500000000",
        "payerEmail": "test@gmail.com",
        "transactionId": "12345678",
        "transactionToken": "e500ce83e0000e82f72fded24efc000"
    }
}
```

### *Failure*:

JSON

```
{
    "status": 0,
    "err": {
        "id": 819,
        "message": "אין באפשרותך לבצע תשלום כעת  \נסה בשלב יותר מאוחר"
    },
    "data": ""
}
```

- **status** is referred to success or failure (1 or 0 respectively).
- **err** - in case of an error, would return as the error code and error message.
- **data** - all the details would return here.

## ***Important!***

*You must NOT reveal the process details such as the**processId** and the **processToken** to the paying customer. You may display the **asmachta** field for unique identification of the transaction.*
