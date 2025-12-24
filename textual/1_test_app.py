from textual.app import App, ComposeResult
from textual.widgets import Input, Static
from textual.containers import Horizontal, Vertical
from rich.markdown import Markdown
from textual.events import Key

class PostingApp(App):
    CSS = """
    Screen {
        layout: horizontal;
    }

    #editor {
        width: 1fr;
        layout: vertical;
        padding: 1;
        border: solid green;
    }

    #preview {
        width: 1fr;
        padding: 1;
        border: round blue;
        background: $panel;
    }

    Input {
        height: 3;               /* ความสูง input พอดี */
        width: 100%;             /* เต็มความกว้าง container */
        background: $surface;    /* สีพื้น input */
        color: $text;            /* สีข้อความ */
        border: solid red;       /* เส้นขอบช่วยดู layout (ลบออกได้ภายหลัง) */
    }
    """

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Vertical(
                Input(placeholder="Type markdown here...", id="editor_input"),
                id="editor"
            ),
            Static("Preview", id="preview")
        )

    def on_input_changed(self, event: Input.Changed):
        md = Markdown(event.value)
        self.query_one("#preview", Static).update(md)

    def on_key(self, event: Key) -> None:
        if event.key in ("q", "ctrl+c"):
            self.exit()

if __name__ == "__main__":
    PostingApp().run()
