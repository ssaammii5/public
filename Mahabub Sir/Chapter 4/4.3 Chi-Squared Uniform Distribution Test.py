from scipy.stats import chi2

ri = [12]
a = 13
b = 1
m = 97
n = 100

i = 1
while i <= n:
    rn = ((a * ri[i - 1]) + b) % m
    ri.append(rn)
    i += 1

ri = ri[1:]
print(ri)
len(ri)

cls = []
i = 0
while i <= n:
    cls.append(i)
    i += 10
cls

frequency = [0] * 10

for i in ri:
    for j in range(len(cls) - 1):
        if i > cls[j] and i <= cls[j + 1]:
            frequency[j] += 1
frequency

dif_sq = 0

for i in frequency:
    x = abs(i - 10)
    x = x * x
    dif_sq += x

chi_sqr = dif_sq / 10
chi_sqr

df = 10 - 1
alpha = 0.05
critical_value = chi2.ppf(1 - alpha, df)

if chi_sqr < critical_value:
    print("accept")
else:
    print("rejerct")