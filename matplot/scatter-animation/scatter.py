#! /usr/bin/env python3

from threading import Thread
import matplotlib.pyplot as plt
import matplotlib.animation as animation

dots = []
cnt = 0

def thread_callback():
    while True:
        try:
            words = input().strip().split()
            global dots
            dots.append([int(words[0]), int(words[1])])
            global cnt
            cnt+=1
        except KeyboardInterrupt:
            print("exit")
            exit()
        except Exception as e:
            print("lines: ", cnt)
            print("thread exit")
            break

thread = Thread(target=thread_callback)
thread.start()


fig=plt.figure(figsize=(8,6))
plt.title('scatter')
plt.grid()

plt.axis([0, 15, 0, 15])
scat = plt.scatter([], [], color='green', marker='o', s=2, edgecolor='black', alpha=0.5)

def animate(i):
    if dots:
        scat.set_offsets(dots)
    return scat

ani = animation.FuncAnimation(fig, func=animate, interval=100, repeat=False, blit=False)
plt.show()
thread.join()
