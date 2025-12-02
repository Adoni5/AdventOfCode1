import sys
from itertools import batched

invalids = []
p2_invalids = []
ids = sys.stdin.read().split(",")
for id in ids:
    start, end = tuple(map(int, id.split("-") ))
    ranges = tuple(map(str, range(start, end + 1)))
    for r in ranges:
        if not len(r) % 2:
            # part 1
            b = set(batched(r, len(r)//2))
            if len(b) == 1:
                invalids.append(int(r))
        # part 2
        for _ in range(1, (len(r)//2) + 1):
            b = set(batched(r, _))
            if len(b) == 1:
                p2_invalids.append(int(r))
                break


            
print(sum(invalids))
print(sum(p2_invalids))

