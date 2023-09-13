test_input = """.....
..##.
..#..
.....
..##.
....."""

from collections import deque
from support import Grid

# N, S, W, E
d = deque([((-1, -1), (0, -1), (1, -1)), ((-1, 1), (0, 1), (1, 1)), ((-1, 1), (-1, 0), (-1, -1)), ((1, 1), (1, 0), (1, -1))])
g = Grid.read_grid(test_input)

starting_elves = g.find_all_items("#")
print(starting_elves)

print(g.grid)
go = True
elf_num = 1
while go:
    proposed = set()
    for elf in starting_elves:
        print("elf", elf, elf_num)
        for coord, neighbours in g.get_neighbours(elf, diagonal=True, enforce_edges=False, return_coords=True, fill_value=".").items():
            x, y = coord
            # print(coord)
            for direction in d:
                # for dx, dy in direction:
                #     print(dx, dy)
                #     print((x + dx, y + dy))
                #     print(g.grid.get((x + dx, y + dy), "."))
                if all((g.grid.get((x + dx, y + dy), ".") != "#" for dx, dy in direction)):
                    print("hello")
                    print(coord, (x + direction[1][0], y + direction[1][1]))
                    proposed.add((x + direction[1][0], y + direction[1][1]))
                    break
                else:
                    print("dead")
        elf_num += 1
        # break

    print(proposed)
    break