test_input = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

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
