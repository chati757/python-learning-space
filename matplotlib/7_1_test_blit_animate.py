#ref : https://matplotlib.org/stable/tutorials/advanced/blitting.html

import matplotlib.pyplot as plt
import numpy as np
import time

x = np.linspace(0, 2 * np.pi, 100)

fig, ax = plt.subplots()

# animated=True tells matplotlib to only draw the artist when we
# explicitly request it
(ln,) = ax.plot(x, np.sin(x), animated=True)
# make sure the window is raised, but the script keeps going
plt.show(block=False)

# stop to admire our empty window axes and ensure it is rendered at
# least once.
#
# We need to fully draw the figure at its final size on the screen
# before we continue on so that :
#  a) we have the correctly sized and drawn background to grab
#  b) we have a cached renderer so that ``ax.draw_artist`` works
# so we spin the event loop to let the backend process any pending operations

print("before first pause")
time.sleep(3)
print('pausing')
plt.pause(3) #pause is not only pause | flush chached renderer and makesure background is complate and ready to grab 
print("after first pause")
time.sleep(3)

print('init test first blit drawing')

print('first copy')
bg = fig.canvas.copy_from_bbox(fig.bbox)
print('first draw')
ax.draw_artist(ln)
print('first blit')
fig.canvas.blit(fig.bbox)
print('first flush')
fig.canvas.flush_events()

time.sleep(3)

for j in range(1,4):
    # reset the background back in the canvas state, screen unchanged
    print('restore')
    fig.canvas.restore_region(bg)
    time.sleep(1)
    # update the artist, neither the canvas state nor the screen have changed
    print('set line')
    ln.set_ydata(np.sin(x + (j / 20) * np.pi))
    ln.set_color('r')
    time.sleep(1)
    # re-render the artist, updating the canvas state, but not the screen
    print('draw on cache')
    ax.draw_artist(ln)
    time.sleep(1)
    # copy the image to the GUI state, but screen might not be changed yet
    print('bliting')
    fig.canvas.blit(fig.bbox)
    time.sleep(1)
    # flush any pending GUI events, re-painting the screen if needed
    print('flushing')
    fig.canvas.flush_events()
    time.sleep(1)
    # you can put a pause in if you want to slow things down
    # print('pause')
    # plt.pause(1)
