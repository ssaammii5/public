import matplotlib.pyplot as plt


def is_safe_state(available, max_claim, allocation):
    """
    Check if the system is in a safe state based on the current resource allocation.
    A safe state means all processes can complete without causing a deadlock.
    """
    num_resources = len(available)
    num_processes = len(max_claim)

    # Initialize work (available resources) and finish array
    work = available.copy()
    finish = [False] * num_processes
    execution_sequence = []  # To store the safe sequence
    work_over_time = [work.copy()]  # Track work resources over time

    print("\nInitial Available Resources:", work)
    print("Initial Allocation Matrix:", allocation)
    print("Initial Max Claim Matrix:", max_claim)
    print("Calculating 'Need' Matrix...")

    # Calculate the need matrix (max_claim - allocation)
    need = [[max_claim[i][j] - allocation[i][j] for j in range(num_resources)] for i in range(num_processes)]
    print("Need Matrix (Max Claim - Allocation):")
    for i in range(num_processes):
        print(f"Process {i}: {need[i]}")

    # Safe state detection algorithm
    print("\nStarting Safe State Detection...\n")
    while True:
        found = False  # Flag to track if any process was able to execute in this round
        for i in range(num_processes):
            # Check if the process is unfinished and if its need can be met by work
            if not finish[i] and all(work[j] >= need[i][j] for j in range(num_resources)):
                # Process can safely complete
                print(f"Process P{i} can execute; its needs are met with current available resources.")
                # Add its allocated resources back to work once it completes
                for j in range(num_resources):
                    work[j] += allocation[i][j]
                finish[i] = True  # Mark this process as finished
                execution_sequence.append(f"P{i}")  # Append to execution sequence
                found = True  # Set found to True, indicating a successful allocation
                print(f"Process P{i} has completed. Updated Available Resources:", work)
                work_over_time.append(work.copy())  # Track resource availability after each process completes
                break

        # If no process could execute in this iteration, exit the loop
        if not found:
            print("\nNo further processes can execute with current resources.")
            break

    # Final check: If all processes are finished, the system is in a safe state
    if all(finish):
        print("\nAll processes have completed. The system is in a SAFE state.")
        print("Safe Execution Sequence:", " -> ".join(execution_sequence))
    else:
        print("\nSome processes could not complete. The system is in an UNSAFE state (deadlock detected).")

    return all(finish), execution_sequence, work_over_time


def bankers_algorithm(request, process_num, available, max_claim, allocation):
    """
    Banker's Algorithm to handle a resource request from a process.
    Checks if granting the request leaves the system in a safe state.
    """
    num_resources = len(available)

    print(f"\nProcess P{process_num} is requesting resources: {request}")
    # Calculate the need matrix (max_claim - allocation)
    need = [[max_claim[i][j] - allocation[i][j] for j in range(num_resources)] for i in range(len(max_claim))]

    # Check if request is less than or equal to need and available resources
    if all(request[j] <= need[process_num][j] for j in range(num_resources)) and \
            all(request[j] <= available[j] for j in range(num_resources)):

        # Temporarily allocate resources to test for a safe state
        print("Request is within the maximum claim and available resources. Testing for safe state...")
        available_temp = available.copy()
        allocation_temp = [row.copy() for row in allocation]
        for j in range(num_resources):
            available_temp[j] -= request[j]
            allocation_temp[process_num][j] += request[j]

        # Check if this state is safe
        is_safe, sequence, work_over_time = is_safe_state(available_temp, max_claim, allocation_temp)
        if is_safe:
            # If safe, grant the resources
            for j in range(num_resources):
                available[j] -= request[j]
                allocation[process_num][j] += request[j]
            print("Request granted. System remains in a safe state.")
            return sequence, work_over_time  # Return sequence and work over time for plotting
        else:
            print("Request denied. Granting the resources would make the system unsafe.")
            return None, None  # No sequence if unsafe
    else:
        print("Request denied. Requested resources exceed the process's maximum claim or available resources.")
        return None, None  # No sequence if request is invalid


def deadlock_detection(available, max_claim, allocation):
    """
    Perform deadlock detection to check if the system is currently in a safe or unsafe state.
    """
    print("Starting Deadlock Detection...\n")
    is_safe, sequence, work_over_time = is_safe_state(available, max_claim, allocation)
    if is_safe:
        print("\nResult: The system is in a safe state. No deadlock detected.")
    else:
        print("\nResult: Deadlock detected. The system is in an unsafe state.")
    return sequence, work_over_time  # Return sequence and work over time for plotting


def plot_execution_sequence(sequence, work_over_time, ax, title):
    """
    Plot the execution sequence and resource availability over time on a given axis.
    """
    num_steps = len(work_over_time)
    resources = len(work_over_time[0])

    for i in range(resources):
        resource_availability = [work[i] for work in work_over_time]
        ax.plot(range(num_steps), resource_availability, label=f'Resource {i + 1}')

    # Add labels and title
    ax.set_xlabel("Execution Step")
    ax.set_ylabel("Available Units")
    ax.set_title(title)
    ax.set_xticks(range(num_steps))
    ax.set_xticklabels(["Start"] + sequence)
    ax.legend()
    ax.grid(True)


if __name__ == "__main__":
    # Example scenario
    available_resources = [3, 3, 2]
    max_claim_per_process = [
        [7, 5, 3],  # Maximum resources process P0 may need
        [3, 2, 2],  # Maximum resources process P1 may need
        [9, 0, 2],  # Maximum resources process P2 may need
        [2, 2, 2],  # Maximum resources process P3 may need
        [4, 3, 3]  # Maximum resources process P4 may need
    ]
    current_allocation = [
        [0, 1, 0],  # Resources currently allocated to process P0
        [2, 0, 0],  # Resources currently allocated to process P1
        [3, 0, 2],  # Resources currently allocated to process P2
        [2, 1, 1],  # Resources currently allocated to process P3
        [0, 0, 2]  # Resources currently allocated to process P4
    ]

    # Perform deadlock detection
    sequence_deadlock, work_over_time_deadlock = deadlock_detection(available_resources, max_claim_per_process, current_allocation)

    # Example resource request for Banker's Algorithm
    request = [1, 0, 2]  # Process P1 requests additional resources
    process_num = 1  # Process making the request

    print("\nPerforming Banker's Algorithm for Deadlock Avoidance...\n")
    sequence_bankers, work_over_time_bankers = bankers_algorithm(request, process_num, available_resources, max_claim_per_process, current_allocation)

    # Plot both results in subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    if sequence_deadlock and work_over_time_deadlock:
        plot_execution_sequence(sequence_deadlock, work_over_time_deadlock, ax1, "Deadlock Detection")

    if sequence_bankers and work_over_time_bankers:
        plot_execution_sequence(sequence_bankers, work_over_time_bankers, ax2, "Banker's Algorithm Execution")

    plt.tight_layout()
    plt.show()
