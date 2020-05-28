#! /usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.1)
y = np.sin(t*np.pi)

plt.subplot(3, 3, 1) # row, column, index
plt.plot(t, y, 'r--')
plt.ylabel('y1')
plt.xlabel('x1')

plt.subplot(3, 3, 2)
plt.plot(2*t, y, 'g.-')
plt.ylabel('y2')

plt.subplot(3, 3, 3)
plt.plot(3*t, y, 'b+-')

plt.subplot(3, 3, 4)
plt.plot(4*t, y, 'co-', label="test")
plt.legend(loc=1) #loc: quadrant, and others

plt.subplot(3, 3, 5)
plt.plot(5*t, y, 'mo-', label='test')
plt.legend(loc=2)

plt.subplot(3, 3, 6)
plt.plot(6*t, y, 'y^-', label='lw=1', linewidth=1)
plt.legend(loc=3)

plt.subplot(3, 3, 7)
plt.plot(7*t, y, 'k*-', label='lw=2', linewidth=2)
plt.legend(loc=4)

plt.subplot(3, 3, 8)
plt.plot(8*t, y, color='orange', linestyle='-', marker='x')

plt.subplot(3, 3, 9)
plt.plot(9*t, y, color='#a0a0a0', linestyle='-', marker='1')
plt.show()
