test_input = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""
from collections import deque
from support import get_input

test_input = get_input(21, 2023)
rocks = set()
start = 0
for y, line in enumerate(test_input.splitlines()):
    for x, char in enumerate(line):
        if char == "#":
            rocks.add((x, y))
        if char == "S":
            start = (x, y)


print(start)
can_reach = deque([start])
ds = [(0, 1), (1, 0), (-1, 0), (0, -1)]
i = 1
for i in range(64):
    new_spaces = set()
    to_take = deque()
    while can_reach:
        x, y = can_reach.popleft()
        # print(x, y)
        for dx, dy in ds:
            nx, ny = x + dx, y + dy
            # print(nx, ny, dx, dy)
            if (nx, ny) not in rocks and (nx, ny) not in new_spaces:
                # print(f"adding {nx, ny}")
                to_take.append((nx, ny))
                new_spaces.add((nx, ny))
        i += 1
        # print(can_reach)
    can_reach = to_take
print(len(can_reach))
