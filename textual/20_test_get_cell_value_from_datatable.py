from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, DataTable
from textual.containers import Container
from textual.widget import Widget

class GetRowDataScreen(Widget):

    BINDINGS = [
        ("d", "display_data", "Display Data from Row Key"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        with Container():
            yield DataTable(id="my_data_table")
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one("#my_data_table", DataTable)
        table.add_column("Name",key="Name")
        table.add_column("Age",key="Age")
        table.add_column("City",key="City")

        # เพิ่มข้อมูลพร้อมกำหนด custom_key
        self.user_alice_key = table.add_row("Alice", 30, "New York", key="user_alice")
        self.user_bob_key = table.add_row("Bob", 25, "London", key="user_bob")
        
        self.notify(f"Alice's Row Key: {self.user_alice_key}")
        self.notify(f"Bob's Row Key: {self.user_bob_key}")

    def action_display_data(self) -> None:
        table = self.query_one("#my_data_table", DataTable)
        
        # สมมติว่าเราต้องการดึงข้อมูลของ Alice
        target_row_key = self.user_alice_key # ซึ่งคือ ('user_alice',)
        
        
        row_data = table.get_row(target_row_key)
        self.notify(f"Data for {target_row_key}: {row_data}")
            
        # หากต้องการเข้าถึงข้อมูลแต่ละคอลัมน์:
        # สมมติว่า "Age" เป็นคอลัมน์ที่ 2 (index 1)
        age = row_data[table.get_column_index('Age')] 
        self.notify(f"Alice's Age: {age}")
        

class MyApp(App):
    def compose(self):
        yield GetRowDataScreen()

if __name__ == "__main__":
    app = MyApp()
    app.run()