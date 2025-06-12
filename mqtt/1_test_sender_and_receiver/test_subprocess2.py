import subprocess

# เรียกใช้ subprocess กับสคริปต์
process = subprocess.Popen(
    ['python3','test_process.py'], 
    stdin=subprocess.PIPE, 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE, 
    text=True
)

process.stdin.write('jonh\n')
process.stdin.flush()

process.stdin.write('doe\n')
process.stdin.flush()

# อ่าน error ที่เกิดขึ้น (ถ้ามี)
error_output = process.stderr.read()
if error_output:
    print("Error encountered : ", error_output.strip())
else:
    print(f"SUCCESS : {process.stdout.read()}")

# รอให้ subprocess สิ้นสุดการทำงาน
process.wait()
print(f'error code : {process.returncode}')