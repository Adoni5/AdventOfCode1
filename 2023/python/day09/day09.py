test_input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

import numpy as np
from collections import deque
from support import get_input

test_input = get_input(9, 2023)

total = 0
total_p2 = 0
for line in test_input.splitlines():
    print()
    print(line)

    diffs = deque([])
    diffs.append(list(map(int, line.split())))
    while any(x for x in diffs[-1]):
        arr = np.diff(diffs[-1])
        diffs.append(arr.tolist())

    new_val = 0
    new_val_p2 = 0
    while diffs:
        term_diff = diffs.pop()
        print(term_diff)
        new_val += term_diff[-1]
        new_val_p2 = term_diff[0] - new_val_p2
        print(new_val_p2)
        print()
    total += new_val
    total_p2 += new_val_p2
print(total)
print(total_p2)
