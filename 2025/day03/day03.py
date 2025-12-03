import sys
from itertools import combinations

total = 0
for bank in sys.stdin.read().splitlines():
    total += max(map(int, map("".join, combinations(bank, 2))))
    print(total)