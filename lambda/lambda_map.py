'''
#old process
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)

#new process
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

'''

test_arr1 = [2,4,7]
test_arr2 = [6,8,1]

result = map(lambda x,y:x+y,test_arr1,test_arr2)
print(result)
print(list(result))

'''
def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

# Output:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]
'''