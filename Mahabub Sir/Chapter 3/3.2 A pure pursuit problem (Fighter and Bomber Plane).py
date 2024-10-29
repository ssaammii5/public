import math
xb = [100, 100, 120, 129, 140, 149, 158, 168, 179, 188]
yb = [0, 3, 6, 10, 15, 20, 26, 32, 37, 34]
xf = 0
yf = 50
s = 25
res = []
def distance(xb, yb):
    y = yb - yf
    y = y ** 2
    x = xb - xf
    x = x ** 2
    val = x + y
    return math.sqrt(val)
for i in range(len(xb)):
    dist = distance(xb[i], yb[i])
    sin = (yb[i] - yf) / dist
    cos = (xb[i] - xf) / dist
    xf_1 = xf + s * cos
    yf_1 = yf + s * sin
    res.append([xb[i], yb[i], xf, yf, dist, cos, sin, xf_1, yf_1])
    xf = xf_1
    yf = yf_1
t = 0
hit = []
for i in res:
    t += 1
    if i[4] <= 20:
        hit.append(t)
    print("T", t, "xb=", round(i[0], 4), "yb=", round(i[1], 4), "xf=", round(i[2], 4), "yf=", round(i[3], 4),
          "Distance=", round(i[4], 4), "Cos=", round(i[5], 4), "Sin=", round(i[6], 4), "xf+1=", round(i[7], 4), "yf+1=",
          round(i[8], 4))

print("The fighter can hit in",*hit,"s")