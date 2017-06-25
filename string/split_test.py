str = "Line1-abcdef Line2-abc Line4-abcd"
print(len(str))
print str.split()#['Line1-abcdef','Line2-abc','Line4-abcd']
print str.split()[0]#Line1-abcdef
print "ls/etc:"
print 'ls/etc'.split("/")

str2 = "abc"*5
print(str2)

print(" ".join(str.split())) #is opposite of split command

print("testlen")
test=""
print(len(test))