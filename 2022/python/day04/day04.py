import re
from support import get_input

test_input="""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

def super_clean(input: list[str], pat: re.Pattern) -> tuple[int, int]:
    """Return counts of whole and partial subsets in input ranges
    """
    count = 0
    count_p2 = 0
    for lin in input:
        elf_1_start, elf_1_end, elf_2_start, elf_2_end = map(int, pat.findall(lin))
        elf_1, elf_2 = set(range(elf_1_start, elf_1_end+1)), set(range(elf_2_start, elf_2_end+1))
        count += any((elf_1.issubset(elf_2), elf_1.issuperset(elf_2)))
        count_p2 += any((elf_1.intersection(elf_2)))
    return count, count_p2


pat = re.compile(r"(\d+)")
print(super_clean(test_input.strip().splitlines(), pat))
# Part 1
p1, p2 = super_clean(get_input("4", split="\n"), pat)
print(f"Part 1 {p1} \nPart 2 {p2}")
    
