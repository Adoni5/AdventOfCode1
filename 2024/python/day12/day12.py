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
    p2_q = deque([plot])
    while plot:
        c, r = plot.popleft()
        pu = pd = pl = pr = 0
        for dc, dr in d:
            _c, _r = c, r
            while True:
                nc, nr = _c + dc, _r + dr
                nn = plot.get((nc, nr))
                if nn 

    # print(content, region, perimeter, c, r)
    s += region * perimeter
    ans[content] = (region, perimeter)
print(s)
