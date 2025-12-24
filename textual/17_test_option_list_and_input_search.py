from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, OptionList, Input
from textual.widgets.option_list import Option
from textual.containers import Vertical
from textual.events import Key # Import Key for event type hinting

class OptionListApp(App[None]):
    """
    Textual App ที่แสดง OptionList ที่สามารถค้นหาและเรียงลำดับได้.
    """

    # CSS สำหรับจัดวางองค์ประกอบและสไตล์
    CSS = """
    Screen {
        align: center middle; /* จัดกึ่งกลางหน้าจอ */
    }

    Vertical {
        width: 70%; /* กำหนดความกว้างของคอนเทนเนอร์หลัก */
        height: 80%; /* กำหนดความสูงของคอนเทนเนอร์หลัก */
        border: solid $accent; /* เพิ่มกรอบเพื่อความสวยงาม */
        padding: 0; /* เพิ่ม padding ภายในคอนเทนเนอร์ */
    }

    Input {
        width: 100%; /* Input field ให้เต็มความกว้างของคอนเทนเนอร์ */
        margin-bottom: 0; /* ระยะห่างด้านล่างของ Input */
        border: round $primary; /* เพิ่มกรอบโค้งมนให้กับ Input */
        padding: 0 1; /* Padding ภายใน Input */
    }

    OptionList {
        width: 100%; /* OptionList ให้เต็มความกว้างของคอนเทนเนอร์ */
        height: 1fr; /* ใช้พื้นที่ที่เหลือทั้งหมดใน Vertical container */
        border: round $panel; /* เพิ่มกรอบโค้งมนให้กับ OptionList */
    }

    OptionList > .option-list--option.option-list--highlighted {
        background: $accent; /* สีพื้นหลังเมื่อเลือก Option */
        color: $text; /* สีข้อความเมื่อเลือก Option */
    }
    """

    def compose(self) -> ComposeResult:
        """
        สร้างและจัดเรียง Widgets สำหรับ App.
        """
        # เก็บรายการ Option ดั้งเดิมทั้งหมดไว้ เพื่อใช้ในการรีเซ็ต
        self.original_options = [
            Option("Aerilon", id="aer"),
            Option("Aquaria", id="aqu"),
            None, # ตัวคั่น (separator)
            Option("Canceron", id="can"),
            Option("Caprica", id="cap", disabled=True), # Option ที่ถูกปิดใช้งาน
            None,
            Option("Gemenon", id="gem"),
            None,
            Option("Leonis", id="leo"),
            Option("Libran", id="lib"),
            None,
            Option("Picon", id="pic"),
            None,
            Option("Sagittaron", id="sag"),
            Option("Scorpia", id="sco"),
            None,
            Option("Tauron", id="tau"),
            None,
            Option("Virgon", id="vir1"),
            Option("Leonis", id="leo2"),
            Option("Libran", id="lib3"),
            None,
            Option("Picon", id="pic4"),
            None,
            Option("Sagittaron", id="sag5"),
            Option("Scorpia", id="sco6"),
            None,
            Option("Tauron", id="tau7"),
            None,
            Option("Virgon", id="vir8"),
        ]

        # สร้าง Input widget สำหรับการค้นหา
        self.search_input = Input(placeholder="search command list...", id="search_input")
        # สร้าง OptionList โดยเริ่มต้นด้วยรายการ Option ดั้งเดิม
        self.option_list = OptionList(*self.original_options)

        yield Header() # ส่วนหัวของ App
        with Vertical(): # ใช้ Vertical container เพื่อจัดเรียง Input และ OptionList ในแนวตั้ง
            yield self.search_input
            yield self.option_list
        yield Footer() # ส่วนท้ายของ App

    def on_mount(self) -> None:
        """
        เรียกเมื่อ Widgets ถูก mount เข้ากับ DOM.
        """
        # ตั้งค่าโฟกัสไปที่ Input field เมื่อ App เริ่มต้น
        self.search_input.focus()

    def on_input_changed(self, event: Input.Changed) -> None:
        """
        เรียกเมื่อค่าใน Input field (search_input) มีการเปลี่ยนแปลง.
        จะทำการกรองและเรียงลำดับรายการ OptionList.
        """
        # รับข้อความค้นหา, ลบช่องว่างหัวท้าย, และแปลงเป็นตัวพิมพ์เล็ก
        search_term = event.value.strip().lower()

        if not search_term:
            # ถ้าข้อความค้นหาว่างเปล่า, ให้แสดงรายการ Option ดั้งเดิมทั้งหมด
            self.option_list.clear_options()
            self.option_list.add_options(self.original_options)
            return

        # กรองเฉพาะ Option ที่มีข้อความค้นหาอยู่ใน prompt (ไม่รวม None)
        # แก้ไข: ใช้ str(option.prompt).lower() เพื่อให้แน่ใจว่าเป็น string ก่อนแปลงเป็นตัวพิมพ์เล็ก
        matching_options = [
            option for option in self.original_options
            if option is not None and search_term in str(option.prompt).lower()
        ]

        # เรียงลำดับ Option ที่ตรงกันตามตัวอักษร (prompt text)
        # แก้ไข: ใช้ str(option.prompt).lower() ใน key สำหรับการเรียงลำดับ
        sorted_matching_options = sorted(
            matching_options,
            key=lambda option: str(option.prompt).lower()
        )

        # ล้าง OptionList ปัจจุบันและเพิ่ม Option ที่ถูกกรองและเรียงลำดับแล้ว
        self.option_list.clear_options()
        self.option_list.add_options(sorted_matching_options)

    def on_key(self, event: Key) -> None:
        """
        จัดการการกดปุ่ม, โดยเฉพาะปุ่ม Escape เพื่อรีเซ็ตการค้นหา.
        """
        # ตรวจสอบว่าปุ่มที่กดคือ Escape และโฟกัสอยู่ที่ search_input
        if event.key == "escape" and self.search_input.has_focus:
            if self.search_input.value: # ตรวจสอบว่ามีข้อความใน Input หรือไม่
                # ล้างค่าใน Input field
                self.search_input.value = ""
                # ล้าง OptionList และเพิ่มรายการ Option ดั้งเดิมกลับเข้าไป
                self.option_list.clear_options()
                self.option_list.add_options(self.original_options)
                # ตั้งค่าโฟกัสกลับไปที่ Input field
                self.search_input.focus()
                # ป้องกันไม่ให้ Textual ประมวลผลปุ่ม Escape ต่อไป
                event.prevent_default()

if __name__ == "__main__":
    OptionListApp().run()