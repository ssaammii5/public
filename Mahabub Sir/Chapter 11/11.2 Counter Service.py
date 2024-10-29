import random
iat = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
iat_frequency = [5, 35, 25, 15, 10, 7, 3]
st = [1, 2, 3, 4, 5]
st_frequency = [5, 25, 35, 20, 15]

cumulative_probability_iat = [0]
for i in range(len(iat_frequency)):
    cumulative_probability_iat.append(cumulative_probability_iat[i] + iat_frequency[i])

cumulative_probability_st = [0]
for i in range(len(st_frequency)):
    cumulative_probability_st.append(cumulative_probability_st[i] + st_frequency[i])
counter = 4
num_customer = 20000
waiting_time = 0

for num_counter in range(1, counter + 1):
    se = [0.0] * num_counter
    next_arrival_time = 0.0
    waiting_time = 0

    for i in range(num_customer):

        inter_arrival_time = 0
        service_time = 0
        wt = 0

        rn = random.randint(1, 100)
        for i in range(len(cumulative_probability_iat) - 1):
            if cumulative_probability_iat[i] > rn and rn <= cumulative_probability_iat[i + 1]:
                inter_arrival_time = iat[i]
                break

        rn = random.randint(1, 100)
        for i in range(len(cumulative_probability_st) - 1):
            if cumulative_probability_st[i] > rn and rn <= cumulative_probability_st[i + 1]:
                service_time = st[i]
                break

        next_arrival_time += inter_arrival_time

        min_counter = se.index(min(se))

        if next_arrival_time <= se[min_counter]:
            se[min_counter] += service_time
            wt = se[min_counter] - next_arrival_time

        else:
            se[min_counter] += service_time
        waiting_time += wt

    print(waiting_time)
    print("Number of Counter = ", num_counter, " Average waiting time = ", waiting_time / num_customer)