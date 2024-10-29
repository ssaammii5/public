from scipy.stats import kstwo

n = 10
ri = [12]
a = 13
b = 1
m = 97

i = 1
while i <= 10:
    rn = ((a * ri[i - 1]) + b) % m
    ri.append(rn)
    i += 1

for i in range(n + 1):
    ri[i] = ri[i] / 100
ri = ri[1:]

ri.sort()
print(ri)

one_by_n = []

i = 1
while i <= n:
    one_by_n.append(i / n)
    i += 1
one_by_n


one_by_n_sub_ri = []

for i in range(n):
    one_by_n_sub_ri.append(one_by_n[i] - ri[i])

positived = max(one_by_n_sub_ri)
print("D+: ", positived)


ri_sub_i_sub_1_div_n = ri.copy()

i = 1
while i < n:
    ri_sub_i_sub_1_div_n[i] = ri_sub_i_sub_1_div_n[i] - one_by_n[i - 1]
    i += 1

negatived = max(ri_sub_i_sub_1_div_n)
print("D-: ", negatived)


longest_dev = max(positived, negatived)

print("Longest Deviation", longest_dev)

degree_of_freedom = 10
alpha1 = 0.05
alpha2 = 0.01
c1 = kstwo.ppf(1 - alpha1, degree_of_freedom)
c2 = kstwo.ppf(1 - alpha2, degree_of_freedom)


if longest_dev < c1:
    print("95%")
elif longest_dev < c2:
    print("99%")
else:
    print("Failed")