from collections import defaultdict, deque
from pprint import pprint
test_input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

# Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi 

from support import Grid, get_input
test_input = get_input("12")


grid = Grid()
grid.read_grid(test_input)
visited = set()

def djik():
    """fuuuuu"""
    pass

cur_pos = grid.find_item("S")
neighbourinos = grid.get_neighbours(cur_pos, enforce_edges=True)
check_me = deque()
stop = False

for new_pos, neighbours in neighbourinos.items():
    cur_val = grid[cur_pos] if grid[cur_pos] != "S" else "a"
    # Don't come back here
    visited.add(cur_pos)
    # path[cur_pos] += 1
    # Lets check all the neighbours
    for neighbour_xy, n in neighbours.items():
        if ord(n) <= ord(cur_val) + 1:

            check_me.append((1, neighbour_xy))
path_lens = []
# print(visited)
# print(check_me)
while check_me and not stop:
    # print(check_me)
    dst , cur_pos = check_me.popleft()
    # print(cur_pos)
    cur_val = grid[cur_pos] if grid[cur_pos] != "S" else "a"
    # print(cur_pos, cur_val)
    # print(cur_val)
    # print(cur_val)
    # print(ord(cur_val))
    # Don't come back here
    if cur_pos not in visited:
        visited.add(cur_pos)

        neighbours = grid.get_neighbours(cur_pos, enforce_edges=True)
        # Lets check all the neighbours
        for neighbour_xy, n in neighbours[cur_pos].items():
            # print(visited)
            # print(neighbour_xy in visited)
            # if neighbour_xy in visited:
            #     continue
                
            if ord(n) <= ord(cur_val) + 1:

                check_me.append((dst+1, neighbour_xy))
            if n == "E" and ord("z") <= ord(cur_val) + 1:
                print("readched eS")
                path_lens.append(dst + 1)
                stop = True
            # visited = defaultdict(int)


# print(visited)

print(min(path_lens))

# P2
all_as = grid.find_all_items("a")
all_as.append(grid.find_item("S"))
print(all_as)
visited = set()

def djik():
    """fuuuuu"""
    pass

path_lens = []

for a_coord in all_as:
    print(a_coord)
    cur_pos = a_coord
    neighbourinos = grid.get_neighbours(cur_pos, enforce_edges=True)
    check_me = deque()
    stop = False
    visited = set()

    for new_pos, neighbours in neighbourinos.items():
        cur_val = grid[cur_pos] if grid[cur_pos] != "S" else "a"
        # Don't come back here
        visited.add(cur_pos)
        # path[cur_pos] += 1
        # Lets check all the neighbours
        for neighbour_xy, n in neighbours.items():
            if ord(n) <= ord(cur_val) + 1:

                check_me.append((1, neighbour_xy))
    # print(visited)
    # print(check_me)
    while check_me and not stop:
        # print(check_me)
        dst , cur_pos = check_me.popleft()
        # print(cur_pos)
        cur_val = grid[cur_pos] if grid[cur_pos] != "S" else "a"
        # print(cur_pos, cur_val)
        # print(cur_val)
        # print(cur_val)
        # print(ord(cur_val))
        # Don't come back here
        if cur_pos not in visited:
            visited.add(cur_pos)

            neighbours = grid.get_neighbours(cur_pos, enforce_edges=True)
            # Lets check all the neighbours
            for neighbour_xy, n in neighbours[cur_pos].items():
                # print(visited)
                # print(neighbour_xy in visited)
                # if neighbour_xy in visited:
                #     continue
                    
                if ord(n) <= ord(cur_val) + 1:

                    check_me.append((dst+1, neighbour_xy))
                if n == "E" and ord("z") <= ord(cur_val) + 1:
                    print("readched eS")
                    path_lens.append(dst + 1)
                    stop = True

print(min(path_lens))