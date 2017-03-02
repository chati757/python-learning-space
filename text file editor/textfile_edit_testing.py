def Main():
    #f=open("C:\Windows\System32\drivers\etc","a") append type 
    f=open("C:/Windows/System32/drivers/etc/test", 'a')
    f.write("\r\n")
    f.write("127.0.0.1		    www.google.com")
    f.close()

if __name__=="__main__":
    Main()        