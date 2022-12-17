from itertools import cycle, groupby
from pprint import pprint
import sys
import time
from support import get_input
from tqdm import tqdm
from collections import defaultdict

rock_types = """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
"""

test_input = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""
print(len(test_input))
d = defaultdict(list)
# test_input = get_input("17")
rock_coords = []
for rock in rock_types.split("\n\n"):
    rock_coord = []
    for y, line in enumerate(rock.splitlines()[::-1]):
        for x, char in enumerate(line):
            if char == "#":
                rock_coord.append((x + 2,y))
    print(rock_coord)
    rock_coords.append(rock_coord)

def print_rocks(rocks: set[tuple[int, int]], cur_rock = []):
    if rocks:
        y_min, y_max = min(xy[1] for xy in iter(rocks)), max(xy[1] for xy in iter(rocks)) + 8
        grid = [["."]*7 for _ in range(y_max+1-y_min)]
        for x, y in iter(rocks):
            grid[y][x] = "#"
    else:
        y_min, y_max = min(xy[1] for xy in cur_rock), max(xy[1] for xy in cur_rock)
        if y_min < 0:
            return None
        grid = [["."]*7 for _ in range(y_max+1-0)]

    for x, y in cur_rock:
        grid[y][x] = "#"
    print("\n"+"\n".join(["".join(list(map(str, p))) for p in grid[::-1]]))
    # pprint(grid[::-1])

hp = -1
floor = 0
lw = 0
rw = 7
rocks = set()
rocks.add((-1, -1))
print(rocks)
# begin
jets = cycle(test_input)
rocks_4eva = cycle(rock_coords)
# for rock in rock_coords:
    # print(rock)

    # print(low_points)
stop_p1 = 2022
target = 1000000000000
heights = []
# sys.exit("dja")
for i, rock in tqdm(enumerate(rocks_4eva, start=0), total = target):
    # print("\n BEGIN")
    # print(rock)
    # print(i)
    if i == stop_p1:
        print_rocks(rocks)
        # break
    rl = min(x[0] for x in rock)
    rr = max(x[0] for x in rock)
    rt = max(xy[1] for xy in rock )
    rock = [(x, y+ hp + 4) for x, y in rock]
    # print(hp)
    # print(rock)
    # print_rocks(rocks, cur_rock=rock)

    # jet me baby
    for n, j in enumerate(jets):
        # print(j)
        # print(j)
                # make a key where we check the position based on the bottom of the leftmost piece, (so y=0 to 3), the index of the jet and rock type (i % 5)
        key = ( i % 5, n % 40)
        if key in d:
            period = i - d[key][0]
            if i % period == target % period:
                p2 = d[key][1] + (hp+1 - d[key][1])*(((target-n)//period)+1)
                break
        else:
            d[key] = (i, hp + 1)
        shift = 1 if j == ">" else -1
        # print(shift)
        trl = rl + shift
        trr = rr + shift
        # print(trl, trr)
        # you ain't going nowhere but down
        if any((trl < lw, trr >= rw, set([(xy[0]+shift, xy[1]) for xy in rock]).intersection(rocks))):
            # print("down")
            rock = [(x, y - 1) for x, y in rock]
            # print(rock)
        else:
            # print("shift n down")
            rl, rr = trl, trr
            # shift the rock in the correct direction
            rock = [(x + shift, y - 1) for x, y in rock]
            # print(rock)
        # print_rocks(rocks, cur_rock=rock)

        
        # we as low as we can go
        # seen = set()
        low_points = []

        for x, xy in groupby(sorted(rock, key=lambda x: x[0]), key=lambda x: x[0]):
            g = list(xy)
            for _xy in g:
                # print(_xy)
                if _xy[1] == min(__xy[1] for __xy in g):
                    # print(_xy)
                    low_points.append(_xy)
                    # seen
        # print(low_rocks)
        # print(f"rock bottom y is {min(xy[1] for xy in rock)}")
        # print(f"bottom in rocks {any(xy in rocks for xy in low_rocks )}")
        if min(xy[1] for xy in rock) < floor or any((xy in rocks for xy in low_points )):
            # print("broken")
            x, y = rock[0]
            # print(i)

            rocks.update({(x, y+1) for x, y in rock})
            hp = max(xy[1] for xy in iter(rocks) )
            heights.append(hp)
            # print(hp - y )
            k1 = (x, hp - y)

            # d[key].append((i, hp+1))
            # print(d)
            break
        # time.sleep(0.25)
print(hp + 1)
print(p2)
# pprint(d)
# for i, (k, v) in enumerate(d.items()):
#     if len(v) >= 2:
#         it = iter(v)
#         print(v)
#         x, dy = next(it)
#         x2, dy2 = next(it)
#         cycle_len, cycle_height = x2 - x, dy2 - dy
#         break
#     if i <= 10:
#         print(k, v)

# maybe = target // cycle_len
# maybe += heights[target % cycle_len]
# print(1514285714288 - maybe)
# print(maybe)