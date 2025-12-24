import numpy as np
import pyqtgraph as pg
import pyqtgraph.opengl as gl
from pyqtgraph.Qt import QtWidgets

app = QtWidgets.QApplication([])
w = gl.GLViewWidget()
w.opts['projection'] = 'ortho'
w.opts['distance'] = 40
w.opts['azimuth'] = 45
w.opts['elevation'] = 30
w.show()
w.setWindowTitle('3D Cloud Point with Custom Colors')
w.setCameraPosition(distance=40)

n = 10000
pos = np.random.normal(size=(n, 3), scale=10)

# สร้าง array สีเปล่า
colors = np.empty((n, 4), dtype=np.float32)

# กำหนดสีตามตำแหน่งแกน Z โดยตรง
z_min = pos[:, 2].min()
z_max = pos[:, 2].max()
z_range = z_max - z_min

# กำหนดสีจากค่า z-coordinate โดยตรง
# จุดที่มีค่า z ต่ำจะเป็นสีน้ำเงิน (Blue)
# จุดที่มีค่า z สูงจะเป็นสีแดง (Red)
colors[:, 0] = (pos[:, 2] - z_min) / z_range  # Red (0-1)
colors[:, 1] = 0.0  # Green
colors[:, 2] = 1.0 - (pos[:, 2] - z_min) / z_range # Blue (1-0)
colors[:, 3] = 1.0 # Alpha (ความทึบแสง 1.0 = ทึบ)

# สร้าง scatter plot
sp = gl.GLScatterPlotItem(pos=pos, color=colors, size=2, pxMode=True)
w.addItem(sp)

app.exec()