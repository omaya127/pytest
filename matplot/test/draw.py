#! /usr/bin/env python3

from threading import Thread
import matplotlib.pyplot as plt
import matplotlib.animation as animation

dots = []
poi = []

def thread_callback():
    while True:
        try:
            words = input().strip().split()
            global dots
            if len(dots) > 100:
                del dots[0:1]
            global poi
            if len(poi) > 100:
                del poi[0:1]

            dots.append([float(words[2]), float(words[3])])
            poi.append(float(words[3]))
        except KeyboardInterrupt:
            print("exit")
            exit()
        except Exception as e:
            print("lines: ", len(dots))
            print("thread exit")
            break



cm = plt.cm.get_cmap('RdYlBu') 
fig=plt.figure(figsize=(7, 7))

plt.title('scatter')
plt.axis('equal') # xy equal scale
plt.grid()

plt.xlim([-400, 400])
plt.ylim([-400, 400])

plt.xticks(range(-400, 400, 50))
plt.yticks(range(-400, 400, 50))

plt.scatter(0, 0, color='r', marker='x', s=100, edgecolor='black', alpha=0.5) # (0, 0) point
scat = plt.scatter([], [], color='green', marker='o', s=10, edgecolor='black', alpha=0.5)
#scat = plt.scatter([], [], c=poi, cmap=cm, vmin=-200, vmax=200, marker='o', s=10, edgecolor='black', alpha=0.5)

def animate(i):
    if dots:
        scat.set_offsets(dots)
    return scat

ani = animation.FuncAnimation(fig, func=animate, interval=100, repeat=False, blit=False)
thread = Thread(target=thread_callback)
thread.start()
plt.show()
thread.join()
