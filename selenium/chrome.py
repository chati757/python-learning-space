from selenium import webdriver
import time
from selenium.webdriver.remote.remote_connection import LOGGER, logging
LOGGER.setLevel(logging.WARNING)

'''
https://chromedriver.chromium.org/downloads
โหลดมาแล้วสร้างที่อยู่สักที พร้อมกับ set path env (system level) ในที่นี้ Ex.C:\chrome_webdriver\chromedriver.exe
ทดสอบ run chromedriver.exe และ enable firewall และ permission ที่ติดทั้งหมดออก
'''
path = "C:\chrome_webdriver\chromedriver.exe"

options = webdriver.ChromeOptions();
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument('--disable-logging')
#if linux use service_log_path='/dev/null'
browser = webdriver.Chrome(executable_path=path,chrome_options=options,service_log_path='NUL')
browser.get("https://www.google.com")
time.sleep(10)
browser.close()