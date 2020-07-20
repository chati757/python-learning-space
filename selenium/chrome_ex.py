#ref : https://chromedriver.chromium.org/capabilities

from selenium import webdriver
import time
from selenium.webdriver.remote.remote_connection import LOGGER, logging
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

LOGGER.setLevel(logging.WARNING)

path = "C:\chrome_webdriver\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument('--disable-logging')
#if linux use service_log_path='/dev/null'
driver = webdriver.Chrome(executable_path=path,chrome_options=options,service_log_path='NUL')
driver.get("http://siamchart.com/stock-chart/$ICT/")
try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,"//*[starts-with(@id,'tradingview')]"))
    )
except TimeoutException:
    print('timeout inexcept')

menu_config = driver.find_element_by_css_selector('#side_menu > div > div:nth-child(3) > img')
#select_drop_down_theme = Select(driver.find_element_by_css_selector('#chart_color')) 
#driver.find_element_by_css_selector('#chart_color > option:nth-child(1)').click()

actions = ActionChains(driver)
actions.click(menu_config)
#import pdb;pdb.set_trace()
actions.perform()
#wait some element
driver.find_element_by_css_selector('#chart_color > option:nth-child(1)').click()
driver.find_element_by_css_selector('input[value="Apply"]').click()
driver.find_element_by_css_selector('span[class="ui-icon ui-icon-closethick"]').click()

time.sleep(3)
driver.switch_to_frame(driver.find_element_by_css_selector('iframe[id^="tradingview"]'))
#click indicator menu
driver.find_element_by_css_selector("#library-container > div.tv-side-toolbar > div:nth-child(4) > span:nth-child(1) > span > svg").click()
time.sleep(1)
#click remove ema default indicator
driver.find_element_by_xpath("/html/body/div[3]/div[4]/div[2]/div/div/div[1]/div/div[1]/div/a[3]/span/a[4]").click()
time.sleep(1)
#click remove moving average exponential
driver.find_element_by_xpath("/html/body/div[3]/div[4]/div[2]/div/div/div[1]/div/div[1]/div/a[3]/span/a[4]").click()
time.sleep(1)
#click remove macd
driver.find_element_by_xpath("/html/body/div[3]/div[4]/div[2]/div/div/div[1]/div/div[2]/div[2]/a/span/a[4]").click()
time.sleep(1)
#select rsi setting
driver.find_element_by_xpath("/html/body/div[3]/div[4]/div[2]/div/div/div[1]/div/div[2]/div[2]/a/span/a[3]").click()
#select period input box
driver.find_element_by_xpath("/html/body/div[4]/div[4]/div[2]/table/tbody/tr/td[2]/input").click()
#delete rsi period default value
driver.find_element_by_xpath("/html/body/div[4]/div[4]/div[2]/table/tbody/tr/td[2]/input").send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
#set new value
driver.find_element_by_xpath("/html/body/div[4]/div[4]/div[2]/table/tbody/tr/td[2]/input").send_keys(10)
time.sleep(0.5)
#select other tab of rsi setting
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[4]/div[4]/div[1]/a[2]").click()
time.sleep(0.5)
#change color
driver.find_element_by_xpath("/html/body/div[4]/div[4]/div[3]/table[1]/tbody/tr[1]/td[3]/span/input").click()
time.sleep(0.5)
driver.find_element_by_xpath("/html/body/div[5]/div[1]/table[2]/tbody/tr/td[4]/div/div").click()
#click apply
driver.find_element_by_xpath("/html/body/div[4]/div[4]/div[4]/div/a[2]").click()
time.sleep(0.5)
#close indicator menu
driver.find_element_by_xpath("/html/body/div[3]/div[1]/a").click()