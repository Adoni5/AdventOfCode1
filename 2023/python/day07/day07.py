test_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

ranked_hands = []
from collections import Counter, defaultdict
from functools import cmp_to_key
from pprint import pprint
from support import get_input

test_input = get_input(7, 2023)

# five of a kind
# four of a kind
# full house (three and 2 the same)
# three of a kind
# 2 pair
# 1 pair
# High card
# sorted_by_type = defaultdict(list)
# cards = "A,K,Q,J,T,9,8,7,6,5,4,3,2"
# order_value = dict(zip(cards.split(","), range(len(cards))))
# print(order_value)
# for line in test_input.splitlines():
#     hand, bid = line.split()
#     bid = int(bid)  #
#     # print(hand)
#     hand = list(hand)
#     # print(hand)
#     # Rules are ranked so let's go through them highest to lowest
#     c = Counter(hand)
#     # print(c)
#     # do rules
#     counts = c.most_common(2)
#     # Only one letter/number
#     # print(c)
#     if len(counts) == 1:
#         # print("five of a kind!")
#         sorted_by_type[7].append((hand, bid))
#         continue
#     counts_max, counts_2_max = counts[0][1], counts[1][1]
#     if counts_max == 4:
#         # print("Four of a kind")
#         sorted_by_type[6].append((hand, bid))
#     elif counts_max == 3 and counts_2_max == 2:
#         # print("Full house baby")
#         sorted_by_type[5].append((hand, bid))
#     elif counts_max == 3:
#         # print("three of akind")
#         sorted_by_type[4].append((hand, bid))
#     elif counts_max == 2 and counts_2_max == 2:
#         # print("2 PAIR")
#         sorted_by_type[3].append((hand, bid))

#     elif counts_max == 2:
#         # print("1 pair!")
#         sorted_by_type[2].append((hand, bid))

#     elif counts_max == 1 and counts_2_max == 1:
#         # print("High cared")
#         sorted_by_type[1].append((hand, bid))
#     else:
#         print("WHAT IS HTIS")


def sort_me(a: tuple[list[str], int], b: tuple[list[str]]) -> int:
    c = a[0][:5]
    d = b[0][:5]
    for e, f in zip(c, d):
        e, f = order_value[e], order_value[f]
        if e == f:
            continue
        if e > f:
            return -1
        if e < f:
            return 1
    return 0


# for hand_type, hands in sorted(sorted_by_type.items()):
#     if len(hands) > 1:
#         # print(hands)
#         hands.sort(key=cmp_to_key(sort_me))
# rank = 1
# total = 0
# for _, value in sorted(sorted_by_type.items()):
#     for _, bid in value:
#         total += rank * bid
#         rank += 1
# print(total)

# p2 big gulps huh
cards = "A,K,Q,T,9,8,7,6,5,4,3,2,J"
order_value = dict(zip(cards.split(","), range(len(cards))))
sorted_by_type = defaultdict(list)


def sort_me2(a: tuple[list[str], int], b: tuple[list[str]]) -> int:
    c = a[0][:5]
    d = b[0][:5]
    for e, f in zip(c, d):
        e, f = order_value[e], order_value[f]
        if e == f:
            continue
        if e > f:
            return -1
        if e < f:
            return 1
    return 0


print(order_value)
for line in test_input.splitlines():
    hand_, bid = line.split()
    bid = int(bid)  #
    # print(hand)
    hand = list(hand_)
    # print(hand)
    # Rules are ranked so let's go through them highest to lowest
    c = Counter(hand)
    if "J" in hand:
        print(f"joker hand {hand}")
        c = Counter(hand_.replace("J", ""))
        # all Js baby
        if not c:
            c = Counter("#####")
        counts = c.most_common()
        # ASSUME just adding the most common card is always the best thing to do else sadge
        most_common_card = counts[0][0]
        hand__ = list(hand_.replace("J", most_common_card))
        c = Counter(hand__)
        # break
    counts = c.most_common(2)
    print(hand, counts)
    # Only one letter/number
    if len(counts) == 1:
        print("five of a kind!")
        sorted_by_type[7].append((hand, bid))
        continue
    counts_max, counts_2_max = counts[0][1], counts[1][1]
    # Joker five of a kind
    if counts_max == 5:
        sorted_by_type[7].append((hand, bid))
        print("five of a kind!")
    elif counts_max == 4:
        print("Four of a kind")
        sorted_by_type[6].append((hand, bid))
    elif counts_max == 3 and counts_2_max == 2:
        print("Full house baby")
        sorted_by_type[5].append((hand, bid))
    elif counts_max == 3:
        print("three of akind")
        sorted_by_type[4].append((hand, bid))
    elif counts_max == 2 and counts_2_max == 2:
        print("2 PAIR")
        sorted_by_type[3].append((hand, bid))

    elif counts_max == 2:
        print("1 pair!")
        sorted_by_type[2].append((hand, bid))

    elif counts_max == 1 and counts_2_max == 1:
        print("High cared")
        sorted_by_type[1].append((hand, bid))
    else:
        print("WHAT IS HTIS")
    # input()


for hand_type, hands in sorted(sorted_by_type.items()):
    if len(hands) > 1:
        # print(hand_type, hands)
        hands.sort(key=cmp_to_key(sort_me2))
# print()
rank = 1
total = 0
for _, value in sorted(sorted_by_type.items()):
    for _, bid in value:
        # print(rank, bid)
        total += rank * bid
        rank += 1
print(total)

# 252222186
# too low
