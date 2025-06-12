from collections import deque
from rich.tree import Tree
from rich import print

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []  # สำหรับ N-ary Tree

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
            node_id = node.value["id"]  # ID ของ Node
            node_except_id = {k: v for k, v in node.value.items() if k != 'id'}

            # เพิ่มข้อมูลโหนดลงใน Graph
            graph[node_id] = node_except_id | {
                "level": level,
                "parent": parent,
                "children": []
            }

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
    if(len(root_ids)>1):
        forest = Tree("[bold green]Forest[/]")
        for root_id in root_ids:
            root_data = graph[root_id]
            root_tree = forest.add(f"{root_id} : {root_data}")
            add_children_to_tree(graph, root_tree, root_id)

        return forest
    else:
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
forest = [
    TreeNode({'id': '1', 'b': 'test'}),
    TreeNode({'id': '5', 'b': 'test'})
]
forest[0].children = [
    TreeNode({'id': '2', 'b': '1'}),
    TreeNode({'id': '4', 'b': 'test'})
]
forest[1].children = [
    TreeNode({'id': '6', 'b': 'test'})
]

# ทดสอบ BFS บน Tree
tree_graph = bfs_to_graph(tree_root)
print("Graph from Tree:")
print(tree_graph)
print(display_graph_to_forest(tree_graph))

print("---------")
# ทดสอบ BFS บน Forest
forest_graph = bfs_to_graph(forest)
print("\nGraph from Forest:")
print(forest_graph)
print(display_graph_to_forest(forest_graph))
'''
#ความแตกต่างระหว่าง list-dict กับ Graph-like Structure (Dictionary of Nodes)
output = [
    {"id": "1", "b": "test", "level": 0, "parent": None},
    {"id": "2", "b": "1", "level": 1, "parent": "1"},
    {"id": "4", "b": "test", "level": 1, "parent": "1"},
    {"id": "6", "b": "1", "level": 1, "parent": "1"},
    {"id": "3", "b": "test", "level": 2, "parent": "2"},
    {"id": "5", "b": "1", "level": 2, "parent": "2"}
]

graph = {
    "1": {"b": "test", "level": 0, "parent": None, "children": ["2", "4", "6"]},
    "2": {"b": "1", "level": 1, "parent": "1", "children": ["3", "5"]},
    "4": {"b": "test", "level": 1, "parent": "1", "children": []},
    "6": {"b": "1", "level": 1, "parent": "1", "children": []},
    "3": {"b": "test", "level": 2, "parent": "2", "children": []},
    "5": {"b": "1", "level": 2, "parent": "2", "children": []}
}
'''