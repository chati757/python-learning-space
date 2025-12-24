import pyqtgraph.opengl as gl
import numpy as np
from pyqtgraph.Qt import QtCore
from pyqtgraph.Qt import QtWidgets

app = QtWidgets.QApplication([])
w = gl.GLViewWidget()
w.opts['projection'] = 'ortho'
w.opts['distance'] = 40
w.opts['azimuth'] = 45
w.opts['elevation'] = 30

w.show()
g = gl.GLGridItem()
w.addItem(g)

#generate random points from -10 to 10, z-axis positive
pos = np.random.randint(-10,10,size=(1000,3))
pos[:,2] = np.abs(pos[:,2])

sp2 = gl.GLScatterPlotItem(pos=pos)
w.addItem(sp2)

#generate a color opacity gradient
color = np.zeros((pos.shape[0],4), dtype=np.float32)
color[:,0] = 1
color[:,1] = 0
color[:,2] = 0.5
color[0:100,3] = np.arange(0,100)/100.

def update():
    ## update volume colors
    global color
    color = np.roll(color,1, axis=0)
    sp2.setData(color=color)

t = QtCore.QTimer()
t.timeout.connect(update)
t.start(50)


## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    app.exec()