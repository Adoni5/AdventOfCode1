test_input ="""5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""
from heapq import heappop, heappush
from collections import deque

with open("input.txt") as fh:
    test_input = fh.read()
max_c, max_r = 70, 70
max_k = 1024
g = {tuple(map(int, l.split(","))) for i, l in enumerate(test_input.splitlines()) if i < max_k}
print(len(g))
start = (0,0,0)
end = (max_c,max_r)
ds = ((-1, 0), (0, -1), (1, 0), (0, 1))
q = []
heappush(q, start)
visited = set()
ends = []
while q:
    s, c, r = heappop(q)
    print(c,r)
    if (c, r) == end:
        ends.append((s))
        print(f"EMD {s}")
    if (c, r) in visited:
        continue
    visited.add((c, r))

    for (dc, dr) in ds:
        nc, nr = c + dc, r +dr
        # print(nc, nr)
        if (nc, nr) in g or any(x < 0 or x > max_c for x in (nc, nr)):
            continue
        heappush(q, (s+1, nc, nr))
print(min(ends))