from collections import defaultdict
import heapq

class Graph:
    def __init__(self):
        self.nodes = defaultdict(list)
        self.distances = {}
    
    def add_edge(self, from_node, to_node, distance):
        # Add edges to the graph (bidirectional)
        self.nodes[from_node].append(to_node)
        self.nodes[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance

def dijkstra(graph, initial):
    # Initialize distances dictionary with infinity for all nodes except the start
    distances = {node: float('infinity') for node in graph.nodes}
    distances[initial] = 0
    
    # Initialize priority queue and path tracking
    pq = [(0, initial)]
    previous = {node: None for node in graph.nodes}
    visited = set()

    while pq:
        # Get the node with minimum distance
        current_distance, current_node = heapq.heappop(pq)
        
        # If we've already visited this node, skip it
        if current_node in visited:
            continue
            
        # Mark node as visited
        visited.add(current_node)
        
        # Check all neighboring nodes
        for neighbor in graph.nodes[current_node]:
            if neighbor in visited:
                continue
                
            # Calculate new distance to neighbor
            distance = current_distance + graph.distances[(current_node, neighbor)]
            
            # If we found a shorter path, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    return distances, previous

def get_shortest_path(previous, start, end):
    path = []
    current_node = end
    
    # Reconstruct path from end to start
    while current_node is not None:
        path.append(current_node)
        current_node = previous[current_node]
        
    # Return reversed path (from start to end)
    return path[::-1]

# Example usage
def create_example_graph():
    g = Graph()
    
    # Add edges with weights
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 1)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 8)
    g.add_edge('C', 'E', 10)
    g.add_edge('D', 'E', 2)
    g.add_edge('D', 'F', 6)
    g.add_edge('E', 'F', 3)
    
    return g

# Run the algorithm
graph = create_example_graph()
start_node = 'A'
end_node = 'F'

distances, previous = dijkstra(graph, start_node)
shortest_path = get_shortest_path(previous, start_node, end_node)

print(f"Shortest distances from {start_node}: {distances}")
print(f"Shortest path from {start_node} to {end_node}: {' -> '.join(shortest_path)}")