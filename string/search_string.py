import re

master = "/web/all-brushes/page/1"
content = ["/web/all-brushes/page/2","this is a book","/web/all-brushes/page/3","test","/web/all-brushes/page/116"]

for line in content:
    result = re.search(master.rstrip('1')+".",line) # finds 'bob'
    #filter line level
    if(result!=None):
        #print(result)
        print(line.strip("/web/all-brushes/page/"))
        
    else:
        print("else")
    
'''
import re

content = ["my name is bob","this is a book","my name is rob"]

for line in content:
    result = re.search('my name is (\S+)',line) # finds 'bob'
    #filter line level
    if(result!=None):
        print(result)
        print(line)
        
    else:
        print("else")
    
'''