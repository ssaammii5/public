import random
import numpy as np
import matplotlib.pyplot as plt
length = 1000
height = 600

deviation_x = length / 2
deviation_y = height / 2
def getRNN():
    rnn = np.random.randn()
    return rnn
HIT = 0
N = 0

for i in range(100):
    x = getRNN() * deviation_x
    y = getRNN() * deviation_y
    N += 1
    if (x <= length/2 and x >= -length/2) and (y <= height/2 and y >= -height/2):
        HIT += 1
        plt.scatter(x,y,color = "green")
    else:
        plt.scatter(x,y,color = "blue")


area_x = [-500, 500, 500, -500, -500]
area_y = [-300, -300, 300, 300, -300]

plt.plot(area_x, area_y, color="red")
plt.show()

print(HIT, N)
print("Accuracy : ", (HIT / N) * 100, "%")

