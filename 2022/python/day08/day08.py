from collections import defaultdict
from support import get_input


test_input = """30373
25512
65332
33549
35390"""

def make_rows_and_cols(input: str) -> tuple[dict[str, dict[str: str]], dict[str, list]]:
    """Take a grid and return a dict of rows, keyed to row index and columns, keyed to column index"""
    rows = {i: {j: val for j, val in enumerate(line, start=1)} for i, line in enumerate(input.splitlines(), start=1)}
    # create a columns dict as my smooth brain can't process how to do row and col in the same dict
    cols = defaultdict(list)
    for row, vals in rows.items():
        for col, cvals in vals.items():
            cols[col].append(cvals)
    return rows, cols

def edges(data: dict[str, dict[str: str]]) -> int:
    """All edges are visible so just start count all the edge trees and return"""
    count = 0
    # top and bottom
    count += len(data[1]) * 2
    # edges of middle rows
    for _ in range(2, len(data)):
        count += 2
    return count

def how_far_vis(tree_height: int, neighbours: list[int]) -> int:
    """How far can you see from a tree before you hit an edge or a tree with >= height"""
    dist = 0
    for neighbour in neighbours:
        if neighbour >= tree_height:
            dist+=1
            return dist
        else:
            dist += 1
    return dist


def visible_row(row, cols, row_num, count, p2=False):
    """Solve part one and two"""
    row_values = list(row.values())
    for i in range(1, len(row)-1):
        tree_height = row_values[i]
        left = row_values[:i]
        right = row_values[i+1:]
        # add one to col index as it is a list not a dict, so 0 based index not lookup
        up = cols[i+1][:row_num-1]
        down = cols[i+1][row_num:]
        if not p2:
            vis_to_the_left, vis_to_the_right = all((tree_height > neighbour for neighbour in left)), all((tree_height > neighbour for neighbour in right))
            vis_to_the_up, vis_to_the_down = all((tree_height > neighbour for neighbour in up)), all((tree_height > neighbour for neighbour in down))
            if any((vis_to_the_left, vis_to_the_right, vis_to_the_down, vis_to_the_up)):
                count += 1
        else:
            dist_vis_left, dist_vis_right = how_far_vis(tree_height, left[::-1]), how_far_vis(tree_height, right)
            dist_vis_up, dist_vis_down = how_far_vis(tree_height, up[::-1]), how_far_vis(tree_height, down)
            scenic_score = dist_vis_left * dist_vis_right * dist_vis_up * dist_vis_down
            if scenic_score > count:
                count = scenic_score
    return count

if __name__ == "__main__":
    test_rows, test_cols = make_rows_and_cols(test_input)
    test_visible_num = edges(test_rows)
    test_best_scenic_score = 0
    # test
    # go through each centra edgea and check max in each direction, assumes grid is X by X and not X by Y
    for i in range(2, len(test_rows)):
        test_visible_num = visible_row(test_rows[i], test_cols , i, test_visible_num)
        test_best_scenic_score =  visible_row(test_rows[i], test_cols , i, test_best_scenic_score, p2=True)
    print("TEST")
    print(f"\tP1 {test_visible_num}")
    print(f"\tP2 {test_best_scenic_score}")

    # Actual
    input = get_input("8")
    rows, cols = make_rows_and_cols(input)
    visible_num = edges(rows)
    best_scenic_score = 0
    # test
    # go through each centra edgea and check max in each direction, assumes grid is X by X and not X by Y
    for i in range(2, len(rows)):
        visible_num = visible_row(rows[i], cols , i, visible_num)
        best_scenic_score =  visible_row(rows[i], cols , i, best_scenic_score, p2=True)
    print("ACTUAL")
    print(f"\tP1 {visible_num}")
    print(f"\tP2 {best_scenic_score}")
    
        
    # print(visible_num)        
    # print(best_scenic_score)

        