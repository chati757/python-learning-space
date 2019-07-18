# Python program to illustrate library functions 
# save time while coding with the example of map() 
#-------------------------------------------------

import time 
  
# slower (Without map()) 
start = time.time()  
s = 'geeks'
U = [] 
for c in s:
    U.append(c.upper()) 
print(U) 

print("Time spent in function is: ", time.time() - start)

# Faster (Uses builtin function map()) 
start = time.time()  
s = 'geeks'
U = list(map(str.upper, s))
print(U) 

print("Time spent in builtin function is: ", time.time() - start)