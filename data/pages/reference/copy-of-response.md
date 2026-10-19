---
title: "Response Example"
slug: copy-of-response
type: basic
section: reference
source_url: https://developers.grow.business/reference/copy-of-response
---

# Response Example

## Response from approveTransaction example:

### *Success*:

JSON

```
{
    "err": "",
    "status": 1,
    "data": "",
    "message": ""
}
```

### *Failure*:

JSON

```
{
    "err": {
        "id": 701,
        "message": "פרמטר קוד זיהוי אינו תקין: "
    },
    "status": 0,
    "data": ""
}
```

- - **status** is referred to success or failure (1 or 0 respectively).
- **err** - in case of an error, would return as the error code and error message.
- **data** - all the details would return here.

## ***Important!***

*You must NOT reveal the process details such as the****processId*** *and the* ***processToken*** *to the paying customer.*  
*You may display the* ***asmachta*** *field for unique identification of the transaction.*
