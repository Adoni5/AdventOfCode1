test_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

from collections import deque

with open("input.txt") as fh:
    test_input = fh.read()
g = {}
starts = deque([])
for r, line in enumerate(test_input.splitlines()):
    line = line.replace(".", "1")
    for c, h in enumerate(map(int, line)):
        if h == 0:
            starts.append((c, r))
        g[(c, r)] = h

d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
q = deque([])
s = 0
while starts:
    th = 0
    q = deque([starts.popleft()])
    visited = set()
    while q:
        c, r = q.popleft()
        visited = set()
        h = g[(c, r)]
        for dc, dr in d:
            nc, nr = c + dc, r + dr

            nh = g.get((nc, nr), -1)
            if nh == h + 1:
                if (nc, nr) not in visited:
                    visited.add((nc, nr))
                else:
                    continue
                # print(nh, f"{nc},{nr}")
                q.append((nc, nr))
                if nh == 9:
                    # print("hellooo")
                    th += 1
    # print(visited)
    print(th)
    s += th
print(s)
