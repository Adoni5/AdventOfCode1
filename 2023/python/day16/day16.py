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

# P2
# x, y of min and max row
min_x, min_y = min(x for x, _ in grid.keys()), min(y for _, y in grid.keys())
max_x, max_y = max(x for x, _ in grid.keys()), max(y for _, y in grid.keys())
# starts = [(x, y) for x in range()]
starts = [(-1, y, (1, 0)) for y in range(max_y + 1)]
starts.extend([(max_x + 1, y, (-1, 0)) for y in range(max_y + 1)])
starts.extend([(y, -1, (0, 1)) for y in range(max_y + 1)])
starts.extend([(y, max_x + 1, (0, -1)) for y in range(max_y + 1)])
# Add corners
# start
print(starts)
max_en = -1
for start_x, start_y, d in starts:
    i = 0
    start = deque([(start_x, start_y, d, None)])

    visited = set()
    cache = set()
    while i < 10000000 and start:
        x = start.popleft()
        # print(f"xey {x}")
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
        # print()
        # print(len(visited))
    max_en = max(max_en, len(visited))
print(max_en)
