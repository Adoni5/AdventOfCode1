from collections import deque


test_input = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

with open("input.txt") as fh:
    test_input = fh.read()

maze, inst = test_input.split("\n\n")
inst = inst.replace("\n", "")

d = {"<": (-1, 0), "^": (0, -1), ">": (1, 0), "v": (0, 1)}

g = {}
pos = None
for r, l in enumerate(maze.splitlines()):
    for c, n in enumerate(l):
        if n == "@":
            pos = (c, r)
            n = "."
        g[(c, r)] = n


def draw(g: dict, pos: tuple[int, int]):
    lines = []
    _r = 0
    line = []
    for (c, r), v in g.items():
        if (c, r) == pos:
            v = "@"
        if r != _r:
            lines.append("".join(line))
            line = []
            _r = r
        line.append(v)
    lines.append("".join(line))
    print("\n".join(lines))
    print("\n\n")


for di in inst:
    c, r = pos
    dc, dr = d[di]
    nc, nr = c + dc, r + dr
    nn = g[(nc, nr)]
    if nn == ".":
        pos = (nc, nr)
    elif nn == "#":
        pass
    elif nn == "O":
        rocks = [(nc, nr)]
        _c, _r = nc, nr
        while True:
            _nc, _nr = _c + dc, _r + dr
            if g[(_nc, _nr)] == "#":
                break
            elif g[(_nc, _nr)] == "O":
                rocks.append((_nc, _nr))
                # print(f"appended {_nc},{_nr} to rocks: {rocks}")
            elif g[(_nc, _nr)] == ".":
                pos = rocks[0]
                g[rocks[0]] = "."
                for rock in rocks:
                    # print(rock)
                    g[(rock[0] + dc, rock[1] + dr)] = "O"
                break
            else:
                # print("AHHHH")
                break
            _c, _r = _nc, _nr
    # print(f"instruction {di}")
    # draw(g, pos)

# print(sum((c + r * 100) for (c, r), v in g.items() if v == "O"))

# P2
# widen
g = {}
pos = None
ch = {".": "..", "#": "##", "O": "[]", "@": ".."}
for r, l in enumerate(maze.splitlines()):
    for c, n in enumerate(l):
        if n == "@":
            pos = (c * 2, r)
        chs = ch[n]
        for _ in range(2):
            g[(c * 2 + _, r)] = chs[_]


draw(g, pos)

boxy_lady = {"[", "]"}
for di in inst:
    c, r = pos
    dc, dr = d[di]
    nc, nr = c + dc, r + dr
    nn = g[(nc, nr)]
    if nn == ".":
        pos = (nc, nr)
    elif nn == "#":
        pass
    elif nn in boxy_lady:
        if nn == "[":
            rocks = [(nc, nr, "["), (nc + 1, nr, "]")]
        elif nn == "]":
            rocks = [(nc, nr, "]"), (nc - 1, nr, "[")]
        q = deque(rocks)
        v = set()
        while q:
            _c, _r, _ = q.popleft()
            _nc, _nr = _c + dc, _r + dr
            _nn = g[(_nc, _nr)]
            if _nn in boxy_lady:
                if dr == 0:
                    q.append((_nc, _nr, _nn))
                    if (_nc, _nr, _nn) not in rocks:
                        rocks.append((_nc, _nr, _nn))
                else:
                    if _nn == "[":
                        q.extend([(_nc, _nr, "["), (_nc + 1, _nr, "]")])
                        rocks.extend([(_nc, _nr, "["), (_nc + 1, _nr, "]")])
                    elif _nn == "]":
                        q.extend([(_nc, _nr, "]"), (_nc - 1, _nr, "[")])
                        rocks.extend([(_nc, _nr, "]"), (_nc - 1, _nr, "[")])
            elif _nn == "#":
                rocks = []
                break
        if rocks:
            for rock in rocks:
                g[rock[:2]] = "."
            pos = (nc, nr)
            for rock in rocks:
                g[(rock[0] + dc, rock[1] + dr)] = rock[2]

        print(f"instruction {di}")
        draw(g, pos)

print(sum((c + r * 100) for (c, r), v in g.items() if v == "["))
