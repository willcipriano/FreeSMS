# FreeSMS
A quite hackish, but ultimately free and as anonymous as email SMS/MMS solution. (US only)

Usage:

    # First modify email.config to reflect your email settings. Gmail has been tested and
    # works if you enable this: https://support.google.com/accounts/answer/6010255?hl=en

    import FreeMMS
    FreeMMS.text(Number,Message,Subject)

    # Number: A ten digit phone number in the format 2223334444
    # Message: The message you wish to send to the recipient
    # Subject: Not required, typically displayed on the handset as 'Subject / Message'