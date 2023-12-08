test_input = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

from collections import deque
from itertools import cycle
import re
from support import get_input


test_input = get_input(8, 2023)

pat = re.compile(r"(\w{3})")

instructions, nodes = test_input.split("\n\n")
# print(pat.findall(nodes.splitlines()[0]))
n_lookup = {}
for line in nodes.splitlines():
    source, l, r = pat.findall(line)
    n_lookup[source] = (l, r)

count = 0

instructions = cycle(instructions)
count = 0
dest = "AAA"
while 1:
    count += 1
    instruction = 1 if next(instructions) == "R" else 0
    # print(instruction)
    if n_lookup[dest][instruction] == "ZZZ":
        break
    dest = n_lookup[dest][instruction]


print(count)
# P2 am i dumb?
import math
from functools import reduce

# test_input = """LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)"""

instructions, nodes = test_input.split("\n\n")
# print(pat.findall(nodes.splitlines()[0]))
n_lookup = {}
for line in nodes.splitlines():
    source, l, r = pat.findall(line)
    n_lookup[source] = (l, r)

count = 0
ends_with_a = deque([key for key in n_lookup.keys() if key.endswith("A")])
print(ends_with_a)

numbers = []
for dest in ends_with_a:
    print(dest)
    instructions = cycle(instructions)

    count = 0
    while 1:
        count += 1
        instruction = 1 if next(instructions) == "R" else 0
        # print(instruction)
        if n_lookup[dest][instruction].endswith("Z"):
            break
        dest = n_lookup[dest][instruction]
    numbers.append(count)
print(numbers)


def lcm_of_numbers(nums):
    """
    Calculate the LCM of a list of numbers.
    """

    def lcm(x, y):
        return x * y // math.gcd(x, y)

    return reduce(lcm, nums, 1)


print(lcm_of_numbers(numbers))
