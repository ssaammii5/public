# Import necessary libraries
import threading
import time
import random
import matplotlib.pyplot as plt

# Initialize semaphores and counters
read_count = 0
mutex = threading.Semaphore(1)          # Controls access to read_count
write_lock = threading.Semaphore(1)     # Controls access to the shared resource for writers

# Shared data for demonstration purposes
shared_data = 0

# Variables to hold the actions for visualization
actions = []

# Set read and write limits
read_limit = 6  # Set the limit for the number of reads each reader can perform
write_limit = 4  # Set the limit for the number of writes each writer can perform

# Reader function
def reader(reader_id):
    global read_count
    global shared_data

    for _ in range(read_limit):  # Use read_limit variable for the number of reads
        # Reader tries to acquire the mutex to safely update read_count
        mutex.acquire()
        read_count += 1
        if read_count == 1:
            # If it's the first reader, lock write_lock to block writers
            write_lock.acquire()
        mutex.release()  # Release mutex to allow other readers

        # Reading data (critical section)
        action = (f"Reader {reader_id}", "Reading", shared_data)
        actions.append(action)
        print(f"{action[0]} is {action[1]} data: {action[2]}")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate reading time

        # Reader releases mutex to safely update read_count
        mutex.acquire()
        read_count -= 1
        if read_count == 0:
            # If it's the last reader, release write_lock to allow writers
            write_lock.release()
        mutex.release()  # Release mutex

        # Simulate time before trying to read again
        time.sleep(random.uniform(0.1, 0.5))

# Writer function
def writer(writer_id):
    global shared_data

    for i in range(write_limit):  # Use write_limit variable for the number of writes
        # Writer tries to acquire write_lock to get exclusive access
        write_lock.acquire()

        # Ensure the first operation is always an increment to avoid skip
        if i == 0 or shared_data == 0:
            operation = "increment"
            shared_data += 1
        else:
            # Randomly decide to increment or decrement shared data after initial increment
            operation = random.choice(["increment", "decrement"])
            if operation == "increment":
                shared_data += 1
            elif operation == "decrement" and shared_data > 0:  # Check to avoid negative values
                shared_data -= 1
            else:
                operation = "skip"  # Skip decrement if shared_data is zero

        # Writing data (critical section)
        action = (f"Writer {writer_id}", f"{operation.capitalize()}ing", shared_data)
        actions.append(action)
        print(f"{action[0]} is {action[1]} data: {action[2]}")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate writing time

        # Writer releases write_lock
        write_lock.release()

        # Simulate time before trying to write again
        time.sleep(random.uniform(0.1, 0.5))

# Create reader and writer threads
num_readers = 3
num_writers = 2  # Adjust the number of writers to 5

# Start reader and writer threads with initial random delays
threads = []
for i in range(num_readers):
    t = threading.Thread(target=reader, args=(i+1,))
    threads.append(t)
    t.start()
    time.sleep(random.uniform(0.1, 0.5))  # Random delay before starting the next thread

for i in range(num_writers):
    t = threading.Thread(target=writer, args=(i+1,))
    threads.append(t)
    t.start()
    time.sleep(random.uniform(0.1, 0.5))  # Random delay before starting the next thread

# Wait for all threads to finish
for t in threads:
    t.join()

# Data Preparation for Plotting
steps = list(range(len(actions)))
readers = [1 if action[1] == "Reading" else 0 for action in actions]
writers = [1 if action[1] in ["Incrementing", "Decrementing", "Skipping"] else 0 for action in actions]
data_values = [action[2] for action in actions]

# Plotting the actions
plt.figure(figsize=(12, 6))
plt.plot(steps, data_values, label="Data Value", marker='o', linestyle='-')
plt.plot(steps, readers, label="Reader Action (1=Read)", marker='x', linestyle='--', color='blue')
plt.plot(steps, writers, label="Writer Action (1=Write)", marker='s', linestyle='--', color='red')

# Labeling
plt.xlabel("Steps")
plt.ylabel("Action / Data Value")
plt.title("Readers-Writers Problem Execution with Protected Initial Increment")
plt.legend()
plt.grid(True)
plt.show()
