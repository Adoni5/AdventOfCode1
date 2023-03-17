from math import inf
import re
from support import sliding_window, get_input
from itertools import zip_longest
from pprint import pprint
import time
test_input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

pat = re.compile(r"(\d+)")


rocks = set()
sand = set()
minx = inf
maxx = -inf
maxy = 0
test_input = get_input("14")
for line in test_input.splitlines():
    itery = sliding_window(pat.findall(line), 4, skip=True)
    for coords in itery:
        x1, y1, x2, y2 = map(int, coords)
        minx = min((x1, x2, minx))
        maxx = max((x1, x2, maxx))
        maxy = max((y1, y2, maxy))
        for x in range(min(x1, x2), max(x1, x2) +1):
            rocks.add((x, y1))
        for y in range(min(y1, y2), max(y1, y2)+1):
            rocks.add((x1, y))
        next(itery)

rocks.union(set(zip_longest(range(-5000, 5000), iter([maxy]), fillvalue=maxy)))

def rocks_fall_everbody_duels(rocks, sand, minx, maxx):
    count = 0
    fall = True
    while fall:
        # print(count)
        start = (500, 0)
        drop = True
        x, y = start
        while 1:
            # print(x, y)
            if (x, y+1) in rocks or (x, y+1) in sand:
                dl = (x-1, y+1)
                if dl[0] < minx:
                    fall = False
                    break

                if not dl in sand and not dl in rocks:
                    x, y = dl
                    continue
                dr = (x + 1, y + 1)
                if dr[0] > maxx:
                    fall = False
                    break
                if not dr in sand and not dr in rocks:
                    x, y = dr
                    continue
                                # part 2 check

                sand.add((x, y))
                if (x, y) == (500, 0):
                    print("Got to 500, 0")
                    fall = False
                    break
                break

            y += 1
        count += 1
    return len(sand)

# surely we can reuse the above
# part 1
print(rocks_fall_everbody_duels(rocks=rocks, sand=sand, minx=minx, maxx=maxx))
# part 2
dx, dx2 = - 5000, 5000
minx, maxx = 500 + dx, 500 + dx2
rocks = rocks.union(set(zip_longest(range(minx, maxx), iter([maxy+2]), fillvalue=maxy+2)))

print(rocks_fall_everbody_duels(rocks=rocks, sand=sand, minx=minx, maxx=maxx))