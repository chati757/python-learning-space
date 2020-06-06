test = [2,3,4,5]
#assign to 2 (all values)
print([i*0+2 for i in test])

test2 = [2,3,4,5]
#assign to 0 (all values)
print([0 for i in test2])

test3 = [4,5,6,7]
#assign to 0 (all values)
test3 = [0] * len(test3)
print(test3)