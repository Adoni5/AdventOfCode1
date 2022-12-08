from collections import defaultdict
from support import get_input


test_input = """30373
25512
65332
33549
35390"""
test_input = get_input("8")

rows = {i: {j: val for j, val in enumerate(line, start=1)} for i, line in enumerate(test_input.splitlines(), start=1)}
# cols = {i: {i: val for j, val in enumerate(line, start=1)} for i, line in enumerate(test_input.splitlines(), start=1)}
cols = defaultdict(list)
for row, vals in rows.items():
    for col, cvals in vals.items():
        cols[col].append(cvals)


print(rows)

def edges(data):
    count = 0
    count += len(data[1])
    count += len(data[len(data)])
    for i in range(2, len(data)):
        count += 2
    return count

def how_far_vis(tree_height, neighbours):
    # print(neighbours)
    dist = 0
    for neighbour in neighbours:
        # print(f"neigbour {neighbour}")
        if neighbour >= tree_height:
            dist+=1
            # print(dist)
            return dist
        else:
            dist += 1
            # print(dist)
    return dist


def visible_row(row, cols, row_num, count, p2=False):
    #check left and right on row
    row_values = list(row.values())
    max_val_indx = (None, None)
    for i in range(1, len(row)-1):
        tree_height = row_values[i]
        left = row_values[:i]
        # print(left)
        right = row_values[i+1:]
        # print(right)
        # add one as it is a list not a dict, so 0 based index not lookup
        up = cols[i+1][:row_num-1]
        down = cols[i+1][row_num:]

        if not p2:
            vis_to_the_left, vis_to_the_right = all((tree_height > neighbour for neighbour in left)), all((tree_height > neighbour for neighbour in right))
            vis_to_the_up, vis_to_the_down = all((tree_height > neighbour for neighbour in up)), all((tree_height > neighbour for neighbour in down))
            # print(row_values)
            # print(f"tree {i} with height {tree_height}")
            # print(vis_to_the_left)
            # print(vis_to_the_right)
            if any((vis_to_the_left, vis_to_the_right, vis_to_the_down, vis_to_the_up)):
                # print("adding 1")
                count += 1
        else:
            # print(tree_height)

            dist_vis_left, dist_vis_right = how_far_vis(tree_height, left[::-1]), how_far_vis(tree_height, right)
            dist_vis_up, dist_vis_down = how_far_vis(tree_height, up[::-1]), how_far_vis(tree_height, down)
            # dist_vis_up, dist_vis_down = 0,0
            print(dist_vis_up, dist_vis_left, dist_vis_right, dist_vis_down)
            scenic_score = dist_vis_left * dist_vis_right * dist_vis_up * dist_vis_down
            if scenic_score > count:
                count = scenic_score
        
    # print(count)
    return count

    

if __name__ == "__main__":
    visible_num = edges(rows)
    best_scenic_score = 0
    # print(cols)
    # go through each centra edgea and check max in each direction, assumes grid is X by X and not X by Y
    for i in range(2, len(rows)):
        # visible_num = visible_row(rows[i], cols , i, visible_num)
        best_scenic_score =  visible_row(rows[i], cols , i, best_scenic_score, p2=True)
    print(best_scenic_score)
        
    # print(visible_num)        
    # print(best_scenic_score)

        