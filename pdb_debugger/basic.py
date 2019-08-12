import pdb

"""
Ex.
(l)ist แสดงตำแหน่งบรรทัดที่ pdb ชี้อยู่และบรรทัดที่อยู่รอบข้าง ประมาณ 9 บรรทัด
(n)ext ใช้ next จะไม่กระโดดเข้า function แต่จะ exec ทุกบรรทัด ใน function ต่อ 
(c)ontinue คือการสั้ง run ต่อ และจะหยุดอีกทีตอนจบโปรแกรม เว้นแต่ว่าจะไปติด break point มันจะหยุดและเข้า dubug mode อีกครั้ง 
(s)tep ใช้ step จะกระโดยเข้า function และ run step by step ก่อนจะออกมาและไปบรรทัดต่อไป
(r)eturn คล้าย step แต่หยาบกว่า เพราะจะ return ในส่วน ตอนเจอ call function ,call function, ตอนจะออกจาก function (run หมดจนถึงท้าย function) [แต่ใน main เป็น step by step]
(w)here แสดงที่อยู่ปัจจุบัน
(b)reak <line number> เป็นการตั้งค่า break point
(q)uit ออกจาก program ณ จุดที่ pdb ชี้อยู่ (*โปรแกรมหยุดทำงานไปด้วย)
"""

def test_func():
    test_val = 5
    print("in-func")
    print("run-func")
    print("end-func")


if __name__=='__main__':
    print("before debug")
    pdb.set_trace() # type help on debug mode for list of command in pdb or help <command> for see detail of command
    print("after debug") # >["""]>[--Return--]
    test_func()
    print("after function")
    print("end function")