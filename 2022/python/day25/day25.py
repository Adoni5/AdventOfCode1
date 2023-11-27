test_input = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122"""
from pathlib import Path

# Snafu time
with open(Path(__file__).parent / "input.txt") as f:
    test_input = f.read().strip()
decimals = []
for test_line in test_input.splitlines():
    number = 0
    for power, char in enumerate(test_line[::-1], start=0):
        if char.isdigit():
            number += int(char) * 5**power
        else:
            if char == "-":
                number += -1 * 5**power
            else:
                number += -2 * 5**power
    decimals.append(number)
    # Convert to snafu

snafu_digits = {2: "2", 1: "1", 0: "0", -1: "-", -2: "="}
total = sum(decimals)
output = ""

while total:
    rem = total % 5
    print(rem)
    total //= 5
    print(total)
    if rem <= 2:
        print(f"rem <= 2 adding {rem}")
        output = str(rem) + output
    else:
        print(f"rem > 2 adding {rem} ", "   =-"[rem])

        output = "   =-"[rem] + output
        total += 1

print(output)
