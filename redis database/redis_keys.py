import redis 

redis=redis.StrictRedis(
        host='localhost', 
        port=6379, 
        db=0, 
        password=8182757
        )

#get keys 
test=redis.keys("*")
print(test[0])

#set keys and try to check redis database
redis.set("test" , "test01")

#delete keys
redis.delete("test")