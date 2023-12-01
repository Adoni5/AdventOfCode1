test_input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

with open("input.txt") as f:
    test_input = f.read().strip()

ans = []
for l in test_input.splitlines():
    a = list(filter(str.isdigit, iter(l)))
    # print(a[0], a[-1])
    ans.append(int(f"{a[0]}{a[-1]}"))

print(sum(ans))

# Part 2
import regex as re

lookup = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def dashrepl(matchobj):
    print(matchobj.group(0))
    return str(lookup.get(matchobj.group(0), ""))


# test_input = "jjjjoneight66seven82sevenkas\n"

pat = re.compile(r"(one|two|three|four|five|six|seven|eight|nine|[1-9])")
# test_input = """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen"""
ans = []
print(len(test_input.splitlines()))

for l in test_input.splitlines():
    number = pat.findall(l, overlapped=True)
    print(number)

    a = list(map(lambda x: lookup.get(x, x), iter(number)))
    print(a)
    ans.append(int(f"{a[0]}{a[-1]}"))

print(ans)
print(sum(ans))
