from collections import defaultdict, deque
from support import get_input

test_input = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

# P2 test_input
test_input = """..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
.........."""


test_input = get_input(10, 2023)

grid = {}
start = None
for r, line in enumerate(test_input.splitlines()):
    for c, char in enumerate(line):
        if char != ".":
            grid[(c, r)] = char
            if char == "S":
                start = (c, r)

N = (0, -1)
E = (1, 0)
S = (0, 1)
W = (-1, 0)

ds = list(zip([N, E, S, W], "NESW"))
# print(ds)

Ns = set(["|", "7", "F"])
Ss = set(["|", "L", "J"])
Ws = set(["-", "L", "F"])
Es = set(["-", "J", "7"])
check_chars = {"N": Ns, "S": Ss, "E": Es, "W": Ws}

lookup_turn = {
    "-": [E, W],  # E & W
    "|": [N, S],  # N & S
    "L": [N, E],  # N & E
    "J": [N, W],  # N & W
    "7": [S, W],  # S & W
    "F": [S, E],  # S & E
    "S": [N, E, S, W],
}

# Do you remember how to walk the grid in DECEMBER
points = deque([start])
visited = {start}
print(visited)
while points:
    x, y = points.popleft()
    char = grid[(x, y)]
    for d, card_direc in ds:
        if d in lookup_turn[char]:
            nx, ny = x + d[0], y + d[1]
            # print(card_direc)
            n_char = grid.get((nx, ny), None)

            if n_char in check_chars[card_direc] and (nx, ny) not in visited:
                # print(n_char)
                points.append((nx, ny))
                visited.add((nx, ny))

print(len(visited) / 2)

# P2 - Ray casting ?????! lol
# just looked at my input for the character for S
grid = [row.replace("S", "J") for row in test_input.splitlines()]
# convert the grid into only dots and the actual polygon
grid = [
    "".join(ch if (c, r) in visited else "." for c, ch in enumerate(row))
    for r, row in enumerate(grid)
]

# You ain't enclosed you scrub
outside = set()
from pprint import pprint

pprint(grid)

for r, row in enumerate(grid):
    within = False
    up = None
    # We are going to scan to the right. If we cross the boundary an odd number of times we are enclosed
    # We also have to check we aren't leaking out the top or bottom
    for c, ch in enumerate(row):
        if ch == "|":
            assert up is None
            within = not within
        elif ch == "-":
            assert up is not None
        elif ch in "LF":
            assert up is None
            up = ch == "L"
        elif ch in "7J":
            assert up is not None
            if ch != ("J" if up else "7"):
                within = not within
            up = None
        elif ch == ".":
            pass
        if not within:
            outside.add((c, r))
# Area of the grid minus the length of all outside and boundary nodes
print(len(grid) * len(grid[0]) - len(outside | visited))
