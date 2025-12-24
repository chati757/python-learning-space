from rich.table import Table
from textual import events
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widget import Widget
from textual.widgets import RichLog

class CustomRichlog2Columns(Widget):
    DEFAULT_CSS = """
    #_richlog{
    }
    """
    def __init__(self,css_id:str=None):
        super().__init__()
        self.id = css_id
        self._richlog : RichLog | None = None

    def compose(self):
        self._richlog = RichLog(id='_richlog',highlight=True,markup=True)
        yield self._richlog

    def add_rich_table(self,rich_table_data:list[tuple[str,str]]):
        #padding=(0,1) → ไม่มีเว้นบรรทัดบน/ล่าง แต่เว้นขอบซ้ายและขวาของเนื้อหาเซลล์ไว้ 1 ช่อง
        rich_table = Table(show_header=False,show_edge=False,box=None,padding=(0,1))
        rich_table.add_column(justify='left')
        rich_table.add_column(justify='left')

        for row in rich_table_data:
            rich_table.add_row(*row)

        self._richlog.write(rich_table)

    def clear_richlog(self):
        self._richlog.clear()


class TestViewApp(App):
    CSS = """
    Horizontal{
        align: center top;
    }

    CustomRichlog2Columns{
        width: 30%;
        height: 40%;
    }

    """
    def compose(self) -> ComposeResult:
        with Horizontal():
            yield CustomRichlog2Columns(css_id='testsome')

    async def on_mount(self) -> None:
        test = self.query_one('#testsome')

       
        data = [
            ("Apple", "Red"),
            ("Banana", "Yellow"),
            ("Grapes", "Purple"),
            ("Mango", "Orange")
        ]
        
        test.add_rich_table(data)
        

if __name__ == "__main__":
    TestViewApp().run()