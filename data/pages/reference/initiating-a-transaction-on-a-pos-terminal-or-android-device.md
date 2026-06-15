---
title: "Initiating a Transaction on a POS Terminal or Android Device"
slug: initiating-a-transaction-on-a-pos-terminal-or-android-device
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/initiating-a-transaction-on-a-pos-terminal-or-android-device
---

# Initiating a Transaction on a POS Terminal or Android Device

> This guide explains how to send a transaction from the merchant’s system to a target device in order to complete a payment.

Grow supports initiating payments directly on a payment device or Android payment app through an API request.  
It is designed for physical checkout scenarios where the transaction details are sent to the device and the customer can complete the payment.

Businesses can reduce manual entry at the counter and keep the payment amount, order details, and checkout flow aligned.

Unlike standard online payment flows, this setup focuses on in-person card-present payments, including credit card tap payments and digital wallets.

The transaction is sent by calling [createPaymentProcess](https://grow-il.readme.io/reference/post_api-light-server-1-0-createpaymentprocess) and passing a dedicated pageCode together with the deviceKey of the device that should receive the transaction.

After the call, a url is returned.  
Opening this url sends the transaction to the target device so the payment can continue there.

This guide covers two flows:

- Sending a transaction to a Grow POS terminal
- Sending a transaction to an Android device with the GROW app

## Before You Begin

Before sending a transaction, the initial setup must be completed according to the target device type.

### Sending a Transaction to an Android Device with the GROW App

Before getting started:

1. Purchase the Touch service
2. Contact our support team to receive the deviceKey for the app

### Sending a Transaction to a POS Terminal

Before getting started:

1. Purchase the POS terminal
2. Wait for the terminal to arrive
3. After receiving it, contact our support team to receive the deviceKey for the terminal

## Prerequisites

Before starting, make sure that:

- The service has been purchased and enabled for the merchant
- A deviceKey has been received for the target device or app
- A dedicated pageCode for this flow has been received

## Shared Flow

The following steps are the same for both POS terminal and Android device flows.

### 1. Prepare the Target Device

Prepare the device that will receive the transaction:

- For Android devices: open the GROW app and leave it open on the home screen
- For POS terminals: open the "Masofon Slikah"/"מסופון סליקה" app and leave it open and ready to receive the transaction

This step must be completed **before** opening the link.

### 2. Send the createPaymentProcess Request

Send a [createPaymentProcess](https://grow-il.readme.io/reference/post_api-light-server-1-0-createpaymentprocess) request with:

- A dedicated pageCode
- The deviceKey of the selected target device

### 3. Open the URL Returned in the Response

After the call, a url will be returned.  
Open the url, and the transaction will then be sent to the target device.

### 4. Complete the Payment

Once the transaction has been sent to the device, the payment can be completed directly on that device.

### 5. Receive the Server Update

At the end of the process, a [server update](https://grow-il.readme.io/reference/server-response) will be sent to confirm that the transaction has been completed.

### 6. Call Approve

After receiving the server update, call [Approve](https://grow-il.readme.io/reference/post_api-light-server-1-0-approvetransaction-4) to confirm that the update was received.

Important Notes

- Open the relevant app on the target device **before** opening the url.
- The url must be opened on a **different** device than the one used to complete the payment.
- Do not close the link until the process is complete.
- Multiple deviceKey values can be supported, so the merchant can choose which device to send the transaction to.
- This flow is available only in the live environment.
- When sending a transaction to an Android device with the GROW app, physical card tap transactions are limited to amounts of up to 300 ILS, while digital wallet transactions are not limited in amount.
