test_input = "125 17"

from collections import Counter

with open("input.txt") as fh:
    test_input = fh.read()
stones = Counter(s for s in map(int, test_input.strip().split()))

print(stones)
for _i in range(75):
    s_ = Counter()
    for k, v in stones.items():
        if k == 0:
            s_[1] += v
        elif not len(str(k)) % 2:
            st = str(k)
            a, b = tuple(map(int, (st[: int(len(st) / 2)], st[int(len(st) / 2) :])))
            s_[a] += v
            s_[b] += v
        else:
            s_[k * 2024] += v
    stones = s_
    # print(stones.keys())
print(sum(stones.values()))
