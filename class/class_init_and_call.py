
class test:
    def __init__(self,symbol):
        self.symbol = symbol
        self.call_from_init()

    def call_from_init(self):
        print('call from init')

    def __call__(self,symbol):
        print(f'from __call__:{symbol}')


if __name__=='__main__':
    t1 = test('testsymbol')
    t1('test2symbol')