test_input = """AAAA
BBCD
BBCC
EEEC"""

# with open("input.txt") as fh:
#     test_input = fh.read()
g = {}
from collections import defaultdict, deque
from pprint import pprint

for r, l in enumerate(test_input.splitlines()):
    for c, n in enumerate(l):
        g[(c, r)] = n
# print(g)
s = 0
d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
ans = {}
ans_p2 = 0
visited_ = set()
for (c, r), content in g.items():
    visited = set()
    if (c, r) in visited_:
        continue
    perimeter = 0
    region = 1
    q = deque([(c, r)])
    plot = {(c, r): content}

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
                perimeter += 1
            else:
                term = False
                plot[(nc, nr)] = content
                region += 1
                visited.add((nc, nr))
                visited_.add((nc, nr))
                q.append((nc, nr))
        if term:
            visited.add((c, r))
            # visited_.add((nc, nr))
    # part 2

    print(plot)
    v = set()
    width = height = 0

    w0 = min(x[0] for x in plot.keys())
    width = max(x[0] for x in plot.keys()) - w0
    h0 = min(x[1] for x in plot.keys())
    height = max(x[1] for x in plot.keys()) - h0
    # go alow top points
    top_points = []
    for i in range(width + 1):
        top_points.append(min(k for k in plot.keys() if k[0] == w0 + i))
    print(top_points)
    left_points = []
    # print(content, region, perimeter, c, r)
    s += region * perimeter
    ans[content] = (region, perimeter)
print(s)
