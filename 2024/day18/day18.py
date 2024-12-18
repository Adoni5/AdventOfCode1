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
bytey = test_input.count("\n") + 1
max_c, max_r = 70, 70
max_k = 1024
start = (0,0,0)
end = (max_c,max_r)
ds = ((-1, 0), (0, -1), (1, 0), (0, 1))

for i in range(bytey):
    g = {tuple(map(int, l.split(","))) for j, l in enumerate(test_input.splitlines()) if j < i}
    q = []
    heappush(q, start)
    ends = []
    visited = set()

    while q:
        s, c, r = heappop(q)
        if (c, r) == end:
            ends.append((s))
        if (c, r) in visited:
            continue
        visited.add((c, r))

        for (dc, dr) in ds:
            nc, nr = c + dc, r +dr
            # print(nc, nr)
            if (nc, nr) in g or any(x < 0 or x > max_c for x in (nc, nr)):
                continue
            heappush(q, (s+1, nc, nr))
    if not ends:
        print(test_input.splitlines()[i-1])
        break