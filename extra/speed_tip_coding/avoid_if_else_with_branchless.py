'''
ในกรณีใช้ branch อาจเร็วกว่าทำ branchless ถ้า function เป็นเงื่อนไขเดี่ยว
แต่ branchless จะเร็วกว่ามากถ้ามันไปอยู่ใน loop และ ยิ่งต้องใช้ and ในเงื่อนไข
Ex.พวก loop if แนะนำให้ลองใช้ branchless แทน branch
'''
def branch(a,b):
    if(a<b):
        return a
    else:
        return b

def branchless(a,b):
    return a*(a<b)+b*(a>=b)

if __name__=='__main__':
    print(branch(1,2))
    print(branchless(1,2))
    