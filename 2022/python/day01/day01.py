test_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


def fattest_elf(input: str) -> int:
    elves = input.split("\n\n")
    return max(sum(map(int, elf.strip().split("\n"))) for elf in elves)


def top_3_fattys(input: str) -> int:
    elves = input.strip().split("\n\n")
    return sum(sorted((sum(map(int, elf.strip().split("\n"))) for elf in elves))[-3:])


print(fattest_elf(test_input))
print(top_3_fattys(test_input))

with open("day01.txt") as fh:
    text = fh.read()
    print(f"Part 1 {fattest_elf(text)}")
    # part two
    print(f"Part 2 {top_3_fattys(text)}")
