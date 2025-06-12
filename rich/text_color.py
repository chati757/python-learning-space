from rich import print
from rich.text import Text
from rich.console import Console
from rich.style import Style

# สร้าง Console object
console = Console()

# ความยาวของ Console
console_width = console.width

# สร้าง Text object สำหรับเส้นแบบ expanse
line = Text("─" * console_width,style=f"rgb(0,43,54)")

# แสดงผลผ่าน Console
console.print('test')
console.print(line)
console.print('test')

style = Style(color="red")
text = Text("Hello, world!",spans=[(0,4,style),(7,8,style)])

# แสดงผล Text object
print(text)

style2 = Style(color="grey0",bgcolor="yellow1")
text2 = Text("Hello, world!",style=style2)
print(text2)

print("[bold red on green blink]This text is impossible to read")

target = 'Hello'

test_txt_topic = "Hello\nWorld\nTest\n"
test_txt_content = '123\n25\ntest'

value_from_key = test_txt_content.split()[test_txt_topic.split().index(target)]
pos = test_txt_content.index(value_from_key)


console.print(Text(test_txt_content,spans=[(pos,pos+len(value_from_key),style)]))

'''
value_from_key = test_txt_content.split()[test_txt_topic.split().index(target)]
pos = test_txt_content.index(value_from_key)
[pos:pos+len(value_from_key)]
'''
