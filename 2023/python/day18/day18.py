test_input = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""

import re
from collections import deque
import numpy as np
from support import get_input

test_input = get_input(18, 2023)

holes = {(0, 0): None}
l = {"U": (0, -1), "R": (1, 0), "D": (0, 1), "L": (-1, 0)}

pat = re.compile(r"([UDLR]) (\d+) \((#\w+)")
for line in test_input.splitlines():
    d, n, c = pat.findall(line)[0]
    n = int(n)
    dx, dy = l[d]
    sx, sy = list(holes.keys())[-1]
    for i in range(n):
        sx += dx
        sy += dy
        holes[(sx, sy)] = c
# Lol I hope this is enclosed
start = deque([(1, 1)])
visited = set((1, 1))
while start:
    sx, sy = start.popleft()
    for dx, dy in l.values():
        nx, ny = sx + dx, sy + dy
        if (nx, ny) not in holes and (nx, ny) not in visited:
            visited.add((nx, ny))
            start.append((nx, ny))
print(len(visited) + len(holes) - 1)


# Part 2
# Ohfuck
# JFC
# i think this wil lwork with the shoelace formula? and picks apparently
# https://stackoverflow.com/questions/24467972/calculate-area-of-polygon-given-x-y-coordinates
def PolyArea(x, y):
    return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


start = (0, 0)
boundary = 0
xs = []
ys = []
l = {3: (1, 0), 0: (0, 1), 1: (-1, 0), 2: (0, -1)}

for line in test_input.splitlines():
    d, n, c = pat.findall(line)[0]
    d = l[int(c[-1])]  # Hexadecimal baaby
    n = int(c[1:-1], 16)

    boundary += n
    start = (start[0] + n * d[0], start[1] + n * d[1])
    xs.append(start[0])
    ys.append(start[1])

A = PolyArea(xs, ys)
b = boundary
# A = i + b/2 - 1 -> i = A + 1 - b/2
I = A + 1 - b // 2
print(I + b)
