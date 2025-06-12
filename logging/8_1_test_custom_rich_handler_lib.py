import logging
from logging.handlers import RotatingFileHandler
from rich.logging import RichHandler
from rich.text import Text
import re

'''
script นี้คือการ custom richHandler ใหม่ เพราะโดย default มีการกำหนดสี logging โดยอัตโนมัติ
แล้วสีนั้นไม่ตอบโจยท์การแสดงผลให้ตามที่ผู้พัฒนาต้องการ นอกจากนั้น ตัว richHandler ยังมี default format ในส่วนของการแสดง
level , time และ path ของตัวมันเองซึ่งซ้ำซ้อนกับการตั้ง format โดยตัวผู้พัฒนาเอง เราจึงทำการปิดมันโดยจะเห็นได้จากส่วนนี้ 
CustomRichHandler(show_time=False,show_level=False,show_path=False,markup=True,rich_tracebacks=True)
เมื่อเราปิด default สีของ richHandler แล้ว ส่วนถัดมาเราจะสามารถทำการกำหนดสีลงไปด้วยตัวเองรวมถึงรูปแบบ format แสดง log
โดย CustomRichHandler ทำให้สีแสดงผลลง terminal ได้และสามารถสั่ง Log โดยใส่ markup ลง เช่น logger.info("[red]test[/red]") ได้โดยการแสดงสีทำได้ปกติ
หรือเราจะใส่ สีลง format ของ CustomRichHandler เลยก็ได้โดยกำหนด markup ลง render_message method ได้เลย

ส่วนถัดมาคือเมื่อเราจะเก็บ log ลง file เราไม่อยากให้ติด markup ลงไปด้วย เพราะเมื่อเรานำกลับมาดูจะได้ไม่ติด markup และนำไปประยุกต์ง่ายกว่า (แม้แต่เราจะใส่สีอีกทีตอนอ่านก็ทำได้ถ้าจะทำ)
จึงทำให้เราต้องสร้าง StripMarkupCustomFormatter class ขึ้นมา โดยมี strip_markup function ช่วยในการตัด markup ก่อนบันทึกลง file

ส่วนเพิ่มเติม lib อีกส่วนคือออกมามาให้สามารถเขียน file และ rotate ตามขนาด file ได้เหมือน logger

future : ในอนาคต lib นี้อาจทำงานเริ่มกับ log ของ textual
'''

class CustomConsoleRichHandler(RichHandler):
    def __init__(
            self,
            fmt:logging.Formatter=None,
            markup:bool=False,
            show_time:bool=False,
            show_path:bool=False,
            show_level:bool=False,
            *args, 
            **kwargs
        ):
        super().__init__(markup=markup,show_time=show_time,show_path=show_path,show_level=show_level, *args, **kwargs)
        if(not isinstance(fmt,logging.Formatter)):
            raise ValueError('fmt parameter is empty')
        self.setFormatter(fmt=fmt)

    def render_message(self, record, message):
        # คุณสามารถปรับแต่งตรงนี้เพื่อเปลี่ยนรูปแบบข้อความ log
        color_map = {
            'DEBUG': "[green]",
            'INFO': "[bold green]",
            'WARNING': "[yellow]",
            'ERROR': "[red]",
            'CRITICAL': "[red]"
        }
        level = record.levelname
        tag = color_map.get(level, "")
        if tag:
            message = message.replace(level, f"{tag}{level}[/]")
        return Text.from_markup(message)

class StripMarkupCustomFormatter(logging.Formatter):
    def __init__(self,*args,**kwargs):
        #stripMarkup in format
        kwargs['fmt'] = self.strip_markup(kwargs['fmt'])
        super().__init__(*args,**kwargs)

    def strip_markup(self,msg):
        return re.sub(r'\[/?\w+( [^\]]+)?\]', '', msg)

    def format(self, record):
        #stripMarkup in record.message
        clean_message = self.strip_markup(record.getMessage())
        record_copy = logging.LogRecord(
            record.name, record.levelno, record.pathname, record.lineno,
            clean_message, record.args, record.exc_info
        )
        return super().format(record_copy)
    
class CustomFileHandler(RotatingFileHandler):
    def __init__(self,fmt:logging.Formatter=None,log_file_path:str="",*args,**kwargs):
        if(log_file_path==""):
            raise ValueError('log_file_path is empty')
        
        if(fmt==None):
            raise ValueError('fmt==None or date_fmt==None')
        
        super().__init__(filename=log_file_path,*args,**kwargs)
        self.setFormatter(StripMarkupCustomFormatter(fmt=fmt._fmt,datefmt=fmt.datefmt))
    

logger = logging.getLogger("some_logger")
logger.setLevel(logging.INFO)
logger.propagate = False #ไม่ต้องส่งไปพิมพ์ที่ root logger อีกรอบ (แม้ตอนนี้ยังไม่มี root logger ก็ตาม)

formatter = logging.Formatter(
                fmt='[ %(levelname)s ] [bold green]%(asctime)s[/bold green] - %(filename)s:%(lineno)d - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )

#import pdb;pdb.set_trace()

console_handler = CustomConsoleRichHandler(fmt=formatter)
logger.addHandler(console_handler)

file_handler = CustomFileHandler(
    fmt=formatter,
    log_file_path='testlog.txt',
    maxBytes=1_000_000,
    backupCount=2
)
logger.addHandler(file_handler)

logger.info('test rich 3')
