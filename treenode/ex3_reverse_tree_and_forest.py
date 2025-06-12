from rich import print
from rich.console import Group
from rich.console import Console
from rich.tree import Tree
from rich.text import Text
from rich.panel import Panel
from io import StringIO
from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []  # สำหรับ N-ary Tree
    
    def to_rich_tree(self):
        """แปลงโครงสร้างเป็น Rich Tree"""
        if(isinstance(self.value,str)==True):
            forest_data = {'level':-1,'parent':None,'children':[i.value['id'] for i in self.children]}
            rich_tree = Tree(f"[bold green]{self.value} : {str(forest_data)}[/]",guide_style="bold")
        else:
            for k in self.value.keys():
                if(isinstance(self.value[k],str)==True):
                    self.value[k] = '[bold #ffd75f]'+self.value[k]+'[/]'
            
            data = str(self.value).replace('True','[bold green]TRUE[/]')
            
            title = f"💳 {self.value['id']}"
            panel_node = Panel(data)
            node_content = Group(title,panel_node)

            rich_tree = Tree(node_content,guide_style="bold")
        
        for child in self.children:
            rich_tree.add(child.to_rich_tree())
        return rich_tree

    def __repr__(self):
        """ใช้ Rich แสดงโครงสร้างต้นไม้"""
        with StringIO() as buffer:
            console = Console(file=buffer, force_terminal=True)
            rich_tree = self.to_rich_tree()
            console.print(rich_tree)
            return console.file.getvalue()

    def to_dict(self):
        return {
            'value':self.value,
            'children':[child.to_dict() for child in self.children]
        }

# BFS เพื่อ Traverse Tree หรือ Forest และสร้าง Graph-like Structure
def bfs_to_graph(root_or_forest):
    graph = {}  # โครงสร้าง Graph-like Structure

    # ตรวจสอบว่าเป็น Forest (หลาย root) หรือ Tree (เดี่ยว)
    roots = root_or_forest if isinstance(root_or_forest, list) else [root_or_forest]

    for root in roots:
        # BFS สำหรับแต่ละ root ใน Forest
        queue = deque([(root, 0, None)])  # (Node, Level, Parent)
        while queue:
            node, level, parent = queue.popleft()

            try:
                #incase tree
                node_id = node.value["id"]  # ID ของ Node
                node_except_id = {k: v for k, v in node.value.items() if k != 'id'}
                # เพิ่มข้อมูลโหนดลงใน Graph
                graph[node_id] = node_except_id | {
                    "level": level,
                    "parent": parent,
                    "children": []
                }
            except TypeError:
                #incase forest
                node_id = 'Forest'
                graph[node_id] = {"level":-1,"parent":None,"children":[]}

            # Traverse ลูกของ Node นี้
            for child in node.children:
                child_id = child.value["id"]
                graph[node_id]["children"].append(child_id)  # เพิ่ม ID ของลูกใน children
                queue.append((child, level + 1, node_id))  # ใส่ลูกโหนดลงใน Queue

    return graph

# ฟังก์ชันช่วยสำหรับเพิ่ม children ใน Tree
def add_children_to_tree(graph, tree_node, node_id):
    for child_id in graph[node_id]["children"]:
        child_tree = tree_node.add(f"{child_id} : {graph[child_id]}")
        add_children_to_tree(graph, child_tree, child_id)


# ฟังก์ชันสำหรับสร้าง Rich Tree จาก Forest (Graph-like Structure)
def display_graph_to_forest(graph):
    if not graph:
        return Tree("Empty Forest")

    # ค้นหา root nodes (โหนดที่ parent เป็น None)
    root_ids = [node_id for node_id, node_data in graph.items() if node_data["parent"] is None]
    
    # สร้าง root สำหรับ tree หรือ ของ forest
    root_data = graph[root_ids[0]]
    root_tree = Tree(f"{root_ids[0]} : {root_data}")
    add_children_to_tree(graph, root_tree, root_ids[0])

    return root_tree

# สร้าง Tree
tree_root = TreeNode({'id': '1', 'b': 'test'})
tree_root.children = [
    TreeNode({'id': '2', 'b': '1'}),
    TreeNode({'id': '4', 'b': 'test'}),
    TreeNode({'id': '6', 'b': '1'})
]
tree_root.children[0].children = [
    TreeNode({'id': '3', 'b': 'test'}),
    TreeNode({'id': '5', 'b': '1'})
]

# สร้าง Forest
forest = TreeNode("Forest")
forest.children = [
    TreeNode({'id': '1', 'b': 'test'}),
    TreeNode({'id': '5', 'b': 'test'})
]
forest.children[0].children = [
    TreeNode({'id': '2', 'b': '1'}),
    TreeNode({'id': '4', 'b': 'test'})
]
forest.children[1].children = [
    TreeNode({'id': '6', 'b': 'test'})
]

# ทดสอบ BFS บน Tree
tree_graph = bfs_to_graph(tree_root)
print("Graph from Tree:")
print(tree_graph)
print(display_graph_to_forest(tree_graph))
print(tree_root.to_rich_tree())

print("---------")
# ทดสอบ BFS บน Forest
forest_graph = bfs_to_graph(forest)
print("\nGraph from Forest:")
print(forest_graph)
print(display_graph_to_forest(forest_graph))
print(forest.to_rich_tree())
