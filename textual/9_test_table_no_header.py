from rich.text import Text
from textual.app import App, ComposeResult
from textual.widgets import DataTable

ROWS = [
    ("BBU_MAX_CHG.","123123.44","[red]123.45 %[/red]","123123.44 FP.","123.45 %"),
    ("BBU_CHG.","123123.44","123.45 %","123123.44 FP.","123.45 %"),
    ("CHG.","123123.44","123.45 %","123123.44 FP.","123.45 %"),
    ("BBL_CHG.","123123.44","123.45 %","123123.44 FP.","123.45 %"),
    ("BBL_MIN_CHG.","123123.44","123.45 %","123123.44 FP.","123.45 %")
]


class TableApp(App):
    CSS="""
    DataTable {
        color:#B1C2C2;
        background:#002B36;

        & > .datatable--header {
            color:#B1C2C2; /*#EEE8D5;*/
            background:#002B36;
        }
    }
    """

    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)

        headers = ROWS[0]
        # Adding styled and justified `Text` objects instead of plain strings.
        styled_row_header = [Text(str(cell),style="#EEE8D5",justify="right") if(c==0) else str(cell) for c,cell in enumerate(headers)]
        table.add_columns(*styled_row_header)

        for row in ROWS[1:]:
            # Adding styled and justified `Text` objects instead of plain strings.
            styled_row = [Text(str(cell),style="#EEE8D5",justify="right") if(c==0) else str(cell) for c,cell in enumerate(row)]
            table.add_row(*styled_row)

        table.cursor_type = 'none'


app = TableApp()
if __name__ == "__main__":
    app.run()
