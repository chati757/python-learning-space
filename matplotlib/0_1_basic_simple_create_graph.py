import matplotlib.pyplot as plt
import numpy as np 

x = np.array([1,4,5])
y = np.array([0,0.4,-0.4])

plt.style.use("dark_background")

#plt.subplots_adjust(0.125,0.095,0.95,0.95,0.35,0.35)
fig1 = plt.figure(figsize=[6,6],dpi=100)
fig1.subplots_adjust(0.125,0.095,0.95,0.95,0.35,0.35)

ax1 = fig1.gca()
ax1.plot(x,y,'g')

fig2 = plt.figure(figsize=[6,6],dpi=100)
fig2.subplots_adjust(0.125,0.095,0.95,0.95,0.35,0.35)

ax2 = fig2.gca()
ax2.plot(x,y,'b')

plt.show()