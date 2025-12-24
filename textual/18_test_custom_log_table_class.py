from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.widgets import TabbedContent, TabPane , Label
from textual.containers import Vertical, Horizontal
from textual.widgets import Static
from textual.widgets import Log
from textual.widgets import DataTable
from textual.coordinate import Coordinate
from rich.text import Text
from rich import print

class CellDoesNotExist(Exception):
    """The cell key/index was invalid.

    Raised when the coordinates or cell key provided does not exist
    in the DataTable (e.g. out of bounds index, invalid key)"""

class CustomDciSeriesTabLogTable(Widget):
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

class TestViweApp(App):
    CSS = """
    #CustomDciSeriesTabLogTable {
        width: 50%;
        height: 30%;
    }
    """
    def compose(self) -> ComposeResult:
        with Vertical():
            yield CustomDciSeriesTabLogTable(css_id='CustomDciSeriesTabLogTable',border_title='DCI_SERIES',cursor_type='row')

    async def on_mount(self) -> None:
        custom_dci_series_tab_log_table = self.query_one("CustomDciSeriesTabLogTable")
        custom_dci_series_tab_log_table.insert_header_columns_maintable1(['STRIKE_PRICE','CHANGE','APR/HR.','SETTLEMENT'])

        rows = [
            ('1xxxxxx.xxxxxx','xxx.xx','xxx.xx','xx'),
            ('2xxxxxx.xx','xxx.xx','xxx.xx','xx'),
            ('3xxxxxx.xx','xxx.xxxxxxxx','xxx.xx','xx'),
            ('4xxxxxx.xx','xxx.xx','xxx.xx','xx'),
            ('5xxxxxx.xx','xxx.xx','xxx.xx','xx')
        ]

        for row in rows:
            custom_dci_series_tab_log_table.update_by_rows_maintable1(row)

        #custom_dci_series_tab_log_table._MainHorzontal1_BuyLow.children[3].styles.width = 13
        #custom_dci_series_tab_log_table.update_cell_at_maintable1(2,1,'testval')
       
if __name__ == "__main__":
    TestViweApp().run()