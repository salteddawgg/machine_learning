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



Xy = np.column_stack((data[:, 12], data[:,5], np.ones(data.shape[0])))
print(Xy.shape)
print(Xy)
#test = 
#train = 
#X, y =
#_X, _y =  