test_input = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

import heapq
from collections import defaultdict, deque
from pprint import pprint

with open("input.txt") as fh:
    test_input = fh.read()
g = {}
q = []
end = None
for r, line in enumerate(test_input.splitlines()):
    for c, x in enumerate(line.strip()):
        if x == "S":
            heapq.heappush(q, (0, c, r, (-1, 0), 0, 0))
            x = "."
        if x == "E":
            end = (c, r)
        g[(c, r)] = x

lscore = 20000000
_rot_clock = {(-1, 0): (0, -1), (0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0)}
_rot_anti = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}
fin = []
visited = set()
paths = defaultdict(list)
while q:
    score, c, r, d, st, ro = heapq.heappop(q)
    if score > lscore:
        continue
    if (c, r, d) in visited:
        continue
    visited.add((c, r, d))
    if g.get((c, r)) == "E":
        print(st, ro, score)
        lscore = min(lscore, score)
        continue
    dc, dr = d
    nc, nr = c + dc, r + dr
    nn = g.get((nc, nr))

    for rot in (_rot_clock[d], _rot_anti[d]):
        rs = score + 1000
        paths[(c, r, rs, rot)].append((c, r, score, d))
        heapq.heappush(q, (rs, c, r, rot, st, ro + 1))
    if nn != "#":
        heapq.heappush(q, (score + 1, nc, nr, d, st + 1, ro))
        paths[(nc, nr, score + 1, d)].append((c, r, score, d))

print(lscore)
path = set()
test = [
    (*end, lscore, (1, 0)),
    (*end, lscore, (0, -1)),
]
while test:
    c, r, s, d = test.pop()
    path.add((c, r))
    for state in paths[(c, r, s, d)]:
        test.append(state)
print(len(path))
