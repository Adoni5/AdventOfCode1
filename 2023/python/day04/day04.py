test_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
from collections import defaultdict
from support import get_input

test_input = get_input(4, 2023)

card_wins = defaultdict(int)
total = 0
for index, card in enumerate(test_input.splitlines()):
    card = card.split(":")
    winning_card, card = card[1].split("|")
    winning_numbers = set(int(x) for x in winning_card.strip().split())
    your_numbers = set(int(x) for x in card.strip().split())
    u_win = winning_numbers.intersection(your_numbers)
    card_wins[index + 1] = (len(u_win)) if len(u_win) else 0
    total += 2 ** (len(u_win) - 1) if len(u_win) else 0

print(total)
print(card_wins)
# p2
counts = defaultdict(int)
total = 0
for card_number, card_value in enumerate(test_input.splitlines(), start=1):
    # Numbers that match
    copies = counts[card_number]
    # For as many numbers that match
    for _ in range(copies + 1):
        # For the card after this one until the number of matches add 1
        for i in range(card_number + 1, card_number + 1 + card_wins[card_number]):
            counts[i] += 1
print(sum(val + 1 for val in counts.values()))
