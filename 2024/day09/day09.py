test_input = "2333133121414131402"

from collections import deque
from itertools import cycle, islice


def roundrobin(*iterables):
    "Visit input iterables in a cycle until each is exhausted."
    # roundrobin('ABC', 'D', 'EF') → A D E B F C
    # Algorithm credited to George Sakkis
    iterators = map(iter, iterables)
    for num_active in range(len(iterables), 0, -1):
        iterators = cycle(islice(iterators, num_active))
        yield from map(next, iterators)


d = list(zip(enumerate(map(int, test_input))))

files = d[::2][::-1]
print(d)
id = len(files) - 1
new_order = []
b = {}
for f in files:
    for i, block in enumerate(d):
        if i % 2:
            # f_blokc
            if block >= f:
                d[i] -= f

    id -= 1
print(d)
