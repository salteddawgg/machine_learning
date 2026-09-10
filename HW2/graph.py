from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(5 * np.pi, -5 * np.pi, 3600)
f = x * np.sin(x) ** 2
g = -x * np.sin(x) ** 2

plt.title("Trigonometric Functions")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(x, f, "b-", label=r"$f(x) = x\sin^2(x)$")
plt.plot(x, g, "r-", label=r"$g(x) = -x\sin^2(x)$")
plt.tight_layout()

plt.show()

categories = list("abcdefghijklmnopqrstuvwxyz")
values = [
	24168, 4722, 8157, 13336, 38024, 6941, 7025, 17631, 19682,
	637, 2896, 12564, 7568, 22144, 24102, 5832, 303, 17714,
	16818, 28951, 8342, 2893, 7529, 588, 5858, 487,
]
#these numbers were calculatet form frequency(letters).py

order = np.argsort(values)
catagories = np.array(categories)[order]
values = np.array(values)[order]

plt.bar(categories, values, color="blue", width=0.5)
plt.xlabel("letters")
plt.ylabel("frequency")
plt.title("Letter Frequency in The Cosmic Computer")
plt.tight_layout()

plt.show()
board = np.array([
	[0, 1, 0, 1, 0, 1, 0, 1],
	[1, 0, 1, 0, 1, 0, 1, 0],
	[0, 1, 0, 1, 0, 1, 0, 1],
	[1, 0, 1, 0, 1, 0, 1, 0],
	[0, 1, 0, 1, 0, 1, 0, 1],
	[1, 0, 1, 0, 1, 0, 1, 0],
	[0, 1, 0, 1, 0, 1, 0, 1],
	[1, 0, 1, 0, 1, 0, 1, 0],
])

#board = np.arrange(64).reshape((8,8))
# print(board)

plt.imshow(board, cmap="binary", origin="lower", interpolation="nearest")
plt.xticks(range(8), list("ABCDEFGH"))
plt.yticks(range(8), range(1, 9))
plt.title("Chess Board Pattern")
#i think this is what is being asked for

plt.show()


x = [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]]
y = [[1, 2, 1], [2, 3, 1], [4, 2, 2]]

print("Matrix X:")
print(x)
print("Matrix Y:")
print(y)

z = np.dot(x, y)
print("Result:")
print(z)
#this is pretty much a 1 for 1 copy from geeks for geeks. 
#that website is the only thing getting me through tasheen homework for the past 4 years lol


n = np.arange(1, 101)
terms = 4 * (-1) ** (n + 1) / (2 * n - 1)
f_n = np.cumsum(terms)
error = (np.pi - f_n) ** 2

plt.figure()
plt.plot(n, f_n)
plt.xlabel("n")
plt.ylabel("f(n)")
plt.title("Gregory Series Partial Sums")
plt.grid(True)

plt.figure()
plt.plot(n, error)
plt.xlabel("n")
plt.ylabel("(pi - f(n))^2")
plt.title("Gregory Series Squared Error")
plt.grid(True)

print("lim f(n) as n approaches infinity = pi")
#this is the hardest part of the hw tbh
# but we persist, still going over the math to make sure i got it but im not 100% on this kinda math


plt.show()


