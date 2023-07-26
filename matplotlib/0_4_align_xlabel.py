import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 2)
for tick in axs[0].get_xticklabels():
    tick.set_rotation(55)
axs[0].set_xlabel('XLabel 0',loc='left')
axs[1].set_xlabel('XLabel 1')
fig.align_xlabels()

plt.show()