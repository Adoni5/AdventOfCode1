from collections import deque
from support import get_input
import sys

test_input = rf""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""
test_input = get_input("16", 2023)
grid = {}
for y, row in enumerate(test_input.splitlines()):
    for x, char in enumerate(row):
        grid[(x, y)] = char
print(grid)
start = deque([(-1, 0, (1, 0), None)])
print(start)
cache = {}
dirs = {
    "|": lambda x: ((0, 1), (0, -1)),
    "-": lambda x: ((1, 0), (-1, 0)),
    "\\": lambda x: [(x[1], x[0])],
    "/": lambda x: [(-x[1], -x[0])],
}
i = 0
visited = set()
cache = set()
while i < 10000000 and start:
    x = start.popleft()
    print(x)
    x, y, (dx, dy), prev = x
    nx, ny = x + dx, y + dy
    # print(f"GOing to {(nx, ny)}")
    if (nx, ny) in grid:
        if (nx, ny, x, y, dx, dy, prev) in cache:
            continue
        cache.add((nx, ny, x, y, dx, dy, prev))
        visited.add((nx, ny))
        new_char = grid[(nx, ny)]
        # don#t bounce back and forth
        # print(new_char)
        if new_char in "|-" and prev == new_char:
            new_dirs = ((dx, dy),)
        else:
            new_dirs = dirs.get(new_char, lambda x: [(dx, dy)])((dx, dy))
        # print(f"new _dir {new_dirs}")
        for new_dir in new_dirs:
            start.append((nx, ny, new_dir, new_char if new_char != "." else prev))
    i += 1
    print()
    print(len(visited))
    # if len(visited) == 46:
    #     print(i)
    #     break
    # input()
print(len(visited))
