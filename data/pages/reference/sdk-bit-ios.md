---
title: "Bit SDK IOS"
slug: sdk-bit-ios
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/sdk-bit-ios
---

# Bit SDK IOS

**iOS SDK Installation:**

1. Run 'pod init' command from the terminal in your project directory.
2. Open the Podfile file.
3. Add 'MeshulamSDK' dependency to your Podfile
4. Run 'pod install command from the terminal in your project directory.

![](https://files.readme.io/3f922ae-image.png)

Add MeshulamSDK Initialization code:

1. Add import MeshulamSDK to your UIViewController.

Swift: import MeshulamSDK

Objective-C: #import <MeshulamSDK/MeshulamSDK-Swift.h>

2. Add Meshulam Delegate.

   Swift , Objective-C: MeshulamDelegate

Swift: Protocol

![](https://files.readme.io/a67958d-image.png)

Objective-C: Protocol

![](https://files.readme.io/ce3b491-image.png)

After setting up an account you will need to receive the followings from us:  
userId, pageCode, and an apiKey in case required.  
• UserId (required) refers to every business that is connected to Grow.  
• ApiKey (required) refers to companies that are working with multiple businesses. In this case, you will need to send both the apiKey and the userId for every transaction that you would like to clear.  
• PageCode (required) is for your API settings at Grow. There might be more than one pageCode, for instance, a pageCode for credit card template only and a pageCode for Bit.  
• Sum (required) the amount you want to charge the client with.  
• FullName (required) the full name of the user.  
• Phone (required) the phone num of the user.  
• Delegate (required) protocol.  
• Email (optional) the email of the user.  
• Description (optional) description of the user.

There are 4 functions that extroversion out for the developer.

• CreatePaymentProcess (required) A function to execute the transaction should pass the necessary parameters to finish the transaction.  
• SettleSuspendedTransaction (optional) A transaction approval function should pass the necessary parameters to it.  
• CancelBitTransaction (optional) A transaction cancellation function should pass the necessary parameters to it..  
• getPaymentProcessInfoSuccess (optional) get information about specific transaction

Examples:

• CreatePaymentProcess:  
Swift:

![](https://files.readme.io/5e6ee29-image.png)

Objective - C:

![](https://files.readme.io/b5dd359-image.png)

• SettleSuspendedTransaction:  
Swift:

![](https://files.readme.io/cfdb289-image.png)

Objective - C:

![](https://files.readme.io/fa6831f-image.png)

• CancelBitTransaction:  
Swift:

![](https://files.readme.io/785b84f-image.png)

Objective - C:

![](https://files.readme.io/70d8253-image.png)

• GetPaymentProcessInfo:  
Swift:

![](https://files.readme.io/18dbbc0-image.png)

Objective C:

![](https://files.readme.io/22199a5-image.png)

Add MeshulamSDK Deep Link:

1. Open Info.plist file add URL types array with URL Identifier and URL Scheme. In the example below the URL Scheme is ‘imeshulamsdk’ and the URL Identifier is promotion.

![](https://files.readme.io/3e261a3-image.png)

1. In Xcode go to: Targets -> Info -> URL Types…
2. Add ‘imeshulamsdk’ in the URL Schemes.
3. In your AppDelegate file: import MeshulamSDK module.

   Swift: import MeshulamSDK

![](https://files.readme.io/2430aad-image.png)

4. In your AppDelegate file: import MeshulamSDK module.

   Swift: import MeshulamSDK

Objective-C: #import <MeshulamSDK/MeshulamSDK-Swift.h>

Add Debug Mode:

1. In your UIViewController file add debug Mode (debug mode is false by default).

Swift: Meshulam.shared().isDebugMode = true

Objective-C: [Meshulam shared].isDebugMode = YES;


## Images

- https://files.readme.io/3f922ae-image.png
- https://files.readme.io/a67958d-image.png
- https://files.readme.io/ce3b491-image.png
- https://files.readme.io/5e6ee29-image.png
- https://files.readme.io/b5dd359-image.png
- https://files.readme.io/cfdb289-image.png
- https://files.readme.io/fa6831f-image.png
- https://files.readme.io/785b84f-image.png
- https://files.readme.io/70d8253-image.png
- https://files.readme.io/18dbbc0-image.png
- https://files.readme.io/22199a5-image.png
- https://files.readme.io/3e261a3-image.png
- https://files.readme.io/2430aad-image.png