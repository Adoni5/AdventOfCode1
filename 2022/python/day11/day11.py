test_input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""

import re 
from operator import sub, add, mul, floordiv
from collections import defaultdict, deque
from support import get_input
import sys
import math
import numpy as np
sys.set_int_max_str_digits(1000000)
op_lookup = {"+": add, "-": sub, "*": mul}
pat = re.compile(r"(\d+|[*+-]|old)")
monkeys = defaultdict(dict)
keys = ("monkey", "items", "op", "test", True, False)
key1 = False
test_input = get_input("11")
for monkey in test_input.split("\n\n"):
    print(monkey)
    for key, line in zip(keys, monkey.splitlines()):
        key1 = pat.findall(line)[0] if not key1 else key1
        monkeys[key1][key] = pat.findall(line)
    monkeys[key1]["inspected"] = 0
    monkeys[key1]["items"] = deque(map(int, monkeys[key1]["items"]))
    monkeys[key1]["op"][-1] = int(monkeys[key1]["op"][-1]) if monkeys[key1]["op"][-1] != "old" else monkeys[key1]["op"][-1]

    key1 = False
print(monkeys)
# Congruence is a pack of lies and the wikipedia article onit can do one I remember you from last year you wankstain ANGER AHHHHHHHHHHHHHHHH
mod = math.prod([int(m.get("test")[0]) for m in monkeys.values()])
print(mod)
# sys.exit()
for i in range(10000):
    print(i)
    for monkey, value in monkeys.items():
        while value["items"]:
            item = value["items"].popleft()
            value["inspected"] += 1
            # print(item)
            # print(value["op"])
            _, op, amt = value["op"]
            amt = item if amt == "old" else amt
            # worry_level = floordiv(op_lookup[op](item, int(amt)), 3)
            # print(op, amt)
            
            worry_level = (op_lookup[op](item, amt) % mod)
            print(worry_level)
            throw_to = value[not bool(worry_level % int(value["test"][0]))][0]

            monkeys[throw_to]["items"].append(worry_level)



print(monkeys)
print(mul(*sorted([v.get("inspected") for v in monkeys.values()])[-2:]))