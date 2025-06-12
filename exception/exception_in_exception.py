def test_except():
    try:
        raise Exception()
    except Exception:
        #เข้ามาเฉพาะส่วนนี้
        print('test_except : in exception from test_except()')
        exit() #จะทำให้ excpt ของ func_except2 ทำงาน แต่จะไม่ได้ทำให้ exception ของ func_except ทำงานไปด้วย

def func_except():
    try:
        test_except()
        print('func_except : do another')
    except Exception:
        #ส่วนนี้ไม่เข้า
        print('func_except : in except from function_except()')
    
    print('do another 2')

def func_except2():
    try:
        func_except()
        print('func_except2 : do another')
    except:
        print('func_except2 : in except from function_except2()')


if __name__=='__main__':
    func_except2()