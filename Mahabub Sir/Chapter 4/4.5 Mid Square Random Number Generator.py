n = 10
seed = 5673

var = int(len(str(seed))/2)

rn = []

for i in range(n):
    x = seed ** 2
    st = str(x)
    dig = int((len(st)) / 2)
    r = st[dig - var : dig + var]
    seed = int(r)
    rn.append(seed)
print(rn)