import random
import numpy as np
def rand():
    x = random.randint(1, 100)
    x /= 100
    return x
zero_or_positive = 0
n = 0
for i in range(100):
    A = 1.95 + 0.1 * (rand())
    B = 1.95 + 0.1 * (rand())
    C = 29.95 + 1 * (rand())
    D = 34.00 + 1 * (rand())

    n += 1
    dif = False
    if D - (A + B + C) >= 0:
        zero_or_positive += 1
        dif = True

    print(round(A,2)," ",round(B,2)," ",round(C,2)," ",round(A+B+C,2)," ",round(D,2)," ",round(D - (A + B + C),2)," ",dif)

result = (zero_or_positive / n) * 100
print("Result : ", result, "%")