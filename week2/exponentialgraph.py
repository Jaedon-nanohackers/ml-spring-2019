import numpy as np
import matplotlib.pyplot as plt
quickmaths = lambda x: x**4- 3*x**3+ x**2-3*x + 10
x= np.linspace(-2,4,100)
plt.plot(x, quickmaths(x))
plt.savefig('plottest.png')
print("finish")
