from support import Grid, get_input

if __name__ == "__main__":
    input = get_input("12")
    test_input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

    grid = Grid.read_grid(input)

    start = grid.find_item("S")
    end = grid.find_item("E")
    print(start, end)
    print(grid.walk(start, end, check_func=lambda n, cv: ord(n) <= ord(cv) + 1))
    # p2
    p2_starts = grid.find_all_items("a")
    p2_starts.append(start)
    print(
        min(
            filter(
                None,
                (
                    grid.walk(
                        start, end, check_func=lambda n, cv: ord(n) <= ord(cv) + 1
                    )
                    for start in p2_starts
                ),
            )
        )
    )
