---
title: "Bit SDK Android"
slug: sdk-bit-android-copy
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/sdk-bit-android-copy
---

# Bit SDK Android

**Android SDK Installation:**

1. Add authToken to gradle.properties

**authToken=jp_c34jsq8ncgmv7km89aq1sk2dr5**

2. Add maven to gradle - allprojects - repositories

**maven**
`{ url "[https://jitpack.io"](https://jitpack.io")\ credentials { username authToken}\ }`

![](https://files.readme.io/6d62257-image.png)

**If gradle is version 7.0 or above the following code needs to be inserted in settings.gradle:**

![](https://files.readme.io/12b0623-image.png)

3. Add 'MeshulamSDK' dependency to your gradle:

implementation 'com.github.inManage:MeshulamSDK-Android:1.0.2'

**In case your project uses volley and you're getting a duplicate class error, use implementation below:**

implementation (`com.github.inManage:MeshulamSDK-Android:1.0.2`,
`{ exclude group: "com.android.volley"\ }`)

4. Sync project

Add MeshulamSDK Initialization code:

1. Add import MeshulamSDK to your Class.

`import il.co.inmanage.meshulam_sdk.sdk.MeshulamSdk;`

2. Meshulam Callbacks.

   Contains the following callbacks :

![](https://files.readme.io/382081d-image.png)

After setting up an account you will need to receive the followings from us:  
userId, pageCode, and an apiKey in case required.  
• UserId (required) refers to every business that is connected to Meshulam.  
• ApiKey (required) refers to companies that are working with multiple businesses. In this case, you will need to send both the apiKey and the userId for every transaction that you would like to clear.  
• PageCode (required) is for your API settings at Meshulam. There might be more than one pageCode, for instance, a pageCode for credit card template only and a pageCode for Bit.  
• Sum (required) the amount you want to charge the client with.  
• FullName (required) the full name of the user.  
• Phone (required) the phone num of the user.  
• Email (optional) the email of the user.  
• Description (optional) description of the user.

There are 3 functions that extroversion out for the developer.

• CreatePaymentProcess (required) A function to execute the transaction should pass the necessary parameters to finish the transaction.  
• SettleSuspendedTransaction (optional if) A transaction approval function should pass the necessary parameters to it.  
• CancelBitTransaction (optional if) A transaction cancellation function should pass the necessary parameters to it.

Examples:

• CreatePaymentProcess:  
CreatePaymentData Object :

![](https://files.readme.io/b422fe8-image.png)

Passed to Create Payment Process Method :

![](https://files.readme.io/444875e-image.png)

• SettleSuspendedTransaction:  
GetPaymentData Object:

![](https://files.readme.io/7b16a50-image.png)

Passed to Settle Suspended Transaction Method :

![](https://files.readme.io/800c2f7-image.png)

• CancelBitTransaction:  
GetPaymentData Object:

![](https://files.readme.io/cda6cf4-image.png)

Passed to Cancel Bit Payment Method :

![](https://files.readme.io/9518426-image.png)

• CancelBitTransaction:  
GetPaymentData Object:

![](https://files.readme.io/16d5ad8-image.png)

Passed to Cancel Bit Payment Method :

![](https://files.readme.io/62fc91c-image.png)

Add Debug Mode:

1. In your UIViewController file add debug Mode (debug mode is true by default).

**MeshulamSdk.getInstance(this).setDevMode(false);**


## Images

- https://files.readme.io/6d62257-image.png
- https://files.readme.io/12b0623-image.png
- https://files.readme.io/382081d-image.png
- https://files.readme.io/b422fe8-image.png
- https://files.readme.io/444875e-image.png
- https://files.readme.io/7b16a50-image.png
- https://files.readme.io/800c2f7-image.png
- https://files.readme.io/cda6cf4-image.png
- https://files.readme.io/9518426-image.png
- https://files.readme.io/16d5ad8-image.png
- https://files.readme.io/62fc91c-image.png