from rich.table import Table
from textual import events
from textual.app import App, ComposeResult
from textual.widgets import RichLog

class RichLogTwoColumnApp(App):
    def compose(self) -> ComposeResult:
        yield RichLog(highlight=True, markup=True)

    def on_ready(self) -> None:
        log = self.query_one(RichLog)

        # ✅ สร้างตาราง 2 columns ชิดซ้าย ไม่มี header
        table = Table(show_header=False, show_edge=False, box=None , padding=(0,1))
        table.add_column(justify="left")
        table.add_column(justify="left")

        # ✅ ข้อมูลตัวอย่าง
        data = [
            ("Apple", "Red"),
            ("Banana", "Yellow"),
            ("Grapes", "Purple"),
            ("Mango", "Orange")
        ]

        for row in data:
            table.add_row(*row)

        # ✅ ส่งตารางไปที่ RichLog
        log.write("[bold cyan]Fruit Colors (No Header Table):")
        log.write(table)
        log.write("[green]Done rendering 2-column table without header!")

    def on_key(self, event: events.Key) -> None:
        log = self.query_one(RichLog)
        log.write(f"[yellow]Key pressed:[/] {event.key}")

if __name__ == "__main__":
    RichLogTwoColumnApp().run()
