from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.widgets import Static,RichLog
from textual.message import Message
from textual import events
import logging


# 1. Event สำหรับส่งข้อความ log ไปที่ LogWidget
class LogEvent(Message):
    def __init__(self, log_message: str) -> None:
        super().__init__()
        self.log_message = log_message


# 2. LogWidget แสดงข้อความ log รวมทั้งหมด
class LogWidget(Widget):
    def __init__(self):
        super().__init__()
        self._rich_log : RichLog | None = None

    def compose(self) -> ComposeResult:
        self._rich_log = RichLog(id="_log",markup=True)
        self._rich_log.wrap = True
        yield self._rich_log
    
    def on_log_event(self, event: LogEvent) -> None:
        self._rich_log.write(event.log_message)


# 3. Handler ดัก log แล้วส่ง event ไป LogWidget
class AppLoggerHandler(logging.Handler):
    def __init__(self, log_view: LogWidget):
        super().__init__()
        self.log_view = log_view

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
            # แทนที่ levelname (เช่น INFO) ด้วย [bold green]INFO[/]
            # ต้องใช้ replace บนข้อความที่ได้จาก formatter
            message = message.replace(record.levelname, f"{tag}{record.levelname}[/]")
        return message  

    def emit(self, record: logging.LogRecord) -> None:
        msg = self.format(record)
        msg_with_markup = self.render_message_with_markup(record, msg)
        # ส่ง event ไปยัง LogWidget ผ่าน post_message
        self.log_view.post_message(LogEvent(msg_with_markup))


# 4. ตัวอย่าง widget A ใช้ logger
class WidgetA(Static):
    def on_mount(self) -> None:
        logger = logging.getLogger("WidgetA")
        logger.info("WidgetA started")

    def on_click(self, event: events.Click) -> None:
        logger = logging.getLogger("WidgetA")
        logger.info("WidgetA clicked")


# 5. ตัวอย่าง widget B ใช้ logger
class WidgetB(Static):
    def on_mount(self) -> None:
        logger = logging.getLogger("WidgetB")
        logger.info("WidgetB started")
        self.can_focus = True
        self.focus()

    def on_key(self, event: events.Key) -> None:
        logger = logging.getLogger("WidgetB")
        logger.info(f"WidgetB received key: {event.key}")


# 6. App หลัก
class MyApp(App):
    CSS = """
    LogWidget {
        height: 10;
        width:75;
        border: round yellow;
    }
    WidgetA {
        border: round green;
        height: 5;
    }
    WidgetB {
        border: round blue;
        height: 5;
    }
    """

    def compose(self) -> ComposeResult:
        self.log_widget = LogWidget()
        yield self.log_widget
        yield WidgetA()
        yield WidgetB()

    def on_mount(self) -> None:
        # สร้าง logger handler ที่ส่งข้อความไป log_widget
        handler = AppLoggerHandler(self.log_widget)
        handler.setFormatter(logging.Formatter("[ %(levelname)s ] %(asctime)s | %(name)s | %(message)s"))
        
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)
        root_logger.addHandler(handler)


if __name__ == "__main__":
    MyApp().run()
