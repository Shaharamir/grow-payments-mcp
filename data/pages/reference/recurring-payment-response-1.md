---
title: "Response"
slug: recurring-payment-response-1
type: basic
section: reference
source_url: https://developers.grow.business/reference/recurring-payment-response-1
---

# Response

## *Response example:*

### *Success*:

JSON

```
{
    "status": 1,
    "err": "",
    "data": ""
}
```

### *Failure*:

JSON

```
{
    "status": 0,
    "err": {
        "id": 801,
        "message": "קוד זיהוי עסק אינו תקין"
    },
    "data": ""
}
```

- **status** is referred to success or failure (1 or 0 respectively).
- **err** - in case of an error, would return as the error code and error message.
- **data** - all the details would return here.

## ***Important!***

*You must NOT reveal the process details such as the**processId** and the **processToken** to the paying customer. You may display the **asmachta** field for unique identification of the transaction.*
