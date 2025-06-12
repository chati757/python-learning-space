import logging
import queue
from textual.app import App
from textual.widgets import RichLog
from textual.containers import Container
from rich.text import Text

# === Custom Handler ===
class BufferedTextualLogHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.queue = queue.Queue()
        self.log_widget = None

    def emit(self, record):
        msg = self.format(record)
        if not msg.endswith("\n"):
            msg += "\n"

        if self.log_widget:
            self.log_widget.write(Text.from_markup(msg))
        else:
            self.queue.put(msg)

    def bind(self, log_widget: RichLog):
        """Attach log widget + flush buffered logs."""
        self.log_widget = log_widget

        while not self.queue.empty():
            msg = self.queue.get()
            self.log_widget.write(Text.from_markup(msg))

# === Textual App ===
class LogApp(App):
    CSS_PATH = "app.tcss"  # Optional if using styles

    def compose(self):
        self.log_widget = RichLog()
        yield Container(self.log_widget)

    def on_mount(self):
        # Bind logger's handler to UI
        handler.bind(self.log_widget)

        # Emit some test logs
        logger.info("[green]App started[/green]")
        logger.warning("This is a warning")
        logger.error("Something went wrong.")


# === Setup logger globally ===
logger = logging.getLogger("textual_logger")
logger.setLevel(logging.DEBUG)
handler = BufferedTextualLogHandler()
handler.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))
logger.addHandler(handler)

# Even before app runs, this works!
logger.info("[blue]Logger started before app[/blue]")

if __name__ == "__main__":
    LogApp().run()
