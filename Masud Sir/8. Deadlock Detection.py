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

    plot_execution_sequence(execution_sequence, work_over_time)
    return all(finish)


def deadlock_detection(available, max_claim, allocation):
    """
    Perform deadlock detection to check if the system is currently in a safe or unsafe state.
    """
    print("Starting Deadlock Detection...\n")
    if is_safe_state(available, max_claim, allocation):
        print("\nResult: The system is in a safe state. No deadlock detected.")
    else:
        print("\nResult: Deadlock detected. The system is in an unsafe state.")


def plot_execution_sequence(sequence, work_over_time):
    """
    Plot the execution sequence and resource availability over time.
    """
    num_steps = len(work_over_time)
    resources = len(work_over_time[0])

    # Create a figure with subplots for each resource type
    plt.figure(figsize=(10, 6))

    for i in range(resources):
        resource_availability = [work[i] for work in work_over_time]
        plt.plot(range(num_steps), resource_availability, label=f'Resource {i + 1}')

    # Add labels and title
    plt.xlabel("Execution Step")
    plt.ylabel("Available Units")
    plt.title("Resource Availability Over Time")
    plt.xticks(range(num_steps), ["Start"] + sequence)
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Example scenario
    # Define the available resources, maximum claim of each process, and current allocation
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
    deadlock_detection(available_resources, max_claim_per_process, current_allocation)
