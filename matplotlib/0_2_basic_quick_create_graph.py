import matplotlib.pyplot as plt
import numpy as np 

x = np.array([1,4,5])
y = np.array([0,0.4,-0.4])

plt.figure(figsize=[6,6],dpi=100)
plt.plot(x,y)
plt.show()