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
การตรวจ process id ทำได้ 2 แบบ 
แบบแรก ให้เรียกโดยใช้ filter proc.info['name'].lower() เป็น firefox connection status established และ connection address เป็น geckodriver หรือเป็น 127.0.0.1
ซึ่งเป็นตัวบ่งบอกว่า browser ดังกล่าวมีการเชื่อมต่อกับ web driver
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

'''
แบบที่สอง ตรวจสอบจาก ppid (ย่อมาจาก Parent Process ID) การตรวจนี้จะต้องมี driver_pid อ้างอิงเพื่อดูว่า web browser นั้นมี ppid เป็น driver_pid หรือไม่
'''
def find_browser_pid(driver_pid):
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.ppid() == driver_pid and 'chrome' in proc.name().lower():
                return proc.pid
            elif proc.ppid() == driver_pid and 'firefox' in proc.name().lower():
                return proc.pid
        except psutil.NoSuchProcess:
            pass
    return None

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

import pdb;pdb.set_trace()

#tab1
driver.execute_script("window.open('about:blank', 'tab1')")
driver.switch_to.window("tab1")
driver.get("https://tradingeconomics.com/commodity/crude-oil")