import re
from support import sliding_window, get_input
from pprint import pprint
test_input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

pat = re.compile(r"(\d+)")

def pgprint(pg):
    """Print a nested list of lists as a grid"""
    print("\n".join(["".join(list(map(str, p))) for p in pg]))


rocks = set()
sand = set()
test_input = get_input("14")
for line in test_input.splitlines():
    itery = sliding_window(pat.findall(line), 4, skip=True)
    for coords in itery:
        x1, y1, x2, y2 = map(int, coords)
        for x in range(min(x1, x2), max(x1, x2) +1):
            # print(f"x is {x-494}")
            # listy[y1][x-494] = "#"
            rocks.add((x, y1))
        for y in range(min(y1, y2), max(y1, y2)+1):
            # print(f"y is {y}")
            # listy[y][x1-494] = "#"
            rocks.add((x1, y))


        next(itery)
# listy = [["."] *  for _ in range(10)]

# pgprint(listy)
        
sandy = True
sand_start = 500, 0
sand_count = 0
lowest_rock = max(r[1] for r in iter(rocks))
print(lowest_rock)
infinte_floor = lowest_rock + 2
# pprint(rocks)
sand_char = "o"
max_x, min_x = max(r[0] for r in iter(rocks)), min(r[0] for r in iter(rocks))
for i in range(min_x - 5000, max_x + 5000):
    rocks.add((i, infinte_floor))


while sandy:
    sand_x, sand_y = sand_start
    # print(f"start {sand_x}, {sand_y}")
    # sand falls everybody drops
    while True:
        sand_down = (sand_x, sand_y+1)
        # print(sand_down)
        # STUPID
        # if sand_down in rocks and sand_down not in sand:
        #     print("hit rock")
        #     sand.add((sand_x, sand_y))
        #     listy[sand_y][sand_x-494] = sand_char

        #     break
        if sand_down in sand or sand_down in rocks:
            # print("hit obstacle")
            sand_down_left = (sand_x - 1 , sand_y + 1)
            sand_down_right = (sand_x + 1, sand_y + 1)
            if sand_down_left not in rocks and sand_down_left not in sand:
                # print("moving left")
                sand_x -= 1
                if sand_y > infinte_floor:
                    print("fell off")
                    sandy = False
                    break
                continue
            elif sand_down_right not in rocks and sand_down_right not in sand:
                # print("moving right")

                sand_x += 1

                if sand_y > infinte_floor:
                    print("fell off")
                    sandy = False
                    break
                continue
            # It's now resting on 3 sand
            else:
                # print("resting on sand")
                # listy[sand_y][sand_x-494] = sand_char

                sand.add((sand_x, sand_y))
                if (sand_x, sand_y) == (500,0):
                    sand_count += 1
                    sandy = False
                break
        
            
        sand_y += 1 
        if sand_y > infinte_floor:
            print("fell off")
            sandy = False
            break
    if sandy:
        sand_count += 1
    # pgprint(listy)
# print(sand)
print(sand_count)

# for x, y in iter(sand):
#     listy[y][x-494] = sand_char
# pgprint(listy)


