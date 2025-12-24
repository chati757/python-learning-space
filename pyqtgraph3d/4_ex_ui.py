import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
import pyqtgraph as pg

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQtGraph + Button Example")

        # สร้าง central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout หลัก
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # สร้างกราฟ
        self.plot_widget = pg.PlotWidget()
        layout.addWidget(self.plot_widget)

        # สร้างปุ่ม
        self.button = QPushButton("Plot Data")
        layout.addWidget(self.button)

        # กำหนด action เมื่อกดปุ่ม
        self.button.clicked.connect(self.plot_data)

    def plot_data(self):
        # ล้างกราฟก่อน
        self.plot_widget.clear()

        # สร้างข้อมูลทดลอง
        x = list(range(10))
        y = [i**2 for i in x]

        # plot ลงในกราฟ
        self.plot_widget.plot(x, y, pen='r', symbol='o')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
