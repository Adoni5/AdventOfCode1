test_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
from support import get_input
from math import prod

test_input = get_input(3, 2023)
grid = {}
for r, line in enumerate(test_input.splitlines()):
    number = ""
    for c, char in enumerate(line):
        if char != "." and char.isdigit():
            number += char
        elif char != "." and not char.isdigit():
            grid[(r, c)] = char
            if number != "":
                for i in range(len(number)):
                    grid[(r, c - i - 1)] = int(number)
            number = ""
        elif char == "." and number != "":
            for i in range(len(number)):
                grid[(r, c - i - 1)] = int(number)

            number = ""
        # print(c)
    # AHHHHH New line rip
    if number != "":
        for i in range(len(number)):
            grid[(r, len(line) - i - 1)] = int(number)

        number = ""

gear_ratios = []
# print(grid)
total = 0
total_p2 = 0
d = ((-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1))
for (x, y), char in grid.items():
    state = set()
    state_p2 = set()
    if isinstance(char, str):
        # P2
        if char == "*":
            num_adjacent = []
            for dx, dy in d:
                if (
                    (x + dx, y + dy) in grid
                    and isinstance(grid[(x + dx, y + dy)], int)
                    and (x + grid[(x + dx, y + dy)]) not in state_p2
                ):
                    num_adjacent.append(grid[(x + dx, y + dy)])
                    state_p2.add(x + grid[(x + dx, y + dy)])
            if len(num_adjacent) == 2:
                total_p2 += prod(num_adjacent)

        for dx, dy in d:
            if (
                (x + dx, y + dy) in grid
                and isinstance(grid[(x + dx, y + dy)], int)
                and (x + grid[(x + dx, y + dy)]) not in state
            ):
                if grid[(x + dx, y + dy)] == 760:
                    print("helo", x + dx, y + dy)
                print(grid[(x + dx, y + dy)])
                total += grid[(x + dx, y + dy)]
                state.add(x + grid[(x + dx, y + dy)])
        # input()

print(total)
print(total_p2)
