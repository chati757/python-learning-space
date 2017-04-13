import redis 

redis=redis.StrictRedis(
        host='localhost', 
        port=6379, 
        db=0, 
        password=8182757
        )

'''
hash value
-hset <myhash> <field> <hashvalue>
-hget <myhash> <field>
-hmset <myhash> <field1> <hashvalue> <field2> <hashvalue2> .. 
-hmget <myhash> <field1> <field2> ..
-hgetall <myhash>
'''

#hset 
print("hset")
redis.hset("myhash","myfield","hashvalue")

#hget 
print("hget")
test=redis.hget("myhash","myfield")
print(test)

#hmset 
print("hmset")
redis.hmset("myhash2",{"test1":"test1","test2":"test2"})

#hmget
print("hmget")
test2=redis.hmget("myhash2",{"test1","test2"})
print(test2)




