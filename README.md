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

Known Issues:
Some gateways will send messages to clients that are not on their network, this software is best used when reciving a few copies of the same message is preferable to none.

Non-US gateways are currently not included.

Dependancies:

smtplib - https://docs.python.org/2/library/smtplib.html
sys (if used as standalone) - https://docs.python.org/2/library/sys.html
