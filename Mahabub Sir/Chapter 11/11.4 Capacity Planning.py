import random
import matplotlib.pyplot as plt

cumulative_frequency = [0, 5, 11, 21, 35, 51, 67, 80, 90, 97, 100]
hours = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
days = 20

task = []

for day in range(days):
    machine_use = 0
    num_of_order = random.randint(1, 10)

    for order in range(num_of_order):
        order_life = 0
        rn = random.randint(1, 100)

        for i in range(len(cumulative_frequency) - 1):
            if cumulative_frequency[i] < rn <= cumulative_frequency[i + 1]:
                order_life = random.randint(hours[i] + 1, hours[i + 1])
                machine_use += order_life

    task.append(machine_use)

avg = sum(task) / 20
print(task)
print(avg)

cost = []
load = []

for i in range(int(avg - 100), int(avg + 100), 20):
    delay = []
    idle = 0
    left = 0
    for t in task:
        t += left
        if t < i:
            idle += i - t
        else:
            delay.append(t - i)
    delay_cost = sum(delay) * 25
    idle_cost = idle * 100
    cost.append((delay_cost + idle_cost))
    load.append(i)
    print("Cost :", delay_cost + idle_cost, " for load: ", i)

plt.scatter(load, cost)