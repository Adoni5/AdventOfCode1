from operator import sub, add
import sys

dial = 50
maxi = 100
ops = {"L": sub, "R": add}
p1 = 0
p2 = 0
for line in sys.stdin.read().splitlines():
    direct = line[0]
    distance = int(line[1:])
    pass_zero = distance // 100
    distance = distance % 100

    if dial == 0 and direct == "L":
        pass_zero -= 1
    dial = ops[direct](dial, distance)
    if dial <= 0 or dial > 99:
        pass_zero += 1
    dial = dial % 100
    if dial == 0:
        p1 += 1

    print(f"The dial is rotated {line} to point at {dial}.")
    p2 += pass_zero

print(f"P1: {p1}")
print(f"P2: {p2}")

