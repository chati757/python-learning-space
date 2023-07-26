from PrettyPrint import PrettyPrintTree
from colorama import Back

class Tree:
    def __init__(self,value,label=None):
        self.val = value
        self.label = label
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        return child


pt = PrettyPrintTree(
    lambda x: x.children, 
    lambda x: x.val, 
    lambda x: x.label,
    max_depth=5
)

tree = Tree(1)
child1 = tree.add_child(Tree('test1\n','testlabel1'))
child2 = tree.add_child(Tree('test2\n',False))
child1.add_child(Tree('error\ntest','testlabel2'))
child1.add_child(Tree('test4\n',False))
child1.add_child(Tree('error\n','testlabel3'))
child2.add_child(Tree('test6\n',False))
pt(tree)