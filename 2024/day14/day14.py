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

print(robots)
print(len(robots))
print()
mx, my = 101, 103
hx, hy = int((mx - 1) / 2), int((my - 1) / 2)
print(f"hx is {hx}, hy is {hy}")
r = Counter()
d = Counter()
for k1, k2, vx, vy in robots:
    x, y = k1, k2
    # for i in range():
    _k1 = x + vx * 100
    _k2 = y + vy * 100
    x, y = _k1 % mx, _k2 % my
    # midpoint
    if x == hx or y == hy:
        continue
    r[(x, y)] += 1
    quad = (int(x > hx), int(y > hy))
    # print(x, y)
    d[quad] += 1
print(r)
print(d)
print(reduce(mul, d.values()))
