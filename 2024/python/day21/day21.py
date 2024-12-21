test_input = """029A
980A
179A
456A
379A"""
from pprint import pprint
from functools import cache
from collections import deque
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


@cache
def move_to_num(target, start, npad=True, depth=0):
    if d > 3:
        return []
    print(f"target is {target}")
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
                        print("".join(steps))
                    continue
        else:
            if x := d_buttons.get((c, r), None):
                if x == target:
                    low_s = min(low_s, s)
                    if s <= low_s:
                        _start = (c, r)
                        routes.append(f"{"".join(steps)}A")
                        print("".join(steps))
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


# We need the optimal routes on the numpad to each place from A as we go back to A each time ( I think)
for line in test_input.splitlines():
    print(line)

    for t in line:
        routes, START = move_to_num(t, START)

        print(routes)

    print(line)
    break
