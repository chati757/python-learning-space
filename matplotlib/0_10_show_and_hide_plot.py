import matplotlib.pyplot as plt
import numpy as np 

def on_press(event):
    if event.key == '1':
        ln.set_visible(not ln.get_visible())
    elif event.key == '2':
        sc.set_visible(not sc.get_visible())
    elif event.key == '3' and len(txt_arr)>0:
        for txt in txt_arr:
            txt.set_visible(not txt.get_visible())

    fig1.canvas.draw_idle()

x = np.array([1,4,5])
y = np.array([0,0.4,-0.4])

plt.style.use("dark_background")

#plt.subplots_adjust(0.125,0.095,0.95,0.95,0.35,0.35)
fig1 = plt.figure(figsize=[6,6],dpi=100)
fig1.subplots_adjust(0.125,0.095,0.95,0.95,0.35,0.35)
fig1.canvas.mpl_connect('key_press_event', on_press)

ax1 = fig1.gca()

#test line
ln, = ax1.plot(x,y,'y')

#test scatter
sc = ax1.scatter(x,y,marker='+',s=200,color='cyan')

#test text
txt_arr = []
for i in x:
    txt_arr.append(ax1.text(x=i,y=0,s=f'txt{i}',fontsize=14))

plt.show()

