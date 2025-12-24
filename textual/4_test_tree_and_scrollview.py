from textual.app import App, ComposeResult
from textual.widgets import Tree
from textual.scroll_view import ScrollView
from textual.containers import Container

class TreeInBoxApp(App):
    CSS = """
    Screen {
        align: center middle;
    }

    Tree > .tree--guides {
        color: #EEE8D5;
    }
    Tree > .tree--guides-hover {
        color: #EEE8D5;
    }
    Tree > .tree--guides-selected {
        color: #EEE8D5;
    }

    #box {
        width: 60;
        height: 20;
        border: round #EEE8D5;
        border-title-color: red;
        border-title-style: bold;
        background:#002B36;
    }


    """

    def compose(self) -> ComposeResult:
        with Container(id="box"):
            with ScrollView():
                tree = Tree("Root")
                for i in range(30):  # ลองให้เกินความสูงเพื่อให้ scroll
                    tree.root.add(f"Item {i}")
                tree.root.expand_all()
                yield tree


if __name__ == "__main__":
    app = TreeInBoxApp()
    app.run()
