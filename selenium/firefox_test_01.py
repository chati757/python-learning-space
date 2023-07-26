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
firefox_options.add_argument('-headless')
#กรณีต้องการ set preference
#firefox_options.set_preference("browser.download.folderList", 2)
#set useragent
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0'
firefox_options.set_preference("general.useragent.override", user_agent)
#set driver
firefox_service = Service('P:\project w\python-learning-space\selenium\geckodriver.exe')
driver = webdriver.Firefox(service=firefox_service,options=firefox_options)
#dafault waiting element
wait = WebDriverWait(driver, 20)

#working
driver.get("https://www.thai-cac.com/who-we-are/our-members/")
print('waiting..')
print(f'speed tag : {(time.time() - start_time):6f}')
try:
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.member-call > tr:nth-child(1) > td:nth-child(2)')))
    print(f'speed tag : {(time.time() - start_time):6f}')
    buff_dataframe = []
    test_source = bs.BeautifulSoup(driver.page_source,'lxml')
    #print(test_source.select('.member-call > tr > td:nth-of-type(1)')[6].get_text())
    for tag in test_source.select('.member-call > tr'):
        buff_symbol = tag.select('td:nth-of-type(1)')[0].get_text()
        if(buff_symbol!=''):
            buff_data = {
                'symbol':buff_symbol,
                'name':tag.select('td:nth-of-type(2)')[0].get_text(),
                'status':tag.select('td:nth-of-type(3)')[0].get_text(),
                'since':tag.select('td:nth-of-type(4)')[0].get_text(),
                'expire':tag.select('td:nth-of-type(5)')[0].get_text(),
                'sector':tag.select('td:nth-of-type(6)')[0].get_text()
            }
            buff_dataframe.append(buff_data)
    
    df = pd.DataFrame(buff_dataframe)
    print(df)
    import pdb;pdb.set_trace()
except selenium.common.exceptions.TimeoutException as e:
    print('error handle')

print('wait to close')
driver.close()