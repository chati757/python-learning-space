from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets import Button, Header, Input, Label, ProgressBar
from textual.widget import Widget

class ProgressCountDownTimeInterval(Widget):
    DEFAULT_CSS = """
    #Bar > Bar {
        width:10;
    }

    #Bar > Bar > .bar--bar {
        color: #EEE8D5;
        background: $primary 30%;
    }

    #Bar > Bar > .bar--indeterminate {
        color: $accent;
        background: $accent;
    }
   
    #Bar > Bar > .bar--complete {
        color: #EEE8D5;
    }

    ETAStatus {
        text-style: underline;
    }

    #CountLabel{
        padding-left:1;
    }
    """
    
    def __init__(self,css_id:str=None,countdown_total:int=None,prefix_count_label:str=''):
        super().__init__()
        self._ProgressBar : ProgressBar | None = None
        self._CountLabel : Label | None = None
        self._countdown_total : int | None = countdown_total
        self._prefix_count_label = prefix_count_label
        self.id = css_id

    def compose(self) -> ComposeResult:
        self._ProgressBar = ProgressBar(total=100, show_eta=False,show_percentage=False,id='Bar')
        self._CountLabel = Label(self._prefix_count_label,id='CountLabel')

        with Horizontal():
            yield self._ProgressBar
            yield self._CountLabel

    def set_current_ProgressBar_and_CountLabel(self,percent:int,count_str:str):
        self._ProgressBar.progress = percent
        self._CountLabel.update(f'{self._prefix_count_label}{count_str}')
    
    '''
    #example usage in on_mount app
    countdown_total = 15   # ⬅ กำหนดเวลานับถอยหลัง (15 วินาที)
    countdown_value = countdown_total
    self.set_interval(1.0,update_custom_procress_countdown)

    def update_custom_procress_countdown() -> None:
        countdown_value -= 1
        percent = int((countdown_value / countdown_total) * 100)
        <ProgressCountDownTimeInterval>.set_current_ProgressBar_and_CountLabel(self,percent=percent,count_str=str(countdown_value))

        if countdown_value <= 0:
            """
            #trigger_zone (controller do something)
            """
            countdown_value = countdown_total
            <ProgressCountDownTimeInterval>.set_current_ProgressBar_and_CountLabel(self,percent=100,count_str=str(countdown_value))
    '''
class TestViewApp(App):
    CSS = """

    """

    def compose(self) -> ComposeResult:
        with Vertical():
            yield ProgressCountDownTimeInterval(css_id='testprogressinterval',prefix_count_label='interval : ')

    def on_mount(self) -> None:
        testprogressinterval = self.query_one("#testprogressinterval")
        countdown_total = 15   # ⬅ กำหนดเวลานับถอยหลัง (15 วินาที)
        countdown_value = countdown_total
        def update_custom_procress_countdown() -> None:
            nonlocal countdown_value
            countdown_value -= 1
            percent = int((countdown_value / countdown_total) * 100)
            testprogressinterval.set_current_ProgressBar_and_CountLabel(percent=percent,count_str=str(countdown_value))

            if countdown_value <= 0:
                """
                #trigger_zone (controller do something)
                """
                countdown_value = countdown_total
                testprogressinterval.set_current_ProgressBar_and_CountLabel(percent=100,count_str=str(countdown_value))

        self.set_interval(1.0,update_custom_procress_countdown)

if __name__=='__main__':
    TestViewApp().run()