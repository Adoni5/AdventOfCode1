test_input = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""


from support import get_input
from collections import defaultdict
import re

test_input = get_input(15, 2023)
total = 0
for step in test_input.split(","):
    cur_val = 0
    for char in step:
        cur_val += ord(char)
        cur_val *= 17
        cur_val = cur_val % 256
    total += cur_val

print(total)

pat = re.compile(r"(\w+)([=-])(\d*)")
boxes = defaultdict(dict)
# P2
for step in test_input.split(","):
    box = 0
    pa = pat.findall(step)[0]
    label, op = pa[:2]
    fl = int(pa[-1]) if op == "=" else None

    for char in label:
        box += ord(char)
        box *= 17
        box = box % 256
    if op == "=":
        boxes[box][label] = fl
    else:
        if label in boxes[box]:
            boxes[box].pop(label)
    # input()
total = 0
for box_num, box in boxes.items():
    for sn, fl in enumerate(box.values(), start=1):
        total += (box_num + 1) * sn * fl
print(total)
