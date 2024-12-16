test_input = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""


from collections import deque
from pprint import pprint

# with open("input.txt") as fh:
#     test_input = fh.read()
g = {}
q = deque([])
for r, line in enumerate(test_input.splitlines()):
    for c, x in enumerate(line.strip()):
        if x == "S":
            q.append((c, r, 0, set(), (-1, 0), 0, 0, []))
            x = "."
        g[(c, r)] = x

_rot_clock = {(-1, 0): (0, -1), (0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0)}
_rot_anti = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}
fin = []
visited = set()
while q:
    # print([(c, r, s, d) for c, r, s, _, d in q])
    c, r, score, v, d, st, rot, path = q.popleft()
    path = list(path)

    # rotate
    _d_cl = _rot_clock[d]
    _d_an = _rot_anti[d]
    for _d, ro in ((_d_cl, 1), (_d_an, 1), (d, 0)):
        dc, dr = _d
        nc, nr = c + dc, r + dr
        nn = g.get((nc, nr))
        nrot = rot
        rscore = score
        if (nc, nr) in v:
            # print(f"visited {nc},{nr},{d} from {c},{r}")
            continue
        v.add((nc, nr))
        if ro:
            nrot = rot + 1
            rscore = score + 1000
        if nn == ".":
            st += 1
            rscore += 1
            path.append((nc, nr, _d, st, nrot))
            if not ro:
                q.appendleft((nc, nr, rscore, v, _d, st, nrot, path))
            else:
                q.append((nc, nr, rscore, v, _d, st, nrot, path))

        elif nn == "E":
            fin.append((rscore + 1, st, rot, path))


def draw(g: dict, path: tuple[int, int]):
    x = {(0, -1): "^", (0, 1): "v", (1, 0): ">", (-1, 0): "<"}
    lines = []
    _r = 0
    line = []
    paths = {(c, r): d for c, r, d, *_ in path}

    for (c, r), v in g.items():
        if r != _r:
            lines.append("".join(line))
            line = []
            _r = r
        if _x := paths.get((c, r), False):
            v = x[_x]
        line.append(v)
    lines.append("".join(line))
    print("\n".join(lines))
    print("\n\n")


print(min(fin, key=lambda x: x[0])[0:3])
print(len(fin))
draw(g, min(fin, key=lambda x: x[0])[-1])
