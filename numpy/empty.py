import numpy as np

'''
#create empty numpy arr
'''
test1 = np.empty((0,),dtype=np.int)
print(test1[0])

'''
#create array by shape
จะสังเกตุเห็นบางครั้งติดตัวเลขมาด้วย ทาง numpy บอกว่าเป็นเพราะเป็นการสร้างที่เร็วจัดๆ เลยไม่สนว่าด้านในจะมีอะไร ว่ากันว่าเร็วกว่าติด 0 
และแนะนำให้ให้ผู้ใช้ไปเปลี่ยนเลขภายในกันเอาเอง และให้ระวังเพราะค่าอาจไม่ใช้ 0 แต่แรก
'''
test2 = np.empty((2,4),dtype=np.int)
print(test2)