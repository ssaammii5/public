def priority_scheduling_void():
    # Define processes, burst times, arrival times, and priorities
    processes = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6']
    burst_times = [15, 10, 5, 20, 5, 15]
    arrival_times = [0, 0, 20, 25, 45, 55]
    priorities = [8, 3, 4, 4, 5, 5]  # Lower number indicates higher priority

    n = len(processes)
    completed = [False] * n
    completion_times = [0] * n
    turnaround_times = [0] * n
    waiting_times = [0] * n

    current_time = 0
    completed_processes = 0

    while completed_processes < n:
        # Find the process with the highest priority that has arrived and is not completed
        idx = -1
        highest_priority = float('inf')
        for i in range(n):
            if arrival_times[i] <= current_time and not completed[i]:
                if priorities[i] < highest_priority or (priorities[i] == highest_priority and arrival_times[i] < arrival_times[idx]):
                    highest_priority = priorities[i]
                    idx = i

        if idx != -1:
            # Process found, execute it
            current_time += burst_times[idx]
            completion_times[idx] = current_time
            turnaround_times[idx] = completion_times[idx] - arrival_times[idx]
            waiting_times[idx] = turnaround_times[idx] - burst_times[idx]
            completed[idx] = True
            completed_processes += 1
        else:
            # No process available to execute, increment time
            current_time += 1

    # Display the results
    print("Without Threading:")
    print("Process  Arrival Time  Burst Time  Priority  Completion Time  Turnaround Time  Waiting Time")
    for i in range(n):
        print(f"{processes[i]:<8} {arrival_times[i]:<13} {burst_times[i]:<11} {priorities[i]:<9} "
              f"{completion_times[i]:<15} {turnaround_times[i]:<15} {waiting_times[i]}")

# Run the non-threaded function
priority_scheduling_void()
