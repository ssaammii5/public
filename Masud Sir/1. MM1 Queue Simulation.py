import simpy
import random
import matplotlib.pyplot as plt

class SingleServerQueue:
    def __init__(self, env, arrival_rate, service_rate, max_customers):
        self.env = env
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate
        self.max_customers = max_customers
        self.queue_length = 0
        self.waiting_times = []
        self.total_customers_served = 0
        self.total_busy_time = 0

    def customer_arrival(self):
        for _ in range(self.max_customers):
            yield self.env.timeout(random.expovariate(self.arrival_rate))
            arrival_time = self.env.now
            self.queue_length += 1
            self.env.process(self.customer_service(arrival_time))

    def customer_service(self, arrival_time):
        service_time = random.expovariate(self.service_rate)
        yield self.env.timeout(service_time)
        departure_time = self.env.now
        self.queue_length -= 1
        waiting_time = departure_time - arrival_time
        self.waiting_times.append(waiting_time)
        self.total_busy_time += service_time
        self.total_customers_served += 1

if __name__ == '__main__':
    mean_inter_arrival_time = 2
    mean_service_time = 1.67
    max_customers = 500
    simulation_time = 1000

    arrival_rate = 1 / mean_inter_arrival_time
    service_rate = 1 / mean_service_time

    env = simpy.Environment()
    queue_system = SingleServerQueue(env, arrival_rate, service_rate, max_customers)
    env.process(queue_system.customer_arrival())
    env.run(until=simulation_time)

    average_waiting_time = sum(queue_system.waiting_times) / len(queue_system.waiting_times) if queue_system.waiting_times else 0
    server_utilization = (queue_system.total_busy_time / simulation_time) * 100
    time_simulation_ended = env.now

    print("Average Delay in Queue (seconds):", average_waiting_time)
    print("System Utilization (%):", server_utilization)
    print("Time Simulation Ended (seconds):", time_simulation_ended)

    plt.hist(queue_system.waiting_times, bins=30, density=True, alpha=0.7, color='blue')
    plt.xlabel('Waiting Time (seconds)')
    plt.ylabel('Probability Density')
    plt.title('Waiting Time Distribution in Single-Server Queuing System')
    plt.show()




# Import necessary libraries for simulation (SimPy), random number generation, and plotting

# Define a SingleServerQueue class representing an M/M/1 queuing system
# M/M/1 Queue: A common single-server queuing model where:
# - "M" indicates a Markov (memoryless) or exponential distribution for both inter-arrival and service times
# - "1" indicates a single server
# This queue model is widely used to study scenarios where arrivals and service times are random and independent

# Initialize the SingleServerQueue class with environment, arrival rate, service rate, and maximum customer count
# Create attributes to store queue length, waiting times, total served customers, and total server busy time

# Define customer_arrival method to handle customer arrivals
# For each customer, wait based on the exponential inter-arrival time, record arrival time, and increment queue length
# Start a new process to handle customer service upon each arrival

# Define customer_service method to handle customer service process
# Wait based on the exponential service time, record departure time, and decrement queue length
# Calculate waiting time, add it to waiting_times list, update total busy time and count of served customers

# Set simulation parameters including mean inter-arrival time, mean service time, max customers, and simulation time
# Calculate arrival and service rates as reciprocals of mean times

# Set up SimPy environment and initialize SingleServerQueue instance with specified parameters
# Start customer arrival process and run the simulation until specified end time

# Calculate average waiting time as the mean of waiting_times list
# Calculate server utilization as the percentage of total busy time over total simulation time
# Record the end time of the simulation

# Print results: average queue delay, system utilization, and simulation end time

# Plot a histogram of waiting times to show their distribution
