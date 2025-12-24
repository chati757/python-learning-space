from textual.app import App, ComposeResult
from textual.widgets import Label
from textual.containers import Vertical
from textual.widgets import Log
from textual.widgets import Tree

class ScrollViaContainerApp(App):
    CSS = """
    #container {
        height: auto;
        width: 1fr;
        border: round green;
        overflow: auto;
    }

    Label {
        padding: 0 1;
    }
    """

    def compose(self) -> ComposeResult:
        with Log(id="container"):
            tree = Tree("Root")
            for i in range(30):  # ลองให้เกินความสูงเพื่อให้ scroll
                tree.root.add(f"Item {i}")
            tree.root.expand_all()
            yield tree

if __name__ == "__main__":
    ScrollViaContainerApp().run()
