---
title: "Testing Environment"
slug: testing-environment
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/testing-environment
---

# Testing Environment

Grow’s Testing Environment helps businesses validate their payment setup before moving to Production environment. The Sandbox is used to run mock credit card transactions, check payment behavior, and confirm that the flow works correctly.

By following these guidelines, you can reduce payment errors and move to production with greater confidence.

  

## Testing Environment Guidelines

To facilitate a smooth integration and testing process, please follow the guidelines below.

---

# Environments

Grow supports two environments:

1. **Sandbox** - The test environment.
2. **Production** - The live environment.

Each environment has its own unique identifiers, such as `pageCode`, `userId`, and `apiKey`, if relevant to your integration.

Make sure to use the correct identifiers for the relevant environment.

---

# Sandbox URL

Use the following URL for testing purposes:

<https://sandbox.meshulam.co.il/api/light/server/1.0/>

  

---

# Credit Card Numbers for Test Transactions

Use the following credit card numbers exclusively for testing purposes in the Sandbox environment:

- `4580458045804580` - Valid for regular single-payment transactions only. Suitable for testing failed transactions in multiple payments.
- `4580000000000000`
- `4580111111111121`

---

# Bank Transfer Test Details

Use the following bank account details for testing bank transfer payments in the Sandbox environment:

- **Bank:** `41`
- **Branch:** `410`
- **Account:** `411111111`

---

# Important Notes

- Bit, Google Pay, and Apple Pay do not have a dedicated test environment.  
  Transactions made using these payment methods are processed in the Live environment and will be charged as real transactions.
- PayBox payments cannot be completed in the Sandbox environment.  
  PayBox is available only in the Production environment.
- Each environment has its own unique identifiers, such as `pageCode`, `userId`, and `apiKey`, if relevant to your integration.
- The Live environment will be provided only after successful completion of development and testing by Grow.

---

By following these testing environment guidelines, you can ensure a reliable and efficient integration process with Grow's payment platform.
