def decorator_function(original_function):
    print('decorator func')
    print('  do another before call '+original_function.__name__+'()')
    def wrap_function():
        print('  wrap func')
        print('    call original function '+original_function.__name__+'()')
        return original_function()
    return wrap_function

print('before first')
def display():
    print('in display function')


print('\nsecond type : no @decorator_function')
df = decorator_function(decorator_function(display))
print('next')
#print(df)
#call warp_function 2 time because @decorator_function was declared
'''
เหตุผลว่าทำไม เรียก df() แล้ว call wrap func 2 ครั้ง
ครั้งแรก (เริ่มจาก function decorator_function รอบนอกก่อน) function name ของ decorator_function(display) คือ wrap
ครั้งสอง display function name ของ display คือ display
'''
#df() #call warp_function 2 time first time : wrap_function() and second time : wrap_function(display(*arg))
'''
df ทำในวงเล็บ > ทำนอกวงเล็บ
df() ทำนอกวงเล็บ > รอทำใน > เจอวงเล็บจาก df() > ทำใน
'''