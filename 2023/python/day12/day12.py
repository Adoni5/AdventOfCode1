test_input = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

# test_input = """??#.### 1,3"""
import collections
from itertools import islice
import math
import re

from collections import deque, Counter


# From itertools - slide along and count all the # in the match
def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n - 1), maxlen=n)
    for x in it:
        window.append(x)
        yield tuple(window)


pat = re.compile(r"([\?#]+)")
pat2 = re.compile(r"(#+)")
poss = 0
count = 0
for line in test_input.splitlines():
    # if count == 3:
    #     break
    springs, contigs = line.split()
    contigs = list(map(int, contigs.split(",")))
    matches = deque(pat.findall(springs))
    print(matches, contigs)
    print()
    go = True
    possy = []
    contigs_done = 0
    while matches:
        match = matches.popleft()
        total_len = len(match)
        print("\n", match, total_len)
        contig_fits = 0
        contig_fits_sum = 0
        num_hash = match.count("#")
        print(f"num hash {num_hash}")
        for i, contig in enumerate(contigs[contigs_done:]):
            print(i, contig)
            if contig_fits_sum + contig > total_len:
                break
            contigs_done += 1
            print(f"adding contig {contig}")
            contig_fits_sum += contig

            contig_fits_sum += 1
            contig_fits += 1
        print(f"contig fits susm {contig_fits_sum}")
        occupied = contig_fits_sum - 1 if contig_fits == 1 else (contig_fits_sum - 2)
        print(f"occupied {occupied}")
        num_hash_matched = 0
        for sub_section in sliding_window(match, occupied):
            print(sub_section)
            num_hash_matched_sub = "".join(sub_section).count("#")
            if num_hash == num_hash_matched_sub:
                num_hash_matched += 1

        print(num_hash_matched)
        # Check all hashtags are covered?

        possy.append(num_hash_matched)
    print(possy)
    print(f"Possible arrangements {math.prod(possy)}")
    count += 1
    poss += math.prod(possy)
print(poss)
