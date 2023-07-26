import matplotlib.pyplot as plt

fig1 = plt.figure(figsize=[5,5],dpi=100,tight_layout=True)
fig1.suptitle('test tight layout', fontsize=14, fontweight='bold')
ax1 = fig1.gca()
ax1.set_title('axes title')
ax1.set_xlabel("test xlabel")
ax1.set_ylabel("test ylabel")

fig2 = plt.figure(figsize=[5,5],dpi=100,constrained_layout=True)
fig2.suptitle('test constrained layout', fontsize=14, fontweight='bold')
ax2 = fig2.gca()
ax2.set_title('axes title')
ax2.set_xlabel("test xlabel")
ax2.set_ylabel("test ylabel")

fig3 = plt.figure(figsize=[5,5],dpi=100)
fig3.suptitle('custom layout', fontsize=14, fontweight='bold')
fig3.subplots_adjust(0.125,0.095,0.95,0.95,0.35,0.35)
ax3 = fig3.gca()
ax3.set_title('axes title')
ax3.set_xlabel("test xlabel")
ax3.set_ylabel("test ylabel")
ax3.set_xlim([0,10])
ax3.set_ylim([0,10])


plt.show()