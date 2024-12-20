test_input = """AAAA
BBCD
BBCC
EEEC"""

with open("input.txt") as fh:
    test_input = fh.read()
g = {}
from collections import deque
from pprint import pprint

for r, l in enumerate(test_input.splitlines()):
    for c, n in enumerate(l):
        g[(c, r)] = n
# print(g)
s = 0
d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
ans = {}
visited_ = set()
for (c, r), content in g.items():
    visited = set()
    if (c, r) in visited_:
        continue
    perimeter = 0
    region = 1
    q = deque([(c, r)])
    while q:
        # print(q)
        c, r = q.popleft()
        visited.add((c, r))
        term = True
        for dc, dr in d:
            nc, nr = c + dc, r + dr
            if (nc, nr) in visited:
                continue
            if g.get((nc, nr), "*") != content:
                # print(content, c, r)
                # print(g.get((nc, nr), "*"))
                # print(f"{content}, perim + 1 for {c}, {r}")
                perimeter += 1
            else:
                term = False
                # print(
                #     f"incrementing region for {content}, ({c, r}) by visiting {nc}, {nr}"
                # )
                region += 1
                visited.add((nc, nr))
                visited_.add((nc, nr))
                q.append((nc, nr))
        if term:
            visited.add((c, r))
            # visited_.add((nc, nr))
    # print(content, region, perimeter, c, r)
    s += region * perimeter
    ans[content] = (region, perimeter)
print(s)
pprint(ans)
