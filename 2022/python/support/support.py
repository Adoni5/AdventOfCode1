"""Helper functions for AoC in python
"""

from typing import Any
import requests
import os
from itertools import islice, tee
from pprint import pprint, pformat
from collections import defaultdict

from dotenv import load_dotenv

load_dotenv()


def get_input(day: str, year: str = "2022", split: str = None) -> list[str] | str:
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
    ret = res.text.strip() if split is None else res.text.strip().split(split)
    return ret


def group_by_lines(n: int, input: list[Any]) -> list[Any]:
    """Group a list by n elements, returning each group as a list"""
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(input)
    while batch := list(islice(it, n)):
        yield batch


class Grid:
    def __init__(self):
        self.grid = None

    def read_grid(self, input: str | list[str]):
        """Read a grid from the given input into a {(x, y): value}

        Parameters
        ----------
        input: str or list
        """
        if isinstance(input, list):
            self.grid = {
                (x, y): v
                for i, line in enumerate(input)
                for x, y, v in zip([i] * len(line), range(len(line)), line)
            }
        elif isinstance(input, str):
            for i, line in enumerate(input.splitlines()):
                self.grid = {
                    (i, y): v
                    for x, y, v in zip([i] * len(line), range(len(line)), line)
                }

    def yield_neighbour_values(self, edges = False, fill_value = None, coords = False):
        """Iterate the grid and yield neighbours for each coordinate"""
        neighbours = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        if coords:
            for (x, y), v in iter(self.grid.items()):
                yield {(x, y): {(x + dx, y + dy): self.grid.get((x + dx, y + dy), fill_value) for dx, dy in neighbours}}
        else:
            for (x, y), v in iter(self.grid.items()):
                    yield {(x, y): [self.grid.get((x + dx, y + dy), fill_value) for dx, dy in neighbours]}

    def get_neighbours(self, coords: tuple[Any, Any]):
        """Get the neigbours for a provided value"""
        return self.grid.get(coord, None)

    def __getitem__(self, obj):
        return self.grid.get(obj, None)

    def __str__(self):
        return pformat(self.grid)


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
