str1 = "Line1-abcdef Line2-abc Line4-abcd"
print(len(str1))
print str1.split()#['Line1-abcdef','Line2-abc','Line4-abcd']
print str1.split()[0]#Line1-abcdef
print "ls/etc:"
print 'ls/etc'.split("/")

str2 = "abc"*5
print(str2)

print(" ".join(str1.split())) #is opposite of split command

print("testlen")
test=""
print(len(test))

str3 = "abc"
print(str3[:-1])
print(len(str3))

#using except multiple space
str4 = "test1    test2"
print(str4.split()) # [test1,test2]