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
    phonbuak = await task
    print('ได้ผลบวก %s'%phonbuak)
    print('สิ้นสุด main')

'''
ขณะ run co-routine main() มีการ run task ด้วย await ก่อนจบ main() ; task จะไม่ทำงานหลังจบ main() 
'''

maincoru = main()
asyncio.run(maincoru)