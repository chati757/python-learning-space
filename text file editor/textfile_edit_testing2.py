def Main():
    #f=open("C:\Windows\System32\drivers\etc","a") append type 
    f = open("C:/Windows/System32/drivers/etc/test","r")
    lines = f.readlines()
    print(lines) #['list1\n','list2\n','list3']
    f.close()

    f = open("C:/Windows/System32/drivers/etc/test","w")
    for line in lines:
        if line!="test.com"+"\n":
            print("write "+line)
            f.write(line)
    f.close()

if __name__=="__main__":
    Main()        

#create txt file command
'''
Makes a 0 byte file a very clear, backward-compatible way:

type nul >EmptyFile.txt
idea via: anonymous, Danny Backett, possibly others, myself inspired by JdeBP's work

A 0 byte file another way, it's backward-compatible-looking:

REM. >EmptyFile.txt
idea via: Johannes

A 0 byte file 3rd way backward-compatible-looking, too:

echo. 2>EmptyFile.txt
idea via: TheSmurf

A 0 byte file the systematic way probably available since Windows 2000:

fsutil file createnew EmptyFile.txt 0
idea via: Emm

A 0 bytes file overwriting readonly files

ATTRIB -R filename.ext>NUL
(CD.>filename.ext)2>NUL
idea via: copyitright

A single newline (2 bytes: 0x0D 0x0A in hex notation, alternatively written as \r\n):

echo.>AlmostEmptyFile.txt
Note: no space between echo, . and >.

idea via: How can you echo a newline in batch files?

edit It seems that any invalid command redirected to a file would create an empty file. heh, a feature! compatibility: uknown

TheInvisibleFeature <nul >EmptyFile.txt
A 0 bytes file: invalid command/ with a random name (compatibility: uknown):

%RANDOM%-%TIME:~6,5% <nul >EmptyFile.txt
via: great source for random by Hung Huynh

edit 2 Andriy M points out the probably most amusing/provoking way to achieve this via invalid command

A 0 bytes file: invalid command/ the funky way (compatibility: unknown)

*>EmptyFile.txt
idea via: Andriy M

A 0 bytes file 4th-coming way:

break > file.txt
'''