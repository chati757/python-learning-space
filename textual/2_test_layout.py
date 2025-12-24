from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane , Label
from textual.containers import Vertical, Horizontal
from textual.widgets import Log
from textual.widgets import Tree
from rich.text import Text


class ComplexLayoutApp(App):
    CSS = """
    Screen {
        padding:1 0 0 1;
        layout: vertical;
        background: #002B36;
    }

    TabbedContent {
        height: 1fr;
        background: #002B36;
    }

    /* underline of tabs */
    Underline {
        width: 1fr;
        height: 1;
        & > .underline--bar {
            color: #B1C2C2;
            background: $foreground 10%;
        }
    }

    Tabs {
        width: 100%;
        height: 2;
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
    #row1 {
        layout: horizontal;
        width: 1fr;
        height: 3fr;
    }

    #col1-top {
        /* support tree and scrollbar */
        border: round #B1C2C2;
        border-title-color: #EEE8D5;
        /* border-title-background: white; */
        border-title-style: bold;
        border-title-align: right;
        width: 1fr;
        height: 50%;
        overflow: auto;
        background: #002B36;
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
    }

    #col1-bottom {
        /* support tree and scrollbar */
        border: round #B1C2C2;
        border-title-color: #EEE8D5;
        /* border-title-background: white; */
        border-title-style: bold;
        border-title-align: right;
        width: 1fr;
        height: 50%;
        overflow: auto;
        background: #002B36;
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
    }

    #col2 {
        /* support tree and scrollbar */

        border: round #B1C2C2;
        border-title-color: #EEE8D5;
        /* border-title-background: white; */
        border-title-style: bold;
        border-title-align: right;
        width: 1fr;
        height: 100%;
        overflow: auto;
        background: #002B36;
        & * {
            color: #18BFE8; /*blue*/
            background: #002B36;
            scrollbar-color: #EEE8D5;
            scrollbar-background: #002B36;
            
            scrollbar-color-hover:  #EEE8D5;
            scrollbar-background-hover: #002B36;

            scrollbar-color-active: #EEE8D5;
            scrollbar-background-active: #002B36;
        }
    }

    /* คอลัมน์ที่ 3 แบ่ง vertical */
    #col3-top {
        border: round #B1C2C2;
        border-title-color: #EEE8D5;
        /* border-title-background: white; */
        border-title-style: bold;
        border-title-align: right;
        width: 1fr;
        height: 2fr;
    }

    #col3-bottom {
        border: round #B1C2C2;
        border-title-color: #EEE8D5;
        /* border-title-background: white; */
        border-title-style: bold;
        border-title-align: right;
        width: 1fr;
        height: 1fr;
    }

    /* แถวที่ 2: Input 1 บรรทัด */
    #row2 {
        height: 1;
        width: 1fr;
        padding-left: 1;
    }

    /* แถวที่ 3: พื้นที่ที่เหลือ */
    #row3 {
        width: 1fr;
        height: 1fr;
        border: round #B1C2C2;
    }
    """

    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("MAIN"):
                # Row 1: 3 Columns          
                with Horizontal(id='row1'):
                    with Vertical():
                        with Log(id='col1-top'):
                            tree = Tree("Root")
                            for i in range(30):  # ลองให้เกินความสูงเพื่อให้ scroll
                                tree.root.add(f"Item {i}")
                            tree.root.expand_all()
                            yield tree
                        with Log("Col 1 - Bottom",id='col1-bottom'):
                            tree = Tree("Root")
                            for i in range(30):  # ลองให้เกินความสูงเพื่อให้ scroll
                                tree.root.add(f"Item {i}")
                            tree.root.expand_all()
                            yield tree

                    with Log("Col 2",id='col2'):
                        tree = Tree("Root")
                        for i in range(30):  # ลองให้เกินความสูงเพื่อให้ scroll
                            tree.root.add(f"Item {i}")
                        tree.root.expand_all()
                        yield tree

                    with Vertical():
                        yield Label("Col 3 - Top",id='col3-top')
                        yield Label("Col 3 - Bottom",id='col3-bottom')

                # Row 2: Input 1 line
                with Horizontal(id='row2'):
                    yield Label("Main Content Area (fills remaining space)")

                # Row 3: Remaining area
                yield Label("Main Content Area (fills remaining space)",id='row3')

            with TabPane("LOG", id="other-tab"):
                yield Label("Other content...")
    
    def on_mount(self) -> None:
        self.query_one("#col1-top", Log).border_title = "USDT-FREE"
        self.query_one("#col1-bottom", Log).border_title = "EQUITY"
        self.query_one("#col2", Log).border_title = "ORDER"
        self.query_one("#col3-top", Label).border_title = "ORDER_DETAIL"
        self.query_one("#col3-bottom", Label).border_title = "ORDER_TRACKING"


if __name__ == "__main__":
    ComplexLayoutApp().run()
