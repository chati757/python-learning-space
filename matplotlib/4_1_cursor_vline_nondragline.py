import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
import matplotlib.lines as lines

xdata = ['d1','d2','d3']
ydata = [0,0.4,-0.4]

#plt.subplots_adjust(0.125,0.095,0.95,0.95,0.35,0.35)
#fig = plt.figure(layout="constrained",dpi=100)
fig = plt.figure(figsize=[4,4],dpi=100)
fig.suptitle('crosshair testing')

gs = fig.add_gridspec(1, 1)
sgs = gs[0].subgridspec(1, 1)

ax = fig.add_subplot(sgs[0,0])
c = fig.canvas

ax.plot(xdata,ydata)

line1 = lines.Line2D([1,1],[ax.get_ylim()[0],ax.get_ylim()[1]],picker=5,snap=True)
#snap function cannot use for default backend (TkAgg)
#for use snap function you must be set backend with below
'''
print(matplotlib.get_backend())
matplotlib.use('agg')
#but cannot use plt.show() function
#so , create the snap function with yourself
'''
line1.set_visible(False)

line2 = lines.Line2D([1,1],[ax.get_ylim()[0],ax.get_ylim()[1]],picker=5,snap=True)
line2.set_visible(False)

ax.add_line(line1)
ax.add_line(line2)

#mouse and event
cursor = Cursor(ax,horizOn=True,vertOn=True,useblit=True,color='r',linewidth=1)

def onclick(event):
    global swiching
    if(line1.get_visible()==False and line2.get_visible()==False):
        line1.set_visible(True)
        line1.set_xdata([event.xdata,event.xdata])
    elif(line1.get_visible()==True and line2.get_visible()==False):
        line2.set_visible(True)
        line2.set_xdata([event.xdata,event.xdata])
    else:
        line1.set_xdata([event.xdata,event.xdata])
        line2.set_visible(False)


    if(line1.get_visible()==True and line2.get_visible()==True):
        print(line1.get_xdata())
        print(line2.get_xdata())
        print(ax.get_yaxis())
        print(ax.get_ylim())

    c.draw_idle()

fig.canvas.mpl_connect('button_press_event',onclick)

plt.show()