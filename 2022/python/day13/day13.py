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

# test_input = get_input("13")

def compare_items(cl, cr):
    """COmpare items"""
    for cl, cr in zip_longest(cl, cr):
        # print(cl, cr)
        if cl is None:
            return True
        if cr is None:
            return False
        # both ints
        if isinstance(cl, int) and isinstance(cr, int):
            # print(f"both ints {cl} {cr}")
            if cl == cr:
                continue
            return cl < cr
        #one of them is a list
        elif isinstance(cl, int) or isinstance(cr, int):
            # print("gello")
            # cr is the list
            if isinstance(cl, int):
                ans = compare_items([cl], cr)
            else:
                ans = compare_items(cl, [cr])
            if ans is None:
                continue
            return ans
        # both lists
        else:
            # print(f"both lists {cl} {cr}")
            ans = compare_items(cl, cr)
            if ans is None:
                continue
            return ans
sums = []
for i, pair in enumerate(map(str.split, test_input.split("\n\n")), start=1):
    left, right = map(eval, pair)
    print(left, right)
    sums.append(i * compare_items(left, right))
print(sum(sums))


# p2
p2_test_input = test_input.replace("\n\n", "\n")
# print(p2_test_input)
print(sorted(map(eval, p2_test_input.splitlines()), key=cmp_to_key(compare_items)))
print(list(map(eval, p2_test_input.splitlines())))