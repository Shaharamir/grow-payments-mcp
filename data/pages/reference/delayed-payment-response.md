---
title: "Response"
slug: delayed-payment-response
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/delayed-payment-response
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
      	"processId":"734754",
      	"processToken":"2153287cd9af46457ae842337250b78d",
      	"url":"https://sandbox.meshulam.co.il/far?l=89a71a421b8e0686024fbb762dab61e1"
    	}
    }
```

### *Failure*:

JSON

```
  {
    "err": {
        "id": 54,
        "message": "חסרים שדות חובה: pageCode"
    },
    "status": 0,
    "data":""
    }
```

- **status** is referred to success or failure (1 or 0 respectively).
- **err** - in case of an error, would return as the error code and error message.
- **data** - all the details would return here.

## ***Important!***

*You must NOT reveal the process details such as the**processId** and the **processToken** to the paying customer. You may display the **asmachta** field for unique identification of the transaction.*
