class Node:
    def __init__(self, position, parent=None, cost=0, heuristic=0):
        self.position = position
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
        self.total_cost = cost + heuristic

def heuristic_estimate(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def get_neighbors(node):
    x, y = node.position
    neighbors = [(x + 2, y + 1), (x + 2, y - 1), (x - 2, y + 1), (x - 2, y - 1),
                 (x + 1, y + 2), (x + 1, y - 2), (x - 1, y + 2), (x - 1, y - 2)]
    return [(x, y) for (x, y) in neighbors if 1 <= x <= 8 and 1 <= y <= 8]

def get_obstacles_from_user():
    obstacles = []
    num_obstacles = int(input("Enter the number of obstacles: "))
    for i in range(num_obstacles):
        x = int(input(f"Enter x-coordinate for obstacle {i + 1}: "))
        y = int(input(f"Enter y-coordinate for obstacle {i + 1}: "))
        obstacles.append((x, y))
    return obstacles

def a_star(start, goal, obstacles):
    open_set = [Node(start, None, 0, heuristic_estimate(start, goal))]
    closed_set = set()

    while open_set:
        current_node = min(open_set, key=lambda node: node.total_cost)

        if current_node.position == goal:
            path = []
            while current_node:
                path.insert(0, current_node.position)
                current_node = current_node.parent
            return path

        open_set.remove(current_node)
        closed_set.add(current_node.position)

        for neighbor_position in get_neighbors(current_node):
            if neighbor_position not in obstacles and neighbor_position not in closed_set:
                neighbor = Node(neighbor_position, current_node, current_node.cost + 1, heuristic_estimate(neighbor_position, goal))

                if neighbor not in open_set or neighbor.total_cost < open_set[open_set.index(neighbor)].total_cost:
                    open_set.append(neighbor)

    return None

# Get obstacles from the user
obstacles = get_obstacles_from_user()

# Example start and goal
start = (1, 1)
goal = (8, 8)

# Find the path
path = a_star(start, goal, obstacles)

# Print the result
if path:
    print("Path found:", path)
else:
    print("No path found.")
