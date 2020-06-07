#olc process
product = 1
num_list = [1, 2, 3, 4]

for num in num_list:
    product = product * num
print(product)

#new process
print('new process')
from functools import reduce
product = reduce((lambda x, y: print(f'{x},{y}')), num_list)
print(product)
product_2 = reduce((lambda x, y: x*y), num_list)
print(product_2)
