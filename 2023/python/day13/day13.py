test_input = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

# test_input = """....###
# #..#..#
# #..#..#
# ....###
# .####.#
# #.##...
# ####.##
# .#####.
# .#####.
# ####.##
# #.##...
# .####.#
# #...###"""

from support import get_input
from collections import Counter

test_input = get_input(13, 2023)

from pprint import pprint

patterns = test_input.split("\n\n")
total = 0

for pattern in patterns:
    rows = []
    for line in pattern.splitlines():
        rows.append(line.strip())
    cols = list(zip(*rows))
    print(pattern, "\n")
    found = False
    sym_rows, prev_r = 0, -1
    sym_cols, prev_c = 0, -1
    for i in range(1, len(rows)):
        if (
            sum(
                x != y
                for j in range(min(len(rows[:i]) - 1, len(rows[i:]) - 1) + 1)
                for a, b in zip(rows[:i][-j - 1], rows[i:][j])
                for x, y in zip(a, b)
            )
            == 1
        ):
            # if (
            #     sum(
            #         x != y for a, b in zip(rows[:i][-j - 1], comp_below) for x, y in zip(a, b)
            #     )
            #     == 1
            # ):
            print(f"ahh rows {i}")
            total += 100 * i
            # if (
            #     sum(x != y for j in range(d) for x, y in zip(comp_above, comp_below))
            #     == 1
            # ):
            #     print(f"ahhh rows {i}")
            #
            #     found = True
    if not found:
        for i in range(1, len(cols)):
            if (
                sum(
                    x != y
                    for j in range(min(len(cols[:i]) - 1, len(cols[i:]) - 1) + 1)
                    for a, b in zip(cols[:i][-j - 1], cols[i:][j])
                    for x, y in zip(a, b)
                )
                == 1
            ):
                print(f"ahhh cols {i}")
                total += i
                found = True
    print(sym_rows)
    print(sym_cols, "\n")
    # input()
    total += sym_rows
    total += sym_cols

print(total)
