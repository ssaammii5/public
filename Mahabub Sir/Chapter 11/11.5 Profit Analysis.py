import random

n = 30
sp = 10
fc = 60000
profit_lst = []
for i in range(n):
    vc = random.randint(450, 550) / 100
    demand = 0
    reaction = random.randint(1, 10)
    if reaction <= 6:
        demand = random.randint(10000, 12000)
    else:
        demand = random.randint(13000, 15000)
    profit = round(demand * (sp - vc) - fc, 2)
    profit_lst.append(profit)

profit_lst.sort()
print(profit_lst)

count = 0
for i in profit_lst:
    if i > 5000:
        count += 1

print(count)