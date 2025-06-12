from threading import Thread

'''
ตัวอย่างนี้ยังใช้งานไม่ได้เป็นเพียงการแสดง concept เชิงลึกของ thread ว่ามี idea ปรับแก้แบบนี้เท่านั้น
'''

def foo(bar):
    print('hello {0}'.format(bar))
    return "foo"

class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs, Verbose)
        self._return = None
    def run(self):
        if self._Thread__target is not None:
            self._return = self._Thread__target(*self._Thread__args,
                                                **self._Thread__kwargs)
    def join(self):
        Thread.join(self)
        return self._return

twrv = ThreadWithReturnValue(target=foo, args=('world!',))

twrv.start()
print(twrv.join())  # prints foo