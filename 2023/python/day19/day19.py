test_input = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

from collections import Counter, defaultdict
from math import prod
from operator import gt, lt
import re
from support import get_input

test_input = get_input(19, 2023)
wfs = defaultdict(list)
sorted_parts = Counter()
ops = {">": gt, "<": lt}

wf, ins = test_input.split("\n\n")
for line in wf.splitlines():
    wf_name, rem = line.split("{")
    rules = rem.split(",")
    wfs[wf_name] = ([], rules.pop()[:-1])
    for rule in rules:
        r, dest = rule.split(":")
        check, op, threshold = r[0], r[1], int(r[2:])
        print(check, op, threshold, dest)
        wfs[wf_name][0].append((check, ops[op], threshold, dest))

print(wfs)


def recurse_me(wf_name, part, wfs):
    print(wf_name, wfs)
    if wf_name in "AR":
        return wf_name, sum(int(x) for x in part.values())
    checks, fallback = wfs[wf_name]
    for c, op, t, d in checks:
        if op(int(part[c]), t):
            print("check met")

            return recurse_me(d, part, wfs)
    else:
        return recurse_me(fallback, part, wfs)


pat = re.compile(r"([xmas]).(\d+)+")
total = 0
for line in ins.splitlines():
    part = dict(pat.findall(line))
    status, sum_ = recurse_me("in", part, wfs)
    if status == "A":
        total += sum_

print(total)


def count(ranges, name="in"):
    if name == "R":
        return 0
    if name == "A":
        return prod(hi - lo + 1 for lo, hi in ranges.values())

    rules, fallback = wfs[name]

    total = 0

    for key, cmp, n, target in rules:
        lo, hi = ranges[key]
        if cmp == lt:
            T = (lo, n - 1)
            F = (n, hi)
        else:
            T = (n + 1, hi)
            F = (lo, n)
        if T[0] <= T[1]:
            new_ranges = dict(ranges)
            new_ranges[key] = T
            total += count(new_ranges, target)
        if F[0] <= F[1]:
            ranges = dict(ranges)
            ranges[key] = F
        else:
            break
    else:
        total += count(ranges, fallback)

    return total


print(count({key: (1, 4000) for key in "xmas"}))
