---
title: "Response get payment process info"
slug: response-get-transaction-info-copy
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/response-get-transaction-info-copy
---

# Response get payment process info

## Example Responses:

### *Success:*

JSON

```
{
    "status": 1,
    "err": "",
    "data": {
        "processId": "1234122",
        "processToken": "dc4de4d5ae45cc22dbb7s2s5s1s2s5s4s1",
        "customField": [],
        "transactions": [
            {
                "asmachta": "30012345",
                "cardSuffix": "1234",
                "cardType": "Local",
                "cardTypeCode": "1",
                "cardBrand": "Visa",
                "cardBrandCode": "3",
                "cardExp": "1120",
                "firstPaymentSum": "0",
                "periodicalPaymentSum": "0",
                "status": "שולם",
                "statusCode": "2",
                "transactionTypeId": "1",
                "paymentType": "2",
                "sum": "3",
                "paymentsNum": "0",
                "allPaymentsNum": "1",
                "paymentDate": "24/9/23",
                "description": "תיאור",
                "fullName": "לקוח לקוח",
                "payerPhone": "0500000000",
                "payerEmail": "tst@test.com",
                "cardToken": "e18ec3fa5dd331d0f030ss5d5d4ds5s5d41d",
                "transactionId": "33123456",
                "transactionToken": "9ac26ed383f9c1e7e8absds54ds54s8d"
            }
        ]
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
```

- **status** is referred to success or failure (1 or 0 respectively).
- **err** - in case of an error, would return as the error code and error message.
- **data** - all the details would return here.
