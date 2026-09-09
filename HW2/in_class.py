from matplotlib import pyplot as plt
import numpy as np
m = 15
n = np.arange(0, m+1)
n[0] = 1
n= 1 / np.cumprod(n)
n = np.cumsum(n)
errors = (np.e - n)**2
plt.xlabel("n")
plt.ylabel("(e - f(n))^2")
plt.plot(np.arange(0, m+1), errors)
plt.tight_layout()
plt.show()
