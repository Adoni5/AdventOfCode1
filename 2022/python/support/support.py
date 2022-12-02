"""Helper functions for AoC in python
"""

from typing import List
import requests
import os

from dotenv import load_dotenv

load_dotenv()


def get_input(day: str, year: str = "2022", split: str=None) -> list[str] | str:
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
    print(os.getenv("SESSION"))    # print(request.urlopen(url).read())
    res = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', headers={"Cookie": f"session={os.getenv('SESSION')}"})
    ret = res.text.strip() if split is None else res.text.strip().split(split)
    return res.text.strip()

if __name__ == "__main__":
    print(get_input("1"))