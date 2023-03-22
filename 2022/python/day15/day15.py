import re
from pprint import pprint
from support import get_input, sliding_window
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

real_input = """Sensor at x=3923513, y=2770279: closest beacon is at x=3866712, y=2438950
Sensor at x=675683, y=3223762: closest beacon is at x=-224297, y=2997209
Sensor at x=129453, y=2652332: closest beacon is at x=92656, y=2629486
Sensor at x=3906125, y=2154618: closest beacon is at x=3866712, y=2438950
Sensor at x=65723, y=902062: closest beacon is at x=92656, y=2629486
Sensor at x=3137156, y=2876347: closest beacon is at x=2907507, y=3100765
Sensor at x=32848, y=2676435: closest beacon is at x=92656, y=2629486
Sensor at x=3272472, y=3445147: closest beacon is at x=2907507, y=3100765
Sensor at x=2926008, y=128948: closest beacon is at x=3089364, y=-501737
Sensor at x=2975, y=2769838: closest beacon is at x=92656, y=2629486
Sensor at x=3540455, y=2469135: closest beacon is at x=3866712, y=2438950
Sensor at x=3674809, y=2062166: closest beacon is at x=3719980, y=2000000
Sensor at x=3693706, y=2027384: closest beacon is at x=3719980, y=2000000
Sensor at x=3869683, y=2291983: closest beacon is at x=3866712, y=2438950
Sensor at x=2666499, y=2796436: closest beacon is at x=2650643, y=2489479
Sensor at x=492, y=2601991: closest beacon is at x=92656, y=2629486
Sensor at x=2710282, y=3892347: closest beacon is at x=2907507, y=3100765
Sensor at x=28974, y=3971342: closest beacon is at x=-224297, y=2997209
Sensor at x=3990214, y=2399722: closest beacon is at x=3866712, y=2438950
Sensor at x=3853352, y=1009020: closest beacon is at x=3719980, y=2000000
Sensor at x=1231833, y=3999338: closest beacon is at x=1313797, y=4674300
Sensor at x=2083669, y=875035: closest beacon is at x=1369276, y=-160751
Sensor at x=1317274, y=2146819: closest beacon is at x=2650643, y=2489479
Sensor at x=3712875, y=2018770: closest beacon is at x=3719980, y=2000000
Sensor at x=963055, y=23644: closest beacon is at x=1369276, y=-160751
Sensor at x=3671967, y=64054: closest beacon is at x=3089364, y=-501737
Sensor at x=3109065, y=2222392: closest beacon is at x=2650643, y=2489479
Sensor at x=3218890, y=1517419: closest beacon is at x=3719980, y=2000000
Sensor at x=3856777, y=3987650: closest beacon is at x=4166706, y=3171774
Sensor at x=1912696, y=3392788: closest beacon is at x=2907507, y=3100765
Sensor at x=3597620, y=3100104: closest beacon is at x=4166706, y=3171774"""


def manhattan_distance(point1, point2):
    return sum(abs(value1 - value2) for value1, value2 in zip(point1, point2))

def total_ranges(ranges):
    """
        Take a list of ranges, and work out how many elements they contain
    """
    total = 0
    for rangey in ranges:
        total += rangey.stop - rangey.start
    return total

def coalesce(ranges):
    """
        Take a list of ranges, collapse overlaps and return a list of
          ranges of only unique elements
    """
    s = ranges[0].start
    st = ranges[0].stop
    collated_ranges = []
    for n, n1 in sliding_window(ranges, 2):
        if s is None:
            s = n.start
            st = n.stop
        if n1.start <= st and n1.stop >= st:
            st = n1.stop
            
        elif n1.start > st:
            collated_ranges.append(range(s, st))
            s = None
            st = None
    # Add on the final one
    if s is not None:
        collated_ranges.append(range(s, st))
    return collated_ranges

def parse_input(input):
    """Parse the puzzle input, return a list of tuples of form
    [(sensor_x, sensor_y, beacon_x, beacon_y)]"""
    coords = []
    pat = re.compile(r"(-?\d+)")
    for l in input.splitlines():
        coords.append(tuple(map(int, pat.findall(l))))
    return coords


def range_on_row(y, coords):
    """
        At a given Y, calculate the range of positions a beacon cannot be at and return it
    """

    target_y = y
    ranges = []
    for sx, sy, bx, by in coords:
        man_dist = manhattan_distance((sx, sy), (bx, by))
        y_dist = abs(target_y - sy)
        if y_dist > man_dist:
            continue
        start = sx - abs(man_dist-y_dist)
        end = sx + abs(man_dist-y_dist)
        ranges.append(range(start, end))
    ranges.sort(key=lambda x: (x.start, x.stop))
    ranges = coalesce(ranges)
    return ranges

coords = parse_input(real_input)

part_1_ranges = range_on_row(2_000_000, coords)
print(f"Part 1 {total_ranges(part_1_ranges)}")        

## Part 2
# need to include positions where beacons are already, and we are off by one on our ranges :(
# Somehow we still get the right answer in part 1 but we won't in part 2
# Clamp the ranges between 0 and 4 million and then do the below check
for y in range(0, 4_000_000):
    print(y)
    ranges = range_on_row(y, coords)
    if len(ranges)> 1:
        print(ranges)
        break
