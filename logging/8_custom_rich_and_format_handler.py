import logging
from rich.logging import RichHandler
from rich.text import Text
import re

'''
ตัวอย่างใน script นี้คือการ custom richHandler ใหม่ เพราะโดย default มีการกำหนดสี logging โดยอัตโนมัติ
แล้วสีนั้นไม่ตอบโจยท์การแสดงผลให้ตามที่ผู้พัฒนาต้องการ นอกจากนั้น ตัว richHandler ยังมี default format ในส่วนของการแสดง
level , time และ path ซึ่งซ้ำซ้อนกับการตั้ง format โดยตัวผู้พัฒนาเอง เราจึงทำการปิดมันโดยจะเห็นได้จากส่วนนี้ 
CustomRichHandler(show_time=False,show_level=False,show_path=False,markup=True,rich_tracebacks=True)
เมื่อเราปิด default สีของ richHandler แล้ว ส่วนถัดมาเราจะทำการกำหนดสีลงไปด้วยตัวเองรวมถึงรูปแบบ format แสดง log
โดย CustomRichHandler ทำให้สีแสดงผลลง terminal ได้และสามารถสั่ง Log โดยใส่ markup ลง เช่น logger.info("[red]test[/red]") หรือเราจะใส่ สีลง format ก็กำหนด markup ลง class render_message ได้เลย

ส่วนถัดมาคือเมื่อเราจะเก็บ log ลง file เราไม่อยากให้ติด markup ลงไปด้วย เพราะเมื่อเรานำกลับมาดูจะได้ไม่ติด markup และนำไปประยุกต์ง่ายกว่า (แม้แต่เราจะใส่สีอีกทีตอนอ่านก็ทำได้ถ้าจะทำ)
จึงทำให้เราต้องสร้าง StripMarkupCustomFormatter class ขึ้นมา โดยมี strip_markup function ช่วยในการตัด markup ก่อนบันทึกลง file
'''

class CustomRichHandler(RichHandler):
    def render_message(self, record, message):
        # คุณสามารถปรับแต่งตรงนี้เพื่อเปลี่ยนรูปแบบข้อความ log
        custom_color_level_name = None
        if(record.levelname=='DEBUG'):
            custom_color_level_name = f"[green]{record.levelname}[/green]"
        elif(record.levelname=='INFO'):
            custom_color_level_name = f"[bold green]{record.levelname}[/bold green]"
        elif(record.levelname=='ERROR'):
            custom_color_level_name = f"[red]{record.levelname}[/red]"
        elif(record.levelname=='WARNING'):
            custom_color_level_name = f"[yellow]{record.levelname}[/yellow]"
        elif(record.levelname=='CRITICAL'):
            custom_color_level_name = f"[red]{record.levelname}[/red]"

        return Text.from_markup(message.replace(record.levelname,custom_color_level_name) if(record.levelname!=None) else message)


'''
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[CustomRichHandler(show_time=False)],
)
'''

logger = logging.getLogger("order_logger")
logger.setLevel(logging.INFO)

console_handler = CustomRichHandler(show_time=False,show_level=False,show_path=False,markup=True,rich_tracebacks=True)
formatter = logging.Formatter(
    fmt='[ %(levelname)s ] [bold green]%(asctime)s[/bold green] - %(filename)s:%(lineno)d - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)



file_handler = logging.FileHandler("log.txt")

class StripMarkupCustomFormatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None):
        super().__init__(fmt=self.strip_markup(fmt), datefmt=datefmt)

    def strip_markup(self,msg):
        return re.sub(r'\[/?\w+( [^\]]+)?\]', '', msg)

    def format(self, record):
        record.msg = self.strip_markup(record.getMessage())
        return super().format(record)

file_handler.setFormatter(StripMarkupCustomFormatter(fmt='[%(levelname)s] %(asctime)s - %(filename)s:%(lineno)d - %(message)s',datefmt='%Y-%m-%d %H:%M:%S'))
logger.addHandler(file_handler)

logger.debug("test debug")
logger.info("test info")
logger.warning("test warning")
logger.error("test error")
logger.critical("test critical")
