from string import ascii_lowercase
from support import get_input, group_by_lines

test_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

lookup = dict(zip(ascii_lowercase, range(1,100)))

def score(letter: str) -> int:
    """Convert overlapping letter to score
    """
    return lookup.get(letter) if letter.islower() else lookup.get(letter.lower()) + 26

def score_ord(letter: str) -> int:
    """Just for fun using ord rather than a lookup as it's built in so no extra imports
    """
    return ord(letter) - 96 if letter.islower() else ord(letter) - 38

input = get_input("3", split="\n")

print(sum(score(set(lin[:int(len(lin)/2)]).intersection(set(lin[int(len(lin)/2):])).pop()) for lin in test_input.splitlines()))
print(sum(score(set(lin[:int(len(lin)/2)]).intersection(set(lin[int(len(lin)/2):])).pop()) for lin in input))
print(sum(score_ord(set(lin[:int(len(lin)/2)]).intersection(set(lin[int(len(lin)/2):])).pop()) for lin in input))

# Part 2
print(sum(score(set(elf1).intersection(set(elf2)).intersection(set(elf3)).pop()) for elf1, elf2, elf3 in group_by_lines(3, input)))
print(sum(score_ord(set(elf1).intersection(set(elf2)).intersection(set(elf3)).pop()) for elf1, elf2, elf3 in group_by_lines(3, input)))

