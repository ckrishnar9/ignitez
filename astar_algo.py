import heapq  # Importing the heapq module for heap-based priority queue

class Node:
    """
    Represents a node in the search space.
    """
    def __init__(self, position, g=0, h=0, parent=None):
        """
        Initializes a new Node object.

        Args:
          position: Tuple representing the (x, y) coordinates of the node.
          g: The cost from the start node to this node.
          h: The heuristic estimate of the cost from this node to the goal.
          parent: The parent Node object in the search path.
        """
        self.position = position  # Store the (x, y) coordinates of the node
        self.g = g              # Cost from the start node to this node
        self.h = h              # Heuristic estimate of the cost from this node to the goal
        self.f = g + h          # Total estimated cost (f = g + h)
        self.parent = parent    # The parent node in the search path

    def __lt__(self, other):
        """
        Compares two nodes based on their total cost (f).

        This method is used for heap comparisons, ensuring that nodes 
        with lower 'f' values have higher priority in the priority queue.

        Args:
          other: The other Node object to compare with.

        Returns:
          True if this node's 'f' value is less than the other node's 'f' value, False otherwise.
        """
        return self.f < other.f  # Compare nodes based on their total cost (f)

def heuristic(a, b):
    """
    Calculates the Manhattan distance heuristic between two points.

    Args:
      a: Tuple representing the (x, y) coordinates of the first point.
      b: Tuple representing the (x, y) coordinates of the second point.

    Returns:
      The Manhattan distance between the two points.
    """
    return abs(b[0] - a[0]) + abs(b[1] - a[1])  # Manhattan distance calculation

def get_neighbors(node, grid):
    """
    Gets the valid neighbors of a node in the grid.

    Args:
      node: The Node object for which to find neighbors.
      grid: A 2D list representing the grid, where 1 represents obstacles.

    Returns:
      A list of tuples representing the (x, y) coordinates of valid neighbors.
    """
    neighbors = []
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Check in all 4 directions
        x, y = node.position[0] + dx, node.position[1] + dy  # Calculate neighbor coordinates
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 1:  # Check if neighbor is within grid bounds and not an obstacle
            neighbors.append((x, y))  # Add valid neighbor to the list
    return neighbors

def astar(start, goal, grid):
    """
    Performs the A* search algorithm to find a path from start to goal.

    Args:
      start: Tuple representing the (x, y) coordinates of the start position.
      goal: Tuple representing the (x, y) coordinates of the goal position.
      grid: A 2D list representing the grid, where 1 represents obstacles.

    Returns:
      A list of tuples representing the (x, y) coordinates of the path if found, None otherwise.
    """
    start_node = Node(start, h=heuristic(start, goal))  # Create the starting node with initial heuristic
    open_list = [start_node]  # Initialize the open list (priority queue) with the starting node
    closed_set = set()  # Initialize the closed set (visited nodes)

    while open_list:  # Continue searching while there are nodes in the open list
        current_node = heapq.heappop(open_list)  # Get the node with the lowest 'f' value from the open list

        if current_node.position == goal:  # Check if the goal is reached
            path = []  # Initialize an empty list to store the path
            while current_node:  # Backtrack from the goal node to the start node
                path.append(current_node.position)  # Add the current node's position to the path
                current_node = current_node.parent  # Move to the parent node
            return path[::-1]  # Return the reversed path (from start to goal)

        closed_set.add(current_node.position)  # Add the current node to the closed set

        for neighbor_pos in get_neighbors(current_node, grid):  # Iterate over the neighbors of the current node
            if neighbor_pos in closed_set:  # Skip if the neighbor is already in the closed set
                continue

            neighbor = Node(neighbor_pos,  # Create a new node for the neighbor
                            g=current_node.g + 1,  # Calculate the 'g' value of the neighbor
                            h=heuristic(neighbor_pos, goal),  # Calculate the 'h' value of the neighbor
                            parent=current_node)  # Set the parent of the neighbor

            if neighbor not in open_list:  # If the neighbor is not in the open list
                heapq.heappush(open_list, neighbor)  # Add the neighbor to the open list
            else:  # If the neighbor is already in the open list
                idx = open_list.index(neighbor)  # Find the index of the neighbor in the open list
                if open_list[idx].g > neighbor.g:  # If the new path to the neighbor is shorter
                    open_list[idx] = neighbor  # Update the neighbor in the open list
                    heapq.heapify(open_list)  # Re-heapify the open list to maintain the heap property

    return None  # No path found

# Example usage
grid = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]
start = (0, 0)  # Starting position
goal = (4, 4)   # Goal position

path = astar(start, goal, grid)  # Call the A* search function
print("Path found:", path)  # Print the path found
