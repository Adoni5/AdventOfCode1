from collections import defaultdict, deque
from itertools import islice

test_string = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

with open("input.txt") as fh:
    test_string = fh.read()

rules, ordering = test_string.split("\n\n")

r = defaultdict(list)
for rule in rules.strip().splitlines():
    a, b = tuple(map(int, rule.split("|")))
    r[a].append(b)
p1 = 0
p2 = 0
for o in ordering.strip().splitlines():
    ordered = []
    correct = True
    ns = deque(map(int, o.split(",")))
    _ns = ns.copy()
    popped = -1
    while _ns:
        n = _ns.popleft()
        popped += 1
        rs = r[n]
        if not set(_ns).issubset(set(rs)):
            correct = False
            _correct = False
            i = 0
            while not _correct:
                _ns.insert(i, n)
                if set(list(_ns)[i + 1 :]).issubset(set(rs)):
                    _correct = True

                    break
                else:
                    del _ns[i]
                i += 1
        else:
            ordered.append(n)
    if correct:
        p1 += ns[int((len(ns) - 1) / 2)]
    else:
        p2 += ordered[int((len(ordered) - 1) / 2)]

print(p1)
print(p2)
