test_input = """A Y
B X
C Z"""

scores = {"X": 1, "Y": 2, "Z": 3}
scores_p2 =  {"X": 0, "Y": 3, "Z": 6}

outcomes = {"A": {"X": 3, "Y": 6, "Z": 0}, "B": {"X": 0, "Y": 3, "Z": 6}, "C": {"X": 6, "Y": 0, "Z": 3}}
outcomes_p2 = {"A": {3: "X", 6: "Y", 0: "Z"}, "B": {0: "X", 3: "Y", 6: "Z"}, "C": {6: "X", 0: "Y", 3: "Z"}}


def cheating(input: str) -> int:
    return sum(scores[Y]+outcomes[O][Y] for O, Y in map(str.split, input.split("\n")))

def cheating_p2(input: str) -> int:
    return sum(scores_p2[Y]+scores[outcomes_p2[O][scores_p2[Y]]] for O, Y in map(str.split, input.split("\n")))

print(cheating(test_input))
with open("day02.txt") as fh:
    print(cheating(fh.read().strip()))
    

# Part 2 
# X is now we need to win, 
# Y is now we need to draw 
# and Z is now we need to lose

print(cheating_p2(test_input))
with open("day02.txt") as fh:
    print(cheating_p2(fh.read().strip()))