#ref : https://matplotlib.org/stable/tutorials/advanced/blitting.html

import matplotlib.pyplot as plt
import threading
import numpy as np
import time

def on_close(event):
    print('onclose')
    print(f'{event.canvas.figure.number}')
    plt.close(event.canvas.figure.number)

x = np.linspace(0, 2 * np.pi, 100)

fig, ax = plt.subplots()
(ln,) = ax.plot(x, np.sin(x))
fig2, ax2 = plt.subplots()
(ln2,) = ax2.plot(x, np.sin(x))
plt.pause(0.1)
print('show1')

fig.canvas.mpl_connect('close_event', on_close)
fig2.canvas.mpl_connect('close_event', on_close)
plt.show(block=False)

def figure_show_thread():
    while plt.get_fignums():
        #print(plt.get_fignums())
        for f in plt.get_fignums():
            print(f)
            plt.figure(f).canvas.flush_events()
            #print(plt.figure(f).get_visible())
            if(plt.get_fignums()==[]):
                break
            #print(f'in for {f}')

figure_show_thread()

while True:
    print('do another')
    time.sleep(1)

'''
code มีปัญญาเวลากดปิด เพราะบางครั้ง plt.get_fignums() id ค้างแม้ปิดไปแล้วยังปรากฏใน fignums
แม้จะลองใช้ thread ในวิธีอื่นๆ แต่ matplotlib มักทำงานบน thread ทำให้ thread อาจตีกัน ดังนั้นการเลี่ยงไปใช้ processing ใหม่เลยอาจเข้าท่ากว่า
เลี่ยงไปใช้ multi processing แทน ดูที่ (9_0_multiple_process_plot.py)
'''