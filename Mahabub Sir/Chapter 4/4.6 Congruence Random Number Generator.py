r = [1]
a = 13
b = 1
m = 97
i = 1
while i <= 10:
    rn = ((a*r[i-1])+b) % m
    r.append(rn)
    i+=1
# print(r)

for i in range(1, 11):
    print(r[i], end=" ")