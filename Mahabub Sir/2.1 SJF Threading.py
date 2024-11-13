import threading


def preemptive_sjf_scheduling_threaded():
    processes = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6']
    burst_times = [15, 10, 5, 20, 5, 15]
    arrival_times = [0, 0, 20, 25, 45, 55]

    n = len(processes)
    remaining_burst_times = burst_times[:]
    completion_times = [0] * n
    turnaround_times = [0] * n
    waiting_times = [0] * n

    current_time = 0
    completed = 0
    min_index = -1
    min_remaining_time = float('inf')
    is_process_executing = False

    while completed != n:
        for i in range(n):
            if (arrival_times[i] <= current_time and remaining_burst_times[i] > 0 and remaining_burst_times[
                i] < min_remaining_time):
                min_remaining_time = remaining_burst_times[i]
                min_index = i
                is_process_executing = True

        if not is_process_executing:
            current_time += 1
            continue

        remaining_burst_times[min_index] -= 1
        min_remaining_time = remaining_burst_times[min_index]

        if remaining_burst_times[min_index] == 0:
            completed += 1
            is_process_executing = False
            min_remaining_time = float('inf')
            completion_times[min_index] = current_time + 1
            turnaround_times[min_index] = completion_times[min_index] - arrival_times[min_index]
            waiting_times[min_index] = turnaround_times[min_index] - burst_times[min_index]

        current_time += 1

    print("With Threading:")
    print("Process  Arrival Time  Burst Time  Completion Time  Turnaround Time  Waiting Time")
    for i in range(n):
        print(f"{processes[i]:<8} {arrival_times[i]:<13} {burst_times[i]:<11} "
              f"{completion_times[i]:<15} {turnaround_times[i]:<15} {waiting_times[i]}")


# Create and start the thread
thread = threading.Thread(target=preemptive_sjf_scheduling_threaded)
thread.start()

# Wait for the thread to complete before ending the main program
thread.join()
