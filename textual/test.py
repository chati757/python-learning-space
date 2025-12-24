from rich.text import Text
from textual.widgets import Tree
from textual.app import App
from rich.console import Console

console = Console()

class MyApp(App):
    def compose(self):
        tree = Tree("Root")

        rich_text = Text.from_markup("ep:xxxxxxx,pnl:xxxxxxx [red] test [/red]", style="#D0FF00")
        node = tree.root.add(rich_text, data=rich_text)

        # ลองดึงออกมาจาก data (จะคง style)
        print(rich_text)
        print(rich_text.style)
        print(node.data.style)

        yield tree

MyApp().run()