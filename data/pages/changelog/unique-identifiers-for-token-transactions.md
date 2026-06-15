---
title: "Unique identifiers for token transactions"
slug: unique-identifiers-for-token-transactions
type: none
section: changelog
source_url: https://grow-il.readme.io/changelog/unique-identifiers-for-token-transactions
---

# Unique identifiers for token transactions

01.11.2023 A new development.

The goal of the development is to block double charges by adding two fields for reading and the possibility to query the transactions that have been carried out.  
For this, we will add two permission fields to the request to create a token transaction:

- **transactionUniqueIdentifier** -  
  . Unique identifier for the request - if we send a value in this field, then a check will be requested that this is the first time we see this value for the business. If it finds that a request with this ID has already been sent, then the current request will be rejected outright regardless of the status of the first request that arrived with this ID.  
  This means that even if one charge request fails, another request cannot be sent with the same ID.  
  If an error is returned to the customer that says "ID with a duplicate", the customer will be able to investigate the transaction according to this ID
- **אtransactionGroupIdentifier** - This field is not unique and will not cause a transaction to be rejected. It will be used for investigation only

get information for token transactions based on a unique identifier that comes in the API call  
The name of the new API method is getTokenTransactionsByExternalIdentifiers  
receives the following parameters:  
userId of the business  
cardToken The token of the card with which the transaction was made  
transactionGroupIdentifier A non-unique transaction identifier  
transactionUniqueIdentifier A unique transaction identifier

Only one of the identifiers can be sent, if both are sent an error will be returned

The response structure is similar to the getPaymentProcessInfo response structure  
The differences are:

- Each transaction has two additional fields:  
  received_time  
  complete_time

An incomplete transaction will contain only the two fields:  
received_time  
complete_time
