from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich import box
from rich.align import Align

# สร้าง Console object
console = Console()

# ข้อมูลที่จะแสดงในแต่ละคอลัมน์
data_col1 = ["Header 1","Row 1", "Row 2", "Row 3"]
data_col2 = ["Header 2","Value 1", "Value 2", "Value 3"]
data_col3 = ["Header 3","Info 1", "Info 2", "Info 3"]

# หัวข้อของแต่ละคอลัมน์
header_col1 = "Column 1"
header_col2 = "Column 2"
header_col3 = "Column 3"

# สร้าง Panel เพื่อห่อข้อมูลและหัวข้อของแต่ละคอลัมน์โดยไม่มีเส้นขอบ
panel_data_col1 = Panel("\n".join(data_col1), title='title panel1' , subtitle='subtitle panel1' ,box=box.SIMPLE_HEAD)
panel_data_col2 = Panel("\n".join(data_col2), title='title panel2' , subtitle='subtitle panel2' ,box=box.SIMPLE_HEAD)
panel_data_col3 = Panel("\n".join(data_col3), title='title panel3' , subtitle='subtitle panel3' ,box=box.SIMPLE_HEAD)

# สร้าง Columns object เพื่อจัดวางข้อมูลในหลาย ๆ คอลัมน์
columns = Columns([panel_data_col1, panel_data_col2, panel_data_col3])

# แสดงผล Columns ผ่าน Console
console.print(columns)

print('---')

panel_data_col1 = Panel(Align.center("\n".join(data_col1)), title='title panel1' , subtitle='subtitle panel1' ,box=box.ROUNDED)
panel_data_col2 = Panel("\n".join(data_col2), title='title panel2' , subtitle='subtitle panel2' ,box=box.ROUNDED)
panel_data_col3 = Panel("\n".join(data_col3), title='title panel3' , subtitle='subtitle panel3' ,box=box.ROUNDED)

# สร้าง Columns object เพื่อจัดวางข้อมูลในหลาย ๆ คอลัมน์
columns = Columns([panel_data_col1, panel_data_col2, panel_data_col3])

# แสดงผล Columns ผ่าน Console
console.print(Panel(columns,title='test panel'))

print('---')

# สร้าง Panel เพื่อห่อข้อมูลและหัวข้อของแต่ละคอลัมน์โดยไม่มีเส้นขอบ
panel_data_col1 = "\n".join(data_col1)
panel_data_col2 = "\n".join(data_col2)
panel_data_col3 = "\n".join(data_col3) # it's not affect

# สร้าง Columns object เพื่อจัดวางข้อมูลในหลาย ๆ คอลัมน์
columns = Columns([panel_data_col1, panel_data_col2, panel_data_col3])

# แสดงผล Columns ผ่าน Console
console.print(columns)