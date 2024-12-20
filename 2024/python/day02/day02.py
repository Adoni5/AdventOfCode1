test_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

from itertools import pairwise

safe = 0

with open("input.txt") as fh:
    test_input = fh.read()


def safe(l):
    series = pairwise(l)
    p = None
    for a, b in series:
        d = a - b
        if d < -3 or d == 0 or d > 3:
            return False
        _p = False if d < 0 else True
        if p is None:
            p = _p
        else:
            if p != _p:
                return False
    return True


print(sum(safe(map(int, line.strip().split())) for line in test_input.splitlines()))

count = 0
for line in test_input.splitlines():
    ll = []
    l = list(map(int, line.split()))
    for i in range(len(l)):

        _l = list(map(int, line.split()))
        _l.pop(i)
        ll.append(_l)
    count += int(any((safe(x) for x in ll)))
print(count)
