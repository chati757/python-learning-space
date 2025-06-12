def func1():
    try:
        raise Exception()

    except Exception:
        print('in exception')
        exit()

try:
    func1()
    print('do another')

except Exception:
    print('in exception2')

except:
    print('in except') #เพราะ exit เทำให้มาเข้า except นี้