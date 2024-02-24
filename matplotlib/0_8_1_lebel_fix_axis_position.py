import matplotlib.pyplot as plt

fig = plt.figure(tight_layout=True,dpi=100)
fig.suptitle('bold figure suptitle', fontsize=14, fontweight='bold')

ax = fig.add_subplot()
ax.set_title('axes title')

ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')

ax.text(0.99, 0.01, 'fix pos colored text in axes coords',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='green', fontsize=15)

print(ax.transAxes)

ax.set(xlim=(0, 10), ylim=(0, 10))

plt.show()