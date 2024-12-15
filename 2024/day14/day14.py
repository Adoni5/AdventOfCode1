test_input = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

import re
from collections import Counter
from functools import reduce
from operator import mul

with open("input.txt") as fh:
    test_input = fh.read()

pat = re.compile(r"(-*\d+)")
robots = []
for line in test_input.splitlines():
    x, y, vx, vy = tuple(map(int, pat.findall(line)))
    robots.append((x, y, vx, vy))


mx, my = 101, 103

v = set()
hx, hy = int((mx - 1) / 2), int((my - 1) / 2)
print(f"hx is {hx}, hy is {hy}")
for i in range(100000):
    i = i + 1
    r = Counter()
    d = Counter()

    for k1, k2, vx, vy in robots:
        x, y = k1, k2
        # for i in range():
        _k1 = x + vx * i
        _k2 = y + vy * i
        x, y = _k1 % mx, _k2 % my
        # midpoint
        r[(x, y)] += 1
        if x == hx or y == hy:
            continue
        quad = (int(x > hx), int(y > hy))
        # print(x, y)
        d[quad] += 1
    if tuple(r.keys()) in v:

        break
    v.add(tuple(r.keys()))
    dx, dy = 1, 0
    stop = False
    for x, y in r.keys():
        adj = 0
        _x, _y = x, y
        while True:
            if (_x + dx, _y + dy) in r:
                adj += 1
                _x, _y = _x + dx, _y + dy
            else:
                break

            if adj == 15:
                lines = []
                stop = True
                for _y in range(my):
                    line = []
                    for c in range(mx):
                        if (c, _y) in r:
                            line.append("*")
                        else:
                            line.append(".")
                    lines.append("".join(line))
                    line = []
                print(i)
                print("\n".join(lines))

                break
    if stop:
        print(i)
        break
    print(i)
    if i == 100:
        print(reduce(mul, d.values()))
