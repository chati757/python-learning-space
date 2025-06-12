def re_k(a,*,b,c): #เป็นการระบุให้ ทั้ง b และ c ต้องระบุ key ถ้ามีการเรียกใช้ function แต่ a ไม่ต้องสามารถใส่ค่าได้เลยก็จะถือว่าเป็น a โดยอัตโนมัติ
    print(a)
    print(b)
    print(c)

if __name__ == '__main__':
    re_k(1,b=2,c=3) # not error
    #re_k(1,b=2,3) # error
    #re_k(1,2,c=3) # error