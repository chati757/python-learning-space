#imap4 is online protocal for read mail in the mailserver.
import imaplib
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('po.chatipakorn_st@tni.ac.th', '8182123456')
#print(mail.list())
'''
output : from mail.list() > 
$ ('OK', ['(\\HasNoChildren) "/" "INBOX"', 
          '(\\HasChildren \\Noselect) "/" "[Gmail]"', 
            '(\\All \\HasNoChildren) "/" "[Gmail]/All Mail"', 
            '(\\Drafts \\HasNoChildren) "/" "[Gmail]/Drafts"', 
            '(\\HasNoChildren \\Important) "/" "[Gmail]/Important"', 
            '(\\HasNoChildren \\Sent) "/" "[Gmail]/Sent Mail"', 
            '(\\HasNoChildren \\Junk) "/" "[Gmail]/Spam"', 
            '(\\Flagged \\HasNoChildren) "/" "[Gmail]/Starred"', 
            '(\\HasNoChildren \\Trash) "/" "[Gmail]/Trash"'])       
'''
mail.select("INBOX") #connect to the INBOX

result, data = mail.search(None, "ALL")
#print("result:")
#print(result)
#print("data:")
#print(data)
'''
output is 2 array ["status","number of mail (sort type number)"]
ex ["ok",'1 2 3'] it's mean serach function is ok and it have 3 mail is 1 2 3
'''
ids = data[0] # data is a list.
#print(data[0])
'''
1 2 3 
'''  
id_list = ids.split() # ids is a space separated string
#print(id_list)
'''
['1','2','3']
'''
latest_email_id = id_list[-1] # get the latest
#print(latest_email_id) 
'''
3
'''
#latest_email_id = id_list[-2] # get the latest
#print(latest_email_id)
'''
2
'''
result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body standard(RFC822) for the given ID
#print("result")
#print(result)
#print("data")
#print(data)
'''
result > ok 
data > it's colossal!
'''
raw_email = data[0][1] # here's the body, which is raw text of the whole email
print("raw email")
print(raw_email) # raw mail form
# including headers and alternate payloads

