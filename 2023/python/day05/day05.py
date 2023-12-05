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


def merge_intervals(intervals):
    sorted_intervals = sorted(intervals)
    collapsed_intervals = []
    curr_start, curr_end = sorted_intervals[0]
    for start, end in sorted_intervals[1:]:
        if start > curr_end:  # We have a new non-overlapping start
            collapsed_intervals.append((curr_start, curr_end))
            curr_start, curr_end = start, end
        else:  # Start is within the current range
            curr_end = max(curr_end, end)
    collapsed_intervals.append((curr_start, curr_end))
    return collapsed_intervals


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
    (seed_start, seed_start + seed_end - 1)
    for seed_start, seed_end in batched(seed_numbers, n=2)
]
location = float("inf")
for seed_start, seed_end in seed_ranges:
    key = "seed"
    # print("seed range", seed_start, seed_end)
    ranges = deque([(seed_start, seed_end)])
    while True:
        if key not in source_to_dest or not source_to_dest[key]:
            break
        new_ranges = deque([])
        while ranges:
            if key == "location":
                # print("breaking for location")
                break
            # print("doing a range")

            seed_start, seed_end = ranges.popleft()
            # print(f"\nexamening seed range {seed_start}, {seed_end}")
            found_match = False
            for range_start, range_end, diff in source_to_dest[key]["ranges"]:
                # print(
                #     f"against range_start {range_start}, range_end {range_end}, diff {diff}"
                # )
                # Seed Range is inside the range range
                if (
                    range_end >= seed_start >= range_start
                    and range_end >= seed_end >= range_start
                ):
                    print("Seed Range is inside the range range, breaking")
                    nseed_start = seed_start + diff
                    nseed_end = seed_end + diff
                    new_ranges.append((nseed_start, nseed_end))
                    found_match = True
                    break

                # Seed range overlaps range but runs past end
                elif range_end >= seed_start >= range_start and seed_end > range_end:
                    print("Seed range overlaps range but come off the end")
                    nseed_start = seed_start + diff
                    nseed_end = range_end + diff
                    new_ranges.append((nseed_start, nseed_end))
                    # Append the bit after the range
                    new_ranges.append((range_end + 1, seed_end))
                    found_match = True

                # Seed range overlaps range but starts before range
                elif range_end >= seed_end >= range_start and seed_start < range_start:
                    # print("Seed range overlaps range but comes off the start")

                    nseed_end = seed_end + diff
                    nseed_start = range_start + diff
                    new_ranges.append((nseed_start, nseed_end))
                    # Append the bit after the overlapping ranges
                    new_ranges.append((seed_start, range_start - 1))
                    found_match = True

                # No overlap, add the seed range back in
                # elif not (range_end >= seed_start >= range_start) and not (
                #     range_end >= seed_end >= range_start
                # ):
                #     print("no overlap, adding seed range")
                #     ranges.append((seed_start, seed_end))
            # No overlap too any src dest ranges, add the seed range back in
            if not found_match:
                print(f"no match found, readding same values for key {key}")
                new_ranges.append((seed_start, seed_end))
            # input()

        key = source_to_dest[key]["dest"]
        ranges = deque(merge_intervals(new_ranges))

        # print(f"ranges after all iterations {sorted(ranges)} fro key {key}")
    # print(f"key {key}, val {nseed_start} to {nseed_end}")
    print(sorted(ranges))
    location = min(location, min(range_start for range_start, _ in ranges))
    # input()
    # break

print(f"P2 location {location}")
