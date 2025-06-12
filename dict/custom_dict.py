class subscribe_dict():
    def __init__(self):
        self._dict = {}
    
    def __setitem__(self, key, value):
        print('setitem')
        self._dict[key] = value
    
    def __getitem__(self, key):
        print('getitem')
        return self._dict[key]
    
    def __delitem__(self, key):
        print('delitem')
        del self._dict[key]
    
    def __contains__(self, key):
        print('contains')
        return key in self._dict
    
    def get(self, key, default=None):
        print('get')
        return self._dict.get(key, default)
    
    def keys(self):
        print('keys')
        return list(self._dict.keys())
    
    def values(self):
        print('values')
        return list(self._dict.values())
    
    def items(self):
        print('items')
        return list(self._dict.items())

    def __repr__(self):
        print('repr')
        return str(self._dict)

    def __str__(self):
        print('str')
        return str(self._dict)

if __name__=='__main__':
    test = subscribe_dict()
    print(('a' in test)) #in __contains__
    import pdb;pdb.set_trace()