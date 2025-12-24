import logging
from logging.handlers import RotatingFileHandler
from rich.logging import RichHandler
from rich.text import Text
import re

# ---- Custom Handler สำหรับแสดงผลใน Rich Console ----
class CustomConsoleRichHandler(RichHandler):
    def __init__(
            self,
            fmt: logging.Formatter = None,
            markup: bool = False,
            show_time: bool = False,
            show_path: bool = False,
            show_level: bool = False,
            *args,
            **kwargs
        ):
        super().__init__(markup=markup, show_time=show_time, show_path=show_path, show_level=show_level, *args, **kwargs)
        if not isinstance(fmt, logging.Formatter):
            raise ValueError('fmt parameter is empty')
        self.setFormatter(fmt=fmt)

    def render_message(self, record, message):
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

# ---- Formatter ที่ลบ markup (ไว้ใช้กับ file หรือ capture) ----
class StripMarkupCustomFormatter(logging.Formatter):
    def __init__(self, *args, **kwargs):
        kwargs['fmt'] = self.strip_markup(kwargs['fmt'])
        super().__init__(*args, **kwargs)

    def strip_markup(self, msg):
        return re.sub(r'\[/?\w+( [^\]]+)?\]', '', msg)

    def format(self, record):
        clean_message = self.strip_markup(record.getMessage())
        record_copy = logging.LogRecord(
            record.name, record.levelno, record.pathname, record.lineno,
            clean_message, record.args, record.exc_info
        )
        return super().format(record_copy)

# ---- FileHandler ที่ใช้ StripMarkupCustomFormatter ----
class CustomFileHandler(RotatingFileHandler):
    def __init__(self, fmt: logging.Formatter = None, log_file_path: str = "", *args, **kwargs):
        if log_file_path == "":
            raise ValueError('log_file_path is empty')
        if fmt is None:
            raise ValueError('fmt==None or date_fmt==None')
        super().__init__(filename=log_file_path, *args, **kwargs)
        self.setFormatter(StripMarkupCustomFormatter(fmt=fmt._fmt, datefmt=fmt.datefmt))

# ---- Custom Handler สำหรับเก็บ log message เป็น string ----
class CaptureLogHandler(logging.Handler):
    def __init__(self, fmt: logging.Formatter):
        super().__init__()
        self.setFormatter(fmt)
        self.logs = []

    def render_message_with_markup(self, record, message):
        color_map = {
            'DEBUG': "[green]",
            'INFO': "[bold green]",
            'WARNING': "[yellow]",
            'ERROR': "[red]",
            'CRITICAL': "[red]"
        }
        tag = color_map.get(record.levelname, "")
        if tag:
            record.levelname = f"{tag}{record.levelname}[/]"
        return message  # ไม่แตะ message เลยก็ได้

    def emit(self, record):
        record.msg = self.render_message_with_markup(record, record.getMessage())
        msg = self.format(record)
        self.logs.append(msg)
# ----------------------------
# ✅ Example
# ----------------------------

logger = logging.getLogger("some_logger")
logger.setLevel(logging.INFO)
logger.propagate = False

# 🔧 ล้าง handler เดิม (กันพลาดหากรันซ้ำใน Interactive)
#logger.handlers.clear()

# ✅ ใช้ formatter เดิม (ยังมี markup อยู่)
formatter = logging.Formatter(
    fmt='[ %(levelname)s ] [bold green]%(asctime)s[/bold green] - %(filename)s:%(lineno)d - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# ✅ เพิ่มเฉพาะ handler ที่ใช้เก็บข้อความ (ไม่แสดงผลหน้าจอ)
capture_handler = CaptureLogHandler(fmt=formatter)
logger.addHandler(capture_handler)

# 🔍 Logging ตัวอย่าง
logger.error("test rich 3\n---\nsome_content\n---")

# 📦 ดึงข้อความที่เก็บไว้
from rich import print

if capture_handler.logs:
    captured_message = capture_handler.logs[0]
    print("Captured Log:", captured_message)
else:
    print("No log captured.")
