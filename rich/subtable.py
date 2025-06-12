from rich.console import Console
from rich.table import Table

table = Table(title="Nested", padding=(0, 0))
table.add_column("A")
table.add_column("B")

st = Table(
    padding=(0, 0),
    show_edge=False,
    show_lines=True,
)
st.add_column("C")
st.add_column("D")
for _ in range(3):
    st.add_row("test", "test2")

tt = Table()
tt.add_column("E")
tt.add_column("F")
for _ in range(3):
    tt.add_row("test", "test2")

table.add_row(st, tt)

console = Console()
console.print(table)