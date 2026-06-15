---
title: "Supported Payment Method"
slug: payments
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/payments
---

# Supported Payment Method

> Accepted Payment Methods

Explore Grow payment methods and how each one fits into real-world checkout and payment flows.

Grow brings together leading payment methods in one place, making it easier to offer customers the payment experience they prefer. Businesses can choose the right payment option for each scenario, from credit card payments to Apple Pay, Google Pay, Bit, PayBox, and bank transfers.
Each method has its own capabilities, such as one-time payments, recurring charges, tokenization, refunds, direct debit, and J5/J4 support.
By comparing these options in one place, businesses can plan smoother payment experiences and match each payment flow to their needs.

# Payment options

Discover various payment options with Grow Payment Solutions:

## Credit Card regular payments

- [Supports J5J4](https://grow-il.readme.io/reference/overview-2).
- [Tokenization is available](https://grow-il.readme.io/reference/token).
- [3DS authentication is possible](https://grow-il.readme.io/reference/3ds-1).
- Typically, the transaction limit for credit card payments is up to 20,000 NIS for a single transaction and 40,000 NIS for instalment transactions, subject to each business's commercial terms .

## Bit

- No tokenization available for Bit transactions
- Limited to single regular payments; multiple payments and direct debit are not allowed.
- Maximum transaction amount is 5,000 NIS.
- [Supports J5J4](https://grow-il.readme.io/reference/overview-2)
- There is no testing environment for testing BIt You can test this only in Live environment.

## Google Pay

- No tokenization via Google Pay.
- [Supports J5J4](https://grow-il.readme.io/reference/overview-2)
- There is no testing environment for testing Google Pay. You can test this only in Live environment.
- The GooglePay payment must be displayed in the Chrome browser on Android only.

## Apple Pay

***Important***:

- There is no testing environment for testing Apple pay. You can test this only in Live environment.
- Apple Pay should be opened in Safari browser in a new tab (not in an IFrame). [Domain approval](https://grow-il.readme.io/reference/sdk-apple) is required if opened in an IFrame.
- No tokenization via Apple Pay.
- [Supports J5J4](https://grow-il.readme.io/reference/overview-2)

Please note specific considerations for each payment method. Testing environments may vary, and it's crucial to adhere to the specified conditions for each payment option.
