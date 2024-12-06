test_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

from collections import deque

with open("input.txt") as fh:
    test_input = fh.read()

g = {}
start = (0, 0)
for r, line in enumerate(test_input.strip().splitlines()):
    for c, n in enumerate(line):
        if n == "^":
            start = (c, r)
        g[c, r] = n
# print(start)
check = []
ds = deque([(0, -1), (1, 0), (0, 1), (-1, 0)])

visited = set()
visited.add((start[0], start[1], ds[0][0], ds[0][1]))
c, r = start
while True:
    dc, dr = ds[0]
    nc, nr = c + dc, r + dr
    if (nc, nr, dc, dr) in visited:
        break
    if g.get((nc, nr), "X") != "#":
        if g.get((nc, nr), "X") == "X":
            break
        visited.add((nc, nr, dc, dr))
        check.append((nc, nr))
        c, r = nc, nr
    else:
        # print("\n".join([f"{a}, {b}" for a, b in check]))
        check = []
        # print()
        ds.rotate(-1)

print(visited)
print(len(set((a, b) for a, b, _, _ in visited)))
