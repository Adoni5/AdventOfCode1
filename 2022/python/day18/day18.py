test_input = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""
test_input_1 = """1,1,1
1,1,2"""
from pprint import pprint
from support import get_input
from collections import deque

input = {(x, y, z): 1 for x,y,z in map(lambda x: map(int, x.split(",")), get_input("18").splitlines())}
# input = {(x, y, z): 1 for x,y,z in map(lambda x: map(int, x.split(",")), test_input.splitlines())}

# pprint(input)
neighbours_d = [(1, 0, 0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
total = 0
for (x,y,z), _ in input.items():
    clear_sides = 6
    for dx, dy, dz in neighbours_d:
        if (x+dx, y+dy, z+dz) in input:
            clear_sides -= 1
    total += clear_sides

# starting point of search
minx, maxx = min(x for x, _, _ in input) - 1, max(x for x, _, _ in input) + 1
miny, maxy = min(y for _, y, _ in input) - 1,  max(y for _, y, _ in input) + 1
minz, maxz = min(z for _, _, z in input) - 1,max(z for _, _, z in input) + 1

print(total)
stop = False
visited = set()
check_me = deque([(minx, miny, minz)])
print(check_me)
count = 0
# move the steam around
while check_me and not stop:
    # print(check_me)
    x, y, z  = check_me.popleft()
    cur_pos = (x, y, z )

    if cur_pos not in visited:
        visited.add(cur_pos)

        neighbours = [(x+dx, y+dy, z+dz) for dx, dy, dz in neighbours_d]
        # Lets check all the neighbours
        print(neighbours)

        for neighbour in neighbours:
            print(neighbour)
            x, y, z = neighbour
            if neighbour in input:
                # On the outside
                count += 1
            elif (x, y, z) not in visited and all(
                (
                    minx <= x <= maxx,
                    miny <= y <= maxy,
                    minz <= z <= maxz,
                )
            ):
                check_me.append(neighbour)
            # visited = defaultdict(int)


# for k, v in enclosed.items():
#     if k not in input and v >= 5:
#         print(k)
#         total -= v
# pprint(enclosed)
print(count)
    