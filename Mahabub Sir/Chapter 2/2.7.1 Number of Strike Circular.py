import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
length = 1000
height = 1000

deviation_x = length / 2
deviation_y = length / 2
def getRNN():
    rnn = np.random.randn()
    return rnn
poin_x = []
poin_y = []
HIT = 0
N = 0
for i in range(10):
    x = getRNN() * deviation_x
    y = getRNN() * deviation_y
    poin_x.append(x)
    poin_y.append(y)

    if (x**2 + y**2) <= (500*500):
        HIT += 1
    N += 1


fig = plt.figure()
ax = fig.add_subplot()
circle1 = patches.Circle((0, 0), radius=500, color='red')
ax.add_patch(circle1)
ax.axis('equal')

plt.scatter(poin_x, poin_y)
plt.show()

print(HIT, N)
print("Accuracy : ", (HIT / N) * 100, "%")