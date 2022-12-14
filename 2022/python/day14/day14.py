import re
from support import sliding_window
from pprint import pprint
test_input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

pat = re.compile(r"(\d+)")

def pgprint(pg):
    """Print a nested list of lists as a grid"""
    print("\n".join(["".join(list(map(str, p))) for p in pg]))

listy = [["."] * 10 for _ in range(10)]

rocks = set()
sand = set()

for line in test_input.splitlines():
    itery = sliding_window(pat.findall(line), 4, skip=True)
    for coords in itery:
        x1, y1, x2, y2 = map(int, coords)
        for x in range(min(x1, x2), max(x1, x2) +1):
            # print(f"x is {x-494}")
            listy[y1][x-494] = "#"
            rocks.add((x, y1))
        for y in range(min(y1, y2), max(y1, y2)+1):
            # print(f"y is {y}")
            listy[y][x1-494] = "#"
            rocks.add((x1, y))


        next(itery)
pgprint(listy)
        
sandy = True
sand_start = 500, 0
sand_count = 0
lowest_rock = max(r[1] for r in iter(rocks))
print(lowest_rock)
pprint(rocks)

while sandy:
    sand_x, sand_y = sand_start
    print(f"start {sand_x}, {sand_y}")
    # sand falls everybody drops
    while True:
        sand_down = (sand_x, sand_y+1)
        print(sand_down)
        if sand_down in rocks and sand_down not in sand:
            print("hit rock")
            sand.add((sand_x, sand_y))
            break
        if sand_down in sand:
            print("hit sand")
            sand_down_left = (sand_x - 1 , sand_y + 1)
            sand_down_right = (sand_x + 1, sand_y + 1)
            if sand_down_left not in rocks and sand_down_left not in sand:
                # try falling again
                print("moving left")
                sdl_x, sdl_y = sand_down_left
                while (sdl_x - 1, sdl_y + 1) not in rocks and (sdl_x - 1, sdl_y + 1) not in sand:
                    print("Moved to the left")
                    sdl_x -= 1
                    sdl_y += 1
                    if sdl_y > lowest_rock:
                        print("fell off")
                        sandy = False
                        break
                if sandy:
                    sand.add((sdl_x, sdl_y))
                break
            elif sand_down_right not in rocks and sand_down_right not in sand:
                print("moving right")

                sdr_x, sdr_y = sand_down_right
                while (sdr_x + 1, sdr_y + 1) not in rocks and (sdr_x + 1, sdr_y + 1) not in sand:
                    print("Moved to the right")
                    sdr_x -= 1
                    sdr_y += 1
                    if sdr_y > lowest_rock:
                        print("fell off")
                        sandy = False
                        break

                if sandy:
                    sand.add((sdr_x, sdr_y))
                break
            # It's now resting on 3 sand
            else:
                print("resting on sand")
                sand.add((sand_x, sand_y))
                break
        
            
        sand_y += 1 
        if sand_y > lowest_rock:
            print("fell off")
            sandy = False
            break
    sand_count += 1
print(sand)
print(sand_count)
sand_char = "o"

for x, y in iter(sand):
    print(x, y)
    listy[y][x-494] = sand_char
pgprint(listy)


