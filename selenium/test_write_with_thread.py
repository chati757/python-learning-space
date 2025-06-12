import threading
import configparser


class somecls(threading.Thread):
    def __init__(self):
        super(somecls,self).__init__()
        self.config = configparser.RawConfigParser()

    def run(self):
        self.delconfig(14316)
        
    def delconfig(self,sector):
        print('delconfig running')
        self.config.read(f'./webdriver.cfg')
        print(str(sector) in self.config)
        if str(sector) in self.config:
            del self.config[str(sector)]
            with open('./webdriver.cfg','w') as configfile:
                self.config.write(configfile)

if __name__=='__main__':
    sc = somecls()
    sc.start()
    pass