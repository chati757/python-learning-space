import logging
from logging.handlers import RotatingFileHandler


logger = logging.getLogger("order_logger")
logger.setLevel(logging.INFO)

# 🔹 Formatter format
formatter = logging.Formatter(
    "[%(asctime)s] %(levelname)s | STATE=%(state)s | ORDER_ID=%(order_id)s | RETRY=%(retry_count)s | MSG=%(message)s"
)

# 🔹 Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

'''
#กรณีอยากใช้ rich แทนการแสดงผลของ log บน terminal
from rich.logging import RichHandler
console_handler = RichHandler(rich_tracebacks=True, markup=True)
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
'''

logger.addHandler(console_handler)

# 🔹 File handler with rotation
file_handler = RotatingFileHandler(
    "order_flow.log",           # ไฟล์ log
    maxBytes=1_000_000,         # ขนาดสูงสุด 1 MB ต่อไฟล์
    backupCount=3               # เก็บไฟล์เก่าไว้ 3 ก้อน เช่น .1, .2, .3
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
