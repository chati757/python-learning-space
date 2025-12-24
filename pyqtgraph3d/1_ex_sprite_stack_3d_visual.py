import numpy as np
import pyqtgraph as pg
import pyqtgraph.opengl as gl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
import sys
import math

class VoxelSpriteStack:
    def __init__(self):
        # สร้าง Qt Application
        self.app = QApplication.instance()
        if self.app is None:
            self.app = QApplication(sys.argv)
        
        # สร้าง GLViewWidget
        self.view = gl.GLViewWidget()
        self.view.setWindowTitle('Voxel Sprite Stack Animation')
        self.view.setGeometry(100, 100, 1000, 800)
        
        # ตั้งค่ากล้อง
        self.view.setCameraPosition(distance=80, elevation=25, azimuth=45)
        self.view.setBackgroundColor('#1a1a2e')  # สีพื้นหลังเข้ม
        
        # ตัวแปร animation
        self.angle = 0
        self.bounce_offset = 0
        self.color_shift = 0
        
        # สร้างพื้น grid ก่อน
        self.create_grid_floor()
        
        # สร้าง voxel models หลายแบบ
        self.create_voxel_models()
        self.setup_animation()
        
    def create_grid_floor(self):
        """สร้างพื้น grid pattern"""
        grid_size = 60
        grid_spacing = 2
        
        # สร้าง grid lines
        grid_lines = []
        
        # เส้น grid แนวนอน (X direction)
        for i in range(-grid_size//2, grid_size//2 + 1, grid_spacing):
            x_coords = np.array([-grid_size//2, grid_size//2])
            y_coords = np.array([i, i])
            z_coords = np.array([-2, -2])
            
            line_data = np.column_stack([x_coords, y_coords, z_coords])
            line_item = gl.GLLinePlotItem(pos=line_data, color=(0.3, 0.3, 0.5, 0.6), width=1)
            self.view.addItem(line_item)
        
        # เส้น grid แนวตั้ง (Y direction)
        for i in range(-grid_size//2, grid_size//2 + 1, grid_spacing):
            x_coords = np.array([i, i])
            y_coords = np.array([-grid_size//2, grid_size//2])
            z_coords = np.array([-2, -2])
            
            line_data = np.column_stack([x_coords, y_coords, z_coords])
            line_item = gl.GLLinePlotItem(pos=line_data, color=(0.3, 0.3, 0.5, 0.6), width=1)
            self.view.addItem(line_item)
        
        # สร้างจุดเด่นที่จุดตัดเส้น grid
        self.create_grid_points()
        
        # สร้างวงกลมรอบศูนย์กลาง
        self.create_center_circles()
        
    def create_grid_points(self):
        """สร้างจุดเด่นที่จุดตัดของ grid"""
        grid_size = 60
        grid_spacing = 4  # จุดทุก 4 หน่วย
        
        points_data = []
        colors = []
        
        for x in range(-grid_size//2, grid_size//2 + 1, grid_spacing):
            for y in range(-grid_size//2, grid_size//2 + 1, grid_spacing):
                # คำนวณระยะจากจุดกลาง
                distance = math.sqrt(x*x + y*y)
                
                if distance <= grid_size//2:  # อยู่ในวงกลม
                    points_data.append([x, y, -1.8])
                    
                    # สีที่เปลี่ยนตามระยะ
                    if distance < 10:
                        color = [0.8, 0.9, 1.0, 0.8]  # ฟ้าอ่อนใกล้กลาง
                    elif distance < 20:
                        color = [0.6, 0.8, 0.9, 0.6]  # ฟ้ากลาง
                    else:
                        color = [0.4, 0.6, 0.8, 0.4]  # ฟ้าเข้มขอบนอก
                    
                    colors.append(color)
        
        if points_data:
            points_array = np.array(points_data)
            colors_array = np.array(colors)
            
            scatter_item = gl.GLScatterPlotItem(
                pos=points_array, 
                color=colors_array, 
                size=3
            )
            self.view.addItem(scatter_item)
    
    def create_center_circles(self):
        """สร้างวงกลมรอบศูนย์กลาง"""
        # วงกลมใหญ่
        circle_radius = [15, 25, 35]
        circle_colors = [
            (0.2, 0.8, 1.0, 0.3),  # ฟ้าใส
            (0.8, 0.2, 1.0, 0.2),  # ม่วงใส  
            (1.0, 0.8, 0.2, 0.1)   # ทองใส
        ]
        
        for radius, color in zip(circle_radius, circle_colors):
            circle_points = []
            for angle in range(0, 361, 5):
                x = radius * math.cos(math.radians(angle))
                y = radius * math.sin(math.radians(angle))
                circle_points.append([x, y, -1.5])
            
            circle_array = np.array(circle_points)
            circle_item = gl.GLLinePlotItem(pos=circle_array, color=color, width=2)
            self.view.addItem(circle_item)
    
    def create_voxel_models(self):
        """สร้าง voxel model ทรงกลมเดียว"""
        self.models = []
        self.original_positions = []
        
        # Model เดียว: Sphere shape
        model_pos = [0, 0, 0]
        model = self.create_sphere_shape()
        self.models.append(model)
        self.original_positions.append(model_pos)
        
        # เพิ่ม model ลงใน view
        for mesh_item in model:
            self.view.addItem(mesh_item)
            # ตั้งตำแหน่งเริ่มต้น
            mesh_item.translate(model_pos[0], model_pos[1], model_pos[2])
    
    def create_sphere_shape(self):
        """สร้าง sphere shape แบบ voxel"""
        layers = []
        num_layers = 20
        center_x, center_y = 0, 0
        
        for layer in range(num_layers):
            vertices = []
            colors = []
            faces = []
            
            z = layer * 0.8 - 8  # เริ่มจากล่าง
            
            # คำนวณรัศมีสำหรับแต่ละชั้นให้เป็นทรงกลม
            max_radius = 8  # รัศมีสูงสุด
            layer_height = (layer - num_layers/2) / (num_layers/2)  # -1 to 1
            radius = max_radius * math.sqrt(max(0, 1 - layer_height*layer_height))
            
            # กำหนดสีตามความสูง
            if layer < 5:
                color_base = [0.1, 0.3, 0.9, 1.0]  # น้ำเงินเข้ม (ล่าง)
            elif layer < 10:
                color_base = [0.2, 0.7, 0.9, 1.0]  # ฟ้า (กลางล่าง)
            elif layer < 15:
                color_base = [0.9, 0.7, 0.2, 1.0]  # ทอง (กลางบน)
            else:
                color_base = [0.9, 0.2, 0.2, 1.0]  # แดง (บน)
            
            # สร้าง voxels แบบวงกลมสำหรับแต่ละชั้น
            if radius > 0.5:  # มีขนาดพอ
                for angle in range(0, 360, 15):  # ทุก 15 องศา
                    for r in range(1, int(radius) + 1):
                        # ตรวจสอบว่าอยู่ในวงกลมหรือไม่
                        x = center_x + r * math.cos(math.radians(angle))
                        y = center_y + r * math.sin(math.radians(angle))
                        
                        distance_from_center = math.sqrt(x*x + y*y)
                        if distance_from_center <= radius:
                            # สร้าง cube
                            cube_verts, cube_faces, cube_colors = self.create_voxel_cube(
                                x, y, z, color_base, layer + angle + r
                            )
                            
                            start_idx = len(vertices)
                            vertices.extend(cube_verts)
                            colors.extend(cube_colors)
                            
                            # ปรับ face indices
                            for face in cube_faces:
                                faces.append([start_idx + face[0], start_idx + face[1], start_idx + face[2]])
            
            if len(vertices) > 0:
                vertices = np.array(vertices, dtype=np.float32)
                faces = np.array(faces, dtype=np.uint32)
                colors = np.array(colors, dtype=np.float32)
                
                mesh_data = gl.MeshData(vertexes=vertices, faces=faces, vertexColors=colors)
                mesh_item = gl.GLMeshItem(meshdata=mesh_data, smooth=False, shader='shaded')
                layers.append(mesh_item)
        
        return layers
    
    def create_voxel_cube(self, x, y, z, base_color, variation_seed):
        """สร้าง voxel cube พร้อมสีที่หลากหลาย"""
        size = 0.4  # ขนาด voxel
        
        # 8 vertices ของ cube
        vertices = [
            [x-size, y-size, z-size], [x+size, y-size, z-size],
            [x+size, y+size, z-size], [x-size, y+size, z-size],
            [x-size, y-size, z+size], [x+size, y-size, z+size],
            [x+size, y+size, z+size], [x-size, y+size, z+size]
        ]
        
        # 12 triangular faces
        faces = [
            [0,1,2], [0,2,3],  # bottom
            [4,6,5], [4,7,6],  # top
            [0,4,7], [0,7,3],  # left
            [1,5,6], [1,6,2],  # right
            [0,1,5], [0,5,4],  # front
            [3,2,6], [3,6,7]   # back
        ]
        
        # สีที่หลากหลาย
        np.random.seed(int(variation_seed) % 1000)
        color_variation = np.random.uniform(-0.2, 0.2, 3)
        
        final_color = [
            max(0, min(1, base_color[0] + color_variation[0])),
            max(0, min(1, base_color[1] + color_variation[1])),
            max(0, min(1, base_color[2] + color_variation[2])),
            base_color[3]
        ]
        
        colors = [final_color] * 8
        
        return vertices, faces, colors
    
    def setup_animation(self):
        """ตั้งค่า animation"""
        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(50)  # 50ms = 20fps
    
    def animate(self):
        """Animation function"""
        self.bounce_offset += 0.1
        
        # มี model เดียว
        model = self.models[0]
        base_pos = self.original_positions[0]
        
        # Bouncing effect
        model_bounce = 2.0 * math.sin(self.bounce_offset * 1.2)
        
        for layer_idx, mesh_item in enumerate(model):
            # Reset transformation
            mesh_item.resetTransform()
            
            # เคลื่อนไหวขึ้นลงแต่ละชั้น (subtle layer animation)
            layer_bounce = model_bounce + math.sin(self.bounce_offset * 3 + layer_idx * 0.15) * 0.5
            
            # หมุนรอบแกน Y
            rotation_angle = self.bounce_offset * 2
            
            # วางตำแหน่งใหม่
            mesh_item.translate(base_pos[0], base_pos[1], base_pos[2] + layer_bounce)
            mesh_item.rotate(rotation_angle, 0, 0, 1)  # หมุนรอบแกน Z
                
    def show(self):
        """แสดง widget"""
        self.view.show()
        return self.app.exec_()

# วิธีการใช้งาน
if __name__ == '__main__':
    voxel_demo = VoxelSpriteStack()
    voxel_demo.show()