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
# 1.please check permisstion in your Email.
#   for example if your email is gmail please check at > https://www.google.com/settings/security/lesssecureapps
# 2.please setting path in Enviroment Variables. 2 set
#   2.1 setting python3 can run in command prompt.
#   2.2 setting batch script "AT_batsend" can run in command prompt.
# ps: If you have to do step 2 but command prompt display something like : .. is not recognized as an internal..
# please check step 2 again.

# smtplib module send mail
import smtplib
# for use request data with http protocal
import urllib.request
# for read json data
import json

# desination
TO = "ninjachati@hotmail.com"
SUBJECT = "TEST MAIL"

#---------------------request external ip method-----------------------
response = urllib.request.urlopen("http://ip.jsontest.com/")
content = response.read()
data = json.loads(content.decode("utf8"))
#json object
#print(data)
#specify value
#print(data['ip'])
#---------------------request external ip method-----------------------

TEXT = data['ip']

# Gmail Account : Login Stage
gmail_sender = "thh.hardware.co@gmail.com"
gmail_passwd = ""
    # Mail server connecting metchod
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
    print ("error : sending email")

server.quit()