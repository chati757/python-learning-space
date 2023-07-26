import time
import matplotlib.pyplot as plt
import numpy as np

'''
การทำงานหลักๆภายใน plt.show()
'''
plt.ion()# เป็นการเปิด interactive mode plt.show() จะเปิดโดยค่าเริ่มต้น
print(plt.isinteractive())

fig, ax = plt.subplots()
th = np.linspace(0, 2*np.pi, 512)
ax.set_ylim(-1.5, 1.5)

ln, = ax.plot(th, np.sin(th))
print(ln)

'''
การทำงานของ event หลักๆจะเป็นการงานที่เรียกว่าเป็น GUI event (เป็นการทำงานแบบ loop เพื่อ interact ขณะ user ใช้งานอยู่ Eg.แสดงผลแกนขณะ user เลื่อน mouse ไปบนแกน , etc..)
โดยทั่วไป การสั่ง plt.show()(plt.show() ถือเป็น pack command) จะเป็นการสร้าง GUI event loop แบบ async ขึ้นมาโดยที่มีความเร็วในการ flush event สูงมาก
แต่การทำงานที่จะให้เห็นต่อไปนี้ เราจะไม่ใช้ plt.show() แต่จะลองจำลองสร้าง GUI event loop ที่เราลองแซรกการทำงานอื่นเข้าไป (เปรียบเหมือน GUI event loop ที่มีตวามเร็วต่ำ)
เพื่อเป็นการจำลองให้เห็นภาพ แบบค่อยเป็นค่อยไป โดย GUI event loop ถูกตั้ง rate การทำงานที่ 0.5 วินาที
โดยมี time.sleep เป็นตัว delay เหมือนกำลังทำงานอะไรสักอย่างเป็นเวลา 0.5 แล้วจึงตอบสนอง user ในทุกๆครั้งไป
'''
def slow_loop(N, ln):
    for j in range(N):
        print('inloop')
        time.sleep(.5)  # to simulate some work
        if(j<10):
            ln.set_color('r')
        else:
            ln.set_color('b')
        ln.figure.canvas.flush_events()

slow_loop(30, ln)

'''
โดยสรุป
plt.show() มีการทำงานคร่าวๆคือ
plt.ion()--> ondraw event --> create async GUI event loop 

การสั่ง flush_events() มีส่วนคล้าย fig.show() มากเพราะ interactive mode ไม่ได้เปิดทำงาน
จึงแสดงผลแค่ชั่วพริบเดียวแล้วหายไป
'''