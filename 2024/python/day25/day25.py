test_input = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####"""

keys = []
locks = []
from collections import Counter

# from itertools import
import numpy as np

with open("input.txt") as fh:
    test_input = fh.read()

for schem in test_input.split("\n\n"):
    cols = Counter()
    for line in schem.splitlines():
        for c, char in enumerate(line):
            if c not in cols:
                cols[c] = -1
            if char == "#":
                cols[c] += 1

    if schem[0] == ".":
        keys.append(np.array(list(cols.values())))
    else:
        locks.append(np.array(list(cols.values())))

print(keys)
print(locks)
no_overlap = 0
for key in keys:
    for lock in locks:
        combo = key + lock
        if np.all(combo <= 5):
            no_overlap += 1
print(no_overlap)
