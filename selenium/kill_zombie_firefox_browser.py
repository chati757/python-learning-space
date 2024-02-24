import psutil #ใช้ตรวจสถานะ process id
import subprocess #ใช้ kill process id

def get_firefox_browser_pid_all_webdriver():
    for proc in psutil.process_iter(['pid', 'name']):
        if 'firefox' in proc.info['name'].lower():  # หรือเปลี่ยนเป็นชื่อเบราว์เซอร์ที่คุณใช้
            try:
                connections = proc.connections()
                for conn in connections:
                    if conn.status == 'ESTABLISHED':
                        # ตรวจสอบว่าข้อมูลที่เชื่อมต่อนั้นเป็นของ WebDriver หรือไม่
                        if "geckodriver" in conn.raddr[0] or "127.0.0.1" in conn.raddr[0]:
                            return proc.pid
            except psutil.AccessDenied:
                pass
    return False

if __name__=='__main__':
    while pid := get_firefox_browser_pid_all_webdriver():
        print(f'terminate:{pid}')
        psutil.Process(pid).terminate()