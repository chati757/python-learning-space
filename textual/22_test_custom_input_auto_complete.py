from textual.app import App, ComposeResult ,on
from textual.content import Content
from textual.widgets import Input, Label 
from textual.widget import Widget
from textual.containers import Horizontal,Vertical
from textual_autocomplete import AutoComplete, DropdownItem
from textual.events import Key, Message
import asyncio
import time

class CustomInputAutoComplete(Widget):
    DEFAULT_CSS = """
    CustomInputAutoComplete{
        height:1;
        width:15;
    }
    AutoComplete {
        /* Customize the dropdown */
        & AutoCompleteList {
            max-height: 6;  /* The number of lines before scrollbars appear */
            color: $text-primary;  /* The color of the text */
            background: $primary-muted;  /* The background color of the dropdown */
            border-left: wide $success;  /* The color of the left border */
        }

        /* Customize the matching substring highlighting */
        & .autocomplete--highlight-match {
            color: $text-accent;
            text-style: bold;
        }

        /* Customize the text the cursor is over */
        & .option-list--option-highlighted {
            color: $text-success;
            background: $error 50%;  /* 50% opacity, blending into background */
            /*text-style: italic; */
        }
    }

    #InputAutoComplete {
        height:1;
        width:15;
        padding:0 0 0 1;
        border:none;
    }
    """

    def __init__(self,css_id:str=None,placeholder_input:str=''):
        super().__init__()
        self.id = css_id
        self._placeholder_input = placeholder_input
        self._input : Input | None = None
        self._auto_complete_area : AutoComplete | None = None
        self._last_candidate : str | None = None

    def compose(self):
        self._input = Input(id='InputAutoComplete',placeholder=self._placeholder_input)
        self._auto_complete_area = AutoComplete(target=self._input,candidates=self._get_filtered_candidates)
        
        yield self._input
        yield self._auto_complete_area

    def _get_filtered_candidates(self, current_input: str):
        """
        Callback function for AutoComplete to provide filtered candidates. (after _auto_complate_are created)
        """
        if not current_input:
            # ถ้าไม่มีข้อความใน Input, แสดงทั้งหมด (หรือตามที่คุณต้องการ)
            return self._all_candidates_data
        
        # กรอง candidates ตามข้อความปัจจุบันใน Input
        filtered = []
        for item in self._all_candidates_data:
            # ตรวจสอบว่าเป็น DropdownItem หรือ str
            candidate_text = item.value if isinstance(item, DropdownItem) else item
            if current_input.text.lower() in candidate_text.lower():
                filtered.append(item)
        
        return filtered

    def set_candidates_list(self, candidates_list: list = []):
        """
        Updates the internal list of all possible candidates.
        """
        self._all_candidates_data = candidates_list
        #set default selected
        self._input.value = str(self._all_candidates_data[0].prompt).split()[1]
        
    @on(Input.Submitted, "#InputAutoComplete")
    def input_submitted_event(self,event: Input.Submitted):
        if(self._last_candidate==None):
            self._last_candidate = str(self._all_candidates_data[0].prompt).split()[1]
        #print('on submit') 
        #print(event)
        #print(event.value)
        if(event.value not in [str(i.prompt).split()[1] for i in self._all_candidates_data]):
            #print('inif')
            self._input.value = self._last_candidate
        else:
            #print('inelse')
            #(success case) do something 
            self._last_candidate = self._input.value

    def on_key(self, event):
        if(event.key=='escape'):
            self._input.value = ''


class TestViweApp(App):
    CSS = """
    """

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Label('test1')
            yield CustomInputAutoComplete(css_id='testinput',placeholder_input='press ▼')
            yield Label('test2')

    async def on_mount(self) -> None:
        languages_with_rank = [
            (1, "BTC/USDT"),
            (2, "ETH/USDT"),
            (2, "LTC/USDT")
        ]

        # Create dropdown items with styled rank in prefix
        candidates_list = [
            DropdownItem(
                language,  # Main text to be completed
                prefix=Content.from_markup(
                    f"[$text-primary on $primary-muted] {rank:>2} "
                ),  # Prefix with styled rank
            )
            for rank, language in languages_with_rank
        ]

        testinput = self.query_one('#testinput')

        testinput.set_candidates_list(candidates_list=candidates_list)

       
if __name__ == "__main__":
    TestViweApp().run()