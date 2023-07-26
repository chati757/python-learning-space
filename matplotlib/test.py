import matplotlib.pyplot as plt
import numpy as np 

x = [1,2,4,5,6,9,10]
y = [0,0,0.4,0,0,1,1]

x_arr = []
y_arr = []
start = 0
for c,i in enumerate(x):
    if(c>0 and i!=x[c-1]+1):
            x_arr.append(x[start:c])
            y_arr.append(y[start:c])
            start = c
    elif(c==len(x)-1):
            x_arr.append(x[start:])
            y_arr.append(y[start:])
            start = 0

plt.figure(figsize=[6,6],dpi=100)

print(x_arr)
print(y_arr)

for c in range(0,len(x_arr)):
    print(x_arr[c])
    print(y_arr[c])
    plt.plot(x_arr[c],y_arr[c],color='blue')


plt.show()
'''
plt.figure(figsize=[6,6],dpi=100)

plt.plot(x,y,color='blue')

x = np.array([5,6])
y = np.array([-0.4,0.4])

plt.plot(x,y,color='blue')

plt.show()
'''