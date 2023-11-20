
def find_neighbours(state, landscape):
    neighbours = []
    dim = (5, 5)

    if state[0] != 0:
        neighbours.append((state[0] - 1, state[1]))

    if state[0] != dim[0] - 1:
        neighbours.append((state[0] + 1, state[1]))

    if state[1] != 0:
        neighbours.append((state[0], state[1] - 1))

    if state[1] != dim[1] - 1:
        neighbours.append((state[0], state[1] + 1))

    if state[0] != 0 and state[1] != 0:
        neighbours.append((state[0] - 1, state[1] - 1))

    if state[0] != 0 and state[1] != dim[1] - 1:
        neighbours.append((state[0] - 1, state[1] + 1))

    if state[0] != dim[0] - 1 and state[1] != 0:
        neighbours.append((state[0] + 1, state[1] - 1))

    if state[0] != dim[0] - 1 and state[1] != dim[1] - 1:
        neighbours.append((state[0] + 1, state[1] + 1))

    print(neighbours)
    return neighbours


def hill_climb(curr_state, landscape):
    neighbours = find_neighbours(curr_state, landscape)
    bool
    ascended = False
    next_state = curr_state
    for neighbour in neighbours:
        if landscape[neighbour[0]][neighbour[1]] > landscape[next_state[0]][next_state[1]]:
            next_state = neighbour
            ascended = True

    return ascended, next_state


def __main__():
    landscape = [
        [12, 15, 10, 7, 14],
        [13, 18, 13, 20, 5],
        [17, 9, 23, 24, 19],
        [7, 14, 16, 12, 34],
        [20, 5, 23, 13, 18],
    ]
    print(landscape)
    start_state = (0, 1)
    current_state = start_state
    count = 1
    ascending = True
    while ascending:
        print("\nStep #", count)
        print("Current state coordinates: ", current_state)
        print("Current state value: ", landscape[current_state[0]][current_state[1]])
        count += 1
        ascending, current_state = hill_climb(current_state, landscape)

    print("\nStep #", count)
    print("Optimization objective reached.")
    print("Final state coordinates: ", current_state)
    print("Final state value: ", landscape[current_state[0]][current_state[1]])


__main__()
