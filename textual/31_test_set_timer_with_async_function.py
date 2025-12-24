from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.widgets import ContentSwitcher
from textual.widgets import Tree
from textual.widgets import Static
from textual.containers import Horizontal
from textual.message import Message
from rich.text import Text
import asyncio
import time

class LogTree(Widget):
    DEFAULT_CSS = """
    #_content_switcher {
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
        align: center middle;
        & Static {
            text-align: center;
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
    def __init__(self,css_id:str=None):
        super().__init__()
        self.id = css_id
        self._content_switcher: None | ContentSwitcher = None
        self._tree: None | Tree = None
        self._RootTopic = 'ROOT'
        self.node_tree_dict = {}
        self._static_loading: None | Static = None
        self._static_error_and_retry: None | Static = None
        self._static_error: None | Static = None

    def compose(self) -> ComposeResult:
        self._tree = Tree(self._RootTopic,id='_tree_normal')
        self._static_loading = Static(id='_static_loading')
        self._static_loading.update('LOADING')
        self._static_error_and_retry = Static(id='_static_error_and_retry')
        self._static_error_and_retry.update('ERROR AND RETRY')
        self._static_error = Static(id='_static_error')
        self._static_error.update('ERROR')
        self._content_switcher = ContentSwitcher(initial='_static_loading',id='_content_switcher')
        
        with self._content_switcher:
            yield self._static_loading
            yield self._tree
            yield self._static_error_and_retry
            yield self._static_error
        

    def on_mount(self) -> None:
        self._tree.show_root = False
        self._tree.root.expand_all()

    def set_display_state(self,state:str=None):
        if(state not in ['_static_loading','_tree_normal','_static_error_and_retry','_static_error']):
            raise Exception(f"state not in ['_static_loading','_tree_normal',','_static_error_and_retry','_static_error']")
        self._content_switcher.current = state

    def build_main_tree_node(self,input_treenode_graph:dict,visited=None):
        for index_current_node in [k for k,v in input_treenode_graph.items() if(v['parent']==None)]:
            if(visited==None):
                visited = set()

            visited.add(index_current_node)
            current_node = self._tree.root.add(input_treenode_graph[index_current_node]['node_data'])
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

class CTVFreeBalanceUpdated(Message):
    """Event ที่ส่งจาก Controller ไปยัง View เพื่อแจ้งว่าราคาอัปเดตแล้ว"""
    
    def __init__(self, sender, free_balance: str) -> None:
        super().__init__()
        self.sender = sender   # object ที่ส่ง event (เช่น Controller)
        self.free_balance = free_balance     # ข้อมูลราคาที่ส่งไป

class FreeBalanceController:
    def __init__(self, main_view):
        self.main_view = main_view
        self._running = False

    async def refresh_balance(self):
        free_balance = 123.45  # mock fetch API
        await self.main_view.post_message(CTVFreeBalanceUpdated(free_balance))

    async def _worker(self):
        while self._running:
            await self.refresh_balance()
            await asyncio.sleep(3)

    def start_worker(self):
        self._running = True
        # ✅ ใช้ run_worker ของ Textual เพื่อสอดคล้องกับระบบของ framework
        self.main_view.run_worker(self._worker())

    def stop_worker(self):
        self._running = False

class MainView(App):
    CSS = """
    Horizontal{
    }

    #LogTree{
        align: center middle;
        content-align: center middle;
        height: 40%;
    }

    """
    def __init__(self):
        super().__init__()

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield LogTree(css_id='LogTree')

    #CTVFreeBalanceUpdated
    def on_cvt_free_balance_updated(self,message:CTVFreeBalanceUpdated) -> None:
        print('test message')
        print(message)

    async def do_something(self):
        LogTree = self.query_one('#LogTree')
        input_tree_data = {
            'e1':{'node_data':Text(f"<exchange_1_node>", style="#EEE8D5"),'parent':None,'child':['w1']},
            'w1':{'node_data':Text(f"<wallet_1_node>", style="#98D4D1"),'parent':'e1','child':[]}
        }
        LogTree.build_main_tree_node(input_tree_data)
        LogTree.set_display_state(state='_tree_normal')
        await asyncio.sleep(3)
        LogTree.set_display_state(state='_static_error')

    async def on_mount(self) -> None:
        self.set_timer(delay=3,callback=lambda: self.run_worker(self.do_something()))

if __name__ == "__main__":
    MainView().run()