import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
import matplotlib.lines as lines
import numpy as np
import sys
import time

x = np.array([1,4,5])
y = np.array([0,0.4,-0.4])

fig = plt.figure(figsize=[6,6],dpi=100)
ax = fig.gca()
background = ax.figure.canvas.copy_from_bbox(ax.bbox)

vertical_line = ax.axvline(1,1,0,lw=1, ls='-')
vertical_line2 = ax.axvline(2,1,0,lw=1, ls='--')
vertical_line3 = ax.axvline(3,1,0,lw=1,color='r',ls='--')
plt.plot(x,y)

active = False
def on_draw(event):
    global active
    print('in draw event')
    #time.sleep(3)
    print(vertical_line.get_visible())
    '''
    if(active==False):
        active=True
        ax.figure.canvas.draw()
    '''    
    if(active==False):
        print('in')
        active=True
        vertical_line.set_visible(True) #ไม่ว่าจะวาง set_visible(False) ไว้ส่วนนี้ หรือ ส่วนท้าย ก็ไม่ทำงาน draw_idle ก็ไม่ทำงานหรือวาดใหม่ให้
        print(vertical_line.get_visible()) #แต่ค่าได้ถูก set เป็น False ไว้แล้ว
        ax.figure.canvas.draw_idle()
        vertical_line.set_visible(True)

'''
ปกติ draw event จะทำงาน 1 ครั้งในตอนแรกเมื่อเราสั่ง plt.show()
'''
ax.figure.canvas.mpl_connect('draw_event', on_draw)

def set_cross_hair_visible(visible):
    need_redraw = vertical_line.get_visible() != visible
    vertical_line.set_visible(visible)
    return need_redraw

def on_key(event):
    if(event.key=='1'):
        print('on draw key')
        ax.figure.canvas.draw() #จงใจวางสลับให้ draw ขึ้นก่อน set_cross_hair_visible(False)
        print(vertical_line.get_visible())
        set_cross_hair_visible(False) 
        
    elif(event.key=='2'):
        print('on draw idle key')
        ax.figure.canvas.draw_idle() #จงใจวางสลับให้ draw_idle ขึ้นก่อน set_cross_hair_visible(False)
        print(vertical_line.get_visible())
        set_cross_hair_visible(False)
    
    elif(event.key=='3'):
        print('on draw artist')
        vertical_line3.set_xdata(5)
        ax.draw_artist(vertical_line3)
        ax.figure.canvas.blit(ax.bbox)

    elif(event.key=='4'):
        print('restore_region')
        ax.figure.canvas.restore_region(background)
    
    elif(event.key=='5'):
        print('clear figure')
        ax.figure.clf()

    elif(event.key=='6'):
        print('pause')
        plt.pause(4)
        print('after pause')
    
    elif(event.key=='7'):
        print('set xlim')
        ax.set_xlim(0,10)
    
    elif(event.key=='8'):
        ax.figure.canvas.flush_event()

    sys.stdout.flush()

fig.canvas.mpl_connect('key_press_event',on_key)

plt.show()

'''
เมื่อเราสั่ง plt.show() การทำงาน on_draw event จะเริ่มทำงาน โดยจะทำงานเป็นจำนวน 1 ครั้ง
ซึ่งใน on_draw event state หากเราสั่งคำสั่งเกี่ยวกับการแสดงผลใน เช่นการ 


แต่หากเราสั่งให้ draw_idle ทำงานในส่วน event อื่นๆที่ไม่ใช่ on draw event (ในที่นี้คือ key_press_event) 
คำสั่ง draw_idle จะทำงานได้ปกติ โดยการทำงานของ draw_idle คือการวางตารางงานการวาดไว้ในในช่วงที่ว่างจาก process อื่นๆบน cycle 
control แล้วจริงๆเท่านั้นแล้วจึงจะทำการ draw ก่อนที่จะทำงานใน GUI event loop ตามปกติ
draw_idle ยังมีส่วนการรอ setting อื่นๆถูก set จนหมดก่อนตนเองจะทำงานในแต่ละ cycle ที่ทำงานอีกด้วย เช่น
สั่ง "ax.figure.canvas.draw_idle()" แล้วค่อยสั่ง "set_cross_hair_visible(False)" draw_idle จะรอ "set_cross_hair_visible(False)" run จบ
ก่อนจึงจะทำการ draw
ดังนั้นการสั่ง draw_idle ต้องพึงระวังว่ามันอาจไม่ได้ทำงานตามลำดับอย่างที่เราเขียนไว้เสมอไป หนำซ้ำ หากเอา draw_idle ไปวางใน บาง event (Ex.on_draw) อาจถูกเพิกเฉยได้อีกด้วย
ปล.(การสั่ง draw_idle มีส่วนทำให้วนกลับไป on draw อีกครั้ง)
'''