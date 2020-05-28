#! /usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig=plt.figure(figsize=(8,6))
plt.title('scatter')

x = np.random.rand(40)
y = np.random.rand(40)

scat = plt.scatter([], [], color='green', marker='o', s=7, edgecolor='black', alpha=0.5)

def init():
    scat.set_offsets([])
    return scat

def update(i):
    data = np.hstack((x[:i,np.newaxis], y[:i, np.newaxis]))
    scat.set_offsets(data)
    return scat

ani = animation.FuncAnimation(fig, update, frames=len(x)+1, init_func=init, interval=200, repeat=False)
plt.show()
