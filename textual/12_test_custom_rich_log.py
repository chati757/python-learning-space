from textual import events
from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.widgets import RichLog

class CustomRichLog(Widget):
    DEFAULT_CSS = """
    #MainRichLog {
        background:#002B36;

        border:round #B1C2C2;
        border-title-style: bold;
        border-title-align: right;

        padding: 0 0 0 1;

        overflow: auto;

        scrollbar-color: #EEE8D5;
        scrollbar-background: #002B36;
        
        scrollbar-color-hover:  #EEE8D5;
        scrollbar-background-hover: #002B36;

        scrollbar-color-active: #EEE8D5;
        scrollbar-background-active: #002B36;
    }
    """
    def __init__(self,css_id:str=None,border_title:str=None):
        super().__init__()
        self.id = css_id
        self._border_title = border_title
        self._MainRichLog : RichLog | None = None

    def compose(self) -> ComposeResult:
        self._MainRichLog = RichLog(id='MainRichLog',highlight=True, markup=True)
        self._MainRichLog.max_lines = 300
        self._MainRichLog.border_title = self._border_title
        yield self._MainRichLog

    def on_mount(self) -> None:
        """Called  when the DOM is ready."""
        self._MainRichLog.write("[bold magenta]Write text or any Rich renderable!")

    def add_log(self,text:str=None):
        self._MainRichLog.write(text)

    def clear_log(self):
        self._MainRichLog.clear()

    '''
    def on_key(self, event: events.Key) -> None:
        """Write Key events to log."""
        self._MainRichLog.write(event.key)
    '''

class TestViweApp(App):
    CSS = """
    #CustomRichLog {
    }
    """

    def compose(self) -> ComposeResult:
        yield CustomRichLog(css_id="CustomRichLog",border_title='test')

    def on_mount(self) -> None:
        custom_rich_log = self.query_one("CustomRichLog")
        custom_rich_log.add_log('test')
        custom_rich_log.add_log('test')
        custom_rich_log.clear_log()

if __name__ == "__main__":
    TestViweApp().run()