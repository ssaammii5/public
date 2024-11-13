import threading
import time
import random
import matplotlib.pyplot as plt

# Buffer setup
BUFFER_SIZE = 5
buffer = []
ITEM_LIMIT = 20  # Number of items to produce/consume in total

# Semaphores
empty = threading.Semaphore(BUFFER_SIZE)  # Tracks empty slots
full = threading.Semaphore(0)  # Tracks filled slots
mutex = threading.Lock()  # Ensures mutual exclusion

# Shared counters and tracking lists for visualization
produced_count = 0
consumed_count = 0
buffer_size_over_time = []
produced_over_time = []
consumed_over_time = []

# Tracking individual producer and consumer activities
producer_activities = [[] for _ in range(3)]  # Separate list for each producer
consumer_activities = [[] for _ in range(2)]  # Separate list for each consumer

# Condition to stop the producers and consumers
stop_condition = threading.Event()

# Producer function
def producer(producer_id):
    global produced_count
    while not stop_condition.is_set():
        item = random.randint(1, 100)  # Produce an item
        empty.acquire()  # Wait if buffer is full
        mutex.acquire()  # Lock the buffer for exclusive access

        # Critical section
        if produced_count < ITEM_LIMIT:
            buffer.append(item)
            produced_count += 1
            print(f"Producer {producer_id} produced: {item}")
            # Track data for visualization
            buffer_size_over_time.append(len(buffer))
            produced_over_time.append(produced_count)
            consumed_over_time.append(consumed_count)
            # Record activity for this producer
            for idx, activities in enumerate(producer_activities):
                activities.append(produced_count if idx == producer_id - 1 else None)
            for activities in consumer_activities:
                activities.append(None)  # No consumer activity here
        else:
            stop_condition.set()  # Signal to stop production and consumption

        mutex.release()  # Release lock
        full.release()  # Signal that a new item is available

        if stop_condition.is_set():
            break
        time.sleep(random.uniform(0.5, 2))  # Simulate time to produce another item

# Consumer function
def consumer(consumer_id):
    global consumed_count
    while not stop_condition.is_set():
        full.acquire()  # Wait if buffer is empty
        mutex.acquire()  # Lock the buffer for exclusive access

        # Critical section
        if buffer:
            item = buffer.pop(0)
            consumed_count += 1
            print(f"Consumer {consumer_id} consumed: {item}")
            # Track data for visualization
            buffer_size_over_time.append(len(buffer))
            produced_over_time.append(produced_count)
            consumed_over_time.append(consumed_count)
            # Record activity for this consumer
            for idx, activities in enumerate(consumer_activities):
                activities.append(consumed_count if idx == consumer_id - 1 else None)
            for activities in producer_activities:
                activities.append(None)  # No producer activity here

            if consumed_count >= ITEM_LIMIT:
                stop_condition.set()  # Signal to stop production and consumption
        else:
            stop_condition.set()  # Signal if buffer is empty after reaching limit

        mutex.release()  # Release lock
        empty.release()  # Signal that a slot is now free

        if stop_condition.is_set():
            break
        time.sleep(random.uniform(0.5, 2))  # Simulate time to consume another item

# Number of producers and consumers
NUM_PRODUCERS = 3
NUM_CONSUMERS = 2

# Starting producer threads
producer_threads = []
for i in range(NUM_PRODUCERS):
    t = threading.Thread(target=producer, args=(i + 1,), daemon=True)
    t.start()
    producer_threads.append(t)

# Starting consumer threads
consumer_threads = []
for i in range(NUM_CONSUMERS):
    t = threading.Thread(target=consumer, args=(i + 1,), daemon=True)
    t.start()
    consumer_threads.append(t)

# Wait for the stop condition to be set, then release all semaphores
while not stop_condition.is_set():
    time.sleep(0.1)

# Release any waiting producers and consumers to allow threads to exit
for _ in range(BUFFER_SIZE):
    empty.release()
    full.release()

# Join threads
for t in producer_threads + consumer_threads:
    t.join()

# Plotting the results
plt.figure(figsize=(12, 10))

# Plot buffer size over time
plt.subplot(4, 1, 1)
plt.plot(buffer_size_over_time, label="Buffer Size", color="blue")
plt.title("Buffer Size Over Time")
plt.xlabel("Operations")
plt.ylabel("Buffer Size")
plt.legend()

# Plot produced count over time
plt.subplot(4, 1, 2)
plt.plot(produced_over_time, label="Produced Count", color="green")
plt.title("Produced Count Over Time")
plt.xlabel("Operations")
plt.ylabel("Produced Count")
plt.legend()

# Plot consumed count over time
plt.subplot(4, 1, 3)
plt.plot(consumed_over_time, label="Consumed Count", color="red")
plt.title("Consumed Count Over Time")
plt.xlabel("Operations")
plt.ylabel("Consumed Count")
plt.legend()

# Plot individual producer and consumer actions over time
plt.subplot(4, 1, 4)
for i, activities in enumerate(producer_activities):
    plt.plot(activities, label=f"Producer {i+1} Activity", marker="o", linestyle="None")
for i, activities in enumerate(consumer_activities):
    plt.plot(activities, label=f"Consumer {i+1} Activity", marker="x", linestyle="None")
plt.title("Individual Producer and Consumer Activity Over Time")
plt.xlabel("Operations")
plt.ylabel("Activity Count")
plt.legend()

plt.tight_layout()
plt.show()
