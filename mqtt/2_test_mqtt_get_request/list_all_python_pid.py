import psutil

def list_python_pids():
    python_pids = []
    
    # ตรวจสอบทุก process
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # ตรวจสอบชื่อ process ว่าเป็น 'python' หรือไม่
            if 'python' in proc.info['name']:
                print(f"{proc.info['name']} : {proc.info['pid']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    return python_pids

list_python_pids()