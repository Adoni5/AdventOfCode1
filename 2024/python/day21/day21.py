test_input = """029A
980A
179A
456A
379A"""
from pprint import pprint
from functools import cache
import heapq

d_buttons = " ^A,<v>"
d_buttons = {
    (c, r): char
    for (r, l) in enumerate(d_buttons.split(","))
    for (c, char) in enumerate(l)
    if char != " "
}
pprint(d_buttons)
num_pad = "789,456,123, 0A"
num_pad = {
    (c, r): char
    for (r, l) in enumerate(num_pad.split(","))
    for (c, char) in enumerate(l)
    if char != " "
}
pprint(num_pad)
ds = {(0, -1): "^", (1, 0): ">", (-1, 0): "<", (0, 1): "v"}
PRESS = "A"
START = (2, 3)
# with open("input.txt") as fh:
#     test_input = fh.read()


@cache
def move_to_num(target, start, npad=True):
    q = [(0, *start, list(), (0, 0), set())]
    # visited = set()
    routes = []
    _start = None
    low_s = float("inf")
    while q:
        s, c, r, steps, d, visited = heapq.heappop(q)
        if (c, r) in visited:
            continue
        visited.add((c, r))
        if npad:
            if x := num_pad.get((c, r), None):
                if x == target:
                    low_s = min(low_s, s)
                    if s <= low_s:
                        _start = (c, r)
                        routes.append(f"{"".join(steps)}A")
                        # print("".join(steps))
                    continue
        else:
            if x := d_buttons.get((c, r), None):
                if x == target:
                    low_s = min(low_s, s)
                    if s <= low_s:
                        _start = (c, r)
                        routes.append(f"{"".join(steps)}A")
                        # print("".join(steps))
                    continue
                    # return "".join(steps), (c, r)
        for d in ds:
            a = list(steps)
            dc, dr = d
            nc, nr = c + dc, r + dr
            if npad:
                if x := num_pad.get((nc, nr), None):
                    a.append(ds[(dc, dr)])
                    heapq.heappush(q, (s + 1, nc, nr, a, d, set(visited)))
            else:
                if x := d_buttons.get((nc, nr), None):
                    a.append(ds[(dc, dr)])
                    heapq.heappush(q, (s + 1, nc, nr, a, d, set(visited)))
    return routes, _start


@cache
def recurse_move(targets, start, npad=True):
    if not targets:
        return [[]]  # Base case: return an empty path to concatenate later
    # print(f"targets are {targets}, npad is {npad}, depth is {depth}")
    target = targets[0]
    # Get all shortest paths and the next starting point(s)
    routes, _ = move_to_num(target, start, npad)

    all_paths = []
    for route in routes:
        # Extract the endpoint of the current route to use as the start for the next recursion
        # Define how to calculate this
        # Recursively find paths for the remaining targets
        sub_paths = recurse_move(targets[1:], _, npad)

        # Combine the current route with each sub-path
        for sub_path in sub_paths:
            all_paths.append([route] + sub_path)

    return sorted(all_paths)[:1000]


# We need the optimal routes on the numpad to each place from A as we go back to A each time ( I think)
p1 = 0
for line in test_input.splitlines():

    paths = recurse_move(line, START)

    for _ in range(2):
        print(_)
        _help = []
        for path in paths:
            path = "".join(path)
            _help.extend(recurse_move(path, (2, 0), False))
        paths = _help
    p1 += int(line[:3]) * min(len("".join(path)) for path in paths)
print(p1)
