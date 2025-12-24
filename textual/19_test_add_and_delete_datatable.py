from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, DataTable, Button
from textual.containers import Container
from textual.widget import Widget

class DeleteRowScreen(Widget):

    BINDINGS = [
        ("a", "add_row", "Add Row"),
        ("d", "delete_last_row", "Delete Last Row"),
    ]

    def __init__(self):
        super().__init__()
        self.product_keys_in_table = {}

    def compose(self) -> ComposeResult:
        yield Header()
        with Container():
            yield DataTable()
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns("Column A", "Column B", "Column C")
        # เพิ่ม Row แรกเข้าไป และเก็บ Row Key
        row_count = table.row_count + 1
        self.first_row_key = table.add_row("Hello", "World", "Textual!",key=f'test_key_{row_count}')
        self.notify(f"Added row test_key_{row_count} : {self.first_row_key}")

    def action_add_row(self) -> None:
        table = self.query_one(DataTable)
        row_count = table.row_count + 1
        new_row_data = [f"Data {row_count}-A", f"Data {row_count}-B", f"Data {row_count}-C"]
        row_key = table.add_row(*new_row_data,key=f'test_key_{row_count}')
        self.product_keys_in_table[f'test_key_{row_count}'] = row_key
        self.notify(f"Added row test_key_{row_count} : {row_key}")

    def action_delete_last_row(self) -> None:
        table = self.query_one(DataTable)
        #ทดสอบระุบุ row_key ที่สร้างก่อนหน้าเพื่อทำการลบแถวนั้น
        table.remove_row('test_key_1')

class MyApp(App):
    """Textual app with a DataTable."""

    def compose(self):
        yield DeleteRowScreen()

    def on_mount(self) -> None:
        pass

if __name__ == "__main__":
    app = MyApp()
    app.run()