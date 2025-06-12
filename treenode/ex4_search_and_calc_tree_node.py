'''
ตัวอย่างการสร้าง function ใน treenode เพื่อใช้ค้นหา pattern ของ node ที่ต้องการและนำไปคำนวณ
'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    # Method เพื่อค้นหา node ตาม pattern และคำนวณผลรวม
    def calculate_sum_by_pattern(self, pattern):
        total_sum = 0
        if pattern in str(self.value):  # ตรวจสอบ pattern ใน value
            total_sum += self.value  # เพิ่มค่า value ของ node นี้เข้าไปในผลรวม

        # ตรวจสอบ children แบบ recursive
        for child in self.children:
            total_sum += child.calculate_sum_by_pattern(pattern)
        
        return total_sum

    # Method เพื่ออัปเดตค่าหลังจากคำนวณ
    def update_nodes_by_pattern(self, pattern, add_value):
        if pattern in str(self.value):  # ถ้า value ตรงกับ pattern
            self.value += add_value  # อัปเดตค่าของ node นี้

        # อัปเดต children แบบ recursive
        for child in self.children:
            child.update_nodes_by_pattern(pattern, add_value)


# ตัวอย่างการใช้งาน
root = TreeNode(10)
child1 = TreeNode(15)
child2 = TreeNode(20)
child3 = TreeNode(25)

root.add_child(child1)
root.add_child(child2)
child1.add_child(child3)

# คำนวณผลรวมของ node ที่มีเลข "5"
result_sum = root.calculate_sum_by_pattern("5")
print("Sum:", result_sum)  # Output: Sum: 40 (15 + 25)

# อัปเดต node ที่มีเลข "5" โดยเพิ่มค่า 10
root.update_nodes_by_pattern("5", 10)

# ตรวจสอบผลลัพธ์หลังการอัปเดต
print(child1.value)  # Output: 25
print(child3.value)  # Output: 35