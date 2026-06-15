---
title: "Approve Transaction"
slug: approve-transation
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/approve-transation
---

# Approve Transaction

The Approve Transaction step confirms that Grow’s server update was received after a payment is completed.

Grow uses this unique approval flow to make sure the business has acknowledged the transaction details and status.

It helps keep the payment process synchronized between Grow and the business, so each successful transaction is clearly recognized and handled.

When Grow consistently does not receive these acknowledgments, Grow will resend the server update up to 5 additional times. If acknowledgments are still not received, Grow may contact the business to confirm that everything is working properly and that transactions are being handled correctly.

# Approve Transaction

**Upon the completion of the payment process, it is crucial to inform Grow that a response has been received and the transaction process was successfully completed.**  
Transaction Approval Method:  
To officially approve the transaction, utilise the approveTransaction method at the conclusion of the process. This step involves sending the pageCode and all data received frome the server update.

Important Notes:  
● This step does not alter the transaction status nor does it cancel or approve it; the charging process proceeds as planned.  
● It is a critical component of the overall process and must be performed for every successful transaction.  
● Do not send this request in the case of token transactions (created with createTransactionWithToken) or delayed transactions (J4J5), or for save token only scenarios.

For a detailed example of the API request, please see the API Request Example [Approve Transaction](https://grow-il.readme.io/reference/post_api-light-server-1-0-approvetransaction-4).
