import numpy as np
from matplotlib import pyplot as plt

PATH = r"C:\Users\Talon\OneDrive\Documents\GitHub\machine_learning\hw5\BostonHousing.csv"

Xy = np.genfromtxt(
    PATH,
    delimiter=",",
    skip_header=1,
    dtype=np.float64,
    converters = {3: lambda s: float(s[1:-1])}
    
    
    
)

RM, LSTAR = 5, 12
Xy = np.column_stack((Xy[:, RM], Xy[:, LSTAR], np.ones(shape=Xy.shape[0]) ,Xy[:, -1]))
test = Xy[-100:, :]
train = Xy[:-100, :]
X, y = train[:, :-1], train[:, -1]
_X, _y = test[:, :-1], test[:, -1]


lmbs = []
rmses = []
I = np.identity(X.shape[1])

for lmb in range(-9,  20):
    lmbs.append(lmb)
    beta = np.linalg.inv(X.T @ X + lmb * I) @ (X.T @ y)
    ypred = _X @ beta
    j = np.sum((ypred - _y) ** 2)
    rsmse = np.sqrt(j / len(ypred))
    rmses.append(rsmse)


best_index = np.argmin(rmses)
print(f"best lambda: {lmbs[best_index]}, RMSE: {rmses[best_index]}")

plt.plot(lmbs, rmses, color='blue', label= 'Test RMSE')
plt.title(' regression of RMSE vs lambda')
plt.ylabel('RSME')
plt.xlabel('lambda')
plt.tight_layout()
plt.show()