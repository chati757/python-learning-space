import asyncio

class AsyncSafeDict:
    def __init__(self):
        self._dict = {}  # เก็บข้อมูลจริง
        self._lock = asyncio.Lock()  # ล็อกสำหรับควบคุมการเขียน

    async def set(self, key, value):
        """ล็อกและตั้งค่า key-value โดย value จะเป็น AsyncSafeDict"""
        async with self._lock:
            if isinstance(value, dict):  # ถ้า value เป็น dict
                value = await self._convert_dict_to_async_safe_dict(value)  # แปลง dict ทั้งหมดให้เป็น AsyncSafeDict
            self._dict[key] = value
            return self  # คืนค่าของ self เพื่อให้สามารถใช้งาน chain method ได้

    async def _convert_dict_to_async_safe_dict(self, dictionary):
        """แปลง dict ทั้งหมดให้เป็น AsyncSafeDict โดยแปลงค่าที่เป็น dict ให้เป็น AsyncSafeDict ด้วย"""
        async_safe_dict = AsyncSafeDict()  # สร้าง AsyncSafeDict ใหม่
        for k, v in dictionary.items():
            if isinstance(v, dict):  # ถ้าค่าของ key เป็น dict ก็แปลงให้เป็น AsyncSafeDict
                v = await self._convert_dict_to_async_safe_dict(v)
            await async_safe_dict.set(k, v)  # ตั้งค่าใน AsyncSafeDict
        return async_safe_dict

    async def get(self, key):
        """อ่านค่า key"""
        return self._dict.get(key)

    async def delete(self, key):
        """ล็อกและลบค่า"""
        async with self._lock:
            if key in self._dict:
                del self._dict[key]

    async def update(self, other_dict):
        """ล็อกและอัปเดตหลายค่าในครั้งเดียว โดยแปลง dict ที่มีค่าภายในเป็น AsyncSafeDict"""
        async with self._lock:
            if isinstance(other_dict, AsyncSafeDict):
                other_dict = other_dict._dict  # เข้าถึง dict ที่อยู่ใน AsyncSafeDict
                
            for key, value in other_dict.items():
                if isinstance(value, dict):  # ถ้า value เป็น dict
                    value = await self._convert_dict_to_async_safe_dict(value)  # แปลง dict ให้เป็น AsyncSafeDict
                self._dict[key] = value  # อัปเดตค่าลงใน dict ของตัวเอง
            return self  # คืนค่าของ self เพื่อให้สามารถใช้งาน chain method ได้

    def __repr__(self):
        """เพื่อดูค่าปัจจุบันของ dict"""
        return f"{self._dict}"


async def main():
    safe_dict = AsyncSafeDict()

    # ตั้งค่า key "a" เป็น AsyncSafeDict แทน dict
    await safe_dict.set("a", {"x": 1, "y": 2, "z": {"inner_key": 100}})
    print("Set 'a':", safe_dict)

    # อ่านค่าของ "a"
    value = await safe_dict.get("a")
    print("Get 'a':", await value.get('z'))

    # อ่านค่าของ "z" ภายใน 'a' ซึ่งเป็น AsyncSafeDict
    inner_value = await value.get("z")
    print("Get 'z' inside 'a':", await inner_value.get("inner_key"))

    print(type(inner_value))

    # ลบค่า key "a"
    await safe_dict.delete("a")
    print("Deleted 'a':", safe_dict)

    print(await safe_dict.get("a"))


# รันตัวอย่าง
asyncio.run(main())
