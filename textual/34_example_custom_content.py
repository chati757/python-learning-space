from textual.app import App,ComposeResult
from textual.content import Content
from textual.widgets import Static
from textual.geometry import Size
from rich.segment import Segment
from rich.console import  ConsoleOptions

class ColorBarContent(Content):
    def measure(self, options: ConsoleOptions, max_width: int) -> Size:
        return Size(20, 1)

    def render_lines(self, options: ConsoleOptions) -> list[list[Segment]]:
        return [[
            Segment("██████████", style="on red"),
            Segment("██████████", style="on green")
        ]]


class TestView(App):
    CSS = """
    """

    def __init__(self):
        super().__init__()

    def compose(self) -> ComposeResult:
        static = Static()
        static.update(ColorBarContent())

    def on_mount(self) -> None:
        pass

if __name__=='__main__':
    TestView().run()