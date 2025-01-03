test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

with open("input.txt") as fh:
    test_input = fh.read()


g = {}
for r, l in enumerate(test_input.splitlines()):
    for c, x in enumerate(l.strip()):
        g[(c, r)] = x

s_word = "XMAS"
xmas_count = 0
d = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))
for (c, r), ch in g.items():
    search = True
    word = ""
    # print(ch, c, r)
    if ch not in "X":
        continue
    word += ch
    _c, _r = c, r
    for dc, dr in d:
        word = "X"
        c, r = _c, _r
        while True:
            nc, nr = c + dc, r + dr
            nch = g.get((nc, nr))
            if nc is None:
                break
            if nch != s_word[len(word)]:
                break
            else:
                word += nch
                c, r = nc, nr
                if word == s_word:
                    xmas_count += 1
                    break

print(xmas_count)


xmas_count = 0
d = ((1, 1), (-1, -1), (-1, 1), (1, -1))
a = set(("SAM", "MAS"))
for (c, r), ch in g.items():
    # print(ch, c, r)
    if ch != "A":
        continue
    w1, w2 = None, None
    w1 = f"{g.get((c + 1, r +1))}A{g.get((c - 1, r -1))}"
    w2 = f"{g.get((c - 1, r + 1))}A{g.get((c + 1, r - 1))}"
    if w1 in a and w2 in a:
        xmas_count += 1

print(xmas_count)
