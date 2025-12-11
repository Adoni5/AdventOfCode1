import sys

g = {}
for r, line in enumerate(sys.stdin.readlines()):
    for c, space in enumerate(line):
        if space == "@":
            g[(c, r)] = space
ds = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]

p1 = 0
for (c, r), space in g.items():
    friends = 0
    for dc, dr in ds:
        n = c + dc, r + dr
        if g.get(n):
            friends += 1
    if friends < 4:
        print(c, r)
        p1 += 1
print(p1)