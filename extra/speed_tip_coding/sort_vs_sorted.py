# Python program to illustrate 
# using keys for sorting 
#-----------------------------

import time

start = time.time()
l = [1, -3, 6, 11, 5, 50, -43, 111, -2405] 
l.sort() 
print(l)
print("Time elapsed for keys argument sorting is: ", time.time() - start)

start = time.time()  
l = [1, -3, 6, 11, 5, 50, -43, 111, -2405] 
# use sorted() if you don't want to sort in-place: 
l = sorted(l) 
print(l) 
print("Time elapsed for built-in sort function is: ", time.time() - start)