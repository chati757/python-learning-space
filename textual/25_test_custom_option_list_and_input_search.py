from textual.app import App,ComposeResult,on
from textual.widget import Widget
from textual.widgets import Footer, Header, OptionList, Input
from textual.widgets.option_list import Option
from textual.containers import Vertical
from textual.events import Key # Import Key for event type hinting

class OptionListAndInputSearch(Widget):
    """
    Textual App ที่แสดง OptionList ที่สามารถค้นหาและเรียงลำดับได้.
    """

    # CSS สำหรับจัดวางองค์ประกอบและสไตล์
    DEFAULT_CSS = """
    Vertical {
        width: 100%; /* กำหนดความกว้างของคอนเทนเนอร์หลัก */
        height: 100%; /* กำหนดความสูงของคอนเทนเนอร์หลัก */
        padding: 0; /* เพิ่ม padding ภายในคอนเทนเนอร์ */
        overflow-y: auto;
        overflow-x: auto;
    }

    #_search_input {
        width: 100%; /* Input field ให้เต็มความกว้างของคอนเทนเนอร์ */
        height: 1;
        margin-bottom: 0; /* ระยะห่างด้านล่างของ Input */
        border: none;  /*เพิ่มกรอบโค้งมนให้กับ Input */
        padding: 0 1; /* Padding ภายใน Input */

        &:focus {
            border: none;            
            background-tint: $foreground 5%;
            
        }
    }

    #_option_list {
        width: 100%; /* OptionList ให้เต็มความกว้างของคอนเทนเนอร์ */
        height: 100%; /* ใช้พื้นที่ที่เหลือทั้งหมดใน Vertical container */
        border: round $panel; /* เพิ่มกรอบโค้งมนให้กับ OptionList */
        scrollbar-color: #EEE8D5;
        scrollbar-background: #002B36;
        scrollbar-color-hover:  #EEE8D5;
        scrollbar-background-hover: #002B36;
        scrollbar-color-active: #EEE8D5;
        scrollbar-background-active: #002B36;
    }
    """

    def __init__(self,css_id:str=None):
        super().__init__()
        self.id = css_id
        self._search_input : Input | None = None
        self._options_list_items = []
        self._options_list : OptionList | None = None

    def update_options_list(self,new_options_list:list=[]):
        '''
        #example
        self._options_list_items = [
            Option("Aerilon", id="aer"),
            Option("Aquaria", id="aqu"),
            None, # ตัวคั่น (separator)
        ]
        '''
        # กำหนด options หลัง compose แล้ว
        # อัปเดตรายการใน OptionList
        self._options_list.clear_options()
        self._options_list.add_options(new_options_list)

        # เก็บค่าใหม่ไว้ใน _options_list_items เพื่อใช้ใน on_input_changed
        self._options_list_items = new_options_list

    def compose(self) -> ComposeResult:
        # สร้าง Input widget สำหรับการค้นหา
        self._search_input = Input(placeholder="search command list , [esc] for clear", id="_search_input")
        self._options_list = OptionList(id='_option_list')
        with Vertical(): # ใช้ Vertical container เพื่อจัดเรียง Input และ OptionList ในแนวตั้ง
            yield self._search_input
            yield self._options_list

    def on_mount(self) -> None:
        """
        เรียกเมื่อ Widgets ถูก mount เข้ากับ DOM.
        """
        # ตั้งค่าโฟกัสไปที่ Input field เมื่อ App เริ่มต้น
        #self._search_input.focus()
        pass

    def on_input_changed(self, event: Input.Changed) -> None:
        """
        เรียกเมื่อค่าใน Input field (_search_input) มีการเปลี่ยนแปลง.
        จะทำการกรองและเรียงลำดับรายการ OptionList.
        """
        # รับข้อความค้นหา, ลบช่องว่างหัวท้าย, และแปลงเป็นตัวพิมพ์เล็ก
        search_term = event.value.strip().lower()

        if not search_term:
            # ถ้าข้อความค้นหาว่างเปล่า, ให้แสดงรายการ Option ดั้งเดิมทั้งหมด
            self._options_list.clear_options()
            self._options_list.add_options(self._options_list_items)
            return

        # กรองเฉพาะ Option ที่มีข้อความค้นหาอยู่ใน prompt (ไม่รวม None)
        # แก้ไข: ใช้ str(option.prompt).lower() เพื่อให้แน่ใจว่าเป็น string ก่อนแปลงเป็นตัวพิมพ์เล็ก
        matching_options = [
            option for option in self._options_list_items
            if option is not None and search_term in str(option.prompt).lower()
        ]

        # เรียงลำดับ Option ที่ตรงกันตามตัวอักษร (prompt text)
        # แก้ไข: ใช้ str(option.prompt).lower() ใน key สำหรับการเรียงลำดับ
        sorted_matching_options = sorted(
            matching_options,
            key=lambda option: str(option.prompt).lower()
        )

        # ล้าง OptionList ปัจจุบันและเพิ่ม Option ที่ถูกกรองและเรียงลำดับแล้ว
        self._options_list.clear_options()
        self._options_list.add_options(sorted_matching_options)

    def on_key(self, event: Key) -> None:
        """
        จัดการการกดปุ่ม, โดยเฉพาะปุ่ม Escape เพื่อรีเซ็ตการค้นหา.
        """
        # ตรวจสอบว่าปุ่มที่กดคือ Escape และโฟกัสอยู่ที่ _search_input
        if event.key == "escape" and (self._search_input.has_focus or self._options_list.has_focus):
            if self._search_input.value: # ตรวจสอบว่ามีข้อความใน Input หรือไม่
                # ล้างค่าใน Input field
                self._search_input.value = ""
                # ล้าง OptionList และเพิ่มรายการ Option ดั้งเดิมกลับเข้าไป
                self._options_list.clear_options()
                self._options_list.add_options(self._options_list_items)
                # ตั้งค่าโฟกัสกลับไปที่ Input field
                self._search_input.focus()

        elif event.key == 'down' and self._search_input.has_focus:
            self._options_list.focus()
        elif event.key == 'tab' and self._options_list.has_focus:
            event.stop() #ทำให้ event ไม่ส่งต่อไป handle ที่อื่นเช่น default behavior ของ app
            # สำหรับปุ่ม tab การสั่ง prevent_default() ไม่สามารถหยุดมันได้เพราะการหยุดใน on_key นี้เป็นของ widget ที่หยุด
            # หากมีการสั่ง prevent_default() ซึ่ง default behavior ของ widget ไม่ได้มีการตั้งค่า tab ให้ action อะไร
            # ไว้แต่แรกอยู่แล้ว
            self._search_input.focus()
    
    @on(OptionList.OptionSelected, "#_option_list")
    def option_selected(self, event: OptionList.OptionSelected):
        selected = event.option
        print(f"select : {selected.prompt} (id={selected.id})")

class TestViewApp(App):
    CSS = """

    """
    def compose(self) -> ComposeResult:
        test = OptionListAndInputSearch(css_id='test')
        yield test

    async def on_mount(self) -> None:
        test = self.query_one('#test')
        test_options_list_items = [
            Option("Aerilon", id="aer"),
            Option("Aquaria", id="aqu"),
            Option("Box", id="box"),
            Option("book", id="book"),
            Option("Tank",id='tank'),
            Option("Home",id='home')
        ]
        test.update_options_list(new_options_list=test_options_list_items)

if __name__ == "__main__":
    TestViewApp().run()