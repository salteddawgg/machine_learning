
import numpy as np
from matplotlib import pyplot as plt

#just gonna add this here, jacob promised to send me the original line.py, 
# but answering 1 question he stoped responding for 10 min, 
# only to start sending me instagram reels!! 
# before answering my crazy simple question! 
#some people man

# data generator
mean = [0, 0]
cov = [[1, 0.9],
       [0.9, 1]]

rng = np.random.default_rng()
points_x, points_y = rng.multivariate_normal(mean, cov, 1000).T

#Build matrix X with an added column of 1s for the intercept
n = len(points_x)
X = np.column_stack([points_x, np.ones(n)])
y = points_y

# beta = (X^T X)^(-1) X^T y
beta = np.linalg.inv(X.T @ X) @ X.T @ y

slope = beta[0]
intercept = beta[1]


line_x = np.linspace(points_x.min(), points_x.max(), 100)
line_y = slope * line_x + intercept


plt.figure(figsize=(8, 6))
plt.scatter(points_x, points_y, color='k', alpha=0.5,)
plt.plot(line_x, line_y, color='r', linewidth=2, label=f'Best fit: y = {slope:.2f}x + {intercept:.2f}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression: Line of Best Fit')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()