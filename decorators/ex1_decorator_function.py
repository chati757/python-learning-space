def decorator_function(original_function):
    print('decorator func')
    print('  do another before call '+original_function.__name__+'()')
    def wrap_function(*arg):
        print('  wrap func')
        print('    check arg of '+original_function.__name__+'()')
        print('    call original function '+original_function.__name__+'()')
        return original_function(*arg)
    return wrap_function

print('before first')
'''
@decorator_function เป็นการเรียกทำงาน function แบบนึงแต่ไม่ได้ return ใดๆ
'''
@decorator_function #decorator_display = decorator_function(original_function) ;decorator_deisplay()
def display(name,age):
    print('in display function')
    print('in display',name,age)

print('\ncall first')
print(display) #<function decorator_function.<locals>.wrap_function at 0x000002724369BCA8>
print('\ncall second')
display('name','age')

print('\nsecond type : no @decorator_function')
df = decorator_function(display)
print(df)
print('next')

'''
เหตุผลว่าทำไม call wrap func 2 ครั้ง
'''
df('name','age')
'''
dec(display('name','age')) -> wrap2
dec(warp2) -> wrap
การทำงานจะเริ่มจาก wrap_function บรรทัดที่ 9 ถูก run 
run wrap2(warp('name','age'))
run wrap() , args=('name','age') , original=wrap2 , finally:run:warp2('name','age')
run wrap2() , args=('name','age') , original=display
เทียบเท่า diplay(wrap2(wrap('name','age'))) โดยเริ่มจากในไปนอก และ args=('name','age') ก็ถูกส่งจากในไปนอกเช่นกัน
'''