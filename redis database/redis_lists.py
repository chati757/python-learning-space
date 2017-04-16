import redis 

redis=redis.StrictRedis(
        host='localhost', 
        port=6379, 
        db=0, 
        password=8182757
        )

'''
list value 
create lists value [form bottom to top]
-LPUSH <mylist> <listvalue> .. 
show all list [form bottom to top]
-LRANGE <mylist> 0 -1
create lists value [form top to bottom]
-RPUSH <mylist> <listvalue> .. 
get value and delete list [form bottom to top]
-LPOP <mylist> Ex.list 1 2 3 get 1 and delete 1 in list
get value and delete list [form top to bottom]
-RPOP <mylist> Ex.list 1 2 3 get 3 and delete 3 in list 
if empty wait value before POP
-BLPOP , BRPOP <mylist> .. <timeout>
pop and push other list 
-RPOPLPUSH <source> <desination> Ex.list1 a b c > RPOPLPUSH list1 list2 > list1 a b , list2 c 
edit list 
-LSET <mylist> <index> <listvalue>
delete value 
-LREM <mylist> -n [bottom to top] +n [top to bottom] Ex.RPUSH list1 A B C A A > LREM list1 -1 "A" > LRANGE list > A B C A 
'''
#LPUSH
print("Lpush")
redis.lpush("mylist","a","b","c")
#lrange
print("lrange")
lrange=redis.lrange("mylist",0,-1)
print(lrange)
#RPUSH
print("Rpush")
redis.lpush("mylist","a","b","c")
#lrange
print("lrange")
lrange=redis.lrange("mylist",0,-1)
print(lrange)
#LPOP
print("Lpop")
lpop=redis.lpop("mylist")
print(lpop)
#lrange
print("lrange")
lrange=redis.lrange("mylist",0,-1)
print(lrange)
#RPOP
print("Rpop")
rpop=redis.rpop("mylist")
print(rpop)
#lrange
print("lrange")
lrange=redis.lrange("mylist",0,-1)
print(lrange)
#LSET
print("Lset")
redis.lset("mylist",-1,"lset")
#lrange
print("lrange")
lrange=redis.lrange("mylist",0,-1)
print(lrange)
#LREM
print("LREM")
redis.lrem("mylist",-1,"lset")
#lrange
print("lrange")
lrange=redis.lrange("mylist",0,-1)
print(lrange)


