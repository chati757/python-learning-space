from textual.app import App, ComposeResult
from textual.widgets import Label

class BorderTitleApp(App):
    CSS = """
    Screen {
        align: center middle;
        layout: vertical;
    }

    #label1 {
        border: round cyan;
        border-title-color: green;
        border-title-style: bold;
        border-title-align: left;
    }

    #label2 {
        border: round yellow;
        border-title-color: blue;
        border-title-style: italic;
        border-title-align: center;
    }

    #label3 {
        border: round magenta;
        border-title-color: red;
        border-title-style: underline;
        border-title-align: right;
    }

    Label {
        padding: 2 4;
    }
    """

    def compose(self) -> ComposeResult:
        yield Label("Label One", id="label1")
        yield Label("Label Two", id="label2")
        yield Label("Label Three", id="label3")

    def on_mount(self) -> None:
        self.query_one("#label1", Label).border_title = "Title A"
        self.query_one("#label2", Label).border_title = "Title B"
        self.query_one("#label3", Label).border_title = "Title C"

        self.query_one("#label1", Label).border_subtitle = "Subtitle A"
        self.query_one("#label2", Label).border_subtitle = "Subtitle B"
        self.query_one("#label3", Label).border_subtitle = "Subtitle C"

if __name__ == "__main__":
    app = BorderTitleApp()
    app.run()
