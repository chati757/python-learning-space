from rich.tree import Tree
from rich.console import Console
from rich.panel import Panel
from io import StringIO
from rich.console import Group
from rich.text import Text

class tree_node():
    def __init__(self,value=None):
        self.value = value
        self.children = []

    def add_child(self,child_node):
        self.children.append(child_node)
    
    def to_rich_tree(self):
        """แปลงโครงสร้างเป็น Rich Tree"""
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

if __name__=='__main__':
    root = tree_node({
        'id':'rne_0',
        'exchange':'binance_th',
        'connection_status':'online',
        'can_trade':True,
        'can_withdraw':True,
        'can_deposit':True,
        'orders':[],
        'balance':[
            {'asset':'BTC','free':'','locked':''},
            {'asset':'ETH','free':'','locked':''}
        ],
        'strategies_member_id':[]
    })

    child_1 = tree_node({
        'id':'rne_1',
        'exchange':'binance_global',
        'connection_status':'online',
        'can_trade':True,
        'can_withdraw':True,
        'can_deposit':True,
        'orders':[],
        'balance':[
            {'asset':'BTC','free':'','locked':''},
            {'asset':'ETH','free':'','locked':''}
        ],
        'strategies_member_id':[]
    })

    child_1_1 = tree_node({
        'id':'future_wallet_1',
        'exchange':'binance_global',
        'connection_status':'online',
        'can_trade':True,
        'can_withdraw':True,
        'can_deposit':True,
        'orders':[],
        'balance':[
            {'asset':'BTC','free':'','locked':''},
            {'asset':'ETH','free':'','locked':''}
        ],
        'max_leverage':'',
        'strategies_member_id':[]
    })
    
    child_1_2 = tree_node({
        'id':'future_wallet_2',
        'api_key':'xxx..',
        'api_secret_key':'xxx..',
        'exchange':'binance_global',
        'connection_status':'online',
        'can_trade':True,
        'can_withdraw':True,
        'can_deposit':True,
        'orders':[],
        'balance':[
            {'asset':'BTC','free':'','locked':''},
            {'asset':'ETH','free':'','locked':''}
        ],
        'max_leverage':'',
        'strategies_member_id':[]
    })

    root.add_child(child_1)
    child_1.add_child(child_1_1)
    child_1.add_child(child_1_2)

    print('display')
    print(root)
    #import pdb;pdb.set_trace()