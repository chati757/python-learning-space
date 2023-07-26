import matplotlib.pyplot as plt
import numpy as np 

plt.figure(figsize=[6,6],dpi=100)

x_arr = [1,2,4,5,6,9,10]
y_arr = [0,0,0.4,0,0,1,1]

start = 0
for c,i in enumerate(x_arr):
    if(c>0 and i!=x_arr[c-1]+1):
        plt.plot(x_arr[start:c],y_arr[start:c],color='blue')
        start = c
    elif(c==len(x_arr)-1):
        plt.plot(x_arr[start:],y_arr[start:],color='blue')
        start = 0

plt.show()