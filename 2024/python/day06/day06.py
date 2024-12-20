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
obstacles = []
loop = True
it = deque(g.keys())
while loop:
    c, r = start
    ds = deque([(0, -1), (1, 0), (0, 1), (-1, 0)])
    visited = set()
    visited.add((start[0], start[1], ds[0][0], ds[0][1]))
    og = None
    if it:
        obs = it.popleft()
        og = g.get(obs)
        g[obs] = "#"
    else:
        break
    while True:
        dc, dr = ds[0]
        nc, nr = c + dc, r + dr
        if (nc, nr, dc, dr) in visited:
            obstacles.append(obs)
            break
        if g.get((nc, nr), "X") != "#":
            if g.get((nc, nr), "X") == "X":
                # print(f"left map with new obstacle at {obs} ")
                break
            visited.add((nc, nr, dc, dr))
            c, r = nc, nr
        else:
            ds.rotate(-1)
    g[obs] = og

# print(visited)
print(len(set((a, b) for a, b, _, _ in visited)))

print(obstacles)
print(len(obstacles))
