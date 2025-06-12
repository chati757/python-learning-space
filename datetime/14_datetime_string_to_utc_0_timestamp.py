from datetime import datetime, timezone
from zoneinfo import ZoneInfo

# สมมุติว่า input string ไม่มี timezone (เป็น local time)
datetime_str = "2025-06-02 14:30:00"

# 1. แปลง string เป็น datetime object (ยังไม่มี timezone)
dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")

# 2. สมมุติว่าเวลานี้เป็นเวลาท้องถิ่น (เช่น Asia/Bangkok, UTC+7)
#    ต้องแนบ timezone ก่อน (ใช้ zoneinfo ได้ใน Python 3.9+)
dt_local = dt.replace(tzinfo=ZoneInfo("Asia/Bangkok"))

# 3. แปลงเป็น UTC
dt_utc = dt_local.astimezone(timezone.utc)

# 4. แปลงเป็น timestamp
utc_timestamp = dt_utc.timestamp()

print("Original:", dt)
print("With timezone:", dt_local)
print("UTC time:", dt_utc)
print("UTC timestamp:", utc_timestamp)
