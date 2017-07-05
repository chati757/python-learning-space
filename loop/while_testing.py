import time

data_integrity=False
while True:
    print("loop 1")
    time.sleep(2)
    while True:
        print("loop 2")
        time.sleep(2)
        if(data_integrity==False):
            print("please check resource")
            choice=input("Is resource complete ? [y/n] :")
            if(choice=="y"):
                break
            elif(choice=="n"):
                exit()
            else:
                pass