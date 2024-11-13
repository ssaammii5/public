import random
import time
import threading
import queue
import matplotlib.pyplot as plt

# Balanced parameters to promote both full and empty buffer scenarios occasionally
BSIZE = 6  # Buffer size
PWT = (1, 2)  # Narrow range for Producer wait time to operate at a balanced speed
CWT = (1, 8)  # Narrow range for Consumer wait time to operate at a similar balanced speed
RT = 40  # Extended runtime to allow for natural fluctuations

# Shared resources for Peterson's algorithm
flag = [False, False]  # Flags for each process
turn = 0  # Shared turn variable

# Lists to store timestamps and buffer utilization for plotting
timestamps = []
buffer_occupancy = []
actions = []

# Additional tracking lists for individual producer and consumer actions
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
    global turn, flag
    while not event.is_set():
        time.sleep(1)
        print("\nProducer is ready now.")

        # Entry section for Peterson's algorithm
        flag[0] = True
        turn = 1
        while flag[1] and turn == 1:
            pass  # Busy-wait

        # Critical Section
        if not shared_queue.full():
            tempo = random.randint(1, BSIZE * 3)
            print(f"Job {tempo} has been produced")
            shared_queue.put(tempo)
            print(f"Buffer: {list(shared_queue.queue)}")
            record_buffer_state(shared_queue, 'Produced', 'Producer')  # Record action
        else:
            print("Buffer is full, nothing can be produced!!!")

        # Exit section for Peterson's algorithm
        flag[0] = False

        # Variable Wait Time for Producer within a narrow range
        wait_time = random.randint(*PWT)
        print(f"Producer will wait for {wait_time} seconds")
        time.sleep(wait_time)

def consumer(shared_queue, event):
    global turn, flag
    time.sleep(5)  # To give producer a head start
    while not event.is_set():
        time.sleep(1)
        print("\nConsumer is ready now.")

        # Entry section for Peterson's algorithm
        flag[1] = True
        turn = 0
        while flag[0] and turn == 0:
            pass  # Busy-wait

        # Critical Section
        if not shared_queue.empty():
            job = shared_queue.get()
            print(f"Job {job} has been consumed")
            print(f"Buffer: {list(shared_queue.queue)}")
            record_buffer_state(shared_queue, 'Consumed', 'Consumer')  # Record action
        else:
            print("Buffer is empty, nothing can be consumed!!!")

        # Exit section for Peterson's algorithm
        flag[1] = False

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

    # Plotting the buffer occupancy over time using operation index
    plt.figure(figsize=(12, 12))

    # Subplot for Buffer Occupancy using Operation Index
    plt.subplot(3, 1, 1)
    plt.plot(range(len(buffer_occupancy)), buffer_occupancy, marker='o', linestyle='-', color='b', label="Buffer Occupancy")
    for i, action in enumerate(actions):
        if action == 'Produced':
            plt.plot(i, buffer_occupancy[i], 'go', label='Produced' if 'Produced' not in plt.gca().get_legend_handles_labels()[1] else "")
        elif action == 'Consumed':
            plt.plot(i, buffer_occupancy[i], 'ro', label='Consumed' if 'Consumed' not in plt.gca().get_legend_handles_labels()[1] else "")
    plt.xlabel("Operation Index")
    plt.ylabel("Buffer Occupancy")
    plt.title("Producer-Consumer Buffer Occupancy Over Time with Balanced Parameters")
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
