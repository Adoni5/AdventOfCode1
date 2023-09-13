test_input = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""
# 10L5L7L3R1L10L"""

# 10L5L5R10L4R5L5"""
print(test_input.split("\n\n"))

from math import inf
from itertools import zip_longest
from support import Grid, get_input
import re

# test_input = get_input(22, strip=False)
grid, instructions = test_input.split("\n\n")
g = Grid.read_grid(grid, skip=" ")
# print(g.grid)

lookup = {"L": -90, "R": 90, "NA": 0}
lookup_direction = {90: (1, 0), 180: (0, 1), 270: (-1, 0), 0: (0, -1)}
direction = 90
final_dir = {0: 3, 90: 0, 180: 1, 270: 2}

pos = g.find_item(".")
# print(pos)
pat = re.compile(r"(\d+)")
pat2 = re.compile(r"([RL])")


for dist, turn in zip_longest(map(int,pat.findall(instructions)), pat2.findall(instructions), fillvalue="NA"):
    # print(dist, turn)
    dx, dy = lookup_direction[direction]
    for _ in range(dist):
        x, y = pos
        nx, ny = (x + dx, y + dy)
        # print(nx, ny, dx, dy)
        minx, maxx = g.row_bounds(ny) if dx != 0 else (0, inf)
        # print(minx, maxx)
        miny, maxy = g.column_bounds(nx) if dy != 0 else (0 ,inf)
        # print(miny, maxy)
        # print(f"old nx, ny {nx}, {ny}")

        if minx > nx and dx != 0:
            nx = maxx
        elif nx > maxx and dx != 0:
            nx = minx
        elif miny > ny and dy != 0:
            ny = maxy
        elif maxy < ny and dy != 0:
            ny = miny

        # print(f"new nx, ny {nx}, {ny}")
        if g.grid[(nx, ny)] != "#":

            x = nx
            y = ny
        pos = (x, y)
        # print(f"pos {pos}")
    # factor = -1 if 360 > direction >= 180 else 1
    # print(factor)
    direction = (direction + (lookup[turn])) % 360
    # print(direction)

for (x, y) in g.grid.keys():
    x1, x2 = g.row_bounds(y)
    y1, y2 = g.column_bounds(x)
    

# print(sum(((pos[0] + 1) * 4, (pos[1] + 1) * 1000, final_dir[direction])))
# test input 4 x 4
# wrap = {}
# def edge(face1, dir1, exit, face2, dir2, enter, rot):
#   for k in range(4):
#     p1 = (face1[0] + dir1[0] * k, face1[1] + dir1[1] * k)
#     p2 = (face2[0] + dir2[0] * k, face2[1] + dir2[1] * k)
#     wrap[(p1[0] + exit[0], p1[1] + exit[1])] = (p2, rot)
#     wrap[(p2[0] + enter[0], p2[1] + enter[1])] = (p1, -rot)

# # Front:
# edge((0, 4), (1, 0), (0, -1), (4, 0), (-1, 0), (0, -1), 180) # Left
# edge((0, 50), (0, 1), (-1, 0), (150, 0), (1, 0), (0, -1), 90) # Top

# # Right:
# edge((49, 100), (0, 1), (1, 0), (50, 99), (1, 0), (0, 1), 180) # Under
# edge((0, 100), (0, 1), (-1, 0), (199, 0), (0, 1), (1, 0), 0) # Top
# edge((0, 149), (1, 0), (0, 1), (149, 99), (-1, 0), (0, 1), 90) # Back

# # Under:
# edge((50, 50), (1, 0), (0, -1), (100, 0), (0, 1), (-1, 0), 270) # Left

# # Back:
# edge((149, 50), (0, 1), (1, 0), (150, 49), (1, 0), (0, 1), 90) # Top
# print(wrap[(62, -1)])
# print(wrap)


# for dist, turn in zip_longest(map(int,pat.findall(instructions)), pat2.findall(instructions), fillvalue="NA"):
#     dx, dy = lookup_direction[direction]
#     for _ in range(dist):
#         x, y = pos
#         nx, ny = (x + dx, y + dy)
#         # print(nx, ny, dx, dy)
#         minx, maxx = g.row_bounds(ny) if dx != 0 else (0, inf)
#         # print(minx, maxx)
#         miny, maxy = g.column_bounds(nx) if dy != 0 else (0 ,inf)
#         # print(miny, maxy)
#         # print(f"old nx, ny {nx}, {ny}")

#         if (nx,ny) in wrap:
#             (nx,ny),new_direction = wrap[(nx,ny)]
#             direction = (direction + new_direction)
#         # if minx > nx and dx != 0:
#         #     nx = maxx
#         # elif nx > maxx and dx != 0:
#         #     nx = minx
#         # elif miny > ny and dy != 0:
#         #     ny = maxy
#         # elif maxy < ny and dy != 0:
#         #     ny = miny

#         # print(f"new nx, ny {nx}, {ny}")
#         if g.grid[(nx, ny)] != "#":

#             x = nx
#             y = ny
#         pos = (x, y)
#         # print(f"pos {pos}")
#     # factor = -1 if 360 > direction >= 180 else 1
#     # print(factor)
#     direction = (direction + (lookup[turn])) % 360
    # print(direction)