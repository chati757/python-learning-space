import sys
import matplotlib.pyplot as plt
import matplotlib.lines as lines

fig = plt.figure(tight_layout=True,figsize=[4,4],dpi=100)
fig.suptitle('testing')

mgs = fig.add_gridspec(1, 1) #main grid
sgs = mgs[0].subgridspec(1, 1) #sub grid

ax = fig.add_subplot(sgs[0,0])

xdata = [0,1,2]
ydata = [0,0.4,-0.4]
ax.plot(xdata,ydata)
main_status_txt_str = '[1] scope net val\n[2] scope val by price'
main_status_txt = ax.text(0.99, 0.01, main_status_txt_str,
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='green', fontsize=10)

class Cursor:
    """
    A cross hair cursor using blitting for faster redraw.
    """
    def __init__(self, ax):
        self.ax = ax
        self.background = None
        self.default_color = 'k'
        self.horizontal_line = ax.axhline(color=self.default_color, lw=1, ls='-')
        self.vertical_line = ax.axvline(color=self.default_color, lw=1, ls='-')
        self._creating_background = False
        ax.figure.canvas.mpl_connect('draw_event', self.on_draw)

    def on_draw(self, event):
        print('cursor : on draw')
        self.create_new_background()

    def set_cross_hair_visible(self, visible):
        need_redraw = self.horizontal_line.get_visible() != visible
        self.horizontal_line.set_visible(visible)
        self.vertical_line.set_visible(visible)
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

class two_line_scope:
    def __init__(self,map_key,color_line):
        self.map_key = map_key
        self.color_line = color_line
        self.c = ax.get_figure().canvas
        self.sid_key_press_event = fig.canvas.mpl_connect('key_press_event', self.on_key_press)
        self.sid_click_event = None
        self.line1 = lines.Line2D([0,0],[ax.get_ylim()[0],ax.get_ylim()[1]],picker=5,snap=True,color=color_line,linewidth=1)
        self.line1.set_visible(False)
        ax.add_line(self.line1)
        self.line2 = lines.Line2D([0,0],[ax.get_ylim()[0],ax.get_ylim()[1]],picker=5,snap=True,color=color_line,linewidth=1)
        self.line2.set_visible(False)
        ax.add_line(self.line2)

    def on_key_press(self,event):
        if(event.key==self.map_key):
            main_status_txt.set_text('scoping val net')
            cursor.set_color(self.color_line)
            self.c.draw_idle()
            self.sid_click_event = fig.canvas.mpl_connect('button_press_event',self.on_click)
        else:
            main_status_txt.set_text(main_status_txt_str)
            cursor.set_default_color()
            self.c.draw_idle()
            fig.canvas.mpl_disconnect(self.sid_click_event)
    
    def on_click(self,event):
        if(self.line1.get_visible()==False and self.line2.get_visible()==False):
            #create_first_line
            print('onfirst line')
            self.line1.set_visible(True)
            self.line1.set_xdata([event.xdata,event.xdata])
        elif(self.line1.get_visible()==True and self.line2.get_visible()==False):
            #create_second_line
            print('on second line')
            self.line2.set_visible(True)
            self.line2.set_xdata([event.xdata,event.xdata])
            #calcualte
            print('calculating..')
        elif(self.line1.get_visible()==True and self.line2.get_visible()==True):
            print('on recreate')
            #recreate_first_line
            self.line1.set_xdata([event.xdata,event.xdata])
            self.line2.set_visible(False)
        
        self.c.draw_idle()
                
tls1 = two_line_scope('1','r')

plt.show()