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
from collections import defaultdict
from support import get_input

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
    for mapping in lines:
        dest_, source, range_ = tuple(map(int, mapping.split()))
        # print(dest_, source, range_)
        for i in range(range_):
            # print(i)
            dest[source + i] = dest_ + i


# print(source_to_dest)
location = float("inf")
for seed in seed_numbers:
    key = "seed"
    print("seed", seed)
    while True:
        if key not in source_to_dest or not source_to_dest[key]:
            break
        seed = source_to_dest[key].get(seed, seed)
        key = source_to_dest[key]["dest"]
        # print(key, seed)
        if key == "location":
            location = min(location, seed)
print(location)
