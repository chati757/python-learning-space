class testdictcls():
    def __init__(self):
        self._dict = {}
    
    def __setitem__(self,key,value):
        print('in set item')
        self._dict[key] = value

    def __getitem__(self,key):
        print('in get item')
        return self._dict[key]

    def __contains__(self,key):
        print('in contains')
        return key in self._dict

if __name__=='__main__':
    pass
    testdict = testdictcls()
    
    import pdb;pdb.set_trace()
    
    testdict['somekey'] = 'qwerty'
    print(testdict['somekey'])
    