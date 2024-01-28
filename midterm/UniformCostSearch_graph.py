import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_edge(self, node, neighbor, cost):
        self.graph.add_edge(node, neighbor, weight=cost)

    def uniform_cost_search(self, start, goal):
        priority_queue = [(0, start, [])]
        visited = set()

        while priority_queue:
            current_cost, current_node, path = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            path = path + [current_node]
            visited.add(current_node)

            if current_node == goal:
                return path

            for neighbor in self.graph.neighbors(current_node):
                if neighbor not in visited:
                    cost = self.graph[current_node][neighbor]['weight']
                    heapq.heappush(priority_queue, (current_cost + cost, neighbor, path))

        return None

# Input section
graph = Graph()

num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    edge = input("Enter edge and cost (format: node1 node2 cost): ").split()
    graph.add_edge(edge[0], edge[1], int(edge[2]))

start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")

# Performing Uniform Cost Search
result_path = graph.uniform_cost_search(start_node, goal_node)

# Graphical representation
plt.figure(figsize=(8, 8))
pos = nx.spring_layout(graph.graph)

# Draw the entire graph
nx.draw(graph.graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', edge_color='gray', width=2, edge_cmap=plt.cm.Blues)

# Highlight the nodes and edges of the optimal path
if result_path is not None:
    path_edges = [(result_path[i], result_path[i+1]) for i in range(len(result_path)-1)]
    nx.draw_networkx_nodes(graph.graph, pos, nodelist=result_path, node_color='green', node_size=700)
    nx.draw_networkx_edges(graph.graph, pos, edgelist=path_edges, edge_color='green', width=2)

# Annotate the edges with their weights
nx.draw_networkx_edge_labels(graph.graph, pos, edge_labels={(i, j): graph.graph[i][j]['weight'] for i, j in graph.graph.edges})

plt.title("Graph Representation with Optimal Path")
plt.show()

# Output section
if result_path is not None:
    print(f"\nOptimal path from {start_node} to {goal_node} using Uniform Cost Search: {result_path}")
else:
    print(f"\nGoal not reachable from {start_node} to {goal_node}.")
