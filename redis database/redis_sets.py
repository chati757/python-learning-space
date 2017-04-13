import redis 

redis=redis.StrictRedis(
        host='localhost', 
        port=6379, 
        db=0, 
        password=8182757
        )

'''
sets value
-sadd <meset> <value>
remove sets value
-srem <myset> <value in set>
show members
-smembers <myset>
'''
print("sadd")
redis.sadd("myset" ,"settest1","settest2")

#print("srem")
#redis.srem("myset","settest2")

print("show members")
test=redis.smembers("myset")

print(test)