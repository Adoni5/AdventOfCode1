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
