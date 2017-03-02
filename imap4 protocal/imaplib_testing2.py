import uuid
import imaplib
import email
import json
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('po.chatipakorn_st@tni.ac.th', '8182123456')
mail.select("INBOX") #connect to the INBOX
result, data = mail.uid('search', None, "ALL") # search and return uids instead [xxx xxx ...]
#print("result")
#print(result)
print("data") #['xxxx xxxx ...'] if data[0] > xxxx xxxx ...
print(data[0])
latest_email_uid = data[0].split()[-1] #latest uid > 0xxxx 1xxxx > ['0xxxx','1xxxx'] > 0xxxx 
print("latest_email_uid")
print(latest_email_uid) # 0xxxx
result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
print("before raw mail")
print(data) # 2 array ['result','colossal!..'] 
print("raw email")
raw_email = data[0][1]
print(raw_email)
print("convert with email lib")
email_message = email.message_from_string(raw_email)
print("TO")
print email_message['To'] # ('??','xx@hotmail.com')
print("From")
print email.utils.parseaddr(email_message['From']) # "Yuji Tomita" <yuji@grovemade.com>
print("Subject")
print email_message['Subject']
#print("email_message items")
#print email_message.items() # print all headers
print("email massage")
print(email_message)



# note that if you want to get text content (body) and the email contains
# multiple payloads (plaintext/ html), you must parse each message separately.
# use something like the following: (taken from a stackoverflow post)
def get_first_text_block(email_message_instance):
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return email_message_instance.get_payload()
print(get_first_text_block(email_message))


#------------------------ in gcat -------------------------
print("gcat type")
# in mail have "checkin" subject 
rcode, idlist = mail.uid('search',None,"(SUBJECT 'checkin:')")
print("after sreach...")
print(idlist) #['2179 2180']
print("get split before for loop...")
print(idlist[0].split()) #['2179', '2180']
for idn in idlist[0].split():
    msg_data = mail.uid('fetch',idn,'(RFC822)')
    print("loop..")
    print("idn")
    print(idn)# 2179 and next loop 2180
    print("data")
    print(msg_data)# data(2179) colossal... and next loop data(2180) colossal... 
    print("raw mail")
    print("msg_data[1][0][1]")
    print(msg_data[1][0][1])# rawmail(2179) and next loop rawmail(2180)
    print("payload")
    print(email.message_from_string(msg_data[1][0][1]).get_payload)
    print("email.message_from_string(msg_data[1][0][1])['Subject']")
    print(email.message_from_string(msg_data[1][0][1])['Subject']) #subject content ex.checkin:123654
    subject_data=email.message_from_string(msg_data[1][0][1])['Subject']
    
    print("payload testing..")
    for payload in email.message_from_string(msg_data[1][0][1]).get_payload():
            if payload.get_content_maintype() == 'text':
                print("text")
                text = payload.get_payload()
                print(text)
                print("json load get payload")
                dict = json.loads(payload.get_payload())
                print(dict)

