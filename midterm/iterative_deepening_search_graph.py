import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_edge(self, node, neighbor):
        self.graph.add_edge(node, neighbor)

    def depth_limited_search(self, start, goal, depth_limit, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []

        if start == goal:
            path.append(start)
            return path

        if depth_limit == 0:
            return None

        visited.add(start)

        for neighbor in self.graph.neighbors(start):
            if neighbor not in visited:
                updated_path = path + [start]
                result_path = self.depth_limited_search(neighbor, goal, depth_limit - 1, visited, updated_path)
                if result_path is not None:
                    return result_path

        return None

    def iterative_deepening_search(self, start, goal):
        depth_limit = 0

        while True:
            result_path = self.depth_limited_search(start, goal, depth_limit)
            if result_path is not None:
                return result_path
            depth_limit += 1

# Input section
graph = Graph()

num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    edge = input("Enter edge (format: node1 node2): ").split()
    graph.add_edge(edge[0], edge[1])
    graph.add_edge(edge[1], edge[0])

start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")

# Performing iterative deepening search
result_path = graph.iterative_deepening_search(start_node, goal_node)

# Graphical representation
plt.figure(figsize=(8, 8))

# Highlight the start and goal nodes
node_color = ['red' if node == start_node or node == goal_node else 'skyblue' for node in graph.graph.nodes]

nx.draw(graph.graph, with_labels=True, font_weight='bold', node_size=700, node_color=node_color, edge_color='gray', width=2)
plt.title(f"Graph Representation (Start: {start_node}, Goal: {goal_node})")
plt.show()

# Output section
if result_path is not None:
    print(f"\nPath from {start_node} to {goal_node} using Iterative Deepening Search: {result_path}")
else:
    print(f"\nGoal not reachable from {start_node} to {goal_node}.")
