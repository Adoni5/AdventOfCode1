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
#......
#......
#......
#......
#H.....
# test_input = get_input("9")

visited = set()
#p1
# head, tail = [0, 0], [0, 0]
# print(visited)
# for line in test_input.splitlines():
#     direction, distance = line.split()
#     if direction == "R":
#         index, op = 0, add
#     elif direction == "L":
#         index, op = 0, sub
#     elif direction == "U":
#         index, op = 1, add
#     else:
#         index, op = 1, sub
#     for i in range(int(distance)):
#         head[index] = op(head[index], 1)
#         tail_x, tail_y = tail
#         head_x, head_y = head
#         print(f"dx {head_x - tail_x}")
#         print(f"dy {head_y - tail_y}")
#         dx = head_x - tail_x
#         dy = head_y - tail_y

#         if abs(dx) > 1 and not abs(dy):
#             tail[0] += int(dx / abs(dx))
#         if abs(dy) > 1 and not abs(dx):
#             tail[1] += int(dy / abs(dy))
#         if abs(dx) > 1 and abs(dy):
#             tail[0] += int(dx / abs(dx))
#             tail[1] += int(dy / abs(dy))
#         if abs(dy) > 1 and abs(dx):
#             tail[1] += int(dy / abs(dy))
#             tail[0] += int(dx / abs(dx))
#         visited.add(tuple(tail))

#         print(head, tail)
# print(len(visited))
# print(visited)
# p2
knots = [[0, 0] for _ in range(10)]
print(knots)
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
        print(f"\nmovig {direction} 1")
        head = knots[0]

        head[index] = op(head[index], 1)
        for i, knot in enumerate(knots[1:]):
            tail = knots[1:][i]
            print(head, tail)
            tail_x, tail_y = tail
            head_x, head_y = head
            print(f"dx {head_x - tail_x}")
            print(f"dy {head_y - tail_y}")
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

            print(head, tail)
            head = knot
        
        visited.add(tuple(knots[-1]))

    
print(knots)

print(visited)
print(len(visited))