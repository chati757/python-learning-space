from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout

console = Console()

layout = Layout(name='panel_layout',ratio=6)
sub_layout_1 = Layout(name='panel_sub_layout1',ratio=3)
sub_layout_2 = Layout(name='panel_sub_layout2',ratio=3,size=100)

layout.split_row(
    sub_layout_1,
    sub_layout_2
)

panel = Panel(layout,title='title panel')
panel.height = 20

console.print(panel)