---
title: "Success URL"
slug: success-url
type: basic
section: reference
source_url: https://grow-il.readme.io/reference/success-url
---

# Success URL

After completing the transaction via the transaction form, the user will be redirected to a success page. They will be redirected to the link you have provided us during the initial creation request with a response parameter indicating a success. In this request, no actual details regarding the transaction will be sent. Only customer fields (cField), if there were any that have been pre-defined, will be sent. (All the transaction information will be passed upon update - Server to Server).

Success Url + cancel Url must be sent with each call,  
Please note that you cannot send a local host address under this parameter,  
We concatenate to the end of the URL the &reponse=success and the Cfields sent in the call  
That's why you have to make an adjustment on your side to an address that matches these threads.

**Upon Success**

a success status would return inside the respone:  
<https://yoursite.co.il/return_url_with_params&reponse=success>

**example:**  
successUrl parameter is: <<https://yoursite.co.il/?area=payment>  
The redirect URL will be: <https://yoursite.co.il/area=payment&response=success>

**Upon Failure**  
The user would automatically be redirected back to the beginning of the payment process for them to retry completing the payment process again. (e.g. an error in the customer id number or CVV).
