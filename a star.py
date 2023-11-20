import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    def a_star_search(self, start, goal, heuristic):
        priority_queue = [(0, start, [])]
        visited = set()

        while priority_queue:
            (cost, current, path) = heapq.heappop(priority_queue)

            if current in visited:
                continue

            visited.add(current)
            path = path + [current]

            if current == goal:
                return path

            for (neighbor, weight) in self.graph.get(current, []):
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost + weight + heuristic[neighbor], neighbor, path))

        return None

# Example usage:
if __name__ == "__main__":
    # Create a sample graph
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'E', 3)
    g.add_edge('D', 'E', 1)
    g.add_edge('D', 'F', 7)
    g.add_edge('E', 'G', 2)
    g.add_edge('F', 'G', 1)

    # Heuristic function (estimated cost from each node to the goal)
    heuristic = {'A': 7, 'B': 6, 'C': 2, 'D': 1, 'E': 4, 'F': 5, 'G': 0}

    start_node = 'A'
    goal_node = 'G'

    path = g.a_star_search(start_node, goal_node, heuristic)

    if path:
        print(f"Shortest path from {start_node} to {goal_node}: {path}")
    else:
        print(f"No path found from {start_node} to {goal_node}")
