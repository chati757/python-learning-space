from textual.app import App, ComposeResult
from textual.containers import Center, VerticalScroll, Horizontal
from textual.widgets import Button, Header, Input, Label, ProgressBar

class FundingProgressApp(App[None]):

    CSS = """
    Bar {
        width:10;
    }
    Bar > .bar--bar {
        color: #EEE8D5;
        background: $primary 30%;
    }

    Bar > .bar--indeterminate {
        color: $accent;
        background: $accent;
    }
   
    Bar > .bar--complete {
        color: #EEE8D5;
    }

    PercentageStatus {
        text-style: reverse;
        color: yellow;
    }

    ETAStatus {
        text-style: underline;
    }

    #count_label{
        padding-left:1;
    }
    """

    TITLE = "Funding tracking"

    countdown_total = 15   # ⬅ กำหนดเวลานับถอยหลัง (15 วินาที)
    countdown_value = countdown_total

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Funding: ")
        with Horizontal():
            yield ProgressBar(total=100, show_eta=False,show_percentage=False,id="timer_bar")  
            yield Label("interval : ", id="count_label")
        with Center():
            yield Input(id='InputTest', placeholder="$$$")
            yield Button("Donate")
        yield VerticalScroll(id="history")

    def on_mount(self) -> None:
        """ เริ่ม interval timer สำหรับ countdown """
        self.set_interval(1.0, self.update_countdown)  # ทุก 1 วินาที

    def update_countdown(self) -> None:
        """ ลดค่า countdown และอัปเดต progress bar """
        bar = self.query_one("#timer_bar", ProgressBar)
        label = self.query_one("#count_label", Label)

        self.countdown_value -= 1
        percent = int((self.countdown_value / self.countdown_total) * 100)
        bar.progress = percent
        label.update(f"interval : {self.countdown_value}")

        if self.countdown_value <= 0:
            self.trigger_event()
            self.countdown_value = self.countdown_total
            bar.progress = 100

    def trigger_event(self) -> None:
        """ ฟังก์ชันที่จะถูกเรียกเมื่อ countdown ถึง 0 """
        self.query_one("#history", VerticalScroll).mount(Label("⏰ Countdown reached zero!"))

    def on_button_pressed(self) -> None:
        self.add_donation()

    def on_input_submitted(self) -> None:
        self.add_donation()

    def add_donation(self) -> None:
        text_value = self.query_one(Input).value
        try:
            value = int(text_value)
        except ValueError:
            return
        self.query_one(ProgressBar).advance(value)
        self.query_one(VerticalScroll).mount(Label(f"Donation for ${value} received!"))
        self.query_one(Input).value = ""


if __name__ == "__main__":
    FundingProgressApp().run()
