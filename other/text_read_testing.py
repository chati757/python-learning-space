#-*-coding: utf-8 -*-

testchar=""
def Main():
    global testchar
    f=open('E:\log_th.txt','r')
    lines = f.readlines()
    #print(lines)#['list1\n','list2\n','list3']
    #print(lines[0])#@ปฟl;ylfu
    #print(lines[1])#mflv[
    #print(len(lines[1]))# 5 mean > 0-4
    #print(len(lines))# 2 mean > 0,1
    #store string array
    #loop 2 loop
        #loop 1 split array 
            #loop 2 split character and replace th character
    for line in lines:
        print(line)
        for txt in line:
            print(txt)
            testchar=testchar+txt.replace('l',u'ส')
    f.close()
    print("testchar ",testchar)
    
    #save
    testtxt="l;ylfu"
    print(testtxt.decode("utf-8").replace('l',u'ส').replace(';',u'ว').replace('f',u'ด').replace('u',u'ี').replace('y',u'ั'))
    
    '''
    string="abc&def#ghi"
    for ch in ['&','#']:
        if ch in string:
            string=string.replace(ch,"\\"+ch)
    print string
    #abc\&def\#ghi
    '''
    '''
    f = open("C:\Users\blackcyber\Desktop\log_th.txt","w")
    for line in lines:
        #by line ['list1\n','list2\n','list3']
        for ch in line:
            print(ch)
    f.close()
    '''
def translate_lang():
    #ex split
    str = "Line1-abcdef Line2-abc Line4-abcd"
    print str.split()# ['Line1-abcdef','Line2-abc','Line4-abcd']
    print str.split()[0]# Line1-abcdef
    print str.split()[0][0]# L
    print 'ls /etc'.split()# ['is','/etc']
    
    #ex replace
    str = "this is string example....wow!!! this is really string";
    print str.replace("is", "was")
    
    
if __name__=="__main__":
    Main()
    #translate_lang()