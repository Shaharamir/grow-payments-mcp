---
title: "Response"
slug: response-3
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/response-3
---

# Response

## Response from createPaymentProcess example:

### *Success*:

JSON

```
{
    "status": 1,
    "err": "",
    "data": {
        "processId": 6652,
        "processToken": "ac3f4d3b656d3245454512c5ff33d7030",
				"authCode": "eabbb670ece7f311524f25454c14356d%MjA2MTAzODc"
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

*You must NOT reveal the process details such as the**processId** and the **processToken** to the paying customer.  
You may display the **asmachta** field for unique identification of the transaction.*
