class Atest:
    def __resolve_if_error(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                args[0].resolve_problem()  # เรียกใช้ resolve_problem() ของอ็อบเจกต์ที่ส่งผ่านเป็นอาร์กิวเมนต์
        return wrapper
        
    def resolve_problem(self):
        print("Problem resolved.")

    @__resolve_if_error
    def func_a1(self):
        # โค้ดของ func_a1 ที่อาจเกิดข้อผิดพลาด
        1 / 0  # ตัวอย่าง: การหารด้วยศูนย์ที่จะเกิดข้อผิดพลาด

    @__resolve_if_error
    def func_a2(self):
        # โค้ดของ func_a2 ที่อาจเกิดข้อผิดพลาด
        raise ValueError("An error occurred in func_a2")

# การใช้งาน
a_instance = Atest()
a_instance.func_a1()
a_instance.func_a2()