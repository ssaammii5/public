import math
import random
import matplotlib.pyplot as plt
step = 0
x = 0
y = 0
z = 0

dotx = []
doty = []
dotz = []
direction = []

F_B_L_R_U_D = [0.3, 0.1, 0.2, 0.1, 0.2, 0.1]

itr = 0
while itr < len(F_B_L_R_U_D):
    F_B_L_R_U_D[itr]  = int(F_B_L_R_U_D[itr]*10)
    if itr > 0:
        F_B_L_R_U_D[itr] = F_B_L_R_U_D[itr] + F_B_L_R_U_D[itr - 1]
    itr += 1



while step <= 100:
    rn = random.randint(0, 9)
    if rn in range(F_B_L_R_U_D[0]):
        direction.append('F')
        y += 1
        dotx.append(x)
        doty.append(y)
        dotz.append(z)
    elif rn in range(F_B_L_R_U_D[0], F_B_L_R_U_D[1]):
        direction.append('B')
        y -= 1
        dotx.append(x)
        doty.append(y)
        dotz.append(z)
    elif rn in range(F_B_L_R_U_D[1], F_B_L_R_U_D[2]):
        direction.append('L')
        x -= 1
        dotx.append(x)
        doty.append(y)
        dotz.append(z)
    elif rn in range(F_B_L_R_U_D[2], F_B_L_R_U_D[3]):
        direction.append('R')
        x += 1
        dotx.append(x)
        doty.append(y)
        dotz.append(z)
    elif rn in range(F_B_L_R_U_D[3], F_B_L_R_U_D[4]):
        direction.append('Up')
        z += 1
        dotx.append(x)
        doty.append(y)
        dotz.append(z)
    else:
        direction.append('Down')
        z -= 1
        dotx.append(x)
        doty.append(y)
        dotz.append(z)

    step += 1
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(dotx, doty, dotz, 'green')
plt.show()

print(direction)