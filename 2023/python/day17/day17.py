test_input = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""

from heapq import heappop, heappush
from support import get_input

test_input = get_input(17, 2023)
grid = {}
for r, line in enumerate(test_input.splitlines()):
    for c, char in enumerate(line):
        grid[(r, c)] = int(char)

max_r = r
max_c = c
print(max_r, max_c)

seen = set()
pq = [(0, 0, 0, 0, 0, 0)]

while pq:
    hl, r, c, dr, dc, n = heappop(pq)
    if r == max_r and c == max_c:
        print(hl)
        break
    if (r, c, dr, dc, n) in seen:
        continue

    seen.add((r, c, dr, dc, n))
    if n < 10 and (dr, dc) != (0, 0):
        nr = r + dr
        nc = c + dc
        if (nr, nc) in grid:
            heappush(pq, (hl + grid[(nr, nc)], nr, nc, dr, dc, n + 1))
    if n >= 4 or (dr, dc) == (0, 0):
        for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                nr = r + ndr
                nc = c + ndc
                if (nr, nc) in grid:
                    heappush(pq, (hl + grid[(nr, nc)], nr, nc, ndr, ndc, 1))
