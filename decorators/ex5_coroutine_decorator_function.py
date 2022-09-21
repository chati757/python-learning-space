import asyncio


def test_dec(func):
    print(func.__name__)
    def dec(*arg):
        return func(*arg)
    return dec

async def test_task(num1,num2):
    return num1+num2

@test_dec
async def test_coru(num1,num2):
    return await test_task(num1,num2)


print(asyncio.run(test_coru(1,2)))