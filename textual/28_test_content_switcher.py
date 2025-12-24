from textual.app import App, ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Button, ContentSwitcher, DataTable, Markdown
import asyncio
from textual.reactive import var

MARKDOWN_EXAMPLE = """# Three Flavours Cornetto

The Three Flavours Cornetto trilogy is an anthology series of British
comedic genre films directed by Edgar Wright.

## Shaun of the Dead

| Flavour | UK Release Date | Director |
| -- | -- | -- |
| Strawberry | 2004-04-09 | Edgar Wright |

## Hot Fuzz

| Flavour | UK Release Date | Director |
| -- | -- | -- |
| Classico | 2007-02-17 | Edgar Wright |

## The World's End

| Flavour | UK Release Date | Director |
| -- | -- | -- |
| Mint | 2013-07-19 | Edgar Wright |
"""


class ContentSwitcherApp(App[None]):
    CSS = """
        Screen {
        align: center middle;
        padding: 1;
    }

    #buttons {
        height: 3;
        width: auto;
    }

    ContentSwitcher {
        border: round $primary;
        width: 90%;
        height: 1fr;
    }

    MarkdownH2 {
        background: $panel;
        color: yellow;
        border: none;
        padding: 0 1;
    }
    """

    # แก้ไข: ย้ายการกำหนด var มาที่ระดับคลาส
    current_page = var("data-table")

    def compose(self) -> ComposeResult:
        with Horizontal(id="buttons"):
            yield Button("DataTable", id="data-table")
            yield Button("Markdown", id="markdown")

        with ContentSwitcher(initial="data-table"):
            yield DataTable(id="data-table")
            with VerticalScroll(id="markdown"):
                yield Markdown(MARKDOWN_EXAMPLE)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        print(f"ปุ่มถูกกด: {event.button.id}")
        self.current_page = event.button.id

    async def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns("Book", "Year")
        table.add_rows(
            [
                (title.ljust(35), year)
                for title, year in (
                    ("Dune", 1965),
                    ("Dune Messiah", 1969),
                    ("Children of Dune", 1976),
                    ("God Emperor of Dune", 1981),
                    ("Heretics of Dune", 1984),
                    ("Chapterhouse: Dune", 1985),
                )
            ]
        )
        
        # เริ่ม Worker สำหรับการสลับหน้าอัตโนมัติ
        self.run_worker(self.auto_switch())

    def watch_current_page(self, old_page: str, new_page: str) -> None:
        """
        เมธอดนี้จะทำงานอัตโนมัติเมื่อ 'current_page' เปลี่ยนค่า
        """
        print(f"สถานะเปลี่ยน: {old_page} -> {new_page}")
        switcher = self.query_one(ContentSwitcher)
        switcher.current = new_page

    async def auto_switch(self) -> None:
        """
        Worker ที่ทำงานอยู่เบื้องหลังเพื่อสลับหน้าอัตโนมัติ
        """
        self.current_page = 'data-table'
        await asyncio.sleep(3)

        self.current_page = 'markdown'
        await asyncio.sleep(3)
        
        # สามารถเพิ่มโค้ดที่นี่เพื่อสลับกลับไปกลับมาได้
        self.current_page = 'data-table'


if __name__ == "__main__":
    ContentSwitcherApp().run()