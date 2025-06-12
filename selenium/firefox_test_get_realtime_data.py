import selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import bs4 as bs
import time
import pandas as pd

#check speed
start_time = time.time()

firefox_options = webdriver.FirefoxOptions()
#firefox_options.add_argument('-headless') #ใช้ mode headless ช่วยเพิ่มความเร็ว
#กรณีต้องการ set preference
firefox_options.set_preference("browser.tabs.unloadOnLowMemory", False)

#set useragent
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0'
firefox_options.set_preference("general.useragent.override", user_agent)

#set driver
firefox_service = Service('P:\project w\python-learning-space\selenium\geckodriver.exe')
driver = webdriver.Firefox(service=firefox_service,options=firefox_options)

#set dafault waiting element
wait = WebDriverWait(driver, 50) #ประกาศก่อน request เพื่อใช้หลัง request ด้วย wait.until...

#working
driver.get("https://tradingeconomics.com/crypto")
print('waiting..')
print(f'speed tag : {(time.time() - start_time):6f}')
try:
    element = wait.until(EC.text_to_be_present_in_element((By.XPATH, "html/body/form/div[5]/div/div[1]/div[5]/div/div/table/tbody/tr[1]/td[2]")))
    print('can get element')
    print(element[0].text)
    print('waiting change')
    # กำหนด innerText ของ element ในครั้งแรกที่รอ
    initial_text = element[0].text

    # รอให้ innerText เปลี่ยนแปลง โดยที่ไม่ให้เท่ากับ initial_text
    new_element = wait.until(
        lambda driver: element[0].text != initial_text
    )
    print(new_element)
    print(element[0].text)
    print(f'speed tag : {(time.time() - start_time):6f}')
    
    #import pdb;pdb.set_trace()
except selenium.common.exceptions.TimeoutException as e:
    print('error handle')
    pass

import pdb;pdb.set_trace()
print('wait to close')
try: 
    driver.current_url
    print("WebDriver is still active.")
except selenium.common.exceptions.InvalidSessionIdException:
    print("WebDriver has been closed.")
driver.close()
print('afterclose')
try: 
    driver.current_url
    print("WebDriver is still active.")
except selenium.common.exceptions.InvalidSessionIdException:
    print("WebDriver has been closed.")
