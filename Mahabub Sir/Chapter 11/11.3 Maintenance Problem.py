import random

def policy_one(life):
    num_of_shut = 0

    for i in range(4):
        t = 0
        while t < life:
            lf = random.randint(1000, 2000)
            t += lf
            num_of_shut += 1

    tube_cost = num_of_shut * 100
    shut_cost = num_of_shut * 200
    return tube_cost + shut_cost
def policy_two(life):
    t = 0
    num_of_shut = 0

    while t < life:
        lf = [random.randint(1000, 2000), random.randint(1000, 2000), random.randint(1000, 2000),
              random.randint(1000, 2000)]
        cl = min(lf)
        t += cl
        num_of_shut += 1

    tube_cost = num_of_shut * 4 * 100
    shut_cost = num_of_shut * 2 * 200
    return tube_cost + shut_cost
print(policy_one(10000))
print(policy_two(10000))