import random
import time
from rich.table import Table
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.layout import Layout

layout = None
table_panel = None

def generate_table() -> Table:
    """Make a new table."""
    table = Table()
    table.add_column("ID")
    table.add_column("Value")
    table.add_column("Status")

    for row in range(random.randint(2, 6)):
        value = random.random() * 100
        table.add_row(
            f"{row}", f"{value:3.2f}", "[red]ERROR" if value < 50 else "[green]SUCCESS"
        )
    return table

def make_layout():
    global layout
    global layout_table

    layout = Layout(name="root")

    layout_table = Layout(name='table_layout',ratio=1)
    table_panel = Panel("Loading...",title='table_panel')
    layout_table.update(table_panel)

    layout_prompt = Layout(name='prompt_layout',ratio=1)

    layout['root'].split_column(
        layout_table,
        layout_prompt
    )
    return layout

if __name__ == "__main__":
    console = Console()
    console.print(make_layout())
    with Live(layout, refresh_per_second=2) as live:
        for _ in range(10):
            global layout_table
            table_panel = Panel(generate_table(),title='table_panel')
            layout_table.update(table_panel)
            time.sleep(1)