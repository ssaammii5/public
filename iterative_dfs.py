graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['G'],
    'D': [],
    'E': ['F'],
    'F': [],

}


def DFS(currentNode, destination, graph, maxDepth):
    print("Testing For Destination", currentNode)
    if currentNode == destination:
        return True
    if maxDepth <= 0:
        return False
    for node in graph[currentNode]:
        if DFS(node, destination, graph, maxDepth - 1):
            return True
    return False


def iterativeDFS(currentNode, destination, graph, maxDepth):
    for i in range(maxDepth):
        if DFS(currentNode, destination, graph, i):
            return True
    return False


if not iterativeDFS('A', 'E', graph, 4):
    print("Path is not available")
else:
    print("Path Exists")
