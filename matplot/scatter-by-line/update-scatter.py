#! /usr/bin/env python3

import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig=plt.figure(figsize=(8,6))
plt.title('scatter')

x = 0
y = 0

plt.ion()
while True:
    try:
        line = input()
        data = line.split(' ')
        plt.scatter(int(data[0]), int(data[1]), color='green', marker='o', s=2, edgecolor='black', alpha=0.5)
        print(plt.pause(0.1))
    except EOFError:
        break

plt.ioff()
plt.show()
