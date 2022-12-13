from itertools import zip_longest
from support import get_input
from functools import cmp_to_key

test_input = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

test_input = get_input("13")

def compare_items(cl, cr, p2=True):
    """COmpare items"""
    for cl, cr in zip_longest(cl, cr):
        # print(cl, cr)
        if cl is None:
            return True if not p2 else -1
        if cr is None:
            return False if not p2 else + 1
        # both ints
        if isinstance(cl, int) and isinstance(cr, int):
            # print(f"both ints {cl} {cr}")
            if cl == cr:
                continue
            if p2:
                return -1 if cl < cr else + 1
            else:
                return cl < cr
        #one of them is a list
        elif isinstance(cl, int) or isinstance(cr, int):
            # print("gello")
            # cr is the list
            if isinstance(cl, int):
                ans = compare_items([cl], cr, p2)
            else:
                ans = compare_items(cl, [cr], p2)
            if ans is None:
                continue
            return ans
        # both lists
        else:
            # print(f"both lists {cl} {cr}")
            ans = compare_items(cl, cr, p2)
            if ans is None:
                continue
            return ans
sums = []
for i, pair in enumerate(map(str.split, test_input.split("\n\n")), start=1):
    left, right = map(eval, pair)
    sums.append(i * compare_items(left, right, p2=False))
print(sum(sums))


# p2
p2_test_input = test_input.replace("\n\n", "\n")
p2_test_input += """
[[2]]
[[6]]"""
# print(p2_test_input)
p2 = sorted(map(eval, p2_test_input.splitlines()), key=cmp_to_key(compare_items))
print((p2.index([[2]])+1) * (p2.index([[6]])+1))
