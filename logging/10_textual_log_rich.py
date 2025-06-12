import logging
from textual.widgets import Log
from textual.app import App
from textual.widgets import RichLog
from textual.containers import Container
from rich.text import Text

# Custom Handler
class TextualLogHandler(logging.Handler):
    def __init__(self, log_widget: Log):
        super().__init__()
        self.log_widget = log_widget

    def emit(self, record):
        msg = self.format(record)
        if not msg.endswith("\n"):
            msg += "\n"
        self.log_widget.write(Text.from_markup(msg))  # ส่งข้อความเข้า Log widget

# Textual App
class LogApp(App):
    def compose(self):
        self.log_widget = RichLog()
        yield Container(self.log_widget)

    def on_mount(self):
        # กำหนด logger
        logger = logging.getLogger("textual_logger")
        logger.setLevel(logging.INFO)

        handler = TextualLogHandler(self.log_widget)
        handler.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))
        logger.addHandler(handler)

        # ใช้งาน logger ตามปกติ
        logger.info("[red]Hello from logger![/red]")
        logger.warning("This is a warning.")
        logger.error("Something went wrong.")

if __name__ == "__main__":
    LogApp().run()
