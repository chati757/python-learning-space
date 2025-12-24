from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.widgets import Log
from textual.widgets import Tree
from rich.text import Text
from rich import print

testlog = []

class CustomLogTree(Widget):
    DEFAULT_CSS = """
    #MainLog {
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
        self._RootTopic = 'ROOT'
        self._MainTree = None
        self.node_tree_dict = {}

    def compose(self):
        with Log(id="MainLog"):
            self._MainTree = Tree(self._RootTopic,id='MainTree')
            #self.MainTree.show_root = False
            #self.MainTree.root.expand()
            yield self._MainTree

    def on_mount(self) -> None:
        self.query_one("#MainLog", Log).border_title = self.border_title
        MainTree = self.query_one("#MainTree",Tree)
        MainTree.show_root = False
        MainTree.root.expand_all()

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

class TestViewApp(App):
    def compose(self) -> ComposeResult:
        yield CustomLogTree(css_id='CustomLogTree1',border_title='TEST_TITLE')

    async def on_mount(self) -> None:
        input_tree_data = {
            'e1':{'node_data':Text(f"<exchange_1_node>", style="#EEE8D5"),'parent':None,'child':['w1']},
            'w1':{'node_data':Text(f"<wallet_1_node>", style="#98D4D1"),'parent':'e1','child':['f1']},
            'f1':{'node_data':Text(f"<free_amount_1_node>", style="#C2DBDE"),'parent':'w1','child':[]},
            'e2':{'node_data':Text(f"<exchange_2_node>", style="#EEE8D5"),'parent':None,'child':['w2']},
            'w2':{'node_data':Text(f"<wallet_2_node>", style="#98D4D1"),'parent':'e2','child':['f2']},
            'f2':{'node_data':Text(f"<free_amount_2_node>", style="#C2DBDE"),'parent':'w2','child':[]}
        }
        self.query_one("#CustomLogTree1",expect_type=CustomLogTree).build_main_tree_node(input_tree_data)
        self.query_one("#CustomLogTree1",expect_type=CustomLogTree).node_tree_dict['w1'].set_label(Text(f"<wallet_1_node> update", style="#98D4D1"))

if __name__ == "__main__":
    try:
        TestViewApp().run()
    finally:
        print(testlog)