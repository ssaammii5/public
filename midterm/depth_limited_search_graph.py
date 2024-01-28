import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_edge(self, node, neighbor):
        self.graph.add_edge(node, neighbor)

    def depth_limited_search(self, start, goal, depth_limit, visited=None, path=None, step_count=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        if step_count is None:
            step_count = [0]

        if start == goal:
            path.append(start)
            return path, step_count[0]

        if depth_limit == 0:
            return None, step_count[0]

        visited.add(start)

        for neighbor in self.graph.neighbors(start):
            if neighbor not in visited:
                updated_path = path + [start]
                result_path, result_steps = self.depth_limited_search(neighbor, goal, depth_limit - 1, visited, updated_path, step_count)
                step_count[0] = result_steps + 1
                if result_path is not None:
                    return result_path, step_count[0]

        return None, step_count[0]

# Input section
graph = Graph()

num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    edge = input("Enter edge (format: node1 node2): ").split()
    graph.add_edge(edge[0], edge[1])
    graph.add_edge(edge[1], edge[0])

start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")
depth_limit = int(input("Enter the depth limit: "))

# Performing depth-limited search
result_path, num_steps = graph.depth_limited_search(start_node, goal_node, depth_limit)

# Graphical representation
plt.figure(figsize=(8, 8))
nx.draw(graph.graph, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', edge_color='gray', width=2)
plt.title(f"Graph Representation")
plt.show()

# Output section
if result_path is not None:
    print(f"\nPath from {start_node} to {goal_node} within depth limit {depth_limit}: {result_path}")
    print(f"Number of steps taken: {num_steps}")
else:
    print(f"\nGoal not reachable from {start_node} to {goal_node} within the depth limit.")
