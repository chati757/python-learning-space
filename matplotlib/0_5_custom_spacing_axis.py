#https://stackoverflow.com/questions/66880397/how-can-i-increase-horizontal-space-hspace-between-two-specific-matplotlib-sub
import matplotlib.pyplot as plt 

fig = plt.figure(constrained_layout=True)
#subfigures(nrows=1, ncols=1, squeeze=True, wspace=None, hspace=None, width_ratios=None, height_ratios=None, **kwargs)[source]
subfigs = fig.subfigures(3, 1, height_ratios=[1,2,1], hspace=0.2)

# top 
axtop = subfigs[0].subplots(1, 1)

# 2x2 grid
axs = subfigs[1].subplots(2, 2)

# bottom
axsbot = subfigs[2].subplots(1, 1)

plt.show()