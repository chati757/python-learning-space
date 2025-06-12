from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel

layout = Layout(name="root")
layout.split(
    Layout(name="header", size=3),
    Layout(name="main", ratio=1),
    Layout(name="save_stats_and_unsaved", size=4),
    Layout(name="errors", size=6),
)
layout["main"].split_row(
    Layout(name="left_side"),
    Layout(name="words_by_length", ratio=2, minimum_size=60),
    Layout(name="words_by_order"),
)

# (extraneous code not posted)
console = Console()
with console.screen() as screen:
    while True:
        layout["words_by_order"].update(Panel('a'))
        layout["save_stats_and_unsaved"].update(Panel('b'))
        layout["words_by_length"].update(Panel('c'))

        layout["root"].height = console.height - 4  # <-- restrict the height of the formatted output
        layout["root"].ratio = None
        console.clear()
        screen.update(layout)

        input_line = console.input("\nenter a word: ")
        # process the input, yadda yadda yadda