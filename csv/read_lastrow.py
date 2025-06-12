import csv

def read_last_line(filename):
    with open(filename, 'rb') as file:
        # ข้ามบรรทัดที่ไม่จำเป็น
        file.seek(-2, 2)
        #การอ่าน 1 char ทำให้ cursor ขยับไปทางขวา 1 ครั้งด้วย
        while file.read(1) != b'\n': #อ่าน 1 character ถ้าไม่ใช่ \n (\n ถือเป็น 1 charactor)
            file.seek(-2, 1) #ขยับ cursor จากปัจจุบันไปด้านซ้าย 2 ครั้ง
        # อ่านบรรทัดสุดท้าย
        last_line = file.readline().strip()
        return last_line.decode('utf-8')

if __name__=='__main__':
    # ใช้ฟังก์ชันเพื่ออ่านบรรทัดสุดท้าย
    #last_line = read_last_line_csv('csv_testing.csv')
    #print(last_line)

    some_line = read_last_line('csv_testing2.csv')
    print(some_line.split(','))

   
    import pdb;pdb.set_trace()
