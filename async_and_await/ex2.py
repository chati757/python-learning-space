import asyncio
    
async def buaklek(a,b):
    c = a+b
    print('ฟังก์ชัน buaklek เริ่มทำงาน a+b=%s'%c)
    return c

async def main():
    coru = buaklek(13,10)
    task = asyncio.create_task(coru)
    print(task)
    print(type(task))
    print('สิ้นสุด main')

'''
main สิ้นสุดแล้วแต่ไม่มีการ run task , task จะ run เองหลังจบ main() ; main() คือ co-routine
'''

maincoru = main()
asyncio.run(maincoru)
print('after run asyncio.run')