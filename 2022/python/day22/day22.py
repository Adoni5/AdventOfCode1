test_input = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""


from math import inf
from itertools import zip_longest
from support import Grid, get_input
import re
from pprint import pprint, pformat

# test_input = get_input(22, strip=False)
grid, instructions = test_input.split("\n\n")
g = Grid.read_grid(grid, skip=" ")
# print(g.grid)

lookup = {"L": -90, "R": 90, "NA": 0}
lookup_direction = {90: (1, 0), 180: (0, 1), 270: (-1, 0), 0: (0, -1)}
direction = 90
final_dir = {0: 3, 90: 0, 180: 1, 270: 2}

pos = g.find_item(".")
# print(pos)
pat = re.compile(r"(\d+)")
pat2 = re.compile(r"([RL])")


for dist, turn in zip_longest(
    map(int, pat.findall(instructions)), pat2.findall(instructions), fillvalue="NA"
):
    # print(dist, turn)
    dx, dy = lookup_direction[direction]
    for _ in range(dist):
        x, y = pos
        nx, ny = (x + dx, y + dy)
        # print(nx, ny, dx, dy)
        minx, maxx = g.row_bounds(ny) if dx != 0 else (0, inf)
        # print(minx, maxx)
        miny, maxy = g.column_bounds(nx) if dy != 0 else (0, inf)
        # print(miny, maxy)
        # print(f"old nx, ny {nx}, {ny}")

        if minx > nx and dx != 0:
            nx = maxx
        elif nx > maxx and dx != 0:
            nx = minx
        elif miny > ny and dy != 0:
            ny = maxy
        elif maxy < ny and dy != 0:
            ny = miny

        # print(f"new nx, ny {nx}, {ny}")
        if g.grid[(nx, ny)] != "#":
            x = nx
            y = ny
        pos = (x, y)
        # print(f"pos {pos}")
    # factor = -1 if 360 > direction >= 180 else 1
    # print(factor)
    direction = (direction + (lookup[turn])) % 360
    # print(direction)

for x, y in g.grid.keys():
    x1, x2 = g.row_bounds(y)
    y1, y2 = g.column_bounds(x)


# Part 2 - starting again


class FaceRow:
    def __init__(self, row: list[str], col_start: int, row_start: int) -> None:
        self.row = row
        self.row_start = row_start
        self.col_start = col_start

    @property
    def get_coords(self):
        return (self.col_start, self.row_start)


class Face:
    def __init__(self, size: int) -> None:
        self.face = []
        self.size = 0
        self.x = None
        self.y = None

    def __repr__(self) -> str:
        return pformat(self.face)


lines = [line for line in grid.splitlines()]
face_start = re.compile(r"(\.|#{1})")


def extract_faces(map_data, n=4) -> list[Face]:
    # Determine the size of a face (n x n)
    faces = [Face(n), Face(n), Face(n), Face(n), Face(n), Face(n)]
    complete_faces = 0
    for line_index, line in enumerate(map_data):
        face_start_match = face_start.search(line)
        col_offset = face_start_match.end()
        line = line.strip()
        faces_in_row = len(line) // n
        for face_in_row in range(faces_in_row):
            print(f"face in row {line_index}: {face_in_row}")
            face_row = line[face_in_row * n : (face_in_row * n) + n]
            print(face_row)
            print(f"faces_index: {face_in_row + complete_faces}")
            face = faces[face_in_row + complete_faces]
            face.size = n
            if face.x is None:
                face.x = col_offset + face_in_row * n
                face.y = line_index
            faces[face_in_row + complete_faces].face.append(
                FaceRow(
                    list(face_row),
                    col_start=face_in_row + complete_faces + col_offset,
                    row_start=line_index + 1,
                )
            )
        # Increment completed face counter to get right face index out
        print(f" line index + 1 % 4) {(line_index+1) % n}")
        if not ((line_index + 1) % n) and line_index:
            print("increwmenting complete")
            complete_faces += faces_in_row
        print("\n")
    return faces


# Extract the front face (1)
# Using the test_input data
faces = extract_faces(lines)
pprint(faces)


def check_obstacle(position, face_row):
    """Are we moving into an obstacle"""
    if face_row.row[position[0]] == "#":
        return True


def move(position, direction, face, faces):
    x, y = position
    nx, ny = (0, 0)
    if direction == 0:  # Moving right
        nx, ny = (x + 1, y)
    elif direction == 1:  # Moving down
        nx, ny = (x, y + 1)
    elif direction == 2:  # Moving left
        nx, ny = (x - 1, y)
    elif direction == 3:  # Moving up
        nx, ny = (x, y - 1)
    if check_obstacle(position, faces[face].face[ny]):
        return position
    return (nx, ny)


def hitting_edge(position, direction, size) -> (bool, int):
    """Fallen off the edge of the world, return if we are falling off and the edge we are falling off of"""
    x, y = position
    if y == size - 1 and direction == 1:  # Bottom edge
        return True, 1
    elif x == size - 1 and direction == 0:  # Right edge
        return True, 2
    elif y == 0 and direction == 3:  # Top edge
        return True, 0
    elif x == 0 and direction == 2:  # Left edge
        return True, 3
    return False, None


layout = """
    0
1 2 3 4
    5
"""
#  90 degree directions
lookup_facing = {0: "R", 1: "D", 2: "L", 3: "U"}
lookup_direction = {v: k for k, v in lookup_facing.items()}

graph = {
    1: {"U": (2, 180), "D": (4, 0), "L": (3, -90), "R": (6, 180)},
    2: {"U": (1, 180), "D": (5, 180), "L": (6, 90), "R": (3, 0)},
    3: {"U": (1, 90), "D": (5, -90), "L": (2, 0), "R": (4, 0)},
    4: {"U": (1, 0), "D": (5, 0), "L": (3, 0), "R": (6, 90)},
    5: {"U": (5, 0), "D": (2, 180), "L": (3, 90), "R": (6, 0)},
    6: {"U": (4, -90), "D": (2, -90), "L": (5, 0), "R": (1, 180)},
}


def transition_to_adjacent_face(
    position: tuple[int, int],
    edge: int,
    face: int,
    size: int,
    graph: dict[int, dict[str, tuple[int, int]]],
) -> (int, tuple[int, int], int):
    """Transition to the adjacent face returning the new face, position and direction"""
    x, y = position
    new_face = graph[face][lookup_facing[edge]][0]
    return graph, (x, size - 1), 1


# # face, column, row
position = (0, faces[0].face[0].row.index("."))
facing = 0
face = 1
pat = re.compile(r"(\d+)")
pat2 = re.compile(r"([RL])")
face_size = faces[0].size


for dist, turn in zip_longest(
    map(int, pat.findall(instructions)), pat2.findall(instructions), fillvalue="NA"
):
    steps = dist
    for _ in range(steps):
        position = move(position, direction, face, faces)
        hit, edge = hitting_edge(position, direction, face_size)
        if hit:
            face, position, direction = transition_to_adjacent_face(
                position, edge, face, face_size, graph
            )
face = faces[face - 1]
print(position[0] + face.x, position[1] + face.y)
