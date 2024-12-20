test_input = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""


from functools import cache

with open("input.txt") as fh:
    test_input = fh.read()

towels, patterns = test_input.split("\n\n")
towels = tuple(towels.split(", "))


@cache
def recurse_me(pat):
    # We got it bois
    if len(pat) == 0:
        return 1
    # Gimme some truncated pattern
    return sum(
        recurse_me(pat[len(towel) :]) for towel in towels if pat.startswith(towel)
    )


c = 0
for p in patterns.splitlines():
    if recurse_me(p) > 0:
        c += 1
print(c)
print(sum(recurse_me(p) for p in patterns.splitlines()))
