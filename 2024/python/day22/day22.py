from math import floor

test_input = """1
2
3
2024"""

# 15887950
# 16495136
# 527345
# 704524
# 1553684
# 12683156
# 11100544
# 12249484
# 7753432
# 5908254

with open("input.txt") as fh:
    test_input = fh.read()


def mix(num1, num2):
    return num1 ^ num2


def prune(num):
    return num % 16777216


def step1(num):
    return prune(mix(num * 64, num))


def step2(num):
    return prune((mix(floor(num / 32), num)))


def step3(num):
    return prune(mix(num * 2048, num))


def secretize(num):
    return step3(step2(step1(num)))


from pprint import pprint
from collections import Counter, defaultdict

c = 0
d = defaultdict(list)
for line in test_input.splitlines():
    _d = set()
    n = int(line)
    costs = [int(line[-1])]
    ns = [n]
    changes = []
    for i in range(2000):
        n = secretize(n)
        cost = int(str(n)[-1])
        if costs:
            changes.append(cost - costs[-1])
        if len(changes) >= 4:
            change_string = tuple(changes[-4:])
            if change_string not in _d:
                d[change_string].append(cost)
                _d.add(change_string)
        costs.append(cost)
        ns.append(n)
    c += n

best_change = None
max_banans = -float("inf")

for k, v in d.items():
    if sum(v) > max_banans:
        best_change = k
        max_banans = sum(v)

print(best_change, max_banans)
