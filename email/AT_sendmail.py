# ____  _            _        _____      _               
#|  _ \| |          | |      / ____|    | |              
#| |_) | | __ _  ___| | __  | |    _   _| |__   ___ _ __ 
#|  _ <| |/ _` |/ __| |/ /  | |   | | | | '_ \ / _ \ '__|
#| |_) | | (_| | (__|   <   | |___| |_| | |_) |  __/ |   
#|____/|_|\__,_|\___|_|\_\   \_____\__, |_.__/ \___|_|   
#                                  __/ /                
#                                 |___/            
# this script should be combination with batch script. [name batch file is "AT_batsend"]
# before use... 
# 1.please check permisstion your Email.
#   for example if your email is gmail please check at > https://www.google.com/settings/security/lesssecureapps
# 2.please setting path in Enviroment Variables. 2 set
#   2.1 setting python3 can run in command prompt.
#   2.2 setting batch script "AT_batsend" can run in command prompt.
# smtplib module send mail
import smtplib

TO = "ninjachati@hotmail.com"
SUBJECT = "TEST MAIL"
TEXT = "Here is a message from python."

# Gmail Sign In
gmail_sender = "thh.hardware.co@gmail.com"
gmail_passwd = ""

server = smtplib.SMTP("smtp.gmail.com",587)
server.ehlo()
server.starttls()
server.login(gmail_sender,gmail_passwd)

BODY = "\r\n".join(["To: %s" % TO,
                    "From: %s" % gmail_sender,
                    "Subject: %s" % SUBJECT,
                    "", TEXT])

try:
    server.sendmail(gmail_sender, [TO], BODY)
    print ("email sent")
except:
    print ("error sending mail")

server.quit()