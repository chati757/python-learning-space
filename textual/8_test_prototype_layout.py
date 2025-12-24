from textual.app import App, ComposeResult , on
from textual.widgets import TabbedContent, TabPane, Input, Label , ProgressBar
from textual.containers import Vertical, Horizontal
from textual.widgets import Log
from textual.widgets import ContentSwitcher
from textual.widgets import RichLog
from textual.widgets import Tree
from textual.widgets import DataTable
from textual.widgets import OptionList
from textual.widgets import Static
from textual.widgets.option_list import Option
from textual.events import Key
from textual.widget import Widget
from textual.content import Content
from textual_autocomplete import AutoComplete, DropdownItem
from textual.coordinate import Coordinate
from rich.text import Text
from rich.table import Table

import asyncio

class CellDoesNotExist(Exception):
    """The cell key/index was invalid.

    Raised when the coordinates or cell key provided does not exist
    in the DataTable (e.g. out of bounds index, invalid key)"""

class ProgressCountDownTimeInterval(Widget):
    DEFAULT_CSS = """
    #Bar > Bar {
        width:7;
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

class CustomInputAutoComplete(Widget):
    DEFAULT_CSS = """
    CustomInputAutoComplete {
        height: 1;
        width: 10;
        & Input {
            color: #002B36;
        }
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
        width:13;
        padding:0 0 0 1;
        border:none;
        background:#B1C2C2;
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
        if(event.key=='escape' and self._search_input.has_focus):
            self._input.value = ''

class CustomTabContentLogTable(Widget):
    DEFAULT_CSS = """
    Container{
        background:#002B36;
    }

    Tab {
        color:#B1C2C2;
    }

    Tabs {
        height: 2;
        .-active {
            color: #002B36;
            background: #B1C2C2;
        }
        .underline--bar {
            background: $foreground 30%;
        }
        & Underline {
            height: 1;
            & > .underline--bar {
                color: #B1C2C2;
                background: $foreground 10%;
            }
        }
        &:focus {
            .underline--bar {
                background: $foreground 30%;
            }
            .-active {
                color:#002B36;
                background: #B1C2C2;
                text-style: $block-cursor-text-style;
            }
        }
    }

    #vertical_tabbed_content{
        border:round #B1C2C2;
        border-title-color: #EEE8D5;
        border-title-style: bold;
        border-title-align: right;
        padding:0 0 0 0;
    }
    #horizontal_header{
        height:1;
        padding:0 0 0 0;
    }
    .label_header_content{
        background:#002B36;
        padding:0 0 0 0;
        text_align:right;
    }
    .label_header_space{
        background:#002B36;
    }

    #MainLog1_BuyLow {
        /*scrollbar */
        overflow: auto;
        background: #002B36;

        & #MainTable1_BuyLow {
            color:#B1C2C2;
            background: #002B36;
            text-style: bold;

            background: #002B36;
            scrollbar-color: #EEE8D5;
            scrollbar-background: #002B36;
            
            scrollbar-color-hover:  #EEE8D5;
            scrollbar-background-hover: #002B36;

            scrollbar-color-active: #EEE8D5;
            scrollbar-background-active: #002B36;
        }
    }
    """

    def __init__(self,css_id:str=None,border_title:str=None,cursor_type:bool=False):
        super().__init__()
        self.id = css_id
        self.border_title = border_title
        self.cursor_type = cursor_type
        self._MainTabbedContent : TabbedContent | None = None
        self._MainTabPane1_BuyLow : TabPane | None = None
        self._MainHorzontal1_BuyLow : Horizontal | None = None
        self._MainLog1_BuyLow : Log | None = None
        self._buff_filter_max_width_columns : list | None = None
        self._MainTable1_BuyLow : DataTable | None = None
        self._MainTable1_columns : list | None = None

        self._MainTabPane2_SellHigh : TabPane | None = None
        self._MainLog2_SellHigh : Log | None = None
        self._MainTable2_SellHigh : DataTable | None = None

    def compose(self):
        self._MainTabbedContent = TabbedContent(id='MainTabbedContent')
        self._MainTabPane1_BuyLow = TabPane(title='BUY_LOW',id='MainTabPane1_BuyLow')
        self._MainHorzontal1_BuyLow = Horizontal(id='horizontal_header')
        self._MainLog1_BuyLow = Log(id='MainLog1_BuyLow')
        self._MainTable1_BuyLow = DataTable(id='MainTable1_BuyLow',cursor_type=self.cursor_type)

        self._MainTabPane2_SellHigh = TabPane(title='SELL_HIGH',id='MainTabPane1_SellHigh')

        with self._MainTabbedContent:
            with self._MainTabPane1_BuyLow:
                with Vertical(id='vertical_tabbed_content'):
                    yield self._MainHorzontal1_BuyLow
                    with self._MainLog1_BuyLow:
                        yield self._MainTable1_BuyLow
            with self._MainTabPane2_SellHigh:
                pass

    def insert_header_columns_maintable1(self,col_list:list=[]):
        self._MainHorzontal1_BuyLow.remove_children()
        for col in col_list:
            self._MainHorzontal1_BuyLow.mount(Label(Text.from_markup(col,justify='right'),classes='label_header_content'))
            self._MainTable1_BuyLow.add_column(Text.from_markup(col,justify='right'),key=col)

        self._MainHorzontal1_BuyLow.mount(Label(Text.from_markup(' ',justify='right'),classes='label_header_space'))
        #await asyncio.sleep(0)
        #self._MainHorzontal1_BuyLow.children[0].styles.width = 30
        #log.append(self._MainHorzontal1_BuyLow.children[0].render())

    def update_by_rows_maintable1(self,rows_list):
        self._MainTable1_columns = rows_list
        if(self._buff_filter_max_width_columns==None):
            self._buff_filter_max_width_columns = [[i[1].width+1] if(c==0) else [i[1].width+2] for c,i in enumerate(self._MainTable1_BuyLow.columns.items())]
            #log.append(self._buff_filter_max_width_columns)
        #col_item : [[row1,row2,..],[header_label1_of_horizontal1,..]]

        styled_row = [Text.from_markup(str(i),justify='right') for i in rows_list]
        self._MainTable1_BuyLow.add_row(*styled_row)
        self._MainHorzontal1_BuyLow.refresh()
        
        for c,rows_and_header_label_col_item in enumerate(zip(rows_list,self._MainHorzontal1_BuyLow.children[:-1])):
            row = rows_and_header_label_col_item[0]
            row_length = len(str(row))+1 if c==0 else len(str(row))+2
            if(row_length > max(self._buff_filter_max_width_columns[c])):
                rows_and_header_label_col_item[1].styles.width = row_length
                self._buff_filter_max_width_columns[c].append(row_length)
            else:
                rows_and_header_label_col_item[1].styles.width = max(self._buff_filter_max_width_columns[c])
            
    def update_cell_at_maintable1(self,row,col,value,update_width=True):
        buff_coord = Coordinate(row=row,column=col)
        if not self._MainTable1_BuyLow.is_valid_coordinate(buff_coord) or self._MainTable1_columns==None:
            raise CellDoesNotExist(f"Coordinate {buff_coord!r} is invalid.")

        row_key, column_key = self._MainTable1_BuyLow.coordinate_to_cell_key(buff_coord)
        self._MainTable1_BuyLow.update_cell(row_key, column_key, value, update_width=update_width)
        self._MainHorzontal1_BuyLow.refresh()

        #update header width
        del self._buff_filter_max_width_columns[:]
        self._buff_filter_max_width_columns.append(len(str(self._MainTable1_columns[col])))
        self._buff_filter_max_width_columns += [len(str(col)) for col in self._MainTable1_BuyLow.get_column_at(col)]

        if(col==0):
            self._buff_filter_max_width_columns = [i+1 for i in self._buff_filter_max_width_columns]
        else:
            self._buff_filter_max_width_columns = [i+2 for i in self._buff_filter_max_width_columns]

        self._MainHorzontal1_BuyLow.children[col].styles.width = max(self._buff_filter_max_width_columns)

    def on_mount(self) -> None:
        self.query_one("#vertical_tabbed_content",Vertical).border_title = self.border_title
        self.query_one("#MainTable1_BuyLow",DataTable).cursor_type = self.cursor_type
        self.query_one("#MainTable1_BuyLow",DataTable).show_header = False

class CustomOptionListAndInputSearch(Widget):
    """
    Textual App ที่แสดง OptionList ที่สามารถค้นหาและเรียงลำดับได้.
    """

    # CSS สำหรับจัดวางองค์ประกอบและสไตล์
    DEFAULT_CSS = """
    #_search_input {
        background:#044859;
        width: 99%; /* Input field ให้เต็มความกว้างของคอนเทนเนอร์ */
        height: 1;
        margin-left: 1;
        margin-bottom: 0; /* ระยะห่างด้านล่างของ Input */
        border: none;  /*เพิ่มกรอบโค้งมนให้กับ Input */
        padding: 0 1; /* Padding ภายใน Input */

        &:focus {
            border: none;            
            background-tint: $foreground 5%;
            
        }
    }

    #_option_list {
        width: 100%; /* OptionList ให้เต็มความกว้างของคอนเทนเนอร์ */
        height: 90%; /* ใช้พื้นที่ที่เหลือทั้งหมดใน Vertical container */
        border: round #B1C2C2; /* เพิ่มกรอบโค้งมนให้กับ OptionList */
        background: #002B36;
        scrollbar-color: #EEE8D5;
        scrollbar-background: #002B36;
        scrollbar-color-hover:  #EEE8D5;
        scrollbar-background-hover: #002B36;
        scrollbar-color-active: #EEE8D5;
        scrollbar-background-active: #002B36;
    }
    """

    def __init__(self,css_id:str=None):
        super().__init__()
        self.id = css_id
        self._search_input : Input | None = None
        self._options_list_items = []
        self._options_list : OptionList | None = None

    def update_options_list(self,new_options_list:list=[]):
        '''
        #example
        self._options_list_items = [
            Option("Aerilon", id="aer"),
            Option("Aquaria", id="aqu"),
            None, # ตัวคั่น (separator)
        ]
        '''
        # กำหนด options หลัง compose แล้ว
        # อัปเดตรายการใน OptionList
        self._options_list.clear_options()
        self._options_list.add_options(new_options_list)

        # เก็บค่าใหม่ไว้ใน _options_list_items เพื่อใช้ใน on_input_changed
        self._options_list_items = new_options_list

    def compose(self) -> ComposeResult:
        # สร้าง Input widget สำหรับการค้นหา
        self._search_input = Input(placeholder="search command list , [esc] for clear", id="_search_input")
        self._options_list = OptionList(id='_option_list')
        with Vertical(): # ใช้ Vertical container เพื่อจัดเรียง Input และ OptionList ในแนวตั้ง
            yield self._search_input
            yield self._options_list

    def on_mount(self) -> None:
        """
        เรียกเมื่อ Widgets ถูก mount เข้ากับ DOM.
        """
        # ตั้งค่าโฟกัสไปที่ Input field เมื่อ App เริ่มต้น
        #self._search_input.focus()
        pass

    def on_input_changed(self, event: Input.Changed) -> None:
        """
        เรียกเมื่อค่าใน Input field (_search_input) มีการเปลี่ยนแปลง.
        จะทำการกรองและเรียงลำดับรายการ OptionList.
        """
        # รับข้อความค้นหา, ลบช่องว่างหัวท้าย, และแปลงเป็นตัวพิมพ์เล็ก
        search_term = event.value.strip().lower()

        if not search_term:
            # ถ้าข้อความค้นหาว่างเปล่า, ให้แสดงรายการ Option ดั้งเดิมทั้งหมด
            self._options_list.clear_options()
            self._options_list.add_options(self._options_list_items)
            return

        # กรองเฉพาะ Option ที่มีข้อความค้นหาอยู่ใน prompt (ไม่รวม None)
        # แก้ไข: ใช้ str(option.prompt).lower() เพื่อให้แน่ใจว่าเป็น string ก่อนแปลงเป็นตัวพิมพ์เล็ก
        matching_options = [
            option for option in self._options_list_items
            if option is not None and search_term in str(option.prompt).lower()
        ]

        # เรียงลำดับ Option ที่ตรงกันตามตัวอักษร (prompt text)
        # แก้ไข: ใช้ str(option.prompt).lower() ใน key สำหรับการเรียงลำดับ
        sorted_matching_options = sorted(
            matching_options,
            key=lambda option: str(option.prompt).lower()
        )

        # ล้าง OptionList ปัจจุบันและเพิ่ม Option ที่ถูกกรองและเรียงลำดับแล้ว
        self._options_list.clear_options()
        self._options_list.add_options(sorted_matching_options)

    def on_key(self, event: Key) -> None:
        """
        จัดการการกดปุ่ม, โดยเฉพาะปุ่ม Escape เพื่อรีเซ็ตการค้นหา.
        """
        # ตรวจสอบว่าปุ่มที่กดคือ Escape และโฟกัสอยู่ที่ _search_input
        if event.key == "escape" and (self._search_input.has_focus or self._options_list.has_focus):
            # ล้างค่าใน Input field
            self._search_input.value = ""
            # ล้าง OptionList และเพิ่มรายการ Option ดั้งเดิมกลับเข้าไป
            self._options_list.clear_options()
            self._options_list.add_options(self._options_list_items)
            # ตั้งค่าโฟกัสกลับไปที่ Input field
            self._search_input.focus()

        elif event.key == 'down' and self._search_input.has_focus:
            self._options_list.focus()
        elif event.key == 'tab' and self._options_list.has_focus:
            event.stop() #ทำให้ event ไม่ส่งต่อไป handle ที่อื่นเช่น default behavior ของ app
            # สำหรับปุ่ม tab การสั่ง prevent_default() ไม่สามารถหยุดมันได้เพราะการหยุดใน on_key นี้เป็นของ widget ที่หยุด
            # หากมีการสั่ง prevent_default() ซึ่ง default behavior ของ widget ไม่ได้มีการตั้งค่า tab ให้ action อะไร
            # ไว้แต่แรกอยู่แล้ว
            self._search_input.focus()
    
    @on(OptionList.OptionSelected, "#_option_list")
    def option_selected(self, event: OptionList.OptionSelected):
        selected = event.option
        print(f"select : {selected.prompt} (id={selected.id})")

class CustomRichLog(Widget):
    DEFAULT_CSS = """
    #_MainContentSwitcher {
        background:#002B36;
        border:round #B1C2C2;
        border-title-color: #EEE8D5;
        border-title-style: bold;
        border-title-align: right;
        height: 100%;
        align-vertical: middle;

        & Static{
            text-align: center;
        }

        #_static_loading{
        }

        #_static_error_and_retry{
            color: #F549B1;
        }

        #_static_error{
            color: #F549B1;
        }

        #MainRichLog {
            background:#002B36;
            padding: 0 0 0 1;
            overflow-y: auto;
            overflow-x: auto;
            scrollbar-color: #EEE8D5;
            scrollbar-background: #002B36;
            scrollbar-color-hover:  #EEE8D5;
            scrollbar-background-hover: #002B36;
            scrollbar-color-active: #EEE8D5;
            scrollbar-background-active: #002B36;
        }
    }

    """
    def __init__(self,css_id:str=None,border_title:str=None):
        super().__init__()
        self.id = css_id
        self._border_title = border_title
        self._MainContentSwitcher : None | ContentSwitcher = None
        self._MainRichLog : None | RichLog = None
        self._static_loading: None | Static = None
        self._static_error_and_retry: None | Static = None
        self._static_error: None | Static = None

    def compose(self) -> ComposeResult:
        self._static_loading = Static(id='_static_loading')
        self._static_loading.update('LOADING')
        
        self._MainRichLog = RichLog(id='MainRichLog',highlight=True,markup=True)
        self._MainRichLog.max_lines = 300
        self._MainRichLog.min_width = 0
        self._MainRichLog.wrap = False

        self._static_error_and_retry = Static(id='_static_error_and_retry')
        self._static_error_and_retry.update('ERROR AND RETRY')
        self._static_error = Static(id='_static_error')
        self._static_error.update('ERROR')
        self._MainContentSwitcher = ContentSwitcher(initial='_static_loading',id='_MainContentSwitcher')
        self._MainContentSwitcher.border_title = self._border_title

        with self._MainContentSwitcher:
            yield self._static_loading
            yield self._MainRichLog
            yield self._static_error_and_retry
            yield self._static_error

    def on_mount(self) -> None:
        """Called  when the DOM is ready."""
        #self._MainRichLog.write("Write text or any Rich renderable! test test")
    
    def set_display_state(self,state:str=None):
        if(state not in ['_static_loading','MainRichLog','_static_error_and_retry','_static_error']):
            raise Exception(f"state not in ['_static_loading','MainTree','_static_error_and_retry','_static_error']")
        self._MainContentSwitcher.current = state

    def add_log(self,text:str=None):
        self._MainRichLog.write(text)

    def add_branch(self,text:str=None):
        self._MainRichLog.write(f'└─ {text}')

    def clear_log(self):
        self._MainRichLog.clear()

    '''
    def on_key(self, event: events.Key) -> None:
        """Write Key events to log."""
        self._MainRichLog.write(event.key)
    '''

class CustomLogTree(Widget):
    DEFAULT_CSS = """
    #MainContentSwitcher {
        /* support tree and scrollbar */
        border: round #B1C2C2;
        border-title-color: #EEE8D5;
        /* border-title-background: white; */
        border-title-style: bold;
        border-title-align: right;
        width: 100%;
        height: 100%;
        overflow: auto;
        background: #002B36;
        align-vertical: middle;

        & Static{
            text-align: center;
        }

        #_static_loading{
        }

        #_static_error_and_retry{
            color: #F549B1;
        }

        #_static_error{
            color: #F549B1;
        }

        & Tree {
            background: #002B36;
            scrollbar-color: #EEE8D5;
            scrollbar-background: #002B36;
            
            scrollbar-color-hover:  #EEE8D5;
            scrollbar-background-hover: #002B36;

            scrollbar-color-active: #EEE8D5;
            scrollbar-background-active: #002B36;
        }
        & Tree > .tree--guides {
            color: #EEE8D5;
        }
        & Tree > .tree--guides-hover {
            color: #EEE8D5;
        }
        & Tree > .tree--guides-selected {
            color: #EEE8D5;
        }

        /*& Tree > .tree--highlight {color: red;}*/

        & Tree > .tree--highlight-line {
            color: #EEE8D5; /* arrow color */
        }
        
        /*& Tree > .tree--cursor {color: #EEE8D5;background: #002B36;}*/
    }
    """
    def __init__(self,css_id:str,border_title:str):
        super().__init__()
        self.id = css_id
        self.border_title = border_title
        self._MainLog: None | Log = None
        self._RootTopic = 'ROOT'
        self._MainTree: None | Tree = None
        self.node_tree_dict = {}
        self._static_loading: None | Static = None
        self._static_error_and_retry: None | Static = None
        self._static_error: None | Static = None

    def compose(self):
        self._static_loading = Static(id='_static_loading')
        self._static_loading.update('LOADING')
        self._MainTree = Tree(self._RootTopic,id='MainTree')
        self._static_error_and_retry = Static(id='_static_error_and_retry')
        self._static_error_and_retry.update('ERROR AND RETRY')
        self._static_error = Static(id='_static_error')
        self._static_error.update('ERROR')

        self._MainContentSwitcher = ContentSwitcher(initial='_static_loading',id="MainContentSwitcher")

        with self._MainContentSwitcher:
            yield self._static_loading
            yield self._MainTree
            yield self._static_error_and_retry
            yield self._static_error

    def on_mount(self) -> None:
        self._MainContentSwitcher.border_title = self.border_title
        self._MainContentSwitcher.can_focus = False
        self._MainTree.show_root = False
        self._MainTree.root.expand_all()

    def set_display_state(self,state:str=None):
        if(state not in ['_static_loading','MainTree','_static_error_and_retry','_static_error']):
            raise Exception(f"state not in ['_static_loading','MainTree','_static_error_and_retry','_static_error']")
        self._MainContentSwitcher.current = state

    def build_main_tree_node(self,input_treenode_graph:dict,visited=None):
        for index_current_node in [k for k,v in input_treenode_graph.items() if(v['parent']==None)]:
            if(visited==None):
                visited = set()

            visited.add(index_current_node)
            current_node = self._MainTree.root.add(input_treenode_graph[index_current_node]['node_data'])
            self.node_tree_dict = self.node_tree_dict | {index_current_node:current_node}
            current_node.expand()

            self.populate_tree(
                input_treenode_graph=input_treenode_graph,
                node=current_node,
                index_node=index_current_node,
                visited=visited
            )
    
    def populate_tree(self,input_treenode_graph:dict,node:Tree,index_node:str,visited:set=None):
        for index_neighbor_child in input_treenode_graph[index_node]['child']:
            if index_neighbor_child not in visited:
                visited.add(index_neighbor_child)
                current_node = node.add(input_treenode_graph[index_neighbor_child]['node_data'])
                self.node_tree_dict = self.node_tree_dict | {index_neighbor_child:current_node}
                current_node.expand()
                current_node.allow_expand = False
                self.populate_tree(
                    input_treenode_graph=input_treenode_graph,
                    node=current_node,
                    index_node=index_neighbor_child,
                    visited=visited
                )

    def on_tree_node_collapsed(self, event: Tree.NodeCollapsed) -> None:
        # lock ไม่ให้ node ถูก collapse
        #event.stop()  # ยกเลิก event นี้
        event.node.expand()  # บังคับให้เปิดอีกครั้ง
    
    def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
        # disable selection
        #event.stop()
        #event.node.expand()
        pass

    def on_key(self, event):
        if(event.key=='escape' or event.key=='tab' and self._MainTree.has_focus):
            self._MainTree.unselect()

class Custom2AxisesTable(Widget):
    DEFAULT_CSS = """
    #_datatable {
        color: #B1C2C2;
        background: #002B36;
        width: auto; /* สำคัญ: ให้ DataTable มีความกว้างตามเนื้อหา */
        height: 8; /* สำคัญ: ให้ DataTable มีความสูงตามเนื้อหา */
    }

    #_datatable > .datatable--header {
        color: #EEE8D5;
        background: #002B36;
        text-style: bold;
    }
    """
    def __init__(self,css_id:str=None):
        super().__init__()
        self._datatable: None | DataTable = None
        self.cursor_type='none'
        self.id = css_id

    def compose(self):
        self._datatable = DataTable(id='_datatable',cursor_type=self.cursor_type)
        yield self._datatable

    def insert_column(self, key: str):
        """เพิ่มคอลัมน์พร้อม label ชิดขวา"""
        label = Text.from_markup(key, justify="right")  # ใช้ Rich Text
        self._datatable.add_column(key=key, label=label)

    def insert_row(self, row):
        """เพิ่มแถวโดยทำให้ค่าทุก cell ชิดขวา"""
        styled_row = [
            Text.from_markup(str(cell),justify="right") if (not isinstance(cell, Text) and c==0) else Text.from_markup(str(cell), justify="right")
            for c,cell in enumerate(row)
        ]
        self._datatable.add_row(*styled_row)

    def update_cell_at(self,row,col,value,update_width=True):
        buff_coord = Coordinate(row=row,column=col)
        if not self._datatable.is_valid_coordinate(buff_coord):
            raise CellDoesNotExist(f"Coordinate {buff_coord!r} is invalid.")

        row_key, column_key = self._datatable.coordinate_to_cell_key(buff_coord)
        self._datatable.update_cell(row_key, column_key, value, update_width=update_width)


class CustomRichlog2Columns(Widget):
    DEFAULT_CSS = """
    #_richlog {
        background:#002B36;

        border:round #B1C2C2;
        border-title-color: #EEE8D5;
        border-title-style: bold;
        border-title-align: right;

        padding: 0 0 0 0;

        overflow-y: auto;
        overflow-x: auto;

        scrollbar-color: #EEE8D5;
        scrollbar-background: #002B36;
        
        scrollbar-color-hover:  #EEE8D5;
        scrollbar-background-hover: #002B36;

        scrollbar-color-active: #EEE8D5;
        scrollbar-background-active: #002B36;

        scrollbar-corner-color: #002B36;
    }
    """
    def __init__(self,css_id:str=None,border_title:str=None):
        super().__init__()
        self.id = css_id
        self.border_title = border_title
        self._richlog : RichLog | None = None

    def compose(self):
        self._richlog = RichLog(id='_richlog',highlight=True,markup=True)
        self._richlog.auto_scroll = False
        yield self._richlog

    def on_mount(self):
        self._richlog.border_title = self.border_title

    def add_rich_table(self,rich_table_data:list[tuple[str,str]]):
        #padding=(0,1) → ไม่มีเว้นบรรทัดบน/ล่าง แต่เว้นขอบซ้ายและขวาของเนื้อหาเซลล์ไว้ 1 ช่อง
        rich_table = Table(show_header=False,show_edge=False,box=None,padding=(0,1))
        rich_table.add_column(justify='left')
        rich_table.add_column(justify='left')

        for row in rich_table_data:
            rich_table.add_row(*row)

        self._richlog.write(rich_table)

    def clear_richlog(self):
        self._richlog.clear()

class ViewApp(App):
    CSS = """
    TabbedContent {
        width:100%;
        height: 100%;
        background: #002B36;
    }
    
    TabbedContent > Tabs Tab {
        color:#B1C2C2;
    }

    /* underline of tabs */
    Underline {
        width: 100%;
        height: 1;
        & > .underline--bar {
            color: #B1C2C2;
            background: $foreground 10%;
        }
    }

    Tabs {
        width: 100%;
        height: 1; /*for hide scroll bar or underline bar of tabs*/
        .-active {
            color: #002B36;
            background: #B1C2C2;
        }
        .underline--bar {
            background: $foreground 30%;
        }
        &:focus {
            .underline--bar {
                background: $foreground 30%;
            }
            .-active {
                color:#002B36;
                background: #B1C2C2;
                text-style: $block-cursor-text-style;
            }
        }
    }

    /* Layout ของ Tab เนื้อหา */
    /* แถวแรก: 3 คอลัมน์ */
    #col1 {
        layout: vertical;
        width: 29%;
        height: 1fr;
        align: left top;
    }

    #FreeBalanceLogTree{
        height: 33%;
    }

    #PerformanceRichLog{
        height: 33%;
    }
    
    #LogEventRichLog{
        height: 35%;
    }

    #col2 {
        layout: vertical;
        width: 44%;
        height: 100%;
        align: center top;
    }

    #col2_horizontal {
        width: 100%; /* ให้ Horizontal container ใช้ความกว้างเต็มของ col2 */
        height: 2; /* ให้ Horizontal container ใช้ความสูงเต็มที่เหลือใน col2 */
    }

    #SymbolInputAutoCompleteLabel{
        padding-left:1;
    }
    
    #SymbolInputAutoComplete{
    }

    #LastUpdateLabel{
        padding-left:1;
    }

    #SymbolProgressUpdateInterval{
    }

    #SymbolOverview2AxisesTable{
        height: 26%;
        width: 100%;
        align: center top;
    }

    #DciSerieTabContentLogTable{
        height: 34%;
    }

    #CommandOptionListAndInputSearch{
        width:100%;
        height:38%;
    }

    #col3 {
        layout: vertical;
        width: 27%;
        height: 1fr;
        align: right top;
    }

    #OrderOverviewLogTree{
        height: 33%;
    }
    #EquityLogTree{
        height: 33%;
    }
    #OrderDetailRichLog{
        height: 35%;
    }
    """

    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("MAIN"):
                # Row 1: 3 Columns          
                with Horizontal():
                    with Vertical(id='col1'):
                        yield CustomLogTree(css_id='FreeBalanceLogTree',border_title='FREE_BALANCE')
                        yield CustomRichLog(css_id='PerformanceRichLog',border_title='PERFORMANCE')
                        yield CustomRichLog(css_id='LogEventRichLog',border_title='LOG_EVENT')

                    with Vertical(id='col2'):
                        with Horizontal(id='col2_horizontal'):
                            yield Label('SYMBOL : ',id='SymbolInputAutoCompleteLabel')
                            yield CustomInputAutoComplete(css_id='SymbolInputAutoComplete',placeholder_input=' list [▼]')
                            yield Label('UPDATE_INTERVAL : ',id='LastUpdateLabel')
                            yield ProgressCountDownTimeInterval(css_id='SymbolProgressUpdateInterval',prefix_count_label='in ')

                        yield Custom2AxisesTable(css_id='SymbolOverview2AxisesTable')
                        yield CustomTabContentLogTable(css_id='DciSerieTabContentLogTable',border_title='DCI_SERIES',cursor_type='row')
                        yield CustomOptionListAndInputSearch(css_id='CommandOptionListAndInputSearch')

                    with Vertical(id='col3'):
                        yield CustomLogTree(css_id='OrderOverviewLogTree',border_title='ORDER_OVERVIEW')
                        yield CustomLogTree(css_id='EquityLogTree',border_title='EQUITY')
                        yield CustomRichlog2Columns(css_id='OrderDetailRichLog',border_title='ORDER_DETAIL')

            with TabPane("LOG", id="other-tab"):
                yield Label("Other content...")
    
    def on_mount(self) -> None:
        #FreeBalanceLogTree
        FreeBalanceLogTree = self.query_one('#FreeBalanceLogTree')
        input_free_balance_tree_data = {
            'e1':{'node_data':Text(f"binance_global", style="#EEE8D5"),'parent':None,'child':['w1','w2','w3']},
            'w1':{'node_data':Text(f"earn_wallet", style="#98D4D1"),'parent':'e1','child':['f1']},
            'f1':{'node_data':Text(f"<free_amount_1_node>", style="#C2DBDE"),'parent':'w1','child':[]},
            'w2':{'node_data':Text(f"spot_wallet", style="#98D4D1"),'parent':'e1','child':['f2']},
            'f2':{'node_data':Text(f"<free_amount_2_node>", style="#C2DBDE"),'parent':'w2','child':[]},
            'w3':{'node_data':Text(f"future_wallet", style="#98D4D1"),'parent':'e1','child':['f3']},
            'f3':{'node_data':Text(f"<free_amount_3_node>", style="#C2DBDE"),'parent':'w3','child':[]}
        }
        FreeBalanceLogTree.build_main_tree_node(input_free_balance_tree_data)
        FreeBalanceLogTree.set_display_state(state='MainTree')
        print('testing')
        print(FreeBalanceLogTree.node_tree_dict['w1'])
        print(FreeBalanceLogTree.node_tree_dict['w1'].label)
        print(FreeBalanceLogTree.node_tree_dict['w1'].data)
        #FreeBalanceLogTree.node_tree_dict['w1'].set_label(Text(f"<wallet_1_node> update", style="#98D4D1"))

        #PerformanceRichLog
        PerformanceRichLog = self.query_one('#PerformanceRichLog')
        PerformanceRichLog.add_log('INIT [YYYY-MM-DD]')
        PerformanceRichLog.add_branch('[#C2DBDE]xxxxxxx.xx')
        PerformanceRichLog.add_log('TOTAL [YYYY-MM-DD HH:MM:SS]')
        PerformanceRichLog.add_branch('[#C2DBDE]xxxxxxx.xx')
        PerformanceRichLog.add_log('TOTAL_CHG.[YYYY-MM-DD HH:MM:SS]')
        PerformanceRichLog.add_branch('[#C2DBDE]xxx.xx % | avg_mth : xxx.xx %')
        PerformanceRichLog.add_log('PREV.MONTH : [#C2DBDE]xxxxxxx.xx')
        PerformanceRichLog.add_log('THIS MONTH : [#C2DBDE]xxxxxxx.xx')
        PerformanceRichLog.set_display_state(state='MainRichLog')

        #LogEventRichLog
        LogEventRichLog = self.query_one("#LogEventRichLog")
        LogEventRichLog.set_display_state(state='MainRichLog')

        #SymbolInputAutoComplete
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

        SymbolInputAutoComplete = self.query_one('#SymbolInputAutoComplete')
        SymbolInputAutoComplete.set_candidates_list(candidates_list=candidates_list)

        #SymbolProgressUpdateInterval
        SymbolProgressUpdateInterval = self.query_one("#SymbolProgressUpdateInterval")
        countdown_total = 15   # ⬅ กำหนดเวลานับถอยหลัง (15 วินาที)
        countdown_value = countdown_total
        def update_custom_procress_countdown() -> None:
            nonlocal countdown_value
            countdown_value -= 1
            percent = int((countdown_value / countdown_total) * 100)
            SymbolProgressUpdateInterval.set_current_ProgressBar_and_CountLabel(percent=percent,count_str=str(countdown_value))

            if countdown_value <= 0:
                """
                #trigger_zone (controller do something)
                """
                print('do something..')

                countdown_value = countdown_total
                SymbolProgressUpdateInterval.set_current_ProgressBar_and_CountLabel(percent=100,count_str=str(countdown_value))

        self.set_interval(1.0,update_custom_procress_countdown)

        #SymbolOverview2AxisesTable
        SymbolOverview2AxisesTable = self.query_one('#SymbolOverview2AxisesTable')
        headers = [f"{'11:23:42':>8}",f"{'SPOT':>9}",f"{'DIFF.F':>8}",f"{'FUTURE':>9}",f"{'FUND_RATE':>8}"]
        topic_rows = ['[#EEE8D5]PRICE[/#EEE8D5]','[#EEE8D5]CHANGE[/#EEE8D5]',"-","[#EEE8D5]BBM(7)(1/2)[/#EEE8D5]","[#EEE8D5]F.250327[/#EEE8D5]","123123.44"]
        
        rows = [
            ("123123.44","123.12","123123.44","123123.44"),
            ("123.44 %","123.44 %","123.44 %","123.44 %"),
            ("-","-","-","-"),
            ("12334.00","12345.00","[#EEE8D5]ATR(7)[/#EEE8D5]","12345.00"),
            ("[#EEE8D5]DIFF.S[/#EEE8D5]","[#EEE8D5]DIFF.F[/#EEE8D5]","[#EEE8D5]F.250327[/#EEE8D5]","[#EEE8D5]DIFF.S[/#EEE8D5]"),
            ("123.44 %","123.44 %","123123.44","123.44 %")
        ]

        rows = [(topic_row,) + row for topic_row, row in zip(topic_rows, rows)]

        for header in headers:
            SymbolOverview2AxisesTable.insert_column(header)

        for row in rows:
            SymbolOverview2AxisesTable.insert_row(row)

        #SymbolOverview2AxisesTable.update_cell_at(0,2,'test_update',True)
        SymbolOverview2AxisesTable.refresh()
        
        #DciSerieTabContentLogTable
        DciSerieTabContentLogTable = self.query_one("#DciSerieTabContentLogTable")
        DciSerieTabContentLogTable.insert_header_columns_maintable1(['STRIKE_PRICE','CHANGE','APR/HR.','SETTLEMENT'])

        rows = [
            ('1xxxxxx.xxxxxx','xxx.xx','xxx.xx','xx'),
            ('2xxxxxx.xx','xxx.xx','xxx.xx','xx'),
            ('3xxxxxx.xx','xxx.xxxxxxxx','xxx.xx','xx'),
            ('4xxxxxx.xx','xxx.xx','xxx.xx','xx'),
            ('5xxxxxx.xx','xxx.xx','xxx.xx','xx')
        ]

        for row in rows:
            DciSerieTabContentLogTable.update_by_rows_maintable1(row)

        #DciSerieTabContentLogTable._MainHorzontal1_BuyLow.children[3].styles.width = 13
        #DciSerieTabContentLogTable.update_cell_at_maintable1(2,1,'testval')

        #CommandOptionListAndInputSearch
        CommandOptionListAndInputSearch = self.query_one('#CommandOptionListAndInputSearch')
        options_list_items = [
            Option("Aerilon", id="aer"),
            Option("Aquaria", id="aqu"),
            Option("Box", id="box"),
            Option("book", id="book"),
            Option("Tank",id='tank'),
            Option("Home",id='home')
        ]
        CommandOptionListAndInputSearch.update_options_list(new_options_list=options_list_items)

        #OrderOverviewLogTree
        OrderOverviewLogTree = self.query_one('#OrderOverviewLogTree')
            #FFE016 for state color
        input_order_overview_data = {
            'symbol_1':{'node_data':'BTC/USDT','parent':None,'child':['deploy_1']},
            'deploy_1':{'node_data':Text.from_markup('deploy_1 [bold #FFE016][STATE_1][/bold #FFE016]',style='#98D4D1'),'parent':'symbol_1','child':['d1_dbl1','d1_psf1']},
            'd1_dbl1':{'node_data':Text.from_markup('d1_dbl1',style='#C2DBDE'),'parent':'deploy_1','child':[]},
            'd1_psf1':{'node_data':Text.from_markup('d1_psf1 [#F549B1]\[WARNING][/#F549B1]',style='#C2DBDE'),'parent':'deploy_1','child':[]},
            'symbol_2':{'node_data':'ETH/USDT','parent':None,'child':['deploy_2']},
            'deploy_2':{'node_data':Text.from_markup('deploy_2 [bold #FFE016][STATE_1][/bold #FFE016]',style='#98D4D1'),'parent':'symbol_2','child':['d2_dbl1','d2_psf1']},
            'd2_dbl1':{'node_data':Text.from_markup('d2_dbl1 [#F549B1]\[WARNING][/#F549B1]',style='#C2DBDE'),'parent':'deploy_2','child':[]},
            'd2_psf1':{'node_data':Text.from_markup('d2_psf1',style='#C2DBDE'),'parent':'deploy_2','child':[]},
        }
        OrderOverviewLogTree.build_main_tree_node(input_order_overview_data)
        OrderOverviewLogTree.set_display_state(state='MainTree')

        #EquityLogTree
        EquityLogTree = self.query_one('#EquityLogTree')
        input_equity_tree_data = {
            'f1':{'node_data':Text(f"future_wallet", style="#EEE8D5"),'parent':None,'child':['dp1','dp2','dp3']},
            'dp1':{'node_data':Text.from_markup(f"dp1,ep:xxxxxxx,pnl:xxxxxxx", style="#98D4D1"),'parent':'f1','child':['id1']},
            'id1':{'node_data':Text.from_markup(f"dx_xxxx,pnl:xxxxxxx,ep:xxxxxxx", style="#C2DBDE"),'parent':'dp1','child':[]},
            'dp2':{'node_data':Text.from_markup(f"dp2,ep:xxxxxxx,pnl:xxxxxxx", style="#98D4D1"),'parent':'f1','child':['id2']},
            'id2':{'node_data':Text.from_markup(f"dx_xxxx,pnl:xxxxxxx,ep:xxxxxxx", style="#C2DBDE"),'parent':'dp2','child':[]},
            'dp3':{'node_data':Text.from_markup(f"dp3,ep:xxxxxxx,pnl:xxxxxxx", style="#98D4D1"),'parent':'f1','child':['id3']},
            'id3':{'node_data':Text.from_markup(f"dx_xxxx,pnl:xxxxxxx,ep:xxxxxxx", style="#C2DBDE"),'parent':'dp3','child':[]}
        }
        EquityLogTree.build_main_tree_node(input_equity_tree_data)
        EquityLogTree.set_display_state(state='MainTree')

        #OrderDetailRichLog
        OrderDetailRichLog = self.query_one('#OrderDetailRichLog')
        order_detail_data = [
            ('id','xxxxxx/xxxxxx'),
            ('entry_chg.','xxxxx.xx'),
            ('current_chg.','xxxxx.xx'),
            ('apr','xxxxxx.xx'),
            ('pnl_forecast','xxxx.xx'),
            ("subscribe", "xxxx.xx"),
            ('expire','x days'),
            ('fee_cost','xxxx.xx'),
            ('strike_price','xxxxxx.xx'),
            ('settleDate','yyyy-mm-dd hh:mm:ss'),
            ('entry_time','yyyy-mm-dd hh:mm:ss')
        ]
        OrderDetailRichLog.add_rich_table(order_detail_data)

if __name__ == "__main__":
    ViewApp().run()
