test_input = """#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#"""
from support import get_input
from pathlib import Path

with open(Path(__file__).parent / "input.txt") as f:
    input = f.read().strip()
import math
from collections import deque

directions = "<>^v"
blizzards = tuple((set() for _ in directions))

for r_idx, line in enumerate(input.splitlines()[1:]):
    for c_idx, char in enumerate(line[1:]):
        if char in directions:
            blizzards[directions.index(char)].add((r_idx, c_idx))

# Implement a BFS to find the shortest path to the nearest blizzard


def bfs(
    start: tuple[int, int, int],
    blizzards: tuple[set[tuple[int, int]]],
    r_idx: int,
    c_idx: int,
    target: tuple[int, int],
) -> None:
    # time taken so far, x, y
    queue = deque([start])
    # Where we have been
    seen = set()

    # This is the fancy optimisation I never would have thought of - every n_rows by n_cols / greatest common divisor
    # steps, the blizzard will be in the same place. So we can just find the LCM of the two and NOT have to move the blizzards
    # at all!

    lcm = r_idx * c_idx // math.gcd(r_idx, c_idx)

    while queue:
        time, cr, cc = queue.popleft()
        time += 1
        # R, L, U, D, Not moving
        for dr, dc in ((0, 1), (0, -1), (-1, 0), (1, 0), (0, 0)):
            nr, nc = cr + dr, cc + dc
            if (nr, nc) == target:
                print(time)
                return
            #  Don't go off the edges
            if (nr < 0 or nr >= r_idx or nc < 0 or nc >= c_idx) and not (nr, nc) == (
                -1,
                0,
            ):
                continue
            fail = False
            # Check neighbouring positions are valid
            if (nr, nc) != (-1, 0):
                for i, tr, tc in ((0, 0, -1), (1, 0, 1), (2, -1, 0), (3, 1, 0)):
                    if (
                        (nr - tr * time) % r_idx,
                        (nc - tc * time) % c_idx,
                    ) in blizzards[i]:
                        fail = True
                        break
            if not fail:
                key = (nr, nc, time % lcm)

                if key in seen:
                    continue

                seen.add(key)
                queue.append((time, nr, nc))


bfs((0, -1, 0), blizzards, r_idx, c_idx, (r_idx, c_idx - 1))


# Part 2
def bfs2(
    start: tuple[int, int, int, int],
    blizzards: tuple[set[tuple[int, int]]],
    r_idx: int,
    c_idx: int,
    targets: list[tuple[int, int]],
) -> None:
    # time taken so far, x, y
    queue = deque([start])
    # Where we have been
    seen = set()

    # This is the fancy optimisation I never would have thought of - every n_rows by n_cols / greatest common divisor
    # steps, the blizzard will be in the same place. So we can just find the LCM of the two and NOT have to move the blizzards
    # at all!

    lcm = r_idx * c_idx // math.gcd(r_idx, c_idx)

    while queue:
        time, cr, cc, stage = queue.popleft()
        time += 1
        # R, L, U, D, Not moving
        for dr, dc in ((0, 1), (0, -1), (-1, 0), (1, 0), (0, 0)):
            nr, nc = cr + dr, cc + dc
            nstage = stage
            if (nr, nc) == targets[stage % 2]:
                if stage == 2:
                    print(time)
                    exit(0)
                nstage += 1
            #  Don't go off the edges
            if (nr < 0 or nr >= r_idx or nc < 0 or nc >= c_idx) and (
                nr,
                nc,
            ) not in targets:
                continue
            fail = False
            # Check neighbouring positions are valid
            if (nr, nc) not in targets:
                for i, tr, tc in ((0, 0, -1), (1, 0, 1), (2, -1, 0), (3, 1, 0)):
                    if (
                        (nr - tr * time) % r_idx,
                        (nc - tc * time) % c_idx,
                    ) in blizzards[i]:
                        fail = True
                        break
            if not fail:
                key = (nr, nc, nstage, time % lcm)

                if key in seen:
                    continue

                seen.add(key)
                queue.append((time, nr, nc, nstage))


bfs2((0, -1, 0, 0), blizzards, r_idx, c_idx, [(r_idx, c_idx - 1), (-1, 0)])
