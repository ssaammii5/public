def round_robin_scheduling_void(time_quantum=5):
    # Define processes, burst times, and arrival times
    processes = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6']
    burst_times = [15, 10, 5, 20, 5, 15]
    arrival_times = [0, 0, 20, 25, 45, 55]

    n = len(processes)
    remaining_burst_times = burst_times[:]
    completion_times = [0] * n
    waiting_times = [0] * n
    turnaround_times = [0] * n

    time = 0
    queue = []
    finished_processes = 0
    arrived_processes = [False] * n

    while finished_processes < n:
        # Add newly arrived processes to the queue
        for i in range(n):
            if arrival_times[i] <= time and not arrived_processes[i] and remaining_burst_times[i] > 0:
                queue.append(i)
                arrived_processes[i] = True

        if queue:
            # Round Robin for the process at the front of the queue
            current_index = queue.pop(0)
            executed_time = min(time_quantum, remaining_burst_times[current_index])
            time += executed_time
            remaining_burst_times[current_index] -= executed_time

            # Add new processes arriving while this process is executing
            for i in range(n):
                if arrival_times[i] <= time and not arrived_processes[i] and remaining_burst_times[i] > 0:
                    queue.append(i)
                    arrived_processes[i] = True

            # If the process is not finished, add it back to the queue
            if remaining_burst_times[current_index] > 0:
                queue.append(current_index)
            else:
                # Process is finished
                finished_processes += 1
                completion_times[current_index] = time
                turnaround_times[current_index] = completion_times[current_index] - arrival_times[current_index]
                waiting_times[current_index] = turnaround_times[current_index] - burst_times[current_index]
        else:
            time += 1

    # Display the results
    print("Without Threading:")
    print("Process  Arrival Time  Burst Time  Completion Time  Turnaround Time  Waiting Time")
    for i in range(n):
        print(f"{processes[i]:<8} {arrival_times[i]:<13} {burst_times[i]:<11} "
              f"{completion_times[i]:<15} {turnaround_times[i]:<15} {waiting_times[i]}")

# Run the non-threaded function
round_robin_scheduling_void(time_quantum=5)
