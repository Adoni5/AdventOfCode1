test_input = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""
from support import get_input


from operator import mul, truediv, sub, add, gt, lt
l = {"*": mul, "/": truediv, "-": sub, "+": add}
test_input = get_input("21")
# print(test_input)
monkeys = dict(line.split(": ") for line in test_input.splitlines())
## Lazy cause my brain no work
for k, v in monkeys.items():
    if v.isdigit():
        monkeys[k] = int(v)
    else:
        monkeys[k] = tuple(v.split())

def get_monkey_number(name: str):
    """Recursively walk the tree, calculating a monkeys number"""
    monkey = monkeys[name]
    if isinstance(monkey, int):
        return monkey
    else:
        monkey_dep1, op, monkey_dep2 = monkey
        return l[op](get_monkey_number(monkey_dep1), get_monkey_number(monkey_dep2))
    
### Had to look up part 2
### Looks like fancy brute forcing is the way to go?
### This is so sick
    
def binary_search(target, low:int, high:int, reverse_search=False) -> int:
    """ Generic binary search function that takes a target to find,
    low and high values to start with, and a function to run, plus its args. 
    Implicitly returns None if the search is exceeded. """
    
    res = None  # just set it to something that isn't the target
    candidate = 0  # initialise; we'll set it to the mid point in a second
    
    while low < high:  # search exceeded        
        candidate = int((low+high) // 2)  # pick mid-point of our low and high        
        # print(f"{candidate}->{res}")
        monkeys["humn"] = candidate
        res = get_monkey_number("root")
        if res == target:
            return candidate
        
        comp = gt if not reverse_search else lt
        if comp(res, target):
            low = candidate
        else:
            high = candidate



if __name__ == "__main__":
    print(get_monkey_number("root"))
    print("Part 2")
    monkeys["root"] = (monkeys["root"][0], "-", monkeys["root"][2])
    take1 = binary_search(0, 0, 1e20)
    print(take1)
    if take1 is None:
        print(binary_search(0,0, 1e20, reverse_search=True))
