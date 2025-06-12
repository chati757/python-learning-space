import tempfile

'''
tempfile นี้ถ้าเป็น window จะเก็บไว้ที่ 
C:\Users\<username>\AppData\Local\Temp\

ถ้าเป็น linux จะเก็บไว้ที่
/tmp/

ส่วน filename ระบบจะ gen เองแบบ auto

การตั้ง delete = True มีผลให้ file ถูกลบเมื่อการทำงานออกจาก with tempfile.NamedTemporaryFile
'''

with tempfile.NamedTemporaryFile("w+", delete=True, suffix=".conf") as temp_config:
    temp_config.write("some data")
    temp_config_path = temp_config.name

