import threading
import time
import matplotlib.pyplot as plt

# Shared resource and data for visualization
counter = 0
lock = threading.Lock()
increment_steps = []  # To store (thread name, counter value) tuples for plotting

# Function to increment the counter safely
def increment_counter(thread_name):
    global counter
    for _ in range(5):  # Each thread increments the counter 5 times
        lock.acquire()
        try:
            current_value = counter
            print(f"{thread_name} sees counter as {current_value}. Incrementing...")
            time.sleep(0.1)  # Simulate processing delay
            counter = current_value + 1
            print(f"{thread_name} updated counter to {counter}.")
            increment_steps.append((thread_name, counter))  # Record the thread and counter value
        finally:
            lock.release()
        time.sleep(0.1)  # Additional delay to observe threading behavior

# Creating and starting multiple threads
threads = []
num_threads = 5  # Number of threads

for i in range(num_threads):
    thread = threading.Thread(target=increment_counter, args=(f"Thread {i + 1}",))
    threads.append(thread)
    thread.start()

# Waiting for all threads to complete
for thread in threads:
    thread.join()

# Separating thread names and counter values for plotting
thread_names, counter_values = zip(*increment_steps)

# Assigning a numerical ID to each thread for plotting purposes
thread_ids = {name: idx + 1 for idx, name in enumerate(set(thread_names))}
thread_numeric = [thread_ids[name] for name in thread_names]

# Plotting the results
plt.figure(figsize=(10, 6))
plt.scatter(counter_values, thread_numeric, c=thread_numeric, cmap='viridis', s=100, marker='o', edgecolor='k')
plt.plot(counter_values, thread_numeric, linestyle='-', alpha=0.5)  # Connect points to show progression

# Customizing the plot
plt.title("Counter Increments by Multiple Threads with Mutex Lock")
plt.xlabel("Counter Value")
plt.ylabel("Thread ID")
plt.yticks(range(1, num_threads + 1), [f"Thread {i}" for i in range(1, num_threads + 1)])
plt.grid(True)
plt.colorbar(label="Thread ID")
plt.show()
