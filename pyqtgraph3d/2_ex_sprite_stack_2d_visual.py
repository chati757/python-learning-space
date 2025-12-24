import numpy as np
import pyqtgraph as pg
import pyqtgraph.opengl as gl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
import sys, math

class PixelStackDemo:
    def __init__(self):
        self.app = QApplication.instance() or QApplication(sys.argv)
        self.view = gl.GLViewWidget()
        self.view.setWindowTitle('2D Pixel Stack in 3D')
        self.view.setGeometry(100, 100, 800, 600)
        self.view.setCameraPosition(distance=50, elevation=25, azimuth=45)
        self.view.setBackgroundColor('#1a1a2e')

        self.models = []
        self.create_pixel_stack()
        self.setup_animation()

    def create_pixel_stack(self):
        num_layers = 10
        for layer in range(num_layers):
            verts, faces, colors = [], [], []
            z = layer * 0.5
            for x in range(-5, 6, 2):
                for y in range(-5, 6, 2):
                    v, f, c = self.create_pixel_cube(x, y, z, [0.2, 0.5, 0.8, 1], layer)
                    start = len(verts)
                    verts.extend(v)
                    faces.extend([[a+start, b+start, c+start] for a,b,c in f])
                    colors.extend(c)

            verts = np.array(verts, dtype=np.float32)
            faces = np.array(faces, dtype=np.uint32)
            colors = np.array(colors, dtype=np.float32)

            # ✅ check consistency
            if faces.size == 0 or verts.shape[0] == 0: 
                continue
            if colors.shape[0] != verts.shape[0]:
                colors = np.tile(colors[0], (verts.shape[0], 1))

            meshdata = gl.MeshData(vertexes=verts, faces=faces, vertexColors=colors)
            mesh = gl.GLMeshItem(meshdata=meshdata, smooth=False, shader='shaded')
            mesh.setGLOptions('opaque')
            self.view.addItem(mesh)
            self.models.append(mesh)

    def create_pixel_cube(self, x, y, z, base_color, seed):
        size, z_thin = 0.8, 0.05
        v = [
            [x-size, y-size, z-z_thin], [x+size, y-size, z-z_thin],
            [x+size, y+size, z-z_thin], [x-size, y+size, z-z_thin],
            [x-size, y-size, z+z_thin], [x+size, y-size, z+z_thin],
            [x+size, y+size, z+z_thin], [x-size, y+size, z+z_thin]
        ]
        f = [[0,1,2],[0,2,3],[4,6,5],[4,7,6],
             [0,4,7],[0,7,3],[1,5,6],[1,6,2],
             [0,1,5],[0,5,4],[3,2,6],[3,6,7]]
        np.random.seed(seed)
        variation = np.random.uniform(-0.1,0.1,3)
        col = np.clip(np.array(base_color[:3])+variation,0,1).tolist()+[1.0]
        c = [col]*8
        return v,f,c

    def setup_animation(self):
        self.angle = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(50)

    def animate(self):
        self.angle += 2
        for m in self.models:
            m.resetTransform()
            m.rotate(self.angle, 0, 0, 1)

    def show(self):
        self.view.show()
        return self.app.exec_()

if __name__ == "__main__":
    demo = PixelStackDemo()
    demo.show()
