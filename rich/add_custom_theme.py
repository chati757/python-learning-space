import re
from rich.console import Console
from rich.text import Text
from rich.theme import Theme
import builtins

# สร้าง Theme กำหนดสีของข้อความบางคำ

custom_theme_dict = {
    "ERROR": "bold red",
    "SUCCESS": "green",
    "INFO": "blue"
}
custom_theme = Theme(custom_theme_dict)
console = Console()

def custom_print(*args, **kwargs):
    text = " ".join(map(str, args))
    custom_color_key_list = list(custom_theme_dict.keys())

    for color_key in custom_color_key_list:
        if(color_key in text):
            text_buff = Text()
            regex_pattern = f"({'|'.join(map(re.escape, custom_color_key_list))})"
            split_text = re.split(regex_pattern, text)
            for i in [part for part in split_text if part]:
                if(i in custom_color_key_list):
                    text_buff.append(i,style=custom_theme_dict[i])
                else:
                    text_buff.append(i)
            
            console.print(text_buff)
            return

    console.print(text)

# แทนที่ print() ทั่วทั้งโปรแกรม
builtins.print = custom_print

# ทดสอบใช้งาน
print("ERROR: ABC ESUCCESS")   # สีแดงจาก Theme
print("SUCCESS: ดำเนินการเสร็จสิ้น")   # สีเขียวจาก Theme
print("INFO: ข้อมูลทั่วไป")   # สีน้ำเงินจาก Theme
print(f"ข้อความปกติ {True} {False}")   # ไม่มีสี