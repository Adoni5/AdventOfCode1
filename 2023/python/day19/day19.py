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
from operator import gt, lt
import re
from support import get_input

# test_input = get_input(19, 2023)
wfs = defaultdict(list)
sorted_parts = Counter()
ops = {">": gt, "<": lt}

wf, ins = test_input.split("\n\n")
for line in wf.splitlines():
    wf_name, rem = line.split("{")
    rules = rem.split(",")
    final_dest = rules[-1][:-1]
    for rule in rules[:-1]:
        r, dest = rule.split(":")
        check, op, threshold = r[0], r[1], int(r[2:])
        print(check, op, threshold, dest)
        wfs[wf_name].append((check, ops[op], threshold, dest))
    wfs[wf_name].append((None, None, None, final_dest))

print(wfs)


def recurse_me(wf_name, part, wfs):
    checks = wfs[wf_name]
    for c, op, t, d in checks:
        print(c, op, t, d)
        if t is not None and op(int(part[c]), t):
            print("check met")
            if d in "AR":
                return d, sum(int(x) for x in part.values())
            return recurse_me(d, part, wfs)

    print(f"final d {d}")
    if d in "AR":
        return d, sum(int(x) for x in part.values())
    return recurse_me(d, part, wfs)


pat = re.compile(r"([xmas]).(\d+)+")
total = 0
for line in ins.splitlines():
    part = dict(pat.findall(line))
    status, sum_ = recurse_me("in", part, wfs)
    if status == "A":
        total += sum_

print(total)
