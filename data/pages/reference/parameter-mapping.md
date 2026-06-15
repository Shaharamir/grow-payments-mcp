---
title: "Parameter Mapping"
slug: parameter-mapping
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/parameter-mapping
---

# Parameter Mapping

> Parameters details

Parameter Mapping Guide for Seamless Integration  
For a smooth integration with Grow's payment solutions, understanding parameter details is crucial. Here's a comprehensive mapping guide:

## CardBrandCode

|  |  |
| --- | --- |
| Mastercard | 2 |
| Visa | 3 |
| Isracard | 5 |
| Diners | 8 |
| Discover | 7 |

## CardType

|  |  |
| --- | --- |
| Foreign | 2 |
| Fuel | 3 |
| Gift/Rechargable | 5 |
| Local | 1 |

## PaymentType

|  |  |
| --- | --- |
| Direct Debit (הוראת קבע) | 1 |
| Regular | 2 |
| Payments | 4 |

## TransactionTypeId

|  |  |
| --- | --- |
| Credit card | 1 |
| Bit | 6 |
| Apple Pay | 13 |
| Google Pay | 14 |
| Bank Transfer | 15 |
| Paybox | 5 |

## StatusCode

|  |  |
| --- | --- |
| Canceled before transmission | 4 |
| paid | 2 |
| Transaction denied | 9 |
| Refund transaction | 6 |
| Not paid | 0 |

These parameter details are essential for interpreting transaction information and ensuring accurate communication between your system and Grow's payment platform. Use this mapping guide to enhance the efficiency and reliability of your integration process.
