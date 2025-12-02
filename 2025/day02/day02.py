import sys
from itertools import batched

invalids = []
ids = sys.stdin.read().split(",")
for id in ids:
    start, end = tuple(map(int, id.split("-")))
    ranges = tuple(map(str, range(start, end + 1)))
    for r in ranges:
        if not len(r) % 2:
            h1, h2 = batched(r, len(r)//2)
            if h1 == h2:
                print(f"Invalid {r}")
                invalids.append(int(r))
print(sum(invalids))

