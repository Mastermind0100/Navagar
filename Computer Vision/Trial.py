import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)
y = x**2 + 2*x + 8

plt.plot(x,y)
plt.show()
