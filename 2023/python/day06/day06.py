test_input = """Time:      7  15   30
Distance:  9  40  200"""

from functools import cache
import re
from support import get_input


@cache
def boaty(button, time):
    return (time - button) * button


test_input = get_input(6, 2023)

pat = re.compile(r"(\d+)")
times, dists = test_input.splitlines()
pairs = list(zip(map(int, pat.findall(times)), map(int, pat.findall(dists))))

# Let's try going through every pair
total = 1
for time, dist_to_beat in pairs:
    total *= sum(1 for i in range(1, time) if boaty(i, time) > dist_to_beat)
print(total)

# P2
pat = re.compile(r"(\d+)")
times, dists = test_input.splitlines()
pairs = list(
    zip(
        map(int, ["".join(pat.findall(times)).replace(" ", "")]),
        map(int, ["".join(pat.findall(dists)).replace(" ", "")]),
    )
)
print(pairs)
total = 1
for time, dist_to_beat in pairs:
    total = sum(1 for i in range(1, time) if boaty(i, time) > dist_to_beat)
print(total)
