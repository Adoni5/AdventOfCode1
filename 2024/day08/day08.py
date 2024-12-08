test_input = """##....#....#
.#.#....0...
..#.#0....#.
..##...0....
....0....#..
.#...#A....#
...#..#.....
#....#.#....
..#.....A...
....#....A..
.#........#.
...#......##"""

from itertools import permutations
from collections import defaultdict

with open("input.txt") as fh:
    test_input = fh.read()

bc, br = None, -1
g = defaultdict(list)
for r, line in enumerate(test_input.splitlines()):
    bc = len(line) - 1
    for c, x in enumerate(line.strip()):
        if x != "." and x != "#":
            g[x].append((c, r))
    br += 1

t = 0
antinodes = set()
antinodes_p2 = set()
for an in g.keys():

    p = permutations(g[an], 2)
    for (x1, y1), (x2, y2) in p:
        antinodes_p2.add((x1, y1))
        antinodes_p2.add((x2, y2))
        dx, dy = x1 - x2, y1 - y2
        node = (x1 + dx, y1 + dy)
        if node[0] < 0 or node[0] > bc or node[1] < 0 or node[1] > br:
            continue
        antinodes_p2.add(node)
        while True:
            node = (node[0] + dx, node[1] + dy)
            if node[0] < 0 or node[0] > bc or node[1] < 0 or node[1] > br:
                break
            antinodes_p2.add(node)

        antinodes.add(node)

print(len(antinodes))
print(len(antinodes_p2))
