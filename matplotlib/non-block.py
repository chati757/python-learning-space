import numpy as np
import matplotlib.pyplot as plt
import time

fig1 = plt.figure(figsize=[6,6],dpi=100,facecolor='#292d3e')
ax1 = plt.gca()
ax1.axis([0, 10, 0, 1])


plt.show(block=False)
print('after show')

for i in range(10):
    y = np.random.random()
    #ax1.cla()
    ax1.scatter(i, y)
    plt.pause(2)

print('after plot end')