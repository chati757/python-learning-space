import numpy as np

test = [3,1,2,1,1]
print(test)
print(np.unique(test,return_counts=True)) #(array([1, 2, 3]), array([3, 1, 1], dtype=int64))