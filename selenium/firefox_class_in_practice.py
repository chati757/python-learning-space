import selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import psutil #ใช้ตรวจสถานะ process id
import subprocess #ใช้ kill process id
import configparser
import threading
import time
import pandas as pd

class firefox_selenium_driver_thread(threading.Thread):
    def __init__(self,driver_id,mode='tracking',url='',track_obj={},headless_state=False,el_not_change_timeout=60,intry=5):
        #using init of class threading.Thread
        super(firefox_selenium_driver_thread,self).__init__()
        self.setDaemon(True)

        self.firefox_options = webdriver.FirefoxOptions()
        
        if(headless_state==True):
            self.firefox_options.add_argument('-headless')
        
        self.firefox_options.set_preference("browser.tabs.unloadOnLowMemory", False)#คล้าย AutomaticTabDiscarding ใน chromium
        self.firefox_options.set_preference("browser.tabs.remote.autostart", True)
        #set useragent
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0'
        self.firefox_options.set_preference("general.useragent.override", self.user_agent)
        #set driver
        self.firefox_service = Service('P:\project w\python-learning-space\selenium\geckodriver.exe')
        self.wait_element = None
        self.el_not_change_timeout = el_not_change_timeout
        self.intry = intry
        #regist master(web driver) and slave(web browser) pid
        #master is #driver.service.process.pid
        self.webdriver_register_path = './webdriver.cfg'
        
        if('config' not in globals()):
            global config
            config = configparser.RawConfigParser()
        
        config.read(f'{self.webdriver_register_path}')

        if('global_fsdt_track_value_changed_event' not in globals()):
            raise Exception('global_fsdt_track_value_changed_event , please ceaate and try again')

        if('response_data_series_str' not in globals()):
            raise Exception('global_response_data_series not found please create , try again')

        if('lock' not in globals()):
            global lock
            lock = threading.Lock()

        self.slave_browser_pid = None
        self.driver_id = driver_id

        if(mode not in ['tracking','handle']):
            raise Exception('mode setting error : please select tracking or handle')

        self.mode = mode
        self.url = url
        self.track_obj = track_obj
        self.handle_element_state = False
        self.element_list = []

    def run(self):
        print('running thread')
        with lock:
            self.driver = webdriver.Firefox(service=self.firefox_service,options=self.firefox_options)
        
        self.slave_browser_pid = self.get_slave_browser(self.driver.service.process.pid)
        self.clear_zombie_webbrowser()
        self.wait_element = WebDriverWait(self.driver,self.el_not_change_timeout)
        self.regist_config(self.driver.service.process.pid,'slave_browser_id',self.slave_browser_pid)
        self.keep_tracking_state = True
        
        if(self.mode=='tracking'):
            self.keep_tracking(self.track_obj)
        elif(self.mode=='handle'):
            self.keep_handle(self.track_obj)

    def get_slave_browser(self,driver_pid):
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if proc.ppid() == driver_pid and 'firefox' in proc.name().lower():
                    return proc.pid
            except psutil.NoSuchProcess:
                pass
        return None

    def clear_zombie_webbrowser(self):
        try:
            old_slave_brower_pid = config.get(self.driver.service.process.pid,'slave_browser_id')
            if(old_slave_brower_pid.isnumeric()):
                print(f'{self.driver.service.process.pid}:clear_zombie_webbrowser:terminate:{old_slave_brower_pid}')
                psutil.Process(int(old_slave_brower_pid)).terminate()
        except configparser.NoSectionError:
            pass

    def regist_config(self,sector,name,val):
        config.add_section(sector)
        config.set(sector,name,val)
        with open(f'{self.webdriver_register_path}','w') as configfile:
            config.write(configfile)

    def keep_tracking(self,track_obj):
        global global_fsdt_track_value_changed_event
        global response_data_series_str
        self.element_list = []
        try_count = 0
        while True:
            try:
                self.driver.get(self.url)
                if(try_count<self.intry):
                    for i in track_obj[len(self.element_list):]:
                        self.element_list.append(self.wait_element.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,i['selector']))))

                element_list_exist = [i for i in self.element_list if(i!=None)]
                while(len(element_list_exist)>0 and self.keep_tracking_state==True):
                    for c,element in enumerate(element_list_exist):
                        try:
                            if(response_data_series_str[track_obj[c]['col']]!=element[0].text):
                                with lock:
                                    response_data_series_str[track_obj[c]['col']] = element[0].text
                                    global_fsdt_track_value_changed_event.set()
                        except KeyError:
                            with lock:
                                #print(f'init key:{track_obj[c]["col"]},value:{element[0].text}')
                                response_data_series_str[track_obj[c]['col']] = element[0].text
                                global_fsdt_track_value_changed_event.set()
                        
                        time.sleep(5)
                            
                break

            except selenium.common.exceptions.TimeoutException as e:
                try_count+=1
                if(try_count==self.intry):
                    try:
                        response_data_series_str[track_obj[len(self.element_list)]['col']] != None
                    except KeyError:
                        with lock:
                            response_data_series_str[track_obj[len(self.element_list)]['col']] = None
                        self.element_list.append(None)
                        try_count = 0
                continue

            except Exception as e:
                try_count+=1
                if(try_count==self.intry):
                    print(f'{self.driver_id} : error : {e}')
                    break
                continue

        self.unregist_config(self.driver.service.process.pid)
        self.driver.close()
        self.driver.quit()
        
        '''
        self.driver.get(url)
        element = self.wait_element.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,el_selector)))
        self.tracking_data = element[0].text
        print('first track')
        print(self.tracking_data)
        while(self.keep_tracking_state==True):
            try:
                element_changed_state = self.wait_element.until(
                    lambda driver: element[0].text != self.tracking_data
                )
                if(element_changed_state==True):
                    print('second track')
                    self.tracking_data = element[0].text
                    print(self.tracking_data)

            except selenium.common.exceptions.TimeoutException as e:
                print(f'{self.driver.service.process.pid}:keep_tracking:timeout')
                self.driver.get(url)
                element = self.wait_element.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,el_selector)))
                self.tracking_data = element[0].text
                continue

        if(self.keep_tracking_state==False):
            self.driver.close()
            self.driver.quit()
        '''
    
    def keep_handle(self,track_obj):
        try_count = 0
        while True:
            try:
                self.driver.get(self.url)
                if(try_count<self.intry):
                    for i in track_obj[len(self.element_list):]:
                        self.element_list.append(self.wait_element.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,i['selector']))))
            
                print(self.element_list)
                self.element_list = [i for i in self.element_list if(i!=None)]
                self.handle_element_state = True
                break

            except selenium.common.exceptions.TimeoutException as e:
                try_count+=1
                if(try_count==self.intry):
                    try:
                        self.element_list[track_obj[len(self.element_list)]['col']] != None
                    except KeyError:
                        self.element_list[track_obj[len(self.element_list)]['col']] = None
                        self.element_list.append(None)
                        try_count = 0
                continue

            except Exception as e:
                try_count+=1
                if(try_count==self.intry):
                    print(f'{self.driver_id} : error : {e}')
                    break
                continue

    @property
    def get_keep_handle(self):
        return self.element_list if(self.handle_element_state==True) else []

    def unregist_config(self,sector):
        if sector in config:
            del config[sector]
            with open(f'{self.webdriver_register_path}','w') as configfile:
                config.write(configfile)
    
    def close_driver(self):
        if(self.mode=='tracking'):
            self.keep_tracking_state=False
        elif(self.mode=='handle'):
            self.keep_tracking_state=False
            self.unregist_config(self.driver.service.process.pid)
            self.driver.close()
            self.driver.quit()

'''
fsdt dict
[
    {
        driver_id:str,
        mode:str,
        url:str,
        track_obj:list[col:str,selector:str],
        headless_state:boolean,
        el_not_change_timeout:int(second)
    },
    ...
]
to listobj
[fsdt_obj1,fsdt_obj2,...]
'''
def fsdt_listdict_to_listobj(fsdt_listdict):
    for fsdt_dict in fsdt_listdict:
        if((all([
            isinstance(fsdt_dict['driver_id'],str),
            isinstance(fsdt_dict['mode'],str),
            isinstance(fsdt_dict['url'],str),
            isinstance(fsdt_dict['track_obj'],list),
            isinstance(fsdt_dict['headless_state'],bool),
            isinstance(fsdt_dict['el_not_change_timeout'],int),
            isinstance(fsdt_dict['intry'],int)
        ]))!=True):
            print('fsdt_listdict_to_listobj:type:error')
            raise Exception('type for fsdt_dict incorect')

        for i in fsdt_dict['track_obj']:
            for k,v in i.items():
                if(isinstance(k,str)!=True or isinstance(v,str)!=True):
                    print('fsdt_listdict_to_listobj:type:error')
                    raise Exception('type of track_obj key(col) or value(selector) not string')

    print('fsdt_listdict_to_listobj:check type:pass')
    buff_listobj = []
    for fsdt_dict in fsdt_listdict:
        buff_listobj.append(firefox_selenium_driver_thread(
            driver_id=fsdt_dict['driver_id'],
            mode=fsdt_dict['mode'],
            url=fsdt_dict['url'],
            track_obj=fsdt_dict['track_obj'],
            headless_state=fsdt_dict['headless_state'],
            el_not_change_timeout=fsdt_dict['el_not_change_timeout'],
            intry=fsdt_dict['intry']
        ))
    
    
    return buff_listobj

def fsdt_run_listobj(listobj):
    for i in listobj:
        i.start()

def fsdt_close_listobj(listobj):
    for i in listobj:
        i.close_driver()

def fsdt_get_obj_by_driver_id(id_listobj,listobj):
    for i in listobj:
        if(id_listobj==i.driver_id):
            return i

if(__name__=='__main__'):
    global global_fsdt_track_value_changed_event
    global_fsdt_track_value_changed_event = threading.Event()

    global response_data_series_str
    response_data_series_str = pd.Series({},dtype='object')

    '''
    #for testing handle mode
    fsdt_listobj = fsdt_listdict_to_listobj([
        {
            'driver_id':'tradingeconomics_fsdt',
            'mode':'handle',
            'url':'https://tradingeconomics.com/crypto',
            'track_obj':[
                {'col':'bitcoin','selector':".col-xl-12 > div:nth-child(7) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)"},
                {'col':'ether','selector':".col-xl-12 > div:nth-child(7) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(2)"}
            ],
            'headless_state':False,
            'el_not_change_timeout':120,
            'intry':5
        }
    ])
    '''

   
    #for testing tracking mode
    fsdt_listobj = fsdt_listdict_to_listobj([
        {
            'driver_id':'tradingeconomics_fsdt',
            'mode':'tracking',
            'url':'https://tradingeconomics.com/crypto',
            'track_obj':[
                {'col':'bitcoin','selector':".col-xl-12 > div:nth-child(7) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)"},
                {'col':'ether','selector':".col-xl-12 > div:nth-child(7) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(2)"}
            ],
            'headless_state':True,
            'el_not_change_timeout':120,
            'intry':5
        },
        {
            'driver_id':'investing_fsdt',
            'mode':'tracking',
            'url':'https://th.investing.com/crypto/bitcoin/btc-usd',
            'track_obj':[
                {'col':'bitcoin-usd','selector':'#__next > div.desktop\:relative.desktop\:bg-background-default > div.relative.flex > div.grid.flex-1.grid-cols-1.px-4.pt-5.font-sans-v2.text-\[\#232526\].antialiased.xl\:container.sm\:px-6.md\:grid-cols-\[1fr_72px\].md\:gap-6.md\:px-7.md\:pt-10.md2\:grid-cols-\[1fr_420px\].md2\:gap-8.md2\:px-8.xl\:mx-auto > div.min-w-0 > div.flex.flex-col.gap-6.md\:gap-0 > div.flex.gap-6 > div.flex-1 > div.mb-3.flex.flex-wrap.items-center.gap-x-4.gap-y-2.md\:mb-0\.5.md\:gap-6 > div.text-5xl\/9.font-bold.text-\[\#232526\].md\:text-\[42px\].md\:leading-\[60px\]'}
            ],
            'headless_state':True,
            'el_not_change_timeout':120,
            'intry':5
        }
    ])
    

    fsdt_run_listobj(fsdt_listobj)
    
    
    #for testing tracking mode
    x = 0
    while x<20:
        x+=1
        print('main : waiting')
        global_fsdt_track_value_changed_event.wait()
        print(response_data_series_str)
        global_fsdt_track_value_changed_event.clear()
        print('--------------')
    
    print('closing and quit driver')
    fsdt_close_listobj(fsdt_listobj)
    print('waiting driver close')
    
    
    time.sleep(15)
    
    #thread.join()
    import pdb;pdb.set_trace()
    print('stop')