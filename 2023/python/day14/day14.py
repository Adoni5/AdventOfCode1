test_input = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""
from pprint import pprint
from support import get_input

test_input = get_input(14, 2023)
print(test_input)

rolly_polly_boulders = {}
no_rolly_polly_boulders = {}

num_rows = 0
num_cols = 0
for y, line in enumerate(test_input.splitlines()):
    num_rows += 1
    num_cols = 0
    for x, char in enumerate(line):
        if char == "O":
            rolly_polly_boulders[(x, y)] = char
        if char == "#":
            no_rolly_polly_boulders[(x, y)] = char
        num_cols += 1
print(num_rows)
d1 = (0, -1)
# P1 the boulders head north
final_resting_place = set()  # RIP
for (x, y), char in rolly_polly_boulders.items():
    if y == 0:
        final_resting_place.add((x, y))
    cx, cy = x, y
    while True:
        nx, ny = cx + d1[0], cy + d1[1]
        ncoord = (nx, ny)
        if (
            ncoord not in no_rolly_polly_boulders
            and ncoord not in final_resting_place
            and ny != -1
        ):
            cx, cy = nx, ny
        else:
            final_resting_place.add((cx, cy))
            break
print()
grid = []
for j in range(num_rows):
    row = ""
    for i in range(num_cols):
        if (i, j) in no_rolly_polly_boulders:
            row += "#"
        elif (i, j) not in final_resting_place:
            row += "."
        elif (i, j) in final_resting_place:
            row += "O"
    grid.append(row)
print("\n".join(grid))

num_rows = len(grid)
print(sum(num_rows - y for _, y in final_resting_place))

# Part 2 - http://open.spotify.com/track/1ChulFMnwxoD74Me8eX2TU
d2 = [
    ((0, -1), lambda x: x[0], False),
    ((-1, 0), lambda x: x[1], False),
    ((0, 1), lambda x: x[0], True),
    ((1, 0), lambda x: x[1], True),
]

cache = {}
cycles = 1000000000
pattern = [tuple(rolly_polly_boulders.keys())]
breaky = 0
for _ in range(cycles):
    print(f"cycle {_}")
    for d, key, rev in d2:
        key_ = (tuple(rolly_polly_boulders.keys()), d)
        if key_ in cache:
            breaky = True
            rolly_polly_boulders = cache[key_]
            continue
        # print(d)
        final_resting_place = set()  # RIP
        new_rolly_polly_boulders = {}
        for (x, y), char in sorted(rolly_polly_boulders.items(), key=key, reverse=rev):
            cx, cy = x, y
            while True:
                nx, ny = cx + d[0], cy + d[1]
                ncoord = (nx, ny)
                if (
                    ncoord not in no_rolly_polly_boulders
                    and ncoord not in final_resting_place
                    and num_rows > ny >= 0
                    and num_cols > nx >= 0
                ):
                    cx, cy = nx, ny
                else:
                    final_resting_place.add((cx, cy))
                    new_rolly_polly_boulders[(cx, cy)] = char
                    break
        cache[key_] = new_rolly_polly_boulders
        rolly_polly_boulders = new_rolly_polly_boulders
    if breaky:
        break
    pattern.append(tuple(rolly_polly_boulders.keys()))
cycles = _ + 1
first = pattern.index(tuple(rolly_polly_boulders.keys()))
print(cycles, first)
print(len(pattern))
grid = pattern[(1000000000 - first) % (cycles - first) + first]

print(sum(num_rows - y for _, y in grid))
# print(100000000 % 7)
# print(len(cache))
# for i in
# expected = """.....#....
# ....#...O#
# .....##...
# ..O#......
# .....OOO#.
# .O#...O#.#
# ....O#...O
# .......OOO
# #...O###.O
# #.OOO#...O"""
# print("expected")
# print(expected)
