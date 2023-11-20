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

visited = set() #unique visited element

def dfs(visited, graph, node):  #function for dfs
    if node not in visited:
        print (node,end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '1')

