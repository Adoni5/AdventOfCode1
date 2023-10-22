test_input = """..............
..............
.......#......
.....###.#....
...#...#.#....
....#...##....
...#.###......
...##.#.##....
....#..#......
..............
..............
.............."""

from collections import deque
from support import Grid, get_input

# N, S, W, E
d = deque(
    [
        ((-1, -1), (0, -1), (1, -1)),
        ((-1, 1), (0, 1), (1, 1)),
        ((-1, -1), (-1, 0), (-1, 1)),
        ((1, 1), (1, 0), (1, -1)),
    ]
)
test_input = get_input(23, strip=False)
g = Grid.read_grid(test_input)

elves = g.find_all_items("#")
elf_check = set(elves)
go = True
step = 1
while go:
    # print(f"step {step + 1}\n")
    failed = set()
    proposed = {}
    stop = 0
    c = 0
    for index, elf in enumerate(elves):
        for coord, neighbours in g.get_neighbours(
            elf, diagonal=True, enforce_edges=False, return_coords=True, fill_value="."
        ).items():
            x, y = coord
            if all(
                (
                    (x + dx, y + dy) not in elf_check
                    for direction in d
                    for dx, dy in direction
                )
            ):
                # print(
                #     f"elf {index} at {elf} has no neighbours, breaking",
                # )
                c += 1
                if c == len(elves):
                    go = False
                    break
                break
            for direction in d:
                # print(f"checking direction {direction} for elf {index} at {elf}")
                if all(((x + dx, y + dy) not in elf_check for dx, dy in direction)):
                    # print(
                    #     "proposed for",
                    #     coord,
                    #     (x + direction[1][0], y + direction[1][1]),
                    # )
                    # print(f"ELF {index} at {elf} moving to direction {direction}")
                    if (x + direction[1][0], y + direction[1][1]) not in proposed and (
                        x + direction[1][0],
                        y + direction[1][1],
                    ) not in failed:
                        proposed[(x + direction[1][0], y + direction[1][1])] = index
                    else:
                        proposed.pop((x + direction[1][0], y + direction[1][1]))
                        failed.add((x + direction[1][0], y + direction[1][1]))

                    break
    if c != len(elves):
        for proposal, elf in proposed.items():
            elves[elf] = proposal
        # print(f"elves now {elves}")
        d.rotate(-1)
        # print(f"direction now {d}\n")
        step += 1
    elf_check = set(elves)
    # -1 as we are adding one without executing above
    if step - 1 == 10:
        # print(elves)
        bounds = (
            min(elves, key=lambda x: x[0])[0],
            min(elves, key=lambda x: x[1])[1],
            max(elves, key=lambda x: x[0])[0],
            max(elves, key=lambda x: x[1])[1],
        )
        print(
            f"part 1 {(bounds[2] + 1 - bounds[0]) * (bounds[3] + 1 - bounds[1]) - len(elves)}"
        )


print(f"part 2 {step}")
