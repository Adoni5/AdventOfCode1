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

# test_input = """##..##..###
# ...#..#....
# ...#..#....
# .###..###..
# .#......#..
# .#......#..
# ##..##..###
# ..#.##.#...
# .##....##..
# .###..##...
# .########.."""

from support import get_input

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
        if not len(set(tuple(rows[i:])) - set(tuple(rows[:i]))) or not len(
            set(tuple(rows[:i])) - set(tuple(rows[i:]))
        ):
            if all(
                rows[:i][-j - 1] == rows[i:][j]
                for j in range(min(len(rows[:i]) - 1, len(rows[i:]) - 1) + 1)
            ):
                print(f"symmetry rows starts {i+1}")
                sym_rows = (
                    i * 100 if i * 100 > sym_rows and i - 1 != prev_r else sym_rows
                )
                prev_r = i
                found = True
    if not found:
        for i in range(1, len(cols)):
            if not len(set(tuple(cols[i:])) - set(tuple(cols[:i]))) or not len(
                set(tuple(cols[:i])) - set(tuple(cols[i:]))
            ):
                if all(
                    cols[:i][-j - 1] == cols[i:][j]
                    for j in range(min(len(cols[:i]) - 1, len(cols[i:]) - 1) + 1)
                ):
                    print(f"symmetry cols {i+1}\n")
                    sym_cols = i if i > sym_cols and i - 1 != prev_c else sym_cols
                    prev_c = i
                    found = True
    print(sym_rows)
    print(sym_cols, "\n")
    # input()
    total += sym_rows
    total += sym_cols

print(total)
