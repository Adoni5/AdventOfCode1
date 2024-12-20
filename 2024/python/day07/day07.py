from operator import mul, add
import re
from itertools import product

test_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


with open("input.txt") as fh:
    test_input = fh.read()


def concat(a, b):
    return int(f"{a}{b}")


OPS = (mul, add, concat)
pat = re.compile(r"(\d+)")
c = 0
s = 0
for line in test_input.splitlines():
    t = tuple(map(int, pat.findall(line)))
    targ, cand = t[0], t[1:]
    n = len(cand) - 1
    for ops in list(product(OPS, repeat=n)):
        # print(ops)
        total = None
        n = 2
        for op in ops:
            # print(n)
            # print(total, n, cand, op)
            if total == None:
                total = op(*cand[:n])
            else:

                total = op(total, cand[n])
                n += 1
        if total == targ:
            c += 1
            s += targ
            break
    # break
print(s)
