import threading

def fcfs_scheduling_threaded():
    # Define the process data as extracted from the image
    processes = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6']
    burst_times = [15, 10, 5, 20, 5, 15]
    arrival_times = [0, 0, 20, 25, 45, 55]

    # Sort processes by arrival time
    n = len(processes)
    process_data = sorted(zip(processes, burst_times, arrival_times), key=lambda x: x[2])

    # Initialize tracking variables
    current_time = 0
    completion_times = []
    turnaround_times = []
    waiting_times = []

    # Calculate Completion Time, Turnaround Time, and Waiting Time
    for process, burst_time, arrival_time in process_data:
        # If process arrives after the current time, move current time to arrival time
        if current_time < arrival_time:
            current_time = arrival_time

        # Completion time for the process
        completion_time = current_time + burst_time
        completion_times.append(completion_time)

        # Update current time to this process's completion time
        current_time = completion_time

        # Turnaround time = Completion time - Arrival time
        turnaround_time = completion_time - arrival_time
        turnaround_times.append(turnaround_time)

        # Waiting time = Turnaround time - Burst time
        waiting_time = turnaround_time - burst_time
        waiting_times.append(waiting_time)

    # Display the results
    print("With Threading:")
    print("Process  Arrival Time  Burst Time  Completion Time  Turnaround Time  Waiting Time")
    for i in range(n):
        print(f"{process_data[i][0]:<8} {process_data[i][2]:<13} {process_data[i][1]:<11} "
              f"{completion_times[i]:<15} {turnaround_times[i]:<15} {waiting_times[i]}")

# Create and start the thread
thread = threading.Thread(target=fcfs_scheduling_threaded)
thread.start()

# Wait for the thread to complete before ending the main program
thread.join()
