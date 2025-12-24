from textual.app import App, ComposeResult
from textual.widgets import Label, Button
from textual.widget import Widget
from textual.reactive import var

class CounterWidget(Widget):
    """Widget ที่มีสถานะนับจำนวน"""
    
    # ต้องกำหนด Reactive Variable ที่ระดับคลาสเท่านั้น ไม่สามารถกำหนดใน __init__(self)
    count = var(0) 
    
    def __init__(self):
        super().__init__()
        self.custom_count = 0

    def compose(self) -> ComposeResult:
        """สร้างเลย์เอาต์ของ Widget"""
        # Label จะแสดงค่าเริ่มต้นของ count
        yield Label(f"นับ: {self.count}", id="counter_label")
        yield Button("เพิ่ม", id="increment_button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """จัดการเมื่อกดปุ่ม"""
        if event.button.id == "increment_button":
            # การเปลี่ยนค่าของ self.count จะทำให้ watch_count ทำงาน
            #self.count += 1
            self.custom_watch_count() #หากอยากใช้ reactive ก็ comment บรรทัดนี้ และ uncomment self.count += 1
    
    def custom_watch_count(self):
        if self.is_mounted:
            self.custom_count +=1
            label = self.query_one("#counter_label", Label)
            label.update(f"นับ: {self.custom_count}")

    def watch_count(self, old_value: int, new_value: int) -> None:
        """
        เมธอดนี้จะทำงานโดยอัตโนมัติเมื่อค่าของ self.count เปลี่ยน
        มีหน้าที่อัปเดต UI ให้ตรงกับสถานะใหม่
        """
        # แก้ไข: ตรวจสอบว่า Widget ถูก mount แล้วหรือไม่ก่อน query (ไม่มีการ block แค่เป็นการ check ธรรมดา ถ้าไม่จริงก็ข้ามไปเลย)
        if self.is_mounted:
            label = self.query_one("#counter_label", Label)
            label.update(f"นับ: {new_value}")

class MyApp(App):
    """แอปที่ใช้ CounterWidget"""
    def compose(self) -> ComposeResult:
        yield CounterWidget()

if __name__ == "__main__":
    app = MyApp()
    app.run()