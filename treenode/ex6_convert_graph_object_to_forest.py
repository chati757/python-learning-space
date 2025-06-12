from io import StringIO
from rich.ansi import AnsiDecoder
from rich.tree import Tree
from rich.console import Group
from rich.console import Console
from rich.panel import Panel
from rich import print
import json

def convert_ascii_console_to_mark_console(ascii_text):
    with StringIO() as buffer:
        # กำหนดให้ Console เขียน output ลงใน buffer แทน
        console = Console(file=buffer, force_terminal=True)
        decoder = AnsiDecoder()
        console.print(ascii_text)
        # ดึงข้อความที่อยู่ใน buffer ออกมา
        mark_data = []
        for i in decoder.decode(str(buffer.getvalue())):
            mark_data.append(i.markup)
        
        return "\n".join(mark_data)

def display_forest_from_graph_object(graph,highlight_value=False):
    if not graph:
        return Tree("Empty Forest")

    # ค้นหา root nodes (โหนดที่ parent เป็น None) (หา root หรือ forest)
    root_ids = [node_id for node_id, node_data in graph.items() if node_data["parent"] is None]

    # สร้าง root สำหรับ tree หรือ ของ forest
    root_data = graph[root_ids[0]]
    root_tree = Tree(f"[bold green]{root_ids[0]} : {root_data}[/]",guide_style="bold")

    def add_children_to_tree(graph,node_id,tree_node):
        for child_id in graph[node_id]["children"]:
            for k,v in graph[child_id].items():
                if(k not in ['level','parent','children'] and highlight_value==True):
                    graph[child_id][k] = f"[bold #ffd75f]{v}[/]"

            title = f"💳 {child_id}"
            display_key_list = [i for i in list(graph[child_id].keys()) if(i not in ['level','parent','children'])]
            node_panel = Panel(
                convert_ascii_console_to_mark_console(json.dumps({k:graph[child_id][k] for k in display_key_list},indent=4))+
                "\nlevel : "+str(graph[child_id]['level'])+
                "\nparent : "+str(graph[child_id]['parent'])+
                "\nchildren : "+str(graph[child_id]['children'])
            )
            node_content = Group(title,node_panel)
            child_tree = tree_node.add(node_content,guide_style="bold")
            add_children_to_tree(graph,child_id,child_tree)

    add_children_to_tree(graph,root_ids[0],root_tree)

    return root_tree

if __name__=='__main__':
    forest_graph = {
        'Forest': {'level': -1, 'parent': None, 'children': ['1', '5']},
        '1': {'b': {'a':1,'b':2}, 'level': 1, 'parent': 'Forest', 'children': ['2', '4']},
        '5': {'b': [{'a':1,'b':2},{'a':1,'b':2},{'a':1,'b':2}], 'level': 1, 'parent': 'Forest', 'children': ['6']},
        '2': {'b': '1', 'level': 2, 'parent': '1', 'children': []},
        '4': {'b': 'test', 'level': 2, 'parent': '1', 'children': []},
        '6': {'b': 'test', 'level': 2, 'parent': '5', 'children': []}
    }

    print(display_forest_from_graph_object(forest_graph))
    #import pdb;pdb.set_trace()