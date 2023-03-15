"""Helper functions for AoC in python
"""

from typing import Any
import requests
import os
from itertools import islice, tee
from pprint import pprint, pformat
from collections import defaultdict
from dotenv import load_dotenv
from heapq import heappop, heappush

from collections import deque

load_dotenv()



def sliding_window(iterable, n, skip = False):
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    """Yield a sliding window from an iterable. If skip - we skip a window to yield every other sliding window A
    sliding_window('ABCDEFG', 4) --> ABCD CDEF
    You have to call next at the end of the consuming for loop if skip is true """
    it = iter(iterable)
    window = deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)
    if skip:
        yield []


def get_input(day: str | int, year: str | int = "2022", split: str = None, strip: bool = True) -> list[str] | str:
    """Retreive puzzle input for the given year/day.

    Parameters
    ----------
    year: str
        The year for the puzzle in 4 digits. Ex. 2022
    day: str
        The day in smallest digits, i.e 1-31

    Returns
    ------
    Stripped puzzle input
    """

    # url  = request.Request(, headers={"session": os.getenv("SESSION")}, method="GET")
    res = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input",
        headers={
            "Cookie": f"session={os.getenv('SESSION')}",
            "User-Agent": "Rory Munro, https://github.com/Adoni5/AdventOfCode1"
            "by rory.munro@nottingham.ac.uk (Hi Eric)",
        },
    )
    ret = res.text.strip() if strip else res.text
    ret = ret if split is None else res.split(split)
    return ret


def group_by_lines(n: int, input: list[Any]) -> list[Any]:
    """Group a list by n elements, returning each group as a list"""
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(input)
    while batch := list(islice(it, n)):
        yield batch


class Grid:
    def __init__(self, grid=None):
        self.grid = grid
        self._ncols = None
        self._nrows = None

    @staticmethod
    def read_grid(s, func=lambda x: x, skip=None):
        """Read a grid from the given input into a {(x, y): value}

        Parameters
        ----------
        s: str or list
        """
        s = s.splitlines() if isinstance(s, str) else s
        return Grid(
            {
                (x, y): func(v)
                for i, line in enumerate(s)
                for x, y, v in zip(range(len(line)), [i] * len(line), line)
                if v != skip
            }
        )
    

    @property
    def ncols(self):
        if self._ncols is None:
            self._ncols = max(c for _, c in self.grid.keys()) + 1
        return self._ncols

    @property
    def nrows(self):
        if self._nrows is None:
            self._nrows = max(c for c, _ in self.grid.keys()) + 1
        return self._nrows

    @property
    def bounds(self):
        """Return bounding box
        (x_min, x_max, y_min, y)max)
        """
        return (0, self.nrows, 0, self.ncols)

    def column_bounds(self, col_idx):
        """Return the max and min column coordinate"""
        maxi = max(c for _, c in self.grid.keys() if _ == col_idx)
        mini = min(c for _, c in self.grid.keys() if _ == col_idx)
        return mini, maxi

    def row_bounds(self, row_idx):
        maxi = max(c for c, _ in self.grid.keys() if _ == row_idx)
        mini = min(c for c, _ in self.grid.keys() if _ == row_idx)
        return mini, maxi

    def yield_neighbour_values(self, enforce_edges = False, fill_value = None, coords = False, diagonal=False):
        """Iterate the grid and yield neighbours for each coordinate"""
        neighbours = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        if diagonal:
            neighbours = [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (-1, 0), (-1, -1), (0, -1)]
        if coords:
            for (x, y), v in iter(self.grid.items()):
                _d = {(x, y): {(x + dx, y + dy): self.grid.get((x + dx, y + dy), fill_value) for dx, dy in neighbours}}
                if enforce_edges:
                    __d = {_k: {__k: __v for __k, __v in _v.items() if not any((__k[0] < 0, __k[1]< 0, not bool(__v)))} for _k, _v in _d.items()}
                    yield __d
                else: 
                    yield _d
        else:
            for (x, y), v in iter(self.grid.items()):
                    yield {(x, y): [self.grid.get((x + dx, y + dy), fill_value) for dx, dy in neighbours]}

    def get_neighbours(self, coords: tuple[int, int], enforce_edges = False, return_coords = False, fill_value= None, diagonal=False):
        """Get the neigbours for a provided value"""
        neighbours = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        if diagonal:
            neighbours = [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (-1, 0), (-1, -1), (0, -1)]
        x, y = coords
        _d = {(x, y): {(x + dx, y + dy): self.grid.get((x + dx, y + dy), fill_value) for dx, dy in neighbours}}
        if enforce_edges:
            _d = {_k: {__k: __v for __k, __v in _v.items() if not any((__k[0] < 0, __k[1]< 0, not bool(__v)))} for _k, _v in _d.items()}
        return _d

    def find_item(self, item: str):
        """Return the coordinates of an item in the grid"""
        for k, v in self.grid.items():
            if v == item:
                return(k)

    def find_all_items(self, item_pattern: str) -> list[tuple[int, int]]:
        """Find coordinates for all item patterns"""
        ic = [k for k, v in self.grid.items() if v == item_pattern]
        return ic

    def __getitem__(self, obj, fill=None):
        return self.grid.get(obj, fill)

    def __str__(self):
        return pformat(self.grid)

    def walk(self, start: tuple[int, int], end: tuple[int, int], check_func=None, se_sub: tuple[str, str] = ("a", "z")) -> int:
        """Walk with djikstras algorithm from start coord to end, returning distance as n steps
        """
        heap = [(0, start)]
        seen = set()
        sub_start_end = {self[start]: se_sub[0], self[end]: se_sub[1]}
        while heap:
            dist, cur_pos = heappop(heap)
            cur_val = self[cur_pos] if self[cur_pos] != "S" else se_sub[0]
            if cur_pos == end:
                return dist

            if cur_pos in seen:
                continue
            seen.add(cur_pos)

            neighbours = self.get_neighbours(cur_pos, enforce_edges=True)
            for neighbour_xy, n in neighbours[cur_pos].items():
                if neighbour_xy in seen:
                    continue
                n = sub_start_end.get(n , n)
                if check_func(n, cur_val):
                    heappush(heap, (dist + 1, neighbour_xy))



if __name__ == "__main__":
    # print(get_input("1"))
    # print(list(group_by_lines(3, [1, 2, 3, 4])))
    test_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""
    # test_input = get_input("9", year="2021")
    grid = Grid()
    grid.read_grid(test_input.splitlines())
    risk = 0
    for n in grid.yield_neighbour_values(fill_value=0):
        for coord, neigbour_values in n.items():
            if int(grid[coord]) < min(map(int, filter(None, neigbour_values))):
                risk += 1 + int(grid[coord])
    seen = set()
    # P2
    basins = defaultdict(int)
    for n in grid.yield_neighbour_values(fill_value=9, coords=True):
        for k, ov in n.items():
            val = grid[k]
            for k_i, v in ov.items():
                if int(v) < int(val):
                    seen.add(k)
                    basins[k] += int(v)
    print(seen)                
            # left, up, right, down
