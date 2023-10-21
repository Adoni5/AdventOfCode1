import re
from support import get_input

test_input = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""
test_input = get_input(22, strip=False)
grid, instructions = test_input.split("\n\n")
grid = grid.split("\n")
print(grid)
# pad into cube
width = max(len(row) for row in grid)

grid = [row + " " * (width - len(row)) for row in grid]
regex = re.compile(r"(\d+)([RL]?)")
instructions = regex.findall(instructions)
print(instructions)
c, r = grid[0].index("."), 0
dc, dr = 1, 0
print(c, r)
for steps, turn in instructions:
    for x in range(int(steps)):
        nc = c
        nr = r
        while True:
            nc = (nc + dc) % len(grid[0])
            nr = (nr + dr) % len(grid)
            print(
                "now at ",
                grid[nr][nc],
                nr,
                nc,
                #     (nc + dc) % len(grid[0]),
                #     (nr + dr) % len(grid),
                #     dc,
                #     dr,
            )
            if grid[nr][nc] != " ":
                print("found, breaking", grid[nr][nc])
                break
        if grid[nr][nc] == "#":
            break
        c = nc
        r = nr
    print(f"turn is {turn}, dc is {dc}, dr is {dr}")
    if turn == "R":
        dc, dr = -dr, dc
    elif turn == "L":
        dc, dr = dr, -dc

print(r + 1, c + 1, dc, dr)
d = 0
if dr == 0:
    if dc == 1:
        d = 0
    else:
        d = 2
else:
    if dr == 1:
        d = 1
    else:
        d = 3
print(sum((1000 * (r + 1), 4 * (c + 1), d)))

# Part 3 the hardcodening
c, r = grid[0].index("."), 0
dc, dr = 1, 0
for steps, turn in instructions:
    for x in range(int(steps)):
        cdr = dr
        cdc = dc
        nc = c + dc
        nr = r + dr
        # move up off of first face
        if nr < 0 and 50 <= nc < 100 and dr == -1:
            dr, dc = 0, 1
            nr, nc = nc + 100, 0
        elif nc < 0 and 150 <= nr < 200 and dc == -1:
            dr, dc = 1, 0
            nr, nc = 0, nr - 100
        elif nr < 0 and 100 <= nc < 150 and dr == -1:
            nr, nc = 199, nc - 100
        elif nr >= 200 and 0 <= nc < 50 and dr == 1:
            nr, nc = 0, nc + 100
        elif nc >= 150 and 0 <= nr < 50 and dc == 1:
            dc = -1
            nr, nc = 149 - nr, 99
        elif nc == 100 and 100 <= nr < 150 and dc == 1:
            dc = -1
            nr, nc = 149 - nr, 149
        elif nr == 50 and 100 <= nc < 150 and dr == 1:
            dr, dc = 0, -1
            nr, nc = nc - 50, 99
        elif nc == 100 and 50 <= nr < 100 and dc == 1:
            dr, dc = -1, 0
            nr, nc = 49, nr + 50
        elif nr == 150 and 50 <= nc < 100 and dr == 1:
            dr, dc = 0, -1
            nr, nc = nc + 100, 49
        elif nc == 50 and 150 <= nr < 200 and dc == 1:
            dr, dc = -1, 0
            nr, nc = 149, nr - 100
        elif nr == 99 and 0 <= nc < 50 and dr == -1:
            dr, dc = 0, 1
            nr, nc = nc + 50, 50
        elif nc == 49 and 50 <= nr < 100 and dc == -1:
            dr, dc = 1, 0
            nr, nc = 100, nr - 50
        elif nc == 49 and 0 <= nr < 50 and dc == -1:
            dc = 1
            nr, nc = 149 - nr, 0
        elif nc < 0 and 100 <= nr < 150 and dc == -1:
            dc = 1
            nr, nc = 149 - nr, 50
        if grid[nr][nc] == "#":
            dr = cdr
            dc = cdc
            break
        c = nc
        r = nr
    if turn == "R":
        dc, dr = -dr, dc
    elif turn == "L":
        dc, dr = dr, -dc
d = 0
if dr == 0:
    if dc == 1:
        d = 0
    else:
        d = 2
else:
    if dr == 1:
        d = 1
    else:
        d = 3
print(1000 * (r + 1) + 4 * (c + 1) + d)
