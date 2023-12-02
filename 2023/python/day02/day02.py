test_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

from collections import defaultdict
import re
from support import get_input
from math import prod

test_input = get_input("2", year="2023")
pat = re.compile(r"(\d+) (blue|red|green)")
fake_games = []
real_games = []
for index, line in enumerate(test_input.splitlines(), start=1):
    # print(line)
    fake_line = False
    counts = defaultdict(int)
    for count, color in pat.findall(line):
        # counts[color] = int(count) if int(count) > counts[color] else counts[color]
        count = int(count)
        if count > 12 and color == "red":
            fake_games.append(index)
            fake_line = True
            break
        if count > 13 and color == "green":
            fake_games.append(index)
            fake_line = True
            break
        if count > 14 and color == "blue":
            fake_games.append(index)
            fake_line = True
            break
    if not fake_line:
        real_games.append(index)

print(sum(real_games))

# P2
powers = []
for index, line in enumerate(test_input.splitlines(), start=1):
    # print(line)
    fake_line = False
    counts = defaultdict(int)
    for count, color in pat.findall(line):
        count = int(count)
        counts[color] = count if count > counts[color] else counts[color]
    power = prod(counts.values())
    powers.append(power)
print(sum(powers))
