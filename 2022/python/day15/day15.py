import re
from itertools import combinations, combinations_with_replacement, permutations
from pprint import pprint
from support import get_input
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
# This function takes a point on the grid and the maximum Manhattan distance
# and returns a list of all points within that distance
def points_within_distance(point, max_distance):
  x, y = point
  points = []

  # Loop through all points on the grid
  for i in range(-max_distance-1, max_distance+1):
    for j in range(-max_distance-2, max_distance+1):
      # Calculate the Manhattan distance between the current point and the original point
      distance = manhattan_distance(point,  (x - i, y - j))
      # If the distance is within the maximum distance, add it to the list of points
      if distance <= max_distance:
        points.append((x - i, y - j))

  return points




def manhattan_distance(point1, point2):
    return sum(abs(value1 - value2) for value1, value2 in zip(point1, point2))

# test_input = get_input("15")
pat = re.compile(r"(-*\d+)")
points_on_row_10 = set()
beacons = set()
row = 2000000 # 27 on row 11
sensors = []
b = []
from collections import defaultdict
d = defaultdict(int)

for sensor in test_input.splitlines():
    coords = tuple(map(int, (pat.findall(sensor.strip()))))
    p1, p2 = coords[:2], coords[2:]
    beacons.add(p2)
    sensors.append(p1)
    man_distance = manhattan_distance(p1, p2) +1
    xmin = min(0, p1[0] - man_distance)
    xmax = max(20, p1[0] + man_distance)
    vertical = p1[1]
    for x in range(xmin, xmax):
        if x <= p1[0]:
            vertical += 1
        else:
            vertical -= 1
        cu = (x, p1[1] - vertical)
        cd = (x, p1[1] + vertical)
        if cu == cd:
            d[cu] += 1
        else:
            d[cu] += 1
            d[cd] += 1

        if d[cu] == 4:
            print(cu)
        if d[cd] == 4:
            print(cd)
pprint(d)

beacons_on_line = 0
row = 10
# points_on_row_10 = set()
# for sensor in tqdm(test_input.splitlines()):
#     coords = tuple(map(int, (pat.findall(sensor))))
#     p1, p2 = coords[:2], coords[2:]
#     # if p1 != (8, 7):
#     #     continue
#     # if p1 != (13, 2):
#     #     continue
#     # beacons.add(p2)
#     # sensors.append(p1)
    

#     # print(man_distance)
#     x, y = p1
#     # print(p1)
#     lowest = y + man_distance
#     highest = y - man_distance
#     # print(lowest, highest)
#     # lower_higher = y >= 10
#     if lowest >= row and highest <= row:
#         # closest_edge = 
#         diff = abs(min(abs(lowest-row), abs(highest-row)))
#         # print(diff)
#         for i in range(-diff, (diff+1)):
#             # print(i)
#             # print((x+i, row) in beacons)
#             p_coord = (x+i, row)
#             # if p_coord == (14, row):
#             #     print(f"Gives wrong answer {p1}, {p2}")
#             if p_coord not in beacons and p_coord not in sensors:
#                 points_on_row_10.add((x+i, row))
#             # else:
#                 # print(f"beacon on line {x+i, row}")
#                     # pass

#     # if len(points_on_row_10) < 20:
#     #     print(points_on_row_10)
#     #     break
    
    
#     # return 4_000_000 * ans_x + ans_y

#     # points = points_within_distance(p1, man_distance)


#     # # pprint(points)
#     # for p in points:
#     #     # print(p)
#     #     _, y = p
#     #     if y == 10 and p not in beacons:
#     #         # print("adding")
#     #         points_on_row_10.add(_)
# pprint(points_on_row_10)
# print(len(points_on_row_10))
# print(solve_2())