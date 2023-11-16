# A-Star-algorithm

# Pathfinding with A* Algorithm

This repository contains a simple implementation of the A* algorithm for pathfinding on a chessboard-like grid. The program finds a path from a starting point to a goal point while considering obstacles.

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/a-star-pathfinding.git
    cd a-star-pathfinding
    ```

2. **Run the program:**

    ```bash
    python pathfinding.py
    ```

    Follow the prompts to input the number and coordinates of obstacles, as well as the starting and ending points.

3. **View the result:**

    The program will output whether a path is found or not, and if a path is found, it will print the coordinates of the path.

## Example

```python
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
