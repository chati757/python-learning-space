import numpy as np 
  
# a is an array of integers. 
a = np.array([[1, 2, 3], [4, 5, 6]]) 
  
print(a) 
  
print ('Indices of elements <4') 
  
b = np.where(a<4) 
print(b) # [row],[col]  > (array([0, 0, 0], dtype=int64), array([0, 1, 2], dtype=int64))
  
print("Elements which are <4") 
print(a[b]) # [1,2,3]