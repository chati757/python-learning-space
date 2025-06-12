from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.text import Text

# สร้าง Console object
console = Console()

# ข้อมูลที่จะแสดงในแต่ละคอลัมน์
data_col1 = ["Row 100", "Row 2000", "Row 30000"]
data_col2 = ["Value 1", "Value 2", "Value 3"]
data_col3 = ["Info 1", "Info 2", "Info 3"]

# ห่อข้อมูลแต่ละคอลัมน์ด้วย Panel
panel_data_col1 = Text("\n".join(data_col1),justify='right')
panel_data_col2 = ("\n".join(data_col2))
panel_data_col3 = ("\n".join(data_col3))

# สร้าง Columns object เพื่อจัดวางข้อมูลในหลาย ๆ คอลัมน์
columns = Columns([panel_data_col1, panel_data_col2, panel_data_col3])

# แสดงผล Columns ผ่าน Console
console.print(columns)

console.print('----')

#columns of columns
console.print(Columns([columns],align='right'))