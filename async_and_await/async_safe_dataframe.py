import asyncio
import pandas as pd

class AsyncDFWrapper:
    def __init__(self, df=None):
        self._df = df or pd.DataFrame()
        self._lock = asyncio.Lock()

    async def update(self, func, *args, **kwargs):
        async with self._lock:
            func(self._df, *args, **kwargs)
            return self

    @property
    def df(self):
        return self._df.copy()

# ---------------- ตัวอย่าง ----------------
async def main():
    df_wrapper = AsyncDFWrapper(pd.DataFrame({"a":[1,2,3], "b":[4,5,6]}))

    # ฟังก์ชันแก้ไข DataFrame แบบปกติ
    def modify(df):
        df.loc[df['a'] > 1, 'b'] = 99  # ใช้ pandas syntax ปกติเลย

    # เรียก update
    await df_wrapper.update(modify)

    print(df_wrapper.df)

asyncio.run(main())
