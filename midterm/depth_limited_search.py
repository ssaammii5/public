def dls(visited, graph, node, depth_limit):  # function for depth-limited search
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        if depth_limit > 0:
            for neighbour in graph[node]:
                dls(visited, graph, neighbour, depth_limit - 1)

# Driver Code
graph = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': [],
    '4': ['6'],
    '5': ['7', '8', '2'],
    '6': [],
    '7': ['5', '9', '10'],
    '8': ['5', '11'],
    '9': ['7', '12'],
    '10': ['7', '12'],
    '11': [],
    '12': ['9', '10'],
}

depth_limit = 2  # Set your desired depth limit
visited = set()  # unique visited elements

print(f"Following is the Depth-Limited Search (Depth Limit = {depth_limit}):")
dls(visited, graph, '1', depth_limit)
