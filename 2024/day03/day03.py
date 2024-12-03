import re
from operator import mul

test_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

with open("input.txt") as fh:
    test_input = fh.read()
print(test_input)
f = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", test_input)
print(f)
c = 0
do = True
for x in f:
    if x == "do()":
        do = True
        continue
    elif x == "don't()":
        do = False
        continue
    if do:
        c += eval(x)
print(c)
