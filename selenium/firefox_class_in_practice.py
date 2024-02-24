import selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import psutil #ใช้ตรวจสถานะ process id
import subprocess #ใช้ kill process id
import configparser

# Writing our configuration file to 'example.cfg'
with open('test.ini','w') as configfile:
    config.write(configfile)

class firefox_selenium_driver():
    def __init__(self):
        self.firefox_options = webdriver.FirefoxOptions()
        #self.firefox_options.add_argument('-headless')
        self.firefox_options.set_preference("browser.tabs.unloadOnLowMemory", False)#คล้าย AutomaticTabDiscarding ใน chromium
        self.firefox_options.set_preference("browser.tabs.remote.autostart", True)
        #set useragent
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0'
        self.firefox_options.set_preference("general.useragent.override", user_agent)
        #set driver
        firefox_service = Service('P:\project w\python-learning-space\selenium\geckodriver.exe')
        self.driver = webdriver.Firefox(service=firefox_service,options=firefox_options)

        #regist master(web driver) and slave(web browser) pid
        #master is #driver.service.process.pid
        self.webdriver_register_path = ''
        self.config = configparser.RawConfigParser()
        self.slave_browser_pid = self.get_slave_browser()
        self.clear_zombie_webbrowser()
        self.regist_config(self.driver.service.process.pid,'slave_browser_id',self.slave_browser_pid)
        
    def get_slave_browser(self,driver_pid):
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if proc.ppid() == driver_pid and 'firefox' in proc.name().lower():
                    return proc.pid
            except psutil.NoSuchProcess:
                pass
        return None

    def clear_zombie_webbrowser(self):
        self.config.read(f'{self.webdriver_register_path}/webdriver.cfg')
        old_slave_brower_pid = config.get(self.driver.service.process.pid,'slave_browser_id')
        if(old_slave_brower_pid.isnumeric()):
            print(f'{self.driver.service.process.pid}:clear_zombie_webbrowser:terminate:{old_slave_brower_pid}')
            psutil.Process(int(old_slave_brower_pid)).terminate()

    def regist_config(self,sector,name,val):
        self.config.add_section(sector)
        self.config.set(sector,name,val)
        with open(f'{self.webdriver_register_path}/webdriver.cfg','w') as configfile:
            self.config.write(configfile)
        