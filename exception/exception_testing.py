def Main():
    try:
        f=open("blan.txt","r")
        for line in f:
            print(line.strip("\n\r"))
        f.close()
    except:
        print("the file was either not found..")
    finally:
        #finally function จะทำก็ต่อเมื่อ ผ่าน try หรือ except ไปแล้ว
        print("Exit..")

if __name__=="__main__":
    Main()