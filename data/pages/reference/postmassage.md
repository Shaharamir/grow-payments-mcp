---
title: "Post Message"
slug: postmassage
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/postmassage
---

# Post Message

PostMessage helps your business react instantly to what happens inside the Grow payment page.
It is useful when the merchant uses an iframe, and the system needs to know whether the customer paid, closed the page, or changed direction.

Grow supports different event messages for credit card, Bit, Apple Pay, and Google Pay, so each payment method can be handled in the right context.

With PostMessage, the payment page and the business system stay aligned, helping create a smoother checkout and thank-you page experience.

# Key Functions of PostMessage:

Transaction Completion Notification:  
● After payment, we provide dual notifications, one for the server and one for the browser.

● The PostMessage effectively informs the browser that a transaction has been successfully completed.

### Flexible PostMessage Handling:

● In a new page definition, a PostMessage is sent to the newly opened tab.  
● When defining a process within a new page in the same browser, the PostMessage is sent to the newly created tab.  
● In a definition within the original tab, a PostMessage is directed back to the original tab.

### Customizable Thank-You Pages:

Three distinct types of thank-you pages can be defined within the pageCode definition:

● **New Page**: This type of thank-you page is designed as a completely new tab, independent of the original tab. It doesn't retrieve data from the original tab, and there's no ongoing process in the original tab waiting for the new page.

● **New Page in the Same Browser**: Here, the thank-you page loads data from the original tab. Additionally, there may be a process in the original tab that is waiting for the new page to load.

● **The Original Tab**: This refers to the tab from which the purchase was initially initiated. The thank-you page communicates directly with the original tab, completing the transaction loop.

# PostMessage Event Codes:

## Credit Card Transactions:

**Success**: payment

**Failure**: failed_to_load_page

**Cancel** (if user closed the tab): close

# Bit

**Success**: *bit_payment*

**Failure**: *הודעה לא קיימת*

**Cancel** (if user closed the tab): *close*

**Close**: *bit_cancel*

# Apple Pay

**Success**: *apple_payment*

**Failure**: *הודעה לא קיימת*

**Cancel** (if user closed the tab): *close*

# Google Pay

**Success**: *google_payment*

**Failure**: *הודעה לא קיימת*

**Cancel** (if user closed the tab): *close*

In Google Pay transactions, if you click on "X" or select another payment method, a PostMessage is generated without redirection to any cancel URL. In contrast, on other pages, a redirection may occur.

For detailed guidance on using the PostMessage feature, here's an example of code to help you get started:

```
window.addEventListener('message', function (result) {  
    if (result.origin === '<https://meshulam.co.il'> || result.origin === '<https://sandbox.meshulam.co.il'){>  
     switch (result.data.action){  
        case 'close' :{  
            document.getElementsByTagName('iframe')[0].style.setProperty('display','none');  
            break;  
        }  
        case 'payment' :{  
            if(result.data.status == 1){  
                // success  
            }  
            break;  
            }  
        case 'failed_to_load_page':{  
        break;  
        }  
    }  
 }  
});
```

At Grow, we are dedicated to ensuring a seamless and flexible experience for our customers. Should you have any questions or require further assistance regarding Bit transactions and redirection, please do not hesitate to contact our support team. Your satisfaction is our top priority.
