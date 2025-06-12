from datetime import datetime, timezone

# ได้เวลาในปัจจุบันแบบ UTC
utc_now = datetime.now(timezone.utc)

# แปลงเป็น timestamp (float วินาทีตั้งแต่ epoch)
utc_timestamp = utc_now.timestamp()

print("UTC time:", utc_now)
print("UTC timestamp:", utc_timestamp)
