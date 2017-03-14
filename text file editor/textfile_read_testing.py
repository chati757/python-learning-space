def Main():
    #f=open("C:\Windows\System32\drivers\etc","a") append type 
    f = open("C:/Users/lenovo/Desktop/ASCII Art Studio/prototype_pos_logo_d01.txt","r")
    lines = f.readlines()
    print(lines) #['list1\n','list2\n','list3']
    f.close()

if __name__=="__main__":
    Main()