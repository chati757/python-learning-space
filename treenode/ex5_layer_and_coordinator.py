'''
การทำงานร่วมกันหลาย tree (1 tree มีหลาย tree node) จำเป็นต้องมี forest 
และโครงสร้างที่ออกแบบมาให้ง่ายเข้าใจ เป็นอิสระจากกัน แต่สามารถทำงานได้สัมพันธ์กัน
และการทำงานจะต้องรองรับต่อยอด เพิ่ม-ลด function ใน อนาคต

โดยโครงได้ออกแบบให้มีองค์ประกอบดังต่อไปนี้
- domain model (TreeNode , Forest)
- processor layer (TreeProcessor)
- comunication layer (mqtt handler)
- controller layer (coordinator)
'''

#---------------- domain model ----------------
class TreeNode:
    def __init__(self, node_id, data=None):
        self.node_id = node_id
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self):
        return f"TreeNode({self.node_id}, {self.data})"

class Forest:
    def __init__(self):
        self.trees = {}  # เก็บต้นไม้หลายต้นในรูปแบบ {tree_id: root_node}

    def add_tree(self, tree_id, root_node):
        self.trees[tree_id] = root_node

    def get_tree(self, tree_id):
        return self.trees.get(tree_id)

    def __repr__(self):
        return f"Forest({list(self.trees.keys())})"

#----------------------------------------------

#-------------- processor model ---------------
class TreeManager:
    def __init__(self, forest):
        self.forest = forest

    def find_node(self, tree_id, node_id):
        root = self.forest.get_tree(tree_id)
        if not root:
            return None

        def dfs(node):
            if node.node_id == node_id:
                return node
            for child in node.children:
                result = dfs(child)
                if result:
                    return result
            return None

        return dfs(root)

    def update_node_data(self, tree_id, node_id, new_data):
        node = self.find_node(tree_id, node_id)
        if node:
            node.data = new_data
            return True
        return False

    def process_tree(self, tree_id, condition):
        # ตัวอย่าง: ประมวลผล node ที่ตรงตามเงื่อนไข
        root = self.forest.get_tree(tree_id)
        if not root:
            return []

        result = []

        def dfs(node):
            if condition(node):
                result.append(node)
            for child in node.children:
                dfs(child)

        dfs(root)
        return result

#----------------------------------------------

#----------- communication layer --------------
import paho.mqtt.client as mqtt
import json

class MQTTHandler:
    def __init__(self, processor, broker='localhost', port=1883):
        self.processor = processor
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(broker, port, 60)

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe("tree/update")

    def on_message(self, client, userdata, msg):
        payload = json.loads(msg.payload)
        action = payload.get('action')

        if action == 'update_node':
            tree_id = payload['tree_id']
            node_id = payload['node_id']
            data = payload['data']
            success = self.processor.update_node_data(tree_id, node_id, data)
            print(f"Update Node: {success}")

    def start(self):
        self.client.loop_start()

#----------------------------------------------

#------------- controller layer ---------------
class Coordinator:
    def __init__(self, processor, mqtt_handler):
        self.processor = processor
        self.mqtt_handler = mqtt_handler

    def process_condition(self, tree_id, condition):
        # ประมวลผล node ตามเงื่อนไข
        result = self.processor.process_tree(tree_id, condition)
        print("Nodes matched condition:", result)

    def run(self):
        # เริ่มต้นการทำงาน
        self.mqtt_handler.start()
    
#----------------------------------------------

if __name__ == '__main__':
    # ตัวอย่างการใช้งาน 

    # สร้างต้นไม้ตัวอย่าง
    forest = Forest()
    tree1 = TreeNode(1, "Root")
    tree1.add_child(TreeNode(2, "Child A"))
    tree1.add_child(TreeNode(3, "Child B"))
    forest.add_tree("tree1", tree1)

    # เราใช้คำว่า processor เพราะมันมีหน้าที่ทั้งเปลี่ยนแปลงค่าของ scope และ ประมวลผลคิดคำนวณ
    # สร้าง Manager และ MQTT Handler (ทั้งหมดยังไม่เริ่มการทำงานเป็นการตั้งค่าหน้าที่ไว้เท่านั้น)
        #manager จะทำงานใน scope ไหน (ในที่นี้คือทั้ง forest)
        #จะให้ mqttHandler รับข้อมูลมาประมวลผลของ manager scope ไหน
        #coordinator ไหนจะรับหน้าที่ เริ่มการทำงานของ forest , แลำควมคุมการประมวลผลและจัดการ (เพื่อนำไปใช้ในอนาคต)
    forest_manager = TreeManager(forest) #manager จัดการ forest นี้
    mqtt_handler = MQTTHandler(forest_manager) #mqtthandler มีหน้าที่สั่งการ manager ไหน
    coordinator = Coordinator(forest_manager,mqtt_handler) # coordinator ไหนคุมการเริ่มทำงานและมีอำนาจสั่งการ manager

    coordinator.run() #เริ่มการทำงานทุกอย่าง

    # ตัวอย่างการประมวลผลเงื่อนไข ด้วย coordinator
    def condition(node):
        return "Child" in node.data  # ค้นหา node ที่มีคำว่า "Child"

    coordinator.process_condition("tree1", condition)