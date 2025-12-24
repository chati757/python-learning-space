import plotext as plt

l, p = 200, 2
y = plt.sin(length = l, periods = p)
plt.plot(y, label = "My Signal1",marker='hd',color=9)
y2 = plt.sin(phase = -1)
plt.plot(y2 , label = "My Signal2",marker='braille',color=2)

plt.text("test",(l + l//10),0,background='white',color='black')
plt.text("test",(l + l//10),0.09,background='white',color='red')

plt.plotsize(100, 30)
plt.title('Some Smart Title')
plt.ticks_color('yellow')
plt.ticks_style('bold')
plt.xlim(-l//10, (l + l//10)+5)
plt.ylim(-1.5, 1.5)
xticks = [l * i / (2 * p)  for i in range(2 * p + 1)]
xlabels = [str(i) + "π" for i in range(2 * p + 1)]
plt.xticks(xticks, xlabels)
plt.yfrequency(5)
plt.canvas_color((0,43,54))
plt.axes_color((0,43,54))
plt.xlabel('Time','bottom')
plt.ylabel('Mov','top')
plt.show()
