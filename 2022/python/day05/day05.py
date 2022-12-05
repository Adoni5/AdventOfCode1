from collections import deque
import re
from support import get_input

test_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def parse_crates(crate_string: str) -> list[deque[str]]:
    deck = []
    pat = re.compile(r"(\[\w\])")
    for line in crates.splitlines():
        (width := (len(line) + 1) // 4)
        deck = [deque([]) for _ in range(width)] if not deck else deck
        for match in pat.finditer(line):
            deck[(match.start() // 4)].append(match.group())
    return deck

def p(op_instructions: str, deck: list[deque[str]], sort: int =1) -> None:
    pat = re.compile(r"(\d+)")
    for line in op_instructions.splitlines():
        amount, start, end = map(int, pat.findall(line))
        x = [deck[start - 1].popleft() for _ in range(amount)][::sort]
        deck[end-1].extendleft(x)
    print("".join([d[0][1]for d in deck]))

if __name__ == "__main__":
    #test p1
    crates, instruct = test_input.split("\n\n")
    deck = parse_crates(crate_string=crates)
    p(instruct, deck)
    
    #test p2
    deck = parse_crates(crate_string=crates)
    p(instruct, deck, -1)

    #actual p1
    aoc_input = get_input("5")
    crates, instruct = aoc_input.split("\n\n")
    deck = parse_crates(crate_string=crates)
    p(instruct, deck)

    #actual p2
    deck = parse_crates(crate_string=crates)
    p(instruct, deck, -1)