import sys
import numpy as np
import matplotlib.pyplot as plt


def on_press(event):
    print('press', event.key)
    sys.stdout.flush()
    if event.key == '1':
        visible = xl.get_visible()
        xl.set_text("test")
        xl.set_visible(True)
        print(xl)
        fig.canvas.draw_idle()
    elif event.key == '2':
        ax.cla()
        fig.canvas.draw_idle()


# Fixing random state for reproducibility
np.random.seed(19680801)

fig, ax = plt.subplots()

fig.canvas.mpl_connect('key_press_event', on_press)

ax.plot(np.random.rand(12), np.random.rand(12), 'go')
xl = ax.set_xlabel('easy come, easy go')
xl = ax.text(0.5,0.5,'')
ax.set_title('Press a key')
plt.show()