สถานะของ task มี
    1.done เข้าสถานะเมื่อจบบรรทัดสุดท้ายของ async func นั้นๆแล้ว (ไม่ว่าจะมี return หรือไม่ก็ตาม) และ return control task , task นั้นจะอยู่ในสถานะ done หลัง return control และเข้าไม่นำสถานะ done ไปใส่ใน queue (ถือว่าได้รับ futureแล้ว ไม่ )
    2.ready คือสถานะของ task ที่พร้อมให้ทำงานต่อเมื่อ event loop return control และ ถึง queue
    3.pending คือสถานะของ task ที่ไม่พร้อมให้ทำงานแม้ event loop return control และ ถึง queue เพราะกำลังรอผลลัพธ์(future)อยู่
    หมายเหตุ : error มีค่าไม่ต่างจากสถานะ done เพราะถือว่ามีผลใน future object แล้ว 

สรุปการทำงานของ event loop async ที่ทำงานต่อเนื่องเป็นชั้นซ้อนกัน
case 1 : สมมุติการเริ่ม event loop ด้วย main()
async main
    print('start main')
    create task1
    print('end main')

async task1
    print('start task1')
    create task2
    print('end task1')

async task2
    print('start task2')
    do something in task2
    print('end task2')

result : 
    start main
    end main
    start task1
    end task1
logic : 
    0.event loop : ใส่ main queue
    1.event loop : เริ่มทำงาน main 
    2.event loop : เหมือนสร้าง await main ขึ้นมา (เราจะมองไม่เห็นตรงๆ) มันอยู่ภายใต้การทำงาน task = loop.create_task(main());loop.run_until_complete(task)
    
    1.1 main : ทำงานใน main 
    1.2 main : เจอ create task1 เอาไปใส่ใน queue
    1.3 main : ไม่เจอ await (ถ้าเจอจะทำเหมือน 1,2.1,2.2 แต่จะเป็นการเริ่มทำใน main แทน event loop หลักเริ่มเอง)
    1.4 main : สิ้นสุดบรรทัด main , main เตรียม แจ้งสถานะ task เป็น done (ยังไม่ถือว่า done เพราะ main ยังไม่ return control)
    2.1 event loop : เจอ await loop จาก 2. main : เกิด return control , main done ถูกแจ้งแล้ว > ค้นหาว่าใน queue มีงานไหม (ถ้าไม่เจอข้ามไป 2.3) > เจอ task1 
    2.2 event loop : ทำ task1 
    2.2.1 task1 : ทำงานใน task1
    2.2.2 task1 : เจอ create task2 เอาไปใส่ใน queue
    2.2.3 task1 : ไม่เจอ await (ถ้าเจอ ก็ไม่รอเพราะ main ไม่มี await task1)
    2.2.4 task1 : จบการทำงาน
    2.3 event loop : แจ้งว่า main เสร็จ done แล้วเตรียมปิด event loop
    2.4 event loop : ตรวจว่ามี task ค้างใน queue หรือไม่ ถ้ามี ส่ง cancel ไปบังคับปิด
    2.5 event loop : พบ task2 ค้างใน queue ไม่ถูกใช่ เพราะไม่มี await ไปเรียกมาทำงาน > แจ้ง warning ผู้ใช้
    2.6 event loop : ปิด loop
    3.จบการทำงาน

case2 : สมมุติการเริ่ม event loop ด้วย main()
async main
    print('start main')
    create task1
    await task1
    print('end main')

async task1
    print('start task1')
    create task2
    print('end task1')

async task2
    print('start task2')
    do something in task2
    print('end task2')

การ error มีหลักๆ 2 แบบที่ async มักเตือน
    1. error : Task was destroyed but it is pending! 
        1.1 เกิดจาก event loop ปิดตัวไปก่อน await จะทำงานเสร็จ
        1.2 เกิดจาก task create ไว้อยู่ใน queue แต่ event loop ปิดตัวไปก่อนจะถูกนำมาทำงาน
    2. error : Task exception was never retrieved
        2.1 เกิดจาก error ถูก raise แต่ไม่มีไครรับ หรือ handle มันได้ก่อน event loop ปิดตัว สถานะจะเหมือน done , gather จะให้ผ่าน แต่ก็จะมี warning เกิดมาทีหลัง event loop ปิดตัวเพื่อเตือนผู้ใช้

การ cancel loop ของ task ที่สร้างแบบซ้อนกัน มีลำดับแบบ inverse-cascade 
ตัวอย่าง
async def task3():
    try:
        print('start task3')
        await asyncio.sleep(5)
        print('end task3')
    except asyncio.CancelledError:
        print('task3 cancelled')
        raise

async def task2():
    try:
        print('start task2')
        t3 = asyncio.create_task(task3())
        await t3
        print('end task2')
    except asyncio.CancelledError:
        print('task2 cancelled')
        raise

async def task1():
    try:
        print('start task1')
        t2 = asyncio.create_task(task2())
        await t2
        print('end task1')
    except asyncio.CancelledError:
        print('task1 cancelled')
        raise

async def main():
    try:
        print('start main')
        t1 = asyncio.create_task(task1())
        await t1
        print('end main')
    except asyncio.CancelledError:
        print('main cancelled')

result: เมื่อทำงานและสั่ง cancel ก่อน timesleep จบ
start main
start task1
start task2
start task3
task3 cancelled
task2 cancelled
task1 cancelled
main cancelled

การ cancel เป็นแบบ inverse-cascade ดูที่ await ที่ไม่ใช่ task ตัวสุดท้ายที่ทำงานจะถูก cancel ก่อนและตัวก่อนหน้าจะถูก cancel ไปเรื่อยๆจนไปถึง main