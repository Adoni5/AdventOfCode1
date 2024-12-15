test_input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

import re

with open("input.txt") as fh:
    test_input = fh.read()


import numpy as np


def presses(x_target, y_target, a_x, a_y, b_x, b_y):
    """I learned maths today"""
    M = np.array([[a_x, b_x], [a_y, b_y]])
    targets = np.array([x_target, y_target])
    det_M = np.linalg.det(M)

    if det_M == 0:
        return None

    M_inv = np.linalg.inv(M)
    solution = np.dot(M_inv, targets)
    press_a, press_b = np.round(solution)
    if (
        a_x * press_a + b_x * press_b == x_target
        and a_y * press_a + b_y * press_b == y_target
    ):
        return int(press_a), int(press_b)
    else:
        return None


pat = re.compile(r"(\d+)")
s = 0
for cm in test_input.split("\n\n"):
    # print(cm)
    ax, ay, bx, by, px, py = tuple(map(int, pat.findall(cm)))
    px, py = px + 10000000000000, py + 10000000000000
    if x := presses(px, py, ax, ay, bx, by):
        # print(x)
        s += (x[0] * 3) + x[1]

print(s)
