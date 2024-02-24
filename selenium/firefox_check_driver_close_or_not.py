import selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import bs4 as bs
import time
import pandas as pd
import psutil #ใช้ตรวจสถานะ process id
import subprocess #ใช้ kill process id

'''
example proc_list : [6768, 6768, 6768, 6768, 6768, 6768, 6768, 6768, 6768, 14492, 14492, 14492, 14492, 17720, 17720, 17828, 17828]
เวลา kill pid พวกนี้ไม่จำเป็นต้องสั่ง kill ทั้งหมด kill แต่ตัวแรกที่ตรวจเจอตัวอื่นจะปิดตัวเองโดยอัตโนมัติ(ถ้า Proccess มันเกี่ยวข้องกัน)
ดังนั้นในตัวอย่าง kill_zomebie_firefox_browser จึงไม่เก็บ list และ kill แค่ 6768 กับ 14492
เท่านั้นเพราะเมื่อ kill 6768 (6768, 6768, 6768, 6768, 6768, 6768, 6768, 6768 จะหาย) และ
เมื่อ kill 14492 (14492, 14492, 14492, 17720, 17720, 17828, 17828 ก็จะหายเช่นกัน)
'''
def get_firefox_browser_pid_all_webdriver():
    proc_list = []
    for proc in psutil.process_iter(['pid', 'name']):
        if 'firefox' in proc.info['name'].lower():  # หรือเปลี่ยนเป็นชื่อเบราว์เซอร์ที่คุณใช้
            try:
                connections = proc.connections()
                for conn in connections:
                    if conn.status == 'ESTABLISHED':
                        # ตรวจสอบว่าข้อมูลที่เชื่อมต่อนั้นเป็นของ WebDriver หรือไม่
                        if "geckodriver" in conn.raddr[0] or "127.0.0.1" in conn.raddr[0]:
                            proc_list.append(proc.pid)
            except psutil.AccessDenied:
                pass
    return proc_list

def close_with_pid(pid):
    psutil.Process(pid).terminate()

#check speed
start_time = time.time()

firefox_options = webdriver.FirefoxOptions()
#firefox_options.add_argument('-headless') #ใช้ mode headless ช่วยเพิ่มความเร็ว
#กรณีต้องการ set preference
#firefox_options.set_preference("browser.download.folderList", 2)

#set useragent
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0'
firefox_options.set_preference("general.useragent.override", user_agent)

#set driver
firefox_service = Service('P:\project w\python-learning-space\selenium\geckodriver.exe')
driver = webdriver.Firefox(service=firefox_service,options=firefox_options)
print(driver.service.process.pid)

#set dafault waiting element
wait = WebDriverWait(driver, 50) #ประกาศก่อน request เพื่อใช้หลัง request ด้วย wait.until...

#test working
driver.get("https://tradingeconomics.com/commodity/crude-oil")
print('waiting..')
print(f'speed tag : {(time.time() - start_time):6f}')
element = wait.until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#aspnetForm > div.container > div > div.col-xl-8.col-lg-8 > div.table-responsive.markets2.market-border > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2)'))
)

print('delaying')
time.sleep(10)
print('ok')
    
try: 
    driver.current_url
    print("WebDriver is still active.")
except selenium.common.exceptions.InvalidSessionIdException:
    print("WebDriver has been closed.")

print('check process before close')
pid = driver.service.process.pid
print(psutil.pid_exists(pid))#True
print('check browser')
print(get_firefox_browser_pid_all_webdriver())
import pdb;pdb.set_trace()
driver.close()
print('afterclose')

try: 
    driver.current_url
    print("WebDriver is still active.")
except selenium.common.exceptions.InvalidSessionIdException:
    print("WebDriver has been closed.")#True

print('check process after close')
print(psutil.pid_exists(pid))#True

driver.quit()
print('check process after close')
print(psutil.pid_exists(pid))#False