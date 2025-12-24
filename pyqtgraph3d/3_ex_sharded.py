import numpy as np
import pyqtgraph as pg
import pyqtgraph.opengl as gl
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QHBoxLayout, QLabel
from PyQt5.QtCore import QTimer
import sys

class ShaderComparison:
    def __init__(self):
        self.app = QApplication.instance()
        if self.app is None:
            self.app = QApplication(sys.argv)
        
        # สร้าง main widget
        self.main_widget = QWidget()
        self.main_widget.setWindowTitle('Shader Comparison: shaded vs normalColor')
        self.main_widget.setGeometry(100, 100, 1200, 600)
        
        # สร้าง layout
        layout = QHBoxLayout()
        self.main_widget.setLayout(layout)
        
        # สร้าง 2 GLViewWidget เพื่อเปรียบเทียบ
        self.setup_views(layout)
        self.create_test_objects()
        self.setup_animation()
        
    def setup_views(self, layout):
        """สร้าง 2 view สำหรับเปรียบเทียบ"""
        # View 1: shader='shaded'
        left_container = QWidget()
        left_layout = QVBoxLayout()
        left_container.setLayout(left_layout)
        
        left_label = QLabel("shader='shaded' (มี lighting)")
        left_label.setStyleSheet("color: white; background-color: black; padding: 5px;")
        left_layout.addWidget(left_label)
        
        self.view_shaded = gl.GLViewWidget()
        self.view_shaded.setBackgroundColor('black')
        self.view_shaded.setCameraPosition(distance=30, elevation=20, azimuth=45)
        left_layout.addWidget(self.view_shaded)
        
        # View 2: shader='normalColor'  
        right_container = QWidget()
        right_layout = QVBoxLayout()
        right_container.setLayout(right_layout)
        
        right_label = QLabel("shader='normalColor' (ไม่มี lighting)")
        right_label.setStyleSheet("color: white; background-color: black; padding: 5px;")
        right_layout.addWidget(right_label)
        
        self.view_flat = gl.GLViewWidget()
        self.view_flat.setBackgroundColor('black')
        self.view_flat.setCameraPosition(distance=30, elevation=20, azimuth=45)
        right_layout.addWidget(self.view_flat)
        
        layout.addWidget(left_container)
        layout.addWidget(right_container)
        
    def create_test_objects(self):
        """สร้าง objects ทดสอบ"""
        self.mesh_items_shaded = []
        self.mesh_items_flat = []
        
        # สร้าง cube หลายๆ อันเพื่อดู lighting effect
        positions = [
            [-8, -4, 0], [0, -4, 0], [8, -4, 0],
            [-8, 4, 0], [0, 4, 0], [8, 4, 0],
            [-4, 0, 6], [4, 0, 6]
        ]
        
        colors = [
            [1, 0, 0, 1],    # แดง
            [0, 1, 0, 1],    # เขียว  
            [0, 0, 1, 1],    # น้ำเงิน
            [1, 1, 0, 1],    # เหลือง
            [1, 0, 1, 1],    # ม่วง
            [0, 1, 1, 1],    # ฟ้า
            [1, 0.5, 0, 1],  # ส้ม
            [0.5, 0, 1, 1]   # ม่วงเข้ม
        ]
        
        for i, (pos, color) in enumerate(zip(positions, colors)):
            # สร้าง cube mesh data
            mesh_data = self.create_cube_mesh(pos, color, size=3)
            
            # สร้าง mesh item แบบ shaded
            mesh_shaded = gl.GLMeshItem(
                meshdata=mesh_data,
                smooth=False,
                shader='shaded',      # มี lighting
                glOptions='translucent'
            )
            self.mesh_items_shaded.append(mesh_shaded)
            self.view_shaded.addItem(mesh_shaded)
            
            # สร้าง mesh item แบบ flat color
            mesh_flat = gl.GLMeshItem(
                meshdata=mesh_data,
                smooth=False, 
                shader='normalColor', # ไม่มี lighting
                glOptions='translucent'
            )
            self.mesh_items_flat.append(mesh_flat)
            self.view_flat.addItem(mesh_flat)
            
        # เพิ่ม light indicator (sphere เล็กๆ) ใน shaded view
        self.add_light_indicator()
        
    def create_cube_mesh(self, position, color, size=2):
        """สร้าง cube mesh data"""
        x, y, z = position
        s = size / 2
        
        # 8 vertices ของ cube
        vertices = np.array([
            [x-s, y-s, z-s], [x+s, y-s, z-s], [x+s, y+s, z-s], [x-s, y+s, z-s],  # bottom
            [x-s, y-s, z+s], [x+s, y-s, z+s], [x+s, y+s, z+s], [x-s, y+s, z+s]   # top
        ], dtype=np.float32)
        
        # 12 triangular faces
        faces = np.array([
            [0,1,2], [0,2,3],  # bottom
            [4,6,5], [4,7,6],  # top  
            [0,4,7], [0,7,3],  # left
            [1,5,6], [1,6,2],  # right
            [0,1,5], [0,5,4],  # front
            [3,2,6], [3,6,7]   # back
        ], dtype=np.uint32)
        
        # สีของทุก vertex
        colors = np.array([color] * 8, dtype=np.float32)
        
        return gl.MeshData(vertexes=vertices, faces=faces, vertexColors=colors)
    
    def add_light_indicator(self):
        """เพิ่ม indicator แสดงตำแหน่งแสง"""
        # สร้าง sphere เล็กๆ แทนแสง
        sphere_data = gl.MeshData.sphere(rows=10, cols=10, radius=1)
        light_sphere = gl.GLMeshItem(
            meshdata=sphere_data,
            color=(1, 1, 1, 0.8),
            shader='normalColor'
        )
        light_sphere.translate(0, 0, 15)  # วางแสงไว้ด้านบน
        self.view_shaded.addItem(light_sphere)
        
        # เพิ่มป้ายกำกับ
        text = gl.GLTextItem(pos=(0, 0, 20), text='Light Source', color='white')
        self.view_shaded.addItem(text)
        
    def setup_animation(self):
        """ตั้งค่า animation"""
        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.angle = 0
        self.timer.start(50)
        
    def animate(self):
        """หมุน objects เพื่อดู lighting effect"""
        self.angle += 1
        
        # หมุน objects ทั้ง 2 view พร้อมกัน
        for item_shaded, item_flat in zip(self.mesh_items_shaded, self.mesh_items_flat):
            # Reset transformation
            item_shaded.resetTransform() 
            item_flat.resetTransform()
            
            # หมุนรอบแกน Y
            item_shaded.rotate(self.angle, 0, 1, 0)
            item_flat.rotate(self.angle, 0, 1, 0)
            
    def show(self):
        """แสดง widget"""
        self.main_widget.show()
        return self.app.exec_()

# เพิ่ม class สำหรับทดสอบ shadow จริงๆ
class RealShadowExample:
    """ตัวอย่างการสร้าง shadow จริงๆ (ซับซ้อนกว่า)"""
    
    def __init__(self):
        self.app = QApplication.instance()
        if self.app is None:
            self.app = QApplication(sys.argv)
            
        self.view = gl.GLViewWidget()
        self.view.setWindowTitle('Real Shadow Example (Manual Implementation)')
        self.view.setGeometry(100, 100, 800, 600)
        self.view.setBackgroundColor('black')
        self.view.setCameraPosition(distance=40, elevation=30, azimuth=45)
        
        self.create_shadow_scene()
        
    def create_shadow_scene(self):
        """สร้าง scene ที่มี shadow จำลอง"""
        # สร้างพื้น
        floor_verts = np.array([
            [-20, -20, 0], [20, -20, 0], [20, 20, 0], [-20, 20, 0]
        ], dtype=np.float32)
        floor_faces = np.array([[0,1,2], [0,2,3]], dtype=np.uint32)
        floor_colors = np.array([[0.3,0.3,0.3,1]] * 4, dtype=np.float32)
        
        floor_mesh = gl.MeshData(vertexes=floor_verts, faces=floor_faces, 
                               vertexColors=floor_colors)
        floor_item = gl.GLMeshItem(meshdata=floor_mesh, shader='shaded')
        self.view.addItem(floor_item)
        
        # สร้าง object ที่จะมีเงา
        cube_data = gl.MeshData.cylinder(rows=10, cols=20, radius=[3, 3], length=8)
        cube_item = gl.GLMeshItem(meshdata=cube_data, color=(1,0,0,1), shader='shaded')
        cube_item.translate(0, 0, 4)
        self.view.addItem(cube_item)
        
        # สร้าง "เงา" จำลองบนพื้น (เป็นแค่รูปทรงสีเข้ม)
        shadow_verts = np.array([
            [-4, -4, 0.1], [4, -4, 0.1], [4, 4, 0.1], [-4, 4, 0.1]
        ], dtype=np.float32)
        shadow_faces = np.array([[0,1,2], [0,2,3]], dtype=np.uint32) 
        shadow_colors = np.array([[0,0,0,0.5]] * 4, dtype=np.float32)
        
        shadow_mesh = gl.MeshData(vertexes=shadow_verts, faces=shadow_faces,
                                vertexColors=shadow_colors)
        shadow_item = gl.GLMeshItem(meshdata=shadow_mesh, shader='normalColor',
                                  glOptions='translucent')
        self.view.addItem(shadow_item)
        
        # แสง
        light = gl.MeshData.sphere(rows=8, cols=8, radius=1)
        light_item = gl.GLMeshItem(meshdata=light, color=(1,1,1,1))
        light_item.translate(5, 5, 15)
        self.view.addItem(light_item)
        
    def show(self):
        self.view.show()
        return self.app.exec_()

# วิธีการใช้งาน
if __name__ == '__main__':
    print("เลือกตัวอย่าง:")
    print("1. เปรียบเทียบ shader")  
    print("2. ตัวอย่าง shadow จำลอง")
    
    choice = input("เลือก (1 หรือ 2): ").strip()
    
    if choice == "2":
        example = RealShadowExample()
    else:
        example = ShaderComparison() 
        
    example.show()