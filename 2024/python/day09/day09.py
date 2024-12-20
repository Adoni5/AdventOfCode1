from collections import defaultdict, deque
from itertools import cycle, islice
from operator import mul
from tqdm import tqdm

test_input = "2333133121414131472"


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
ordered_2 = {}
ptr = -1
free_block_ptrs = deque([])
free_block_spans = defaultdict(lambda: deque([]))
for x in roundrobin(files, free_blocks):
    if isinstance(x, int):
        free_block_spans[x].append(ptr + 1)
        for _ in range(x):
            ptr += 1
            ordered[ptr] = "."
            free_block_ptrs.append(ptr)

    elif isinstance(x, tuple):
        id, fl = x
        ordered_2[ptr + 1] = tuple(id for _ in range(fl))
        for _ in range(fl):
            ptr += 1
            ordered[ptr] = id
# print(free_block_ptrs)
# ordered_2 = ordered.copy()
# print(free_block_spans)
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
# print(ordered_2)
# part 2
for k, fb_ids in tqdm(ordered_2.items().__reversed__(), total=len(ordered_2)):
    fl = len(fb_ids)
    fits = [l for l in free_block_spans.keys() if l >= fl and free_block_spans[l]]
    if not fits:
        continue
    ptr = 1000000
    poppy = None
    # We need to choos the leftmost span that file can fit in, i.e the lowest ptr stored
    for fit in fits:
        if free_block_spans[fit][0] < ptr:
            ptr = free_block_spans[fit][0]
            poppy = fit
    # Don't move right
    if k < ptr:
        continue
    free_block_spans[poppy].popleft()
    # update order
    ordered_2.pop(k)
    ordered_2[ptr] = fb_ids
    # now update the spans
    free_block_spans[(poppy - fl)].appendleft(ptr + fl)
    free_block_spans[(poppy - fl)] = deque(sorted(free_block_spans[(poppy - fl)]))
# print(dict(sorted(ordered_2.items())))
print(sum(mul(i, id) for (i, id) in enumerate(ordered.values()) if isinstance(id, int)))
print(sum(mul(i + j, id[0]) for (i, id) in ordered_2.items() for j in range(len(id))))
