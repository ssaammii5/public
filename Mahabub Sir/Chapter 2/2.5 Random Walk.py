import math
import random
import matplotlib.pyplot as plt
for asa in range(1):
    step = 0
    x = 0
    y = 0
    dotx = []
    doty = []
    direction = []

    F_L_R = [0.5, 0.2, 0.2, 0.1]
    F_L_R = [int(10 * i) for i in F_L_R]

    while step <= 20:

        rn = random.randint(0, 9)

        if rn in range(F_L_R[0]):
            direction.append('F')
            y += 1
            dotx.append(x)
            doty.append(y)
        elif rn in range(F_L_R[0], F_L_R[0] + F_L_R[1]):
            direction.append('L')
            x -= 1
            dotx.append(x)
            doty.append(y)
        elif rn in range(F_L_R[0] + F_L_R[1], F_L_R[0]+ F_L_R[1]+F_L_R[2]):
            direction.append('R')
            x += 1
            dotx.append(x)
            doty.append(y)
        else:
            y -= 1
            direction.append('B')
            dotx.append(x)
            doty.append(y)
        step += 1
    plt.plot(dotx, doty)
plt.show()

print(direction)