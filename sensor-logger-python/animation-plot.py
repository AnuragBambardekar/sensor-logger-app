""" import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def update_line(num, data, line):
    line.set_data(data[..., :num])
    return line,

fig1 = plt.figure()

data = np.random.rand(2, 25)
l, = plt.plot([], [], 'r-')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel('x')
plt.title('test')
line_ani = animation.FuncAnimation(fig1, update_line, 25, fargs=(data, l),
                                   interval=50, blit=True)

plt.show() """

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 6*np.pi, 100)
y = np.sin(x)

x1 = np.linspace(0, 6*np.pi, 100)
y1 = np.sin(x)

x2 = np.linspace(0, 6*np.pi, 100)
y2 = np.sin(x)

# You probably won't need this if you're embedding things in a tkinter plot...
plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x, y, 'r-') # Returns a tuple of line objects, thus the comma
line2, = ax.plot(x1, y1, 'b') # Returns a tuple of line objects, thus the comma
line3, = ax.plot(x2, y2, 'c') # Returns a tuple of line objects, thus the comma

for phase in np.linspace(0, 10*np.pi, 500):
    line1.set_ydata(np.sin(x + phase))
    line2.set_ydata(np.sin(x1 + phase*0.4))
    line3.set_ydata(np.sin(x1 + phase*2))
    fig.canvas.draw()
    fig.canvas.flush_events()