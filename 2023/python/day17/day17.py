test_input = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""
from collections import deque
import heapq
from support import get_input

# test_input = get_input(17, 2023)


from collections import deque


def get_neighbors(position):
    x, y = position
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    return [(x + dx, y + dy, (dx, dy)) for dx, dy in directions]


def is_valid_move(current_direction, current_count, new_direction):
    if current_direction is None:  # First move
        return True
    if (
        current_direction == new_direction and current_count == 4
    ):  # Change direction after 3 moves
        return False
    if current_direction == (-new_direction[0], -new_direction[1]):
        return False
    return True


def shortest_path_with_constraints(grid):
    start = (0, 0)
    end = max(grid.keys())
    print(end)
    queue = deque([(start, 0, None, 0, [])])  # Position, weight, direction, count, path

    visited = {}
    ends = []

    while queue:
        position, weight, direction, count, path = queue.popleft()

        if (position, direction) in visited and visited[(position, direction)] <= count:
            continue
        if position == end:
            return weight, path

        visited[(position, direction)] = count

        for x, y, new_direction in get_neighbors(position):
            if (x, y) in grid and is_valid_move(direction, count, new_direction):
                path.append((x, y))
                new_count = count + 1 if new_direction == direction else 0
                new_weight = weight + grid[x, y]
                queue.append(((x, y), new_weight, new_direction, new_count, path))

    return ends


# Parsing the grid from the input
grid = {
    (x, y): int(weight)
    for y, line in enumerate(test_input.splitlines())
    for x, weight in enumerate(line)
}

# Calculate the shortest path
shortest_path_weight = shortest_path_with_constraints(grid)
print(shortest_path_weight)
