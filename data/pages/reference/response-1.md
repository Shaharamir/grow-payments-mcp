---
title: "Response get transaction info"
slug: response-1
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/response-1
---

# Response get transaction info

## Example Responses:

### *Success:*

JSON

```
{
    "status": 1,
    "err": "",
    "data": {
        "asmachta": "300000209",
        "cardSuffix": "1234",
        "cardType": "Local",
        "cardTypeCode": "1",
        "cardBrand": "Visa",
        "cardBrandCode": "3",
        "cardExp": "1111",
        "firstPaymentSum": 0,
        "periodicalPaymentSum": 0,
        "status": "שולם",
        "statusCode": 2,
        "transactionTypeId": "1",
        "paymentType": "1",
        "sum": "2",
        "paymentsNum": 0,
        "allPaymentsNum": 1,
        "paymentDate": "21/9/23",
        "description": "test ",
        "fullName": "israeli israel",
        "payerPhone": "0500000000",
        "payerEmail": "",
        "processId": "5000000",
        "processToken": "d088459226b5dbdc8c99c2c2c2c2c",
        "transactionId": "33500000",
        "transactionToken": "ecfd7fe4c8a16a1a1a1a1a1a1a1a1",
        "directDebitId": "19123456",
        "paymentLinkProcessId": "355555",
        "paymentLinkProcessToken": "27bd6f995ca5c10f55d1a1a1a1a1a",
        "recurringDebitId": "20011",
        "customField": []
    }
}
```

### *Error:*

JSON

```
{
    "status": 0,
    "err": {
        "id": 716,
        "message": "פרמטר קוד עסקה או תוקן אינו תקין"
    },
    "data": ""
}
```

- **status** is referred to success or failure (1 or 0 respectively).
- **err** - in case of an error, would return as the error code and error message.
- **data** - all the details would return here.
