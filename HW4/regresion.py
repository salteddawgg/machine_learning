#The Boston house-price data of Harrison, D. and Rubinfeld, D.L. 'Hedonic
# prices and the demand for clean air', J. Environ. Economics & Management,
# vol.5, 81-102, 1978.   Used in Belsley, Kuh & Welsch, 'Regression diagnostics
# ...', Wiley, 1980.   N.B. Various transformations are used in the table on
# pages 244-261 of the latter.#

 #Variables in order:
 #CRIM     per capita crime rate by town
 #ZN       proportion of residential land zoned for lots over 25,000 sq.ft.
 #INDUS    proportion of non-retail business acres per town
 #CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
 #NOX      nitric oxides concentration (parts per 10 million)
 #RM       average number of rooms per dwelling
 #AGE      proportion of owner-occupied units built prior to 1940
 #DIS      weighted distances to five Boston employment centres
 #RAD      index of accessibility to radial highways
 #TAX      full-value property-tax rate per $10,000
 #PTRATIO  pupil-teacher ratio by town
 #B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
 #LSTAT    % lower status of the population
 #MEDV     Median value of owner-occupied homes in $1000's
#

import numpy as np
from matplotlib import pyplot as plt

data = np.loadtxt(
    'BostonHousing.csv', 
    delimiter=',', 
    skiprows=1, 
    usecols=(0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    #skiping 3 as it is just 0 and 1
)
#AI discoser, i made AI will out the rest of the graphs after doing the first two
# 0: CRIM
# plt.plot(data[:, 0], data[:, 12], 'o')
# plt.xlabel("crim")
# plt.ylabel("medv")
# plt.title("Crime Rate against Median Value")
# plt.show()

# # 1: ZN
# plt.plot(data[:, 1], data[:, 12], 'o')
# plt.xlabel("zn")
# plt.ylabel("medv")
# plt.title("Large Land Zones against Median Value")
# plt.show()

# # 2: INDUS
# plt.plot(data[:, 2], data[:, 12], 'o')
# plt.xlabel("indus")
# plt.ylabel("medv")
# plt.title("Industrial Areas against Median Value")
# plt.show()

# # 3: NOX
# plt.plot(data[:, 3], data[:, 12], 'o')
# plt.xlabel("nox")
# plt.ylabel("medv")
# plt.title("Nitric Oxide Levels against Median Value")
# plt.show()

# # 4: RM 
# plt.plot(data[:, 4], data[:, 12], 'o')
# plt.xlabel("rm")
# plt.ylabel("medv")
# plt.title("Average Number of Rooms against Median Value")
# plt.show()

# # 5: AGE
# plt.plot(data[:, 5], data[:, 12], 'o')
# plt.xlabel("age")
# plt.ylabel("medv")
# plt.title("Owner-Occupied Units against Median Value")
# plt.show()

# # 6: DIS
# plt.plot(data[:, 6], data[:, 12], 'o')
# plt.xlabel("dis")
# plt.ylabel("medv")
# plt.title("Distance to Employment Centers against Median Value")
# plt.show()

# # 7: RAD
# plt.plot(data[:, 7], data[:, 12], 'o')
# plt.xlabel("rad")
# plt.ylabel("medv")
# plt.title("Radial Highway Accessibility against Median Value")
# plt.show()

# # 8: TAX
# plt.plot(data[:, 8], data[:, 12], 'o')
# plt.xlabel("tax")
# plt.ylabel("medv")
# plt.title("Property Tax Rate against Median Value")
# plt.show()

# # 9: PTRATIO
# plt.plot(data[:, 9], data[:, 12], 'o')
# plt.xlabel("ptratio")
# plt.ylabel("medv")
# plt.title("Pupil-Teacher Ratio against Median Value")
# plt.show()

# # 10: B
# plt.plot(data[:, 10], data[:, 12], 'o')
# plt.xlabel("b")
# plt.ylabel("medv")
# plt.title("Proportion of Black Residents against Median Value")
# plt.show()

# # 11: LSTAT 
# plt.plot(data[:, 11], data[:, 12], 'o')
# plt.xlabel("lstat")
# plt.ylabel("medv")
# plt.title("Lower Status Population against Median Value")
# plt.show()



#Build design matrix X with bias column of 1s
n = data.shape[0]
X = np.column_stack([data[:, 4], data[:, 11], np.ones(n)])
y = data[:, 12]


X_train = X[:-100, :]
y_train = y[:-100]
#CUT IT IN HALF 
#if you know you know
X_test = X[-100:, :]
y_test = y[-100:]

#beta = (X^T * X)^(-1) * X^T * y 
beta = np.linalg.inv(X_train.T @ X_train) @ X_train.T @ y_train

#RMSE on the 100 records
test_errors = X_test @ beta - y_test
test_rmse = np.sqrt(np.mean(test_errors**2))

#RMSE on the training set
train_errors = X_train @ beta - y_train
train_rmse = np.sqrt(np.mean(train_errors**2))

print("Fitted Beta Parameters:")
print(f"  beta_rm    = {beta[0]:.4f}")
print(f"  beta_lstat = {beta[1]:.4f}")
print(f"  intercept  = {beta[2]:.4f}")
print(f"\nTraining RMSE: {train_rmse:.4f}")
print(f"Testing RMSE (100 records): {test_rmse:.4f}")