---
title: "Response"
slug: response
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/response
---

# Response

## Example Responses:

### *Success:*

JSON

```
{
    "status": 1,
    "err": "",
    "data": {
        "status": "תשלום שזוכה",
        "statusCode": 3,
        "transactionTypeId": "1",
        "paymentType": "2",
        "sum": "2",
        "paymentDate": "14/8/25",
        "description": "Course",
        "fullName": "John Smith",
        "payerPhone": "0500000000",
        "payerEmail": "test@gmail.com",
        "transactionId": "425856",
        "asmachta": "119468739",
        "cardSuffix": "4580",
        "cardType": "Foreign",
        "cardTypeCode": "2",
        "cardBrand": "Visa",
        "cardBrandCode": "3",
        "cardExp": "0541",
        "payerBankAccountDetails": "",
        "refundedTransactionId": 425855
    }
}
```

### *Error:*

JSON

```
{
    "status": 0,
    "err": {
        "id": 210,
        "message": "בוצע זיכוי לעסקה זו, לא ניתן לזכות בשנית."
    },
    "data": ""
}
```

- **status** is referred to success or failure (1 or 0 respectively).
- **err** - in case of an error, would return as the error code and error message.
- **data** - all the details would return here.
