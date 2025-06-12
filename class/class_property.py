class somecls():
    def __init__(self):
        self._somevar = 'test'

    @property
    def somevar(self):
        print('somevar working do something before return self._somever')
        return self._somevar

if __name__=='__main__':
    sc = somecls()
    sc.somevar