from textual.app import App, ComposeResult
from textual.widgets import DataTable, Header, Footer
from textual.containers import Container,Vertical
from textual.coordinate import Coordinate
from rich.text import Text

class CellDoesNotExist(Exception):
    """The cell key/index was invalid."""

class Custom2AxisesTable(DataTable):
    DEFAULT_CSS = """
    Custom2AxisesTable {
        /* ไม่ต้องมี content-align ที่นี่ ถ้าต้องการให้เนื้อหาใน cell จัดขวา */
        color: #B1C2C2;
        background: #002B36;
        width: auto; /* สำคัญ: ให้ DataTable มีความกว้างตามเนื้อหา */
        height: auto; /* สำคัญ: ให้ DataTable มีความสูงตามเนื้อหา */
        padding-top:0;
    }

    Custom2AxisesTable > .datatable--header {
        color: #EEE8D5;
        background: #002B36;
        text-style: bold;
        /* การจัดหัวคอลัมน์จะถูกกำหนดใน insert_column */
    }
    """
    def __init__(self,css_id:str=None):
        super().__init__()
        self.cursor_type='none'
        self.id = css_id

    def insert_column(self, key: str):
        """เพิ่มคอลัมน์พร้อม label ชิดขวา"""
        # ให้ label ของหัวคอลัมน์ชิดขวา
        label = Text.from_markup(key, justify="right") 
        self.add_column(key=key, label=label)

    def insert_row(self, row):
        """เพิ่มแถวโดยทำให้ค่าทุก cell ชิดขวา"""
        styled_row = []
        for c, cell in enumerate(row):
            # ตรวจสอบว่า cell เป็น Text object อยู่แล้วหรือไม่
            if isinstance(cell, Text):
                # ถ้าเป็น Text object อยู่แล้ว ตรวจสอบว่าต้องการปรับ justify มั้ย
                # ถ้าไม่ต้องการให้ override justify เดิม ก็ไม่ต้องทำอะไร
                # แต่ถ้าอยากให้ชิดขวาแน่ๆ ก็กำหนด justify="right"
                styled_row.append(Text(cell.plain, style=cell.style, justify="right"))
            else:
                # ถ้าไม่ใช่ Text object ให้สร้าง Text object และกำหนด justify="right"
                # คอลัมน์แรก (c==0) ให้สี #EEE8D5 ส่วนที่เหลือเป็นสี default
                if c == 0:
                    styled_row.append(Text.from_markup(str(cell), style="#EEE8D5", justify="right"))
                else:
                    styled_row.append(Text.from_markup(str(cell), justify="right"))
        self.add_row(*styled_row)

    def update_cell_at(self,row,col,value,update_width=True):
        buff_coord = Coordinate(row=row,column=col)
        if not self.is_valid_coordinate(buff_coord):
            raise CellDoesNotExist(f"Coordinate {buff_coord!r} is invalid.")

        row_key, column_key = self.coordinate_to_cell_key(buff_coord)
        
        # เมื่ออัปเดตเซลล์ ก็ต้องแน่ใจว่าเนื้อหาถูกจัดชิดขวาด้วย
        if not isinstance(value, Text):
            # คุณอาจจะดึง style เดิมของ cell มาใช้ด้วย ถ้าต้องการรักษา style
            # สำหรับตัวอย่างนี้ กำหนดแค่ justify
            value = Text.from_markup(str(value), justify="right") 
        elif value.justify != "right": # ถ้าเป็น Text object แต่ justify ไม่ใช่ right ก็ปรับ
             value = Text(value.plain, style=value.style, justify="right")

        self.update_cell(row_key, column_key, value, update_width=update_width)


class TestViewApp(App):
    CSS = """
    Vertical {
        /* Container จะปรับขนาดตามเนื้อหาของ Custom2AxisesTable */
        width: 50%;
        height: auto;
        /* ไม่ต้องมี align: center middle ที่นี่อีก เพราะ Screen จัดการให้แล้ว */
        /* ถ้า Container มีขนาดใหญ่กว่า Table และอยากให้ Table อยู่ตรงกลาง Container
           ก็สามารถใส่ align: center middle; ที่นี่ได้ */
        border: thick red; /* เพื่อให้เห็นขอบเขตของ Container */
        align: center middle;
        layout:vertical;
    }
    """
    def compose(self) -> ComposeResult:
        with Vertical():
            # ตรวจสอบว่า ID ตรงกับที่ใช้ใน query_one()
            yield Custom2AxisesTable(css_id='Custom2AxisesTable') 

    async def on_mount(self) -> None:
        custom_spot_and_usdtm_future_change_table = self.query_one("#Custom2AxisesTable")

        headers = ["11:23:42", "SPOT", "SPOT_CHG", "F_PERP","F_PERP_CHG"]
        
        topic_rows = ['BBU_MAX_CHG','BBU_CHG','CHG','BBL_CHG','BBL_MIN_CHG']
        
        rows = [
            ("123123.44","[#a9fcbf]123.45 %[/#a9fcbf]","123123.44","123.45 %"),
            ("123123.44","123.45 %","123123.44","123.45 %"),
            ("123123.44","123.45 %","123123.44","123.45 %"),
            ("123123.44","123.45 %","123123.44","123.45 %"),
            ("123123.44","123.45 %","123123.44","123.45 %")
        ]

        rows = [(topic_row,) + row for topic_row, row in zip(topic_rows, rows)]

        for header in headers:
            custom_spot_and_usdtm_future_change_table.insert_column(header)

        for row in rows:
            custom_spot_and_usdtm_future_change_table.insert_row(row)

        # อัปเดตเซลล์ด้วยค่าใหม่ และจะถูก justify="right" ใน update_cell_at
        custom_spot_and_usdtm_future_change_table.update_cell_at(0,0,'test_update',True)
        custom_spot_and_usdtm_future_change_table.refresh()


if __name__ == "__main__":
    TestViewApp().run()