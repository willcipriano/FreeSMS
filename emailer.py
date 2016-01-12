

def email(server,port,username,password,toaddrs,message):
    import smtplib
    server = smtplib.SMTP(server + ':' + port)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    #Header needed for T-Mobile
    for addr in toaddrs:
        header = "From: %s\r\nTo: %s\r\nSubject: %s\r\nX-Mailer: FreeMMS\r\n\r\n" % (username, toaddrs, 'subject')
        server.sendmail(username, toaddrs, header+message)
    server.quit()
