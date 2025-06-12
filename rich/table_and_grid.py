from rich.console import Console
from rich.table import Table, Column
from rich.panel import Panel
from rich import box

console = Console()

# สร้างตารางภายในที่ไม่มีกรอบและไม่มีเส้นขั้น
inner_table = Table(box=None, show_header=False)

# เพิ่มคอลัมน์โดยใช้ Column
inner_table.add_column(style="red", justify="left")
inner_table.add_column(justify="right")

# เพิ่มแถวในตารางภายใน
inner_table.add_row("alex", "developer")
inner_table.add_row("ben", "designer")
inner_table.add_row("cat", "manager")

# สร้างตารางภายนอกที่มีกรอบ ROUNDED
outer_table = Table(box=box.ROUNDED, show_header=False)

# เพิ่มคอลัมน์ในตารางภายนอกเพื่อใส่ตารางภายใน
outer_table.add_column()

# เพิ่มตารางภายในเป็นแถวในตารางภายนอก
outer_table.add_row(inner_table)

# แสดงตารางภายนอกภายใน Panel
console.print(Panel(outer_table, title='test header'))