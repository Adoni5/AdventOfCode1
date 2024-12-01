test_input = """3   4
4   3
2   5
1   3
3   9
3   3"""

from collections import Counter

with open("input.txt") as fh:
    left_list, right_list = [], []
    test_input = fh.read()
    for line in test_input.splitlines():
        a, b = tuple(map(int, line.strip().split()))
        left_list.append(a)
        right_list.append(b)

    print(sum(abs(a - b) for a, b in zip(sorted(left_list), sorted(right_list))))
    c = Counter(right_list)
    print(sum(id * c[id] for id in left_list))
