from collections import defaultdict, deque
from itertools import cycle, islice
from operator import mul
from tqdm import tqdm

test_input = "2333133121414131402"


def roundrobin(*iterables):
    "Visit input iterables in a cycle until each is exhausted."
    # roundrobin('ABC', 'D', 'EF') → A D E B F C
    # Algorithm credited to George Sakkis
    iterators = map(iter, iterables)
    for num_active in range(len(iterables), 0, -1):
        iterators = cycle(islice(iterators, num_active))
        yield from map(next, iterators)


with open("input.txt") as fh:
    test_input = fh.read()

d = list(map(int, test_input))
# We need indices for the files

# Id, length
files = list(tuple(enumerate(d[::2])))
free_blocks = d[1::2]
ordered = {}
ptr = -1
free_block_ptrs = deque([])
free_block_spans = defaultdict(deque)
for x in roundrobin(files, free_blocks):
    if isinstance(x, int):
        for _ in range(x):
            free_block_spans[ptr].append(x - _)
            ptr += 1
            ordered[ptr] = "."
            free_block_ptrs.append(ptr)

    elif isinstance(x, tuple):
        id, fl = x
        for _ in range(fl):
            ptr += 1
            ordered[ptr] = id
# print(free_block_ptrs)
# print(ordered)

for k, id in tqdm(ordered.items().__reversed__(), total=len(ordered)):
    # for k, id in ordered.items().__reversed__():
    if id == 0 or id == ".":
        continue
    # print(k, id)
    if free_block_ptrs:
        free_block = free_block_ptrs.popleft()
        if k > free_block:
            # print(f"moving {id} from {k} to {free_block}")
            ordered[k] = "."
            ordered[free_block] = id
    else:
        break
# print(ordered)
print(sum(mul(i, id) for (i, id) in enumerate(ordered.values()) if isinstance(id, int)))
