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
from typing import Any


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
        else:
            raise RuntimeError("ahhh")

    def resting_on(self, other_brick) -> bool:
        """Is this brick resting on another brick in some dimension"""
        nbrick_z0, nbrick_z1 = self.z0 - 1, self.z1 - 1
        if other_brick.z0 == nbrick_z0 or other_brick.z1 == nbrick_z1:
            for x in range(*other_brick.rev_orientation(other_brick.orientation())):
                print(x)

    def move_down(self):
        self.z0 -= 1
        self.z1 -= 1

    def __repr__(self):
        return f"Brick(name={self.name}, x={self.x}, y={self.y}, z={self.z})"

    @property
    def coords(self):
        return (self.x, self.y, self.z)


bricks = []
final_pos = {}

n = iter(ascii_uppercase)
pat = re.compile(r"(\d)+")
for line in test_input.splitlines():
    brick = Brick(*list(map(int, pat.findall(line))), next(n))

    print(brick.name, brick.size(), brick.orientation())
    if brick.z0 == 1 or brick.z1 == 1:
        final_pos[brick.coords] = brick
    bricks.append(brick)

print(final_pos)

for brick in bricks:
    while brick.coords not in final_pos:
        print(f"moving down brick {brick.name}")
        brick.move_down()
        for resting_brick in final_pos.values():
            brick.resting_on(resting_brick)
