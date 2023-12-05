test_input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
from collections import defaultdict, deque
from support import get_input
from itertools import batched

test_input = get_input(5, 2023)
lookup = {}
# parse input
lines = iter(test_input.split("\n\n"))
seed_numbers = list(map(int, next(lines).split(": ")[1].split()))

source_to_dest = defaultdict(dict)

for mappy in lines:
    lines = iter(mappy.splitlines())
    _map_to = next(lines).split("-")
    source, dest = _map_to[0], _map_to[2][:-5]
    source_to_dest[source] = {"dest": dest}
    dest = source_to_dest[source]
    dest["ranges"] = []
    for mapping in lines:
        dest_, source, range_ = tuple(map(int, mapping.split()))
        # print(dest_, source, range_)
        diff = dest_ - source
        dest["ranges"].append((source, source + range_ - 1, diff))


# print(source_to_dest)
location = float("inf")
for seed in seed_numbers:
    key = "seed"
    # print("seed", seed)
    while True:
        if key not in source_to_dest or not source_to_dest[key]:
            break
        # If we don't have a range for it, the new value for the dest is the same as the value for the source
        # changed = False
        for range_start, range_end, diff in source_to_dest[key]["ranges"]:
            if range_end >= seed >= range_start:
                seed = seed + diff
                # changed = True
                break
        key = source_to_dest[key]["dest"]
        # print(key, seed)
        if key == "location":
            location = min(location, seed)
# print(location)
# P2 just start again
seed_ranges = [
    (seed_start, seed_start + seed_end)
    for seed_start, seed_end in batched(seed_numbers, n=2)
]
print(seed_ranges)
inputs, *blocks = test_input.split("\n\n")

inputs = list(map(int, inputs.split(":")[1].split()))
seeds = []

for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

location = float("inf")
key = "seed"
# print("seed", seed)
for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new = []
    while seed_ranges:
        s, e = seed_ranges.pop()
        for rs, re, d in ranges:
            os = max(s, re)
            oe = min(e, re + d)
            if os < oe:
                new.append((os - re + rs, oe - re + rs))
                if os > s:
                    seed_ranges.append((s, os))
                if e > oe:
                    seed_ranges.append((oe, e))
                break
        else:
            new.append((s, e))
    seed_ranges = new
    key = source_to_dest[key]["dest"]
print(min(seed_ranges)[0])
