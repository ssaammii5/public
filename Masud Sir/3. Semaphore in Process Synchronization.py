import random
import time
import threading
import queue
import matplotlib.pyplot as plt

# Buffer parameters
BSIZE = 6  # Buffer size
PWT = (1, 2)  # Producer wait time range
CWT = (1, 8)  # Consumer wait time range
RT = 20  # Runtime duration

# Counting Semaphores
empty_slots = threading.Semaphore(BSIZE)  # Counts available slots in the buffer
filled_slots = threading.Semaphore(0)     # Counts filled slots in the buffer
mutex = threading.Semaphore(1)  # Binary semaphore for mutual exclusion

# Lists to store timestamps and buffer utilization for plotting
timestamps = []
buffer_occupancy = []
actions = []
producer_activities = []
consumer_activities = []

def record_buffer_state(shared_queue, action, role):
    """ Record buffer occupancy for visualization and track individual actions. """
    timestamps.append(time.time())
    buffer_occupancy.append(shared_queue.qsize())
    actions.append(action)
    # Track actions for the producer and consumer separately
    if role == "Producer":
        producer_activities.append(shared_queue.qsize())
        consumer_activities.append(None)
    elif role == "Consumer":
        consumer_activities.append(shared_queue.qsize())
        producer_activities.append(None)

def producer(shared_queue, event):
    while not event.is_set():
        time.sleep(1)
        print("\nProducer is ready now.")

        # Wait until there's an empty slot (Counting Semaphore for empty slots)
        empty_slots.acquire()

        # Lock the buffer for mutual exclusion (Binary Semaphore for critical section)
        mutex.acquire()

        # Critical Section
        if not shared_queue.full():
            tempo = random.randint(1, BSIZE * 3)
            print(f"Job {tempo} has been produced")
            shared_queue.put(tempo)
            print(f"Buffer: {list(shared_queue.queue)}")
            record_buffer_state(shared_queue, 'Produced', 'Producer')

        # Release the lock and signal that an item is available (Counting Semaphore for filled slots)
        mutex.release()
        filled_slots.release()

        # Variable Wait Time for Producer within a narrow range
        wait_time = random.randint(*PWT)
        print(f"Producer will wait for {wait_time} seconds")
        time.sleep(wait_time)

def consumer(shared_queue, event):
    time.sleep(5)  # To give producer a head start
    while not event.is_set():
        time.sleep(1)
        print("\nConsumer is ready now.")

        # Wait until there's a filled slot (Counting Semaphore for filled slots)
        filled_slots.acquire()

        # Lock the buffer for mutual exclusion (Binary Semaphore for critical section)
        mutex.acquire()

        # Critical Section
        if not shared_queue.empty():
            job = shared_queue.get()
            print(f"Job {job} has been consumed")
            print(f"Buffer: {list(shared_queue.queue)}")
            record_buffer_state(shared_queue, 'Consumed', 'Consumer')

        # Release the lock and signal that a slot is now empty (Counting Semaphore for empty slots)
        mutex.release()
        empty_slots.release()

        # Variable Wait Time for Consumer within a narrow range
        wait_time = random.randint(*CWT)
        print(f"Consumer will sleep for {wait_time} seconds")
        time.sleep(wait_time)

if __name__ == "__main__":
    shared_queue = queue.Queue(BSIZE)

    # Use threading.Event() to control the state
    stop_event = threading.Event()

    producer_thread = threading.Thread(target=producer, args=(shared_queue, stop_event))
    consumer_thread = threading.Thread(target=consumer, args=(shared_queue, stop_event))

    producer_thread.start()
    consumer_thread.start()

    # Let the program run for RT seconds
    time.sleep(RT)

    # Signal threads to stop and wait for them to finish
    stop_event.set()
    producer_thread.join()
    consumer_thread.join()

    print("\nThe clock ran out.")

    # Define operation steps for plotting
    operation_steps = range(len(timestamps))

    # Create a single window with three subplots for each individual section
    plt.figure(figsize=(12, 12))

    # Subplot for Buffer Occupancy
    plt.subplot(3, 1, 1)
    plt.plot(operation_steps, buffer_occupancy, marker='o', linestyle='-', color='b', label="Buffer Occupancy")
    for i, action in enumerate(actions):
        if action == 'Produced':
            plt.plot(operation_steps[i], buffer_occupancy[i], 'go',
                     label='Produced' if 'Produced' not in plt.gca().get_legend_handles_labels()[1] else "")
        elif action == 'Consumed':
            plt.plot(operation_steps[i], buffer_occupancy[i], 'ro',
                     label='Consumed' if 'Consumed' not in plt.gca().get_legend_handles_labels()[1] else "")
    plt.xlabel("Operation Step")
    plt.ylabel("Buffer Occupancy")
    plt.title("Producer-Consumer Buffer Occupancy Over Operation Steps with Counting Semaphores")
    plt.legend()
    plt.grid()

    # Subplot for Producer Activity Over Time
    plt.subplot(3, 1, 2)
    plt.plot([i for i, x in enumerate(producer_activities) if x is not None],
             [x for x in producer_activities if x is not None], 'go-', label="Producer Activity")
    plt.xlabel("Operation Index")
    plt.ylabel("Buffer Size")
    plt.title("Producer Activity Over Time")
    plt.legend()
    plt.grid()

    # Subplot for Consumer Activity Over Time
    plt.subplot(3, 1, 3)
    plt.plot([i for i, x in enumerate(consumer_activities) if x is not None],
             [x for x in consumer_activities if x is not None], 'ro-', label="Consumer Activity")
    plt.xlabel("Operation Index")
    plt.ylabel("Buffer Size")
    plt.title("Consumer Activity Over Time")
    plt.legend()
    plt.grid()

    # Adjust layout to avoid overlap and display all plots together
    plt.tight_layout()
    plt.subplots_adjust(hspace=0.5)  # Add more vertical space between subplots
    plt.show()
