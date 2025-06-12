import matplotlib.pyplot as plt
import numpy as np 

x = np.array([1,4,5])
y = np.array([0,0.4,-0.4])

def annotate_axes(ax, text, fontsize=18):
    ax.text(0.5, 0.5, text, transform=ax.transAxes,ha="center", va="center", fontsize=fontsize, color="darkgrey")

fig = plt.figure(dpi=100) #constrained_layout=True

gs0 = fig.add_gridspec(1, 2,wspace=0.5)
gs00 = gs0[0].subgridspec(1, 2,wspace=0.5)
gs01 = gs0[1].subgridspec(1, 1)

ax11 = fig.add_subplot(gs00[0, 0])
annotate_axes(ax11, f'axLeft[0, 0]', fontsize=10)
ax11.set_xlabel('xlabel')

ax12 = fig.add_subplot(gs00[0, 1])
annotate_axes(ax12, f'axLeft[0, 1]', fontsize=10)
ax12.set_xlabel('xlabel')

ax2 = fig.add_subplot(gs01[0,0])
annotate_axes(ax2, f'axRight[0,0]', fontsize=10)
ax2.set_ylabel('ylabel')

fig.suptitle('nested gridspecs')

plt.show()