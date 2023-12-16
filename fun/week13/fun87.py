# plot

import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 2*np.pi, 1000)
y = np.sin(x)

plt.plot(x, y)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine function')

plt.show()

