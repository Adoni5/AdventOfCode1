import re
from pprint import pprint
from support import get_input, sliding_window
from tqdm import tqdm
test_input = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

def manhattan_distance(point1, point2):
    return sum(abs(value1 - value2) for value1, value2 in zip(point1, point2))

pat = re.compile(r"(-?\d+)")
target_y = 10
ranges = []
for l in test_input.splitlines():
    sx, sy, bx, by = map(int, pat.findall(l))
    man_dist = manhattan_distance((sx, sy), (bx, by))
    print(man_dist)
    y_dist = abs(target_y - sy)
    if y_dist > man_dist:
        continue
    start = sx - abs(man_dist-y_dist)
    end = sx + abs(man_dist-y_dist)
    ranges.append((start, end))
    ranges.sort(key=lambda x: x[0])
total = 0
s = None
print(ranges)
for n, n1 in sliding_window(ranges, 2):
    if s is None:
        s = n[0]
    if n[1] >=n1[0]:
        s = n[0]
        continue
    else:
        total += n1[1] - s
        s = None
print(total)
        

