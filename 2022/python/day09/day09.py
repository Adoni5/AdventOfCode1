from operator import sub, add
from support import get_input

test_input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

big_test_input = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

# A cool diferent solution using iterators


visited_p1 = set()
visited_p2 = set()
knots = [[0, 0] for _ in range(10)]
for line in get_input("9", split="\n"):
    direction, distance = line.split()
    if direction == "R":
        index, op = 0, add
    elif direction == "L":
        index, op = 0, sub
    elif direction == "U":
        index, op = 1, add
    else:
        index, op = 1, sub
    
    for i in range(int(distance)):
        head = knots[0]
        head[index] = op(head[index], 1)
        # loop all subsequent knots and move them 
        for i, knot in enumerate(knots[1:]):
            tail = knots[1:][i]
            tail_x, tail_y = tail
            head_x, head_y = head
            dx = head_x - tail_x
            dy = head_y - tail_y
            if abs(dx) > 1 and not abs(dy):
                tail[0] += int(dx / abs(dx))
            if abs(dy) > 1 and not abs(dx):
                tail[1] += int(dy / abs(dy))
            if abs(dx) > 1 and abs(dy):
                tail[0] += int(dx / abs(dx))
                tail[1] += int(dy / abs(dy))
            elif abs(dy) > 1 and abs(dx):
                tail[1] += int(dy / abs(dy))
                tail[0] += int(dx / abs(dx))
            head = knot
        visited_p1.add(tuple(knots[1]))
        visited_p2.add(tuple(knots[-1]))

print(f"Part 1: {len(visited_p1)}")
print(f"Part 2: {len(visited_p2)}")