from io import StringIO
from rich.console import Console
from rich.panel import Panel
from rich import print
from rich.ansi import AnsiDecoder
import json

'''
หากเราใส่ข้อมูลจาก console ลงไป panel โดยตรงจะเกิดปัญหาการแสดงผลเพราะ
ข้อมูลจาก console เป็น ascii color ex.[31mredtest[0m แต่ panel รองรับ 
mark เท่านั้น ex. [red]redtest[/]
'''

#data = "[red]testred[/]"
data = json.dumps({'a':1,'b':2,'c':3},indent=4)
# สร้าง buffer สำหรับเก็บ output
def convert_ascii_console_to_mark_console(data):
    with StringIO() as buffer:
        # กำหนดให้ Console เขียน output ลงใน buffer แทน
        console = Console(file=buffer, force_terminal=True)
        decoder = AnsiDecoder()
        console.print(data)
        # ดึงข้อความที่อยู่ใน buffer ออกมา
        mark_data = []
        for i in decoder.decode(str(buffer.getvalue())):
            mark_data.append(i.markup)
        
        return "\n".join(mark_data)
    
panel = Panel(convert_ascii_console_to_mark_console(data), title="Rich Output", border_style="green")
print(panel)