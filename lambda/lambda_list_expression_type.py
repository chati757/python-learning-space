#from lamba only
a=lambda x: x+1
print(a(0))

#this , it's make function , many function depending range setting Ex.range(0,4) = 4 function in one line and for each function one time use
#sometimes it is useful to work with multi-thread but single thread maybe not.
print([(lambda x: x+1)(i) for i in range(0,4)])