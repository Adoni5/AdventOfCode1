test_input = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""
from heapq import heappush, heappop
from itertools import combinations

with open("input.txt") as fh:
    test_input = fh.read()
g = {}
start, end = None, None
for r, l in enumerate(test_input.splitlines()):
    for c, n in enumerate(l):
        g[(c, r)] = n
        if n == "S":
            start = (c, r)
        if n == "E":
            end = (c, r)

ds = ((-1, 0), (0, -1), (1, 0), (0, 1))
q = []
heappush(q, (0, *start))
visited = set()
no_cheat = 0
dists = {}
while q:
    s, c, r = heappop(q)
    if (c, r) in visited:
        continue
    visited.add((c, r))
    dists[(c, r)] = s
    if (c, r) == end:
        print(s)
        no_cheat = s
        break
    for dc, dr in ds:
        nc, nr = c + dc, r + dr
        if g.get((nc, nr)) != "#":
            heappush(q, (s + 1, nc, nr))
from collections import Counter
from pprint import pprint


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


cheats = []
cheats_2 = 0
for ((ac, ar), d1), ((bc, br), d2) in combinations(dists.items(), 2):
    # manhattan distance between nodes

    d = manhattan_distance(ac, ar, bc, br)
    if d == 2 and (d2 - d1 - d) >= 100:
        print("cheating scum")
        cheats.append(d2 - d1 - d)
    if d <= 20 and (d2 - d1 - d) >= 100:
        cheats_2 += 1

print(len(cheats))
# pprint(dict(sorted(Counter(cheats).items())))
print(cheats_2)
