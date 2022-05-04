import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

fig = plt.figure()
ax = fig.add_subplot(111)
line, = ax.plot([], [], 'bo')

def init():
    print('on_init')
    ax.set_xlim(0,20)
    ax.set_ylim(0,20)
    ax.plot([1], [6], 'ro')
    return line,

def update(frame):
    print('on_update')
    x_vals.append(frame)
    y_vals.append(5)
    line.set_data(x_vals, y_vals)
    return line,

ani = FuncAnimation(fig,init_func=init,func=update,frames=[2,3,4,5,6],interval=1000,blit=True,repeat=False)
plt.show()