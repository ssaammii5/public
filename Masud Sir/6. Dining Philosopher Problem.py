import threading
import time
import random
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Number of philosophers
K = 10

# Chopstick semaphore (one for each philosopher)
chopsticks = [threading.Semaphore(1) for _ in range(K)]

class Philosopher(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
        self.left_chopstick = chopsticks[id]
        self.right_chopstick = chopsticks[(id + 1) % K]
        self.cycles = 0  # Number of times the philosopher has eaten
        self.state_log = []  # List of tuples (state, start_time, end_time)

    def think(self):
        start_time = time.time()
        print(f"Philosopher {self.id} is thinking.")
        sleep_time = random.uniform(0.1, 0.5)
        time.sleep(sleep_time)
        end_time = time.time()
        self.state_log.append(('Thinking', start_time, end_time))

    def pick_up_chopsticks(self):
        # To avoid deadlock, let the last philosopher pick up the right chopstick first
        start_time = time.time()
        if self.id == K - 1:
            self.right_chopstick.acquire()
            print(f"Philosopher {self.id} picked up right chopstick.")
            self.left_chopstick.acquire()
            print(f"Philosopher {self.id} picked up left chopstick.")
        else:
            self.left_chopstick.acquire()
            print(f"Philosopher {self.id} picked up left chopstick.")
            self.right_chopstick.acquire()
            print(f"Philosopher {self.id} picked up right chopstick.")
        end_time = time.time()
        self.state_log.append(('Picked up Chopsticks', start_time, end_time))

    def eat(self):
        start_time = time.time()
        print(f"Philosopher {self.id} is eating.")
        sleep_time = random.uniform(0.2, 0.5)
        time.sleep(sleep_time)
        end_time = time.time()
        self.state_log.append(('Eating', start_time, end_time))
        self.cycles += 1

    def put_down_chopsticks(self):
        # Only release the chopsticks without logging for the Gantt chart
        self.left_chopstick.release()
        self.right_chopstick.release()
        print(f"Philosopher {self.id} put down both chopsticks.")

    def run(self):
        # Each philosopher will eat a certain number of times for simulation purposes
        while self.cycles < 5:  # Limit cycles to prevent infinite loop in this example
            self.think()
            self.pick_up_chopsticks()
            self.eat()
            self.put_down_chopsticks()

# Create and start philosopher threads
philosophers = [Philosopher(i) for i in range(K)]
for philosopher in philosophers:
    philosopher.start()

# Wait for all philosophers to finish
for philosopher in philosophers:
    philosopher.join()

print("Dining simulation complete.")

# Generate Gantt chart visualization
# Collect data from philosophers
philosopher_names = [f"Philosopher {i}" for i in range(K)]
states = ['Thinking', 'Picked up Chopsticks', 'Eating']
state_colors = {
    'Thinking': 'skyblue',
    'Picked up Chopsticks': 'yellowgreen',
    'Eating': 'salmon'
}

# Find the minimum start time to normalize times
start_times = []
for philosopher in philosophers:
    if philosopher.state_log:
        start_times.extend([entry[1] for entry in philosopher.state_log])
if start_times:
    global_start_time = min(start_times)
else:
    global_start_time = 0

# Prepare data for Gantt chart
fig, ax = plt.subplots(figsize=(10, 5))

for idx, philosopher in enumerate(philosophers):
    for state in philosopher.state_log:
        state_name, start_time, end_time = state
        start_time -= global_start_time  # Normalize time
        end_time -= global_start_time
        ax.barh(idx, end_time - start_time, left=start_time, color=state_colors[state_name], edgecolor='black')

ax.set_yticks(range(K))
ax.set_yticklabels(philosopher_names)
ax.set_xlabel('Time (s)')
ax.set_title('Dining Philosophers Gantt Chart without "Put down Chopsticks" State')

# Create custom legend
legend_patches = [mpatches.Patch(color=state_colors[state], label=state) for state in states]
ax.legend(handles=legend_patches, bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()
