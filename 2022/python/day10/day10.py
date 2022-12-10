from pprint import pprint
from support import get_input


test_input = """noop
addx 3
addx -5"""


def cycleotron(input: str | list, screen: list[list[str]]) -> int:
    """Cycle me babay"""
    register = 1
    cycles = {"noop": 1, "addx": 2}
    cycle = 0
    banter = []
    pixel = 0
    dx, dy = (1, -1)
    row = 0
    p1 = False

    if isinstance(input, str):
        input = input.splitlines()
    
    for line in input:
    # for line in test_input.splitlines():
        op, amt = line.strip().split() if len(line) > 5 else (line.strip(), 0)
        for _ in range(cycles[op]):
            # print(cycle, register)
            cycle += 1
            sprite_pos = {register + dx, register + dy, register }
            if cycle == 20:
                # print(register)
                banter.append(register * cycle)
            elif not (cycle -20) % 40:
                # print(cycle, register)
                banter.append(register * cycle)
            if not (_ + 1) % 2:
                register += int(amt)
            # move down a row
            if not cycle % 40:
                row += 1
            if pixel % 40 in sprite_pos:
                screen[row][pixel % 40] = "#"
            
            pixel += 1
        if cycle > 220 and not p1:
            p1 = True
            yield sum(banter)
        if cycle == 239:
            # print()
            yield "\n".join(["".join(r) for r in screen])
    yield None
# p2 no banter
rows = [["."] * 40 for _ in range(6)]
# print("\n".join(rows))
parts = ("P1\t", "P2\n")
with open("2022/python/day10/test_input.txt") as fh:
    for part, ans in zip(parts, cycleotron(fh, rows)):
        print(f"{part}{ans}")

# refresh the rows
rows = [["."] * 40 for _ in range(6)]
# print(f"P1 {cycleotron(get_input('10'))}")   
for part, ans in zip(parts, cycleotron(get_input("10"), rows)):
        print(f"{part}{ans}")


