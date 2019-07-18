# to use local variables to make code
# run faster
#------------------------------------

import time

class Test:
    def func(self, x):
        print(x + x)

start = time.time()
Obj = Test()
n = 10
for i in range(n):
    Obj.func(i) 

print("Time elapsed for using class method is:", time.time() - start)

start = time.time()
Obj = Test()
mytest = Obj.func  # Declaring local variable (faster)
n = 10
for i in range(n):
    mytest(i)  # faster than Obj.func(i)

print("Time elapsed for using local variable is:", time.time() - start)