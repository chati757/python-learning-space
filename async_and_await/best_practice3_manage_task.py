import asyncio

#asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class CustomCancelledErrorMessage(BaseException):  # BaseException ใช้สำหรับ asyncio
    def __init__(self, message="Task was cancelled"):
        super().__init__(message)  # กำหนดข้อความไปที่ args[0]
        self.message = message

    def __str__(self):
        return self.message  # ทำให้ str(e) แสดงข้อความถูกต้อง

async def task1():
    test_event = asyncio.Event()
    try:
        print("Task1: Started")
        test_event.clear()
        await test_event.wait()

    except asyncio.CancelledError:
        print('task1 : cancel')
        raise CustomCancelledErrorMessage

    except Exception as e:
        print(f"Exception: {e}")
        raise 

async def main(stop_event):
    print("task main : started")
    try:
        
        #------working state--------
        asyncio.create_task(task1())
        #---------------------------

        try:
            result = await asyncio.gather(*[task for task in asyncio.all_tasks() if(task is not asyncio.current_task())])
            print('task main : report : all sub-task finished')
            print(result)
            print('task main : stand by.. [ctrl+c to exit]')
            await stop_event.wait()
        except CustomCancelledErrorMessage:
            print('cus:some sub task cancalled : close all task for safe')
        except asyncio.CancelledError:
            print('some sub task cancalled : close all task for safe')
        except Exception as e:
            print('some sub task error : close all task for safe')

        print('task main : cancel : all sub_task')
        for task in asyncio.all_tasks():
            if task is not asyncio.current_task():
                task.cancel()
                try:
                    #print(task)
                    await task
                except asyncio.CancelledError:
                    pass
        print('task main : cancelled : all task')

        print('task main : exit')
    except Exception as e:
        print(f'task main : unexpect_error : exception : {e}')

try:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    stop_event = asyncio.Event()
    loop.run_until_complete(main(stop_event))

except KeyboardInterrupt:
    print("program exited by user.")
    # Cancel the task if interrupted
    print(asyncio.all_tasks(loop))
    for task in asyncio.all_tasks(loop):
        stack = task.get_stack()[0]
        print(f'{stack.f_code.co_filename} : {stack.f_code.co_name} : {stack.f_lineno}')
        task.cancel()
        #จะ raise กลับมา หรือ รู้สถานะว่า task นั้นเสร็จถือว่าใช้ได้หมด
    loop.run_until_complete(asyncio.gather(*asyncio.all_tasks(loop),return_exceptions=True))

except Exception as e:
    print('in except')
    print(e)

finally:
    print("Cleaning up...")
    #loop.run_until_complete(asyncio.sleep(0.1))  # ให้ task ที่รันอยู่ปิดตัวก่อน
    loop.close()  # ปิด event loop อย่างปลอดภัย
    print("Event loop closed.")
