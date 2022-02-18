from matplotlib import rcParams
#set default font family
rcParams['font.family'] = ['white Rabbit','Orena'] #or plt.rc('font',family='White Rabbit')
rcParams['axes.unicode_minus'] = False #or plt.rc('axes', unicode_minus=False)
import matplotlib.pyplot as plt
import numpy as np

#util function
def annotate_axes(ax, text, fontsize=22):
    ax.text(0.5, 0.5, text, transform=ax.transAxes,ha="center", va="center" , zorder = -1, fontsize=fontsize, color="#5a5a78",fontfamily=rcParams['font.family'][1])

x = np.array([1,4,5])
y = np.array([0,0.4,-0.4])

fig = plt.figure(figsize=[6,6],dpi=100,facecolor='#292d3e')
plt.subplots_adjust(0.125,0.095,0.95,0.95,0.35,0.35)
#px1 = fig.gca()

'''
#palenight
black : #292d3e
red : #f07178
green : #c3e88d
yello : #ffcb6b
blue : #82aaff
magenta : #c792ea
cyan : #89ddff
white : #d0d0d0
'''
#------------------------------------axis1------------------------------------
px1 = fig.add_subplot(211)
px1.set_title('[ DAILY 200 ]',color='#ffcb6b')
annotate_axes(px1,'STOCKNAME')
px1.set_xlabel('days_period',color='#ffcb6b')
px1.set_ylabel('price_level',color='#ffcb6b')

px1.set_facecolor('#292d3e')
px1.tick_params(axis='x', colors='#ffcb6b')   #setting up X-axis tick color to red
px1.tick_params(axis='y', colors='#ffcb6b')

px1.spines['top'].set_color('#ffcb6b')
px1.spines['left'].set_color('#ffcb6b')
px1.spines['right'].set_color('#ffcb6b')
px1.spines['bottom'].set_color('#ffcb6b')

px1.plot(x,y,color='#82aaff')
px1.grid(c='#d0d0d0', ls='-', lw=0.1)
#-----------------------------------------------------------------------------
#------------------------------------axis2------------------------------------
px2 = fig.add_subplot(223)
px2.set_title('[ PATTERN RATIO ]',color='#ffcb6b')
px2.set_xlabel('days_period',color='#ffcb6b')
px2.set_ylabel('percent_change_level',color='#ffcb6b')

px2.set_facecolor('#292d3e')
px2.tick_params(axis='x', colors='#ffcb6b')   #setting up X-axis tick color to red
px2.tick_params(axis='y', colors='#ffcb6b')

px2.spines['top'].set_color('#ffcb6b')
px2.spines['left'].set_color('#ffcb6b')
px2.spines['right'].set_color('#ffcb6b')
px2.spines['bottom'].set_color('#ffcb6b')

px2.plot(x,y,color='#82aaff')
px2.grid(c='#d0d0d0', ls='-', lw=0.1)
#-----------------------------------------------------------------------------
#------------------------------------axis3------------------------------------
px3 = fig.add_subplot(224)
px3.set_title('[ SOME STOCKNAME ]',color='#ffcb6b')
px3.set_xlabel('days_period',color='#ffcb6b')
px3.set_ylabel('price_level',color='#ffcb6b')

px3.set_facecolor('#292d3e')
px3.tick_params(axis='x', colors='#ffcb6b')   #setting up X-axis tick color to red
px3.tick_params(axis='y', colors='#ffcb6b')

px3.spines['top'].set_color('#ffcb6b')
px3.spines['left'].set_color('#ffcb6b')
px3.spines['right'].set_color('#ffcb6b')
px3.spines['bottom'].set_color('#ffcb6b')

px3.plot(x,y,color='#82aaff')
px3.grid(c='#d0d0d0', ls='-', lw=0.1)
#-----------------------------------------------------------------------------
plt.show()