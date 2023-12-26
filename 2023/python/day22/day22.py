test_input = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""
import re
from string import ascii_uppercase
from operator import sub
import sys


from support import get_input

test_input = get_input(22, 2023)


class Brick:
    def __init__(self, x0, y0, z0, x1, y1, z1, name) -> None:
        self.name = name
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1

    def size(self) -> int:
        return (
            sum(
                (abs(self.x0 - self.x1), abs(self.y0 - self.y1), abs(self.z0 - self.z1))
            )
            + 1
        )

    def orientation(self) -> int:
        if sub(*self.x):
            return 0
        elif sub(*self.y):
            return 1
        elif sub(*self.z):
            return 2
        else:
            # Single cube, 1 in all orientations
            return -1

    @property
    def x(self) -> tuple[int, int]:
        return (self.x0, self.x1)

    @property
    def y(self) -> tuple[int, int]:
        return (self.y0, self.y1)

    @property
    def z(self) -> tuple[int, int]:
        return (self.z0, self.z1)

    def rev_orientation(self, __name: int):
        print(__name)
        if __name == 0:
            return self.x
        if __name == 1:
            return self.y
        if __name == 2:
            return self.z
        return self.x

    def blockupied(self, dz=0):
        orientation = self.orientation()
        range_occ = self.rev_orientation(self.orientation())
        range_occ = range_occ[0], range_occ[1] + 1
        if orientation == 0:
            return {(x, self.y0, self.z0 - dz) for x in range(*range_occ)}
        if orientation == 1:
            return {(self.x0, y, self.z0 - dz) for y in range(*range_occ)}
        if orientation == 2:
            return {
                (self.x0, self.y0, z - dz)
                for z in range(range_occ[0] - dz, range_occ[1] - dz)
            }
        return {(x, self.y0, self.z0 - dz) for x in range(*range_occ)}

    def resting_on(self, other_brick, and_floor=True) -> bool:
        """Is this brick resting on another brick in some dimension, or the floor"""
        print(self.name, self.coords)
        print(f"other {other_brick.name}, {other_brick.coords}")
        nbrick_z0, nbrick_z1 = self.z0 - 1, self.z1 - 1
        blocks_occupied = self.blockupied(dz=1)
        print(nbrick_z0 == 0, and_floor)
        # print(other_brick.blockupied().intersection(blocks_occupied))
        print(f"other brick {other_brick.name} occupies {other_brick.blockupied()}")
        print(other_brick.blockupied().intersection(blocks_occupied))
        print(f"{brick.name} occupies {blocks_occupied} if moved down")
        if self.name == "brick 2" and (nbrick_z0 == 0 and and_floor):
            sys.exit()
        return (
            (other_brick.z0 == nbrick_z0 or other_brick.z1 == nbrick_z1)
            and other_brick.blockupied().intersection(blocks_occupied)
        ) or (nbrick_z0 == 0 and and_floor)

    def move_down(self):
        self.z0 -= 1
        self.z1 -= 1

    def temp_move_down(self):
        return self.z0 - 1, self.z1 - 1

    def __repr__(self):
        return f"Brick(name={self.name}, x={self.x}, y={self.y}, z={self.z})"

    @property
    def coords(self):
        return (self.x, self.y, self.z)


bricks = []
final_pos = {}

n = iter(ascii_uppercase)
pat = re.compile(r"(\d)+")
for i, line in enumerate(test_input.splitlines()):
    brick = Brick(*list(map(int, pat.findall(line))), f"brick {i}")

    print(brick.name, brick.size(), brick.orientation())
    if brick.z0 == 1 or brick.z1 == 1:
        final_pos[brick.coords] = brick
    bricks.append(brick)

# print(final_pos)
resting = set(final_pos.keys())
a = list(final_pos.values())

for brick in bricks:
    while brick.coords not in resting:
        print(f"moving down brick {brick}")
        for resting_brick in a:
            if brick.resting_on(resting_brick):
                print(f"{brick.name} is resting at {brick.coords}")
                final_pos[brick.coords] = brick
                a.append(brick)
                resting.add(brick.coords)
                print(resting)
                break
        else:
            print("moving brick donw")
            brick.move_down()
            break
        print()


sys.exit(0)
total = set()
all_leant_on = set()
for v in final_pos.values():
    count = 0
    v2s = []
    for v2 in final_pos.values():
        if v.name == v2.name:
            continue
        if v.resting_on(v2, and_floor=False):
            print(f"{v.name} on {v2.name}")
            # total += 1
            v2s.append(v2.name)
            all_leant_on.add(v2.name)
        if len(v2s) > 1:
            total.update(set(v2s))
for v in final_pos.values():
    if v.name not in all_leant_on:
        print(v.name)
        total.add(v.name)
print(len(total))
# print(final_pos)
