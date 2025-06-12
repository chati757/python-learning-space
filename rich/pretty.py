from rich import print
from rich.pretty import Pretty

# สร้างโหนดข้อมูล
node = Pretty({
    "name": "John",
    "age": 30,
    "city": "New York",
    "children": [
        {"name": "Alice", "age": 5},
        {"name": "Bob", "age": 8}
    ]
})

# แสดงผลต้นไม้โครงสร้าง
print(node)