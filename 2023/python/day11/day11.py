test_input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
from collections import deque
from itertools import combinations
from support import get_input

test_input = get_input(11, 2023)

empty_rows, empty_cols = [], []
for index, line in enumerate(test_input.splitlines()):
    if "#" not in line:
        empty_rows.append(index)

for index, line in enumerate(zip(*test_input.splitlines())):
    if "#" not in line:
        empty_cols.append(index)

expansion = 1000000
galaxies = []
for y, line in enumerate(test_input.splitlines()):
    for x, char in enumerate(line):
        if char == "#":
            ay, ax = 0, 0
            for dy in empty_rows:
                if y > dy:
                    ay += expansion - 1
            for dx in empty_cols:
                if x > dx:
                    ax += expansion - 1

            galaxies.append((x + ax, y + ay))


def manhattan(X1, Y1, X2, Y2):
    dist = abs(X2 - X1) + abs(Y2 - Y1)
    return dist


print(galaxies)

# Potentially add bounds
# d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
# pos = deque([start])
# visited = set()
# while pos:
#     x, y = pos.popleft()
#     for dx, dy in d:
#         nx, ny = x + dx, y + dy
#         if nx, ny
print(sum(manhattan(*start, *end) for start, end in combinations(galaxies, 2)))
