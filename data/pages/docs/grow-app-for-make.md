---
title: "Grow App for Make"
slug: grow-app-for-make
type: basic
section: docs
source_url: https://grow-il.readme.io/docs/grow-app-for-make
---

# Grow App for Make

## Overview

The Grow app for Make allows you to automate payment flows using Grow’s payment services directly from your Make scenarios.

Using the Grow app, you can create payment links, send payment requests to customers by SMS or email, retrieve payment link details, and approve transaction notifications after a payment is completed.

This integration is useful for businesses that want to automate payment collection as part of a larger workflow, such as customer onboarding, order processing, billing flows, CRM automations, or internal operational processes.

## Before You Start

Before connecting Grow to Make, make sure you have:

- An active Grow account
- A Make account
- The business identification number associated with your Grow account, such as company ID or ID number
- A mobile phone number that is linked to the Grow account
- Access to the mobile phone in order to complete the OTP verification process

You do not need to provide a userId or pageCode when connecting through Make.  
The connection is created using the business identifier and the mobile phone number linked to the Grow account.

## Create a Grow Connection in Make

To connect Grow to Make:

1. Log in to your Make account.
2. Create a new scenario, or open an existing scenario.
3. Click the plus button to add a new module.
4. Search for **Grow**.
5. Select the required Grow action.
6. Click **Create a connection**.
7. Select the required connection type:
   - **Grow** for the production environment
   - **Grow Sandbox** for the test environment
8. Enter the business identifier associated with your Grow account, together with the mobile phone number linked to the same account.
9. Click **Save**.
10. A pop-up window will open.  
    Enter the OTP verification code sent to the mobile phone.

After the verification is completed, the Grow connection will be created and available in your Make scenario.

## Sandbox and Production Environments

When creating a connection, you can choose between the production environment and the sandbox environment.

Use **Grow Sandbox** for testing purposes.

In the sandbox environment, credit card payments can be tested without an actual card charge.  
However, external payment methods such as Bit, Apple Pay, Google Pay, PayBox, or other wallets may create a real charge even when used in the sandbox environment.

If a payment is completed using an external wallet during testing, it may be processed as an actual charge and should be refunded if needed.

### Credit Card Numbers for Test Transactions

Use the following credit card numbers exclusively for testing purposes in the sandbox environment:

- `4580458045804580` - Valid for regular single-payment transactions only.  
  Suitable for testing failed transactions in multiple payments.
- `4580000000000000`
- `4580111111111121`

Use **Grow** for production payments.

Make sure you select the correct environment when creating the connection.  
If a payment was created in the sandbox environment, it will not appear as a production transaction in the merchant account.

## Available Actions

The Grow app includes several actions that can be used in Make scenarios.

| Action / Trigger | Description |
| --- | --- |
| Create Payment Link | Creates a payment request or a one-time payment page |
| Get Payment Link Info | Retrieves information about an existing payment link |
| Approve Transaction | Confirms that a transaction notification was received successfully |
| Settle Suspended Transaction | Captures a previously authorized transaction |
| Refund Transaction | Creates a full or partial refund for an existing transaction |
| Notify URL Webhook | Receives transaction notifications from Grow and can be used to trigger additional Make scenario steps |
| Make an API Call | A generic Make module required by Make.  Not required for the standard Grow payment flow. |

  

## Create a Payment Link

The **Create Payment Link** action creates a payment page and returns a payment URL.  
The payment request can be sent automatically to the customer by SMS or email, or created without automatic delivery so you can use the payment URL independently in your own flow.

### How to Create a Payment Link

To create a payment link:

1. Add the **Create Payment Link** action to your Make scenario.
2. Select the relevant Grow connection.
3. Choose the sending mode.
4. Fill in the required payment details.
5. Fill in the customer details, such as full name and phone number.
6. Configure any additional payment settings if needed.
7. Click **Save**.
8. Click **Run once** to test or run the scenario.

After the module runs successfully, the payment request will be created. If a sending mode such as SMS or email was selected, the payment request will be sent to the customer.

### Create Payment Link Fields

| Field | Required | Description |
| --- | --- | --- |
| Sending Mode | Yes | Defines how the payment request will be delivered to the customer.  Available options: `sms`, `mail`, or `none`. Select `none` if you want to create the payment link without sending it automatically. |
| Full Name | Yes | The customer's full name.  Enter first name and last name, each with at least 2 characters. |
| Phone | Yes | A valid Israeli mobile phone number. Example: `0500000000`. |
| Email | Depends on configuration | The customer's email address.  Required only if the payment request should be sent by email. |
| Invoice Name | Depends on configuration | Defines whether the customer will be required to enter their name for the invoice. Available options: `required` or `optional`. |
| Invoice License Number | Depends on configuration | Defines whether the customer will be required to enter their ID number or company number for the invoice.  Available options: `required` or `optional`. |
| Charge Type | Yes | Defines the transaction charge type. Available options: `regular charge` or `J4/J5` authorization. |
| Success URL | No | An external thank you page URL. If provided, the customer will be redirected to this URL after a successful payment. The URL must use HTTPS, must be an external URL, and cannot be localhost. Example: `https://mysite.co.il?success=true`. |
| Thank Page Title | No | The title displayed on Grow's thank you page.  This is used only when no external Success URL is provided. |
| Thank Page Description | No | The description displayed on Grow's thank you page.  This is used only when no external Success URL is provided. |
| Invoice Notify URL | No | A webhook URL used to receive invoice-related notifications. |
| Notify URL | Yes | A webhook URL used to receive payment status updates.  The URL must use HTTPS, must be an external URL, and cannot be localhost. Example: `https://mysite.co.il/webhook`. |
| Title | Yes | The title of the payment link. This title will be displayed to the customer. |
| Payment Type | Yes | Defines the payment flow.  Select `recurring payment` for a recurring payment page.  Select `payments` for a one-time payment page with 1-12 payments. |
| Products | Yes | A list of product items. Each product item includes the fields listed below and will be displayed on the payment page and reflected in the invoice. |
| Custom Field 1 | No | Optional custom field that can be used to pass an internal identifier or additional data. |
| Custom Field 2 | No | Optional custom field that can be used to pass an internal identifier or additional data. |

### Products Fields

The **Products** field is an array of product objects.  
Each item represents a product that will be displayed on the payment page and reflected in the invoice.

| Field | Required | Description |
| --- | --- | --- |
| Catalog Number | No | The product catalog number or SKU. |
| Product Name | Yes | The product name. |
| Price | Yes | The product price. |
| Quantity | Yes | The product quantity. |
| Minimum Quantity | No | The minimum quantity that can be selected for the product, when relevant. |
| Product URL | No | A URL to the product image.  Supported formats: PNG or JPEG.  Maximum file size: 2 MB. Minimum dimensions: 60x60 px.  Required aspect ratio: 1:1. |
| VAT Type | Yes | Defines the VAT type for the product.  Available options: `regular VAT` or `VAT exempt`.  If the product is VAT exempt, select `VAT exempt` |

  

## Notify URL Webhook

The **Notify URL Webhook** is used to receive transaction status updates from Grow after a payment is completed or updated.

When creating a payment link, the webhook endpoint should be provided in the **Notify URL** field.  
Grow will send an HTTPS server-to-server callback to this URL with the transaction status and payment details.

After receiving the notification, you should execute the **Approve Transaction** action.  
This action confirms that your system received the server notification and is aware of the transaction status.

Please note: the transaction will still be processed even if the **Approve Transaction** action is not executed or fails. However, if the notification is not approved, Grow may continue sending additional notifications for the same transaction.

### Retry Behavior

If Grow does not receive confirmation that the notification was received, additional notification attempts may be sent for the same transaction.

The retry attempts are sent in intervals of approximately 10, 20, and 30 minutes.

### Testing the Webhook

You can test the server-to-server callback using the `updateMyUrl` endpoint in the sandbox environment.

This endpoint simulates a callback notification by sending an HTTP request to the URL you provide, allowing you to verify that your endpoint receives and handles the notification correctly.

Example:

Text

```
https://sandbox.meshulam.co.il/api/light/server/1.0/updateMyUrl/?url=MySiteURL
```

## Approve Transaction

The **Approve Transaction** action is used to confirm that a transaction notification was received successfully.

This action should be executed after receiving a transaction status update through the **Notify URL Webhook**.

If the notification is not approved, Grow may continue sending additional notifications for the same transaction.

## Refund Transaction

The **Refund Transaction** action allows you to create a full or partial refund for an existing transaction.

Use this action when you need to return funds to the customer after a payment was completed.

Please note:

- On the same day the transaction was created, only a full refund can be performed.
- A partial refund can only be performed from the day after the transaction was created.

The refund must be performed according to the original transaction details and the permissions available for the merchant account.

## Settle Suspended Transaction

The **Settle Suspended Transaction** action is used to capture a previously authorized transaction.

This is relevant when the original transaction was created using a J4/J5 authorization flow, where the amount is authorized first and captured later.

Use this action only for transactions that were created as suspended or authorized transactions and are eligible for settlement.

## Limitations

Some actions and settings are not managed through the Grow app for Make.

- recurring payment cancellation cannot currently be performed through Make.  
  It should be handled through the Grow website.
- The business logo can be configured only through the Grow website.
- Existing payment links cannot be edited directly through Make after they are created.  
  Updates to an existing link should be made through the Grow interface.
- The **Make an API Call** module is a generic Make module and is not required for the standard Grow payment flow.

## FAQ

### I can’t connect my Grow account to Make. What should I check?

If you are unable to create a Grow connection in Make, first make sure you entered the correct details:

- Enter the business identifier associated with the Grow account, such as ID number, company ID, or business registration number.
- Do not enter the business bank account number as it appears in Grow.
- Enter the mobile phone number used for logging in to the Grow interface.

If you are still unable to connect after checking these details, please contact Grow support.  
The account status or the phone number configured for login may need to be verified by Grow.

### Why does the business name show MAKE?

If the business name appears as **MAKE**, it usually means the transaction was created in the sandbox environment.

### Why can’t I see a transaction I created in Make?

Make sure the transaction was not created in the sandbox environment.  
Transactions created in the sandbox environment will not appear as production transactions in the merchant account.

### How do I switch from sandbox to production?

To work in production, create or select a connection using **Grow** instead of **Grow Sandbox**.

The environment is selected when creating the Grow connection in Make.

### How do I create a refund through Make?

Use the **Refund Transaction** action.

Please note:

- On the same day the transaction was created, only a full refund can be performed.
- A partial refund can only be performed from the day after the transaction was created.

### Why can’t I send the VAT exempt parameter in the sandbox environment?

The sandbox environment uses a test account that is configured with VAT.  
Therefore, VAT exempt behavior should be tested in the production environment using the actual merchant account configuration.

### How do I use the Make an API Call module?

The **Make an API Call** module is a generic module required by Make for API-based apps.

It is not required for the standard Grow payment flow.

### Can I stop or cancel a recurring payments through Make?

No. recurring payments cancellation cannot currently be performed through the Grow app for Make.

To stop or cancel a direct debit, use the Grow website.

### How do I define a webhook URL for transactions created through Make?

Use the **Notify URL** field in the **Create Payment Link** action.

Grow will send transaction status updates to the URL provided in this field.

### How do I configure the business logo?

The business logo can be configured through the Grow website.

### Can I change product images through Make?

Product images are defined as part of the product details when creating the payment link.

After the payment link is created, existing payment links cannot be edited directly through Make.  
To update an existing payment link, including product details or product images, use the Grow interface.

### Do I need `userId` and `pageCode` to connect Grow to Make?

No.  
When connecting through Make, you do not need to provide `userId` or `pageCode`.  
The connection is created using the business identifier and the mobile phone number linked to the Grow account.

### I created a transaction in the sandbox environment, but I see a card charge. Why?

In the sandbox environment, credit card payments can be tested without an actual card charge.

However, payments completed through external wallets such as Bit, Apple Pay, Google Pay, PayBox, or other wallets may be processed as actual charges.

If needed, these transactions should be refunded through the Grow system.

### How can I receive updates for each recurring payment attempt or failure?

Updates for recurring payment attempts and failures are sent through Grow webhooks.

To receive these updates, add and configure a webhook in the Grow interface.

For more information, see:  
<https://grow-il.readme.io/docs/webhooks>
