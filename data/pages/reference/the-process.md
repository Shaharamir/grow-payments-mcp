---
title: "Payment Process"
slug: the-process
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/the-process
---

# Payment Process

The payment process starts with creating a payment form and ends with completing and approving the transaction.

The process is needed to ensure every payment is securely opened, tracked, confirmed, and finalized through the correct server-to-server approval flow.

### This is the main payment process and flow:

**Important Note:** All data transmitted in the body of HTTP requests is in FormData format.

**The Process:**  
● Initiate the Process: Start by reaching out to GROW's server from your server. GROW will respond with a link. Open this link in an iframe or in redirect—it's your call. This opens the payment page on the user's screen.

● Payment Completion: Following the user's completion of the payment, GROW's server notifies your server. Upon receiving this notification, you must call the “approveTransaction” method to approve the transaction. This prompt action grants the necessary authorization and officially greenlights the concluded transaction.

● Transaction Complete: At this stage, the transaction is a done deal. The user smoothly lands on your success page (the address you provided in the first POST call).

Process Overview :

The process diagram:

![](https://files.readme.io/5dd0ed1-image.png)

# Redirecting the User to Success URL

After completing the transaction via the transaction form, the user will be redirected to a success page. They will be redirected to the link you have provided us during the initial creation request with a response parameter indicating a success. In this request, no actual details regarding the transaction will be sent. Only customer fields (cField), if there were any that have been pre-defined, will be sent. (All the transaction information will be passed upon update - Server to Server).

### Upon Success

a success status would return inside the respone: <https://yoursite.co.il/return_url_with_params&reponse=success>  
example:  
**successUrl parameter is**: <https://yoursite.co.il/?area=payment>

**The redirect URL will be**: <https://yoursite.co.il/?area=payment&response=success>

### Upon Failure

The user would automatically be redirected back to the beginning of the payment process for them to retry completing the payment process again. (e.g. an error in the customer id number or CVV).

In case the user has clicked on the go back button, or on the X button in the iFrame, or in case of Bit declining the transaction, the customer would be redirected to the cancel page you provided at the beginning of the process (e.g. you may redirect the customer back to the product page for them to choose a different payment method).

**Please note**  
Even if the user has closed the browser or for any other reason did NOT made it to the Thank You page, it will not affect your server after executing the transaction. The business would be informed that a transaction has been made, and would be able for example to send a confirmation email to the user, regardless of what had happened on the client's end.

---

## Implementation Options:

● iOS Integration: Smoothly integrate GROW with your iOS setup.  
● Android Integration: Seamlessly incorporate GROW into your Android environment.  
● JavaScript SDK: Easily bring GROW into your web application using the JavaScript SDK.  
● Open in Iframe: Embed the payment process in an iframe for a userfriendly experience.  
● Open in Redirect: Opt to redirect users to the payment process for a straightforward journey.

Explore these options to fine-tune the integration to match your platform and user experience needs effortlessly.


## Images

- https://files.readme.io/5dd0ed1-image.png