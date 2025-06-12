from rich.traceback import install
install()

if __name__=='__main__':
    raise Exception('some error')

'''
ถ้าใช้ RichHandler(traceback=False) ควรตั้ง traceback เป็น False
'''