import time 
import multiprocessing as mp

def other_func():
    print('from other func')

class graph:
    #constructor 
    #ex gender = famale < it's class variable
    def __init__(self,symbol):
        print(f'init graph {symbol}')
        #slef name < it's instance variable
        self.symbol = symbol
        #self.plot_process = mp.Process(target=self.__test_private, daemon=True) #error because private function
        #self.plot_process.start()
        self.test1()
        self.test2()

    def __test_private(self):
        print('in private')

    def test1(self):
        self.test1 = 'hello'
        data1 = 1 #use variable for this function only
        data2 = 2 #use variable for this function only
        print(data1+data2)

    def test2(self):
        print(self.test1)
    
    def plot(self):
        print(f'ploting {self.symbol}')
        other_func()

if __name__=='__main__':
    register_obj = {}
    register_obj['ptt'] = graph('ptt').plot
    register_obj['aot'] = graph('aot').plot

    income_symbol = 'ptt'
    if(income_symbol in register_obj.keys()):
        register_obj[income_symbol]()
    time.sleep(5)
