import numpy as np 

#test 1
a = np.array([[1,2,9],[4,5,9]])

print(a[[0,1],[2,2]])#array[(9,9)]

#test 2
b = np.array(['Iris-setosa','Iris-setosa'])
print(b[1])
print(b[[1]]) #['Iris-setosa']
print([b[1]]) #['Iris-setosa']