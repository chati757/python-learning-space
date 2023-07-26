import sys
import matplotlib.pyplot as plt
import matplotlib.lines as lines

fig = plt.figure(tight_layout=True,figsize=[4,4],dpi=100)
fig.suptitle('testing')

mgs = fig.add_gridspec(2, 1) #main grid
sgs = mgs[0].subgridspec(1, 1) #sub grid
sgs2 = mgs[1].subgridspec(1,1)

ax = fig.add_subplot(sgs[0,0])
xdata = [0,1,2]
ydata = [0,0.4,-0.4]
ax.plot(xdata,ydata)

ax2 = fig.add_subplot(sgs2[0,0])
xdata = [0,1,2]
ydata = [0,0.4,-0.4]
ax2.plot(xdata,ydata)

class Cursor:
    """
    A cross hair cursor using blitting for faster redraw.
    """
    def __init__(self, ax,horizon=True,vertical=True):
        self.ax = ax
        self.background = None
        self.default_color = 'k'
        self.horizon = horizon
        self.vertical = vertical
        self.horizontal_line = ax.axhline(color=self.default_color, lw=1, ls='-')
        self.vertical_line = ax.axvline(color=self.default_color, lw=1, ls='-')
        self._creating_background = False
        ax.figure.canvas.mpl_connect('draw_event', self.on_draw)

    def on_draw(self, event):
        print('cursor : on draw')
        self.create_new_background()

    def set_cross_hair_visible(self, visible):
        need_redraw = self.vertical_line.get_visible() != visible
        self.horizontal_line.set_visible(False if(self.horizon==False) else visible)
        self.vertical_line.set_visible(False if(self.vertical==False) else visible)
        return need_redraw

    def create_new_background(self):
        if self._creating_background:
            print('cursor : exit')
            # discard calls triggered from within this function (from self.ax.figure.canvas.draw() function)
            return
        self._creating_background = True

        self.set_cross_hair_visible(False)
        print('cursor : before draw')
        self.ax.figure.canvas.draw()
        print('cursor : after draw')

        self.background = self.ax.figure.canvas.copy_from_bbox(self.ax.bbox)
        self._creating_background = False
        print('cursor : saving background')

    def on_mouse_move(self, event):
        if self.background is None:
            self.create_new_background()
        if not event.inaxes:
            need_redraw = self.set_cross_hair_visible(False)
            if need_redraw:
                self.ax.figure.canvas.restore_region(self.background)
                self.ax.figure.canvas.blit(self.ax.bbox)
        else:
            self.set_cross_hair_visible(True)
            # update the line positions
            x, y = event.xdata, event.ydata
            self.horizontal_line.set_ydata(y)
            self.vertical_line.set_xdata(x)

            self.ax.figure.canvas.restore_region(self.background)
            self.ax.draw_artist(self.horizontal_line)
            self.ax.draw_artist(self.vertical_line)
            self.ax.figure.canvas.blit(self.ax.bbox)
    
    def set_color(self,color):
        self.horizontal_line.set_color(color)
        self.vertical_line.set_color(color)
    
    def set_default_color(self):
        self.horizontal_line.set_color(self.default_color)
        self.vertical_line.set_color(self.default_color)

cursor = Cursor(ax)
fig.canvas.mpl_connect('motion_notify_event', cursor.on_mouse_move)
cursor2 = Cursor(ax2,horizon=False)
fig.canvas.mpl_connect('motion_notify_event', cursor2.on_mouse_move)

plt.show()