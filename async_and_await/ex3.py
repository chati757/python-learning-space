import asyncio

async def buaklek(a,b):
    return a+b

async def main():
    phonbuak = await buaklek(13,10)
    print(type(phonbuak))
    print('ได้ผลบวก %s'%phonbuak)

asyncio.run(main())