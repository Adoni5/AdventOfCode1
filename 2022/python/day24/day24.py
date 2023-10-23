test_input = """#.#####
#.....#
#>....#
#.....#
#...v.#
#.....#
#####.#"""
import heapq
from support import Grid

g = Grid.read_grid(test_input)
_dots = g.find_all_items(".")
start, end = _dots[0], _dots[-1]
print(start, end)


def shortest_path(grid, start, end):
    if not grid or not start or not end:
        return None

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    def is_valid(x, y):
        return (x, y) in grid and grid[(x, y)] == "."

    dist = {key: float("inf") for key in grid}
    dist[start] = 0
    pq = [(0, start)]  # priority queue initialized with start point

    while pq:
        current_dist, (x, y) = heapq.heappop(pq)

        # If the end point is reached, return the distance
        if (x, y) == end:
            return current_dist

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if is_valid(new_x, new_y):
                new_dist = current_dist + 1
                if new_dist < dist[(new_x, new_y)]:
                    dist[(new_x, new_y)] = new_dist
                    heapq.heappush(pq, (new_dist, (new_x, new_y)))

    # If end is not reachable, return None
    return None


def blizzard_blow(
    blizzards: dict[tuple[int, int], str], directions: dict[str, tuple[int, int]]
):
    """move blizzard about"""
    for coords, direction in blizzards.items():
        dx, dy = directions[direction]
        yield coords, (coords[0] + dx, coords[1] + dy)


blizzards = g.find_all_items(
    ">",
    "^",
    "<",
    "v",
    return_value=True,
)
directions = {">": (1, 0), "^": (0, -1), "<": (-1, 0), "v": (0, 1)}
print(blizzards)
print(shortest_path(g.grid, start, end))
