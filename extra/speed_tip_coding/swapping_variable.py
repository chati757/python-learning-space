#Swapping variables in one line
#------------------------------

import time

start = time.time()
# slower 
x = 2
y = 5
temp = x 
x = y 
y = temp 
print(x, y) 
print("Time elapsed for slow swapping is:", time.time() - start)

start = time.time()
x,y = 3,5
# faster 
x, y = y, x 
print(x, y) 
print("Time elapsed for fast swapping is:", time.time() - start)