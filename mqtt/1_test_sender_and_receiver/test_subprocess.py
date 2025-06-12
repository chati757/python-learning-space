import subprocess

'''
การ สั่ง mosquitto_passwd ผ่าน subprocess จำเป็นต้องใช้ -b ในการทำงานแบบ batch mode
หากไม่ได้สั่งด้วย batch mode จะทำให้การทำงานผิดพลาด
โดยความผิดผลาดอาจเกิดจาก ผู้พัฒนาได้เขียนป้องกันไว้ โดยอาจเป็นไปได้ที่ไฟล์ .exe หรือโปรแกรมใด ๆ อย่าง mosquitto_passwd 
ที่ถูกเรียกใช้งานสามารถตรวจสอบและรับรู้ได้ว่ามันถูกเรียกผ่าน subprocess ของ Python และทำการ throw error
เพราะต้องการให้ทำงานบนคอนโซลแบบปกติ (interactive console)(tty) โดยวิธีการที่ใช้มีหลากหลาย ซึ่งอาจรวมถึง:

1.การตรวจสอบการเชื่อมต่อของ stdin, stdout, และ stderr:
โปรแกรมสามารถตรวจสอบว่ามีการเชื่อมต่ออะไรกับ stdin, stdout, และ stderr โดยการตรวจสอบว่าพวกมันเชื่อมต่อกับ terminal (TTY) หรือไม่
เมื่อเรียกจาก subprocess โดยทั่วไป stdin, stdout, และ stderr อาจถูกเปลี่ยนเป็น pipe แทนที่จะเป็น terminal ซึ่งทำให้โปรแกรมสามารถตรวจจับได้

3.อื่นๆ
'''

# เรียกใช้ subprocess กับสคริปต์
process = subprocess.Popen(
    ['mosquitto_passwd','-b','pw_file','testuser','testpass'], 
    stdin=subprocess.PIPE, 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE, 
    text=True
)

# อ่าน error ที่เกิดขึ้น (ถ้ามี)
error_output = process.stderr.read()
if error_output:
    print("Error encountered:", error_output.strip())
else:
    print(process.stdout.read())


# รอให้ subprocess สิ้นสุดการทำงาน
process.wait()