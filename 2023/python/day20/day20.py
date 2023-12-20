test_input = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""

ffs = {}
cons = {}
broadcast = []
broadcaster = {}
HIGH_PULSE = 1
LOW_PULSE = 0

total_high = 0
total_low = 0

from collections import deque
from itertools import zip_longest
from support import get_input
from math import lcm

test_input = get_input(20, 2023)
for line in test_input.splitlines():
    module, dest = line.split(" -> ")
    if module[0] in "%&":
        if module[0] == "%":
            ffs[module[1:]] = {"is_on": False, "outputs": dest.split(", ")}
        if module[0] == "&":
            cons[module[1:]] = {"inputs": {}, "outputs": dest.split(", ")}
    if module == "broadcaster":
        broadcaster["outputs"] = dest.split(", ")


# go through again and set the memory pulse for each conjunction to default off
for line in test_input.splitlines():
    module, dest = line.split(" -> ")
    if dest in cons:
        cons[dest]["inputs"][module[1:]] = LOW_PULSE

        # P2
print(cons["cl"])
(feed,) = [name for name, module in cons.items() if "rx" in module["outputs"]]

cycle_lengths = {}
seen = {name: 0 for name, module in cons.items() if feed in module["outputs"]}
print(seen)
print(broadcast)
print(cons)
print(ffs)
# Broadcat -> (destination, pulse, origin)
press = 0
while True:
    press += 1
    total_low += 1  # 1 as button press sends one to broadcaster
    broadcast = deque(
        list(
            zip_longest(
                broadcaster["outputs"],
                (LOW_PULSE,),
                ("broadcast" for _ in range(len(broadcaster["outputs"]))),
                fillvalue=LOW_PULSE,
            )
        )
    )
    while broadcast:
        dest, signal, origin = broadcast.popleft()
        # print(f"Porcessing {"low_pulse" if signal == LOW_PULSE else "high_pulse"} goin gto  {dest} from {origin}")
        if signal == HIGH_PULSE:
            total_high += 1
        else:
            total_low += 1
        if dest == feed and signal == HIGH_PULSE:
            seen[origin] += 1

            if origin not in cycle_lengths:
                cycle_lengths[origin] = press
            else:
                assert press == seen[origin] * cycle_lengths[origin]

            if all(seen.values()):
                x = 1
                for cycle_length in cycle_lengths.values():
                    x = lcm(x, cycle_length)
                print(x)
                exit(0)
        if dest in ffs and signal == LOW_PULSE:
            ffs[dest]["is_on"] = not ffs[dest]["is_on"]
            for next_dest in ffs[dest]["outputs"]:
                broadcast.append((next_dest, int(ffs[dest]["is_on"]), dest))
        elif dest in cons:
            # first update the memory
            cons[dest]["inputs"][origin] = signal
            # All high pulse add low pulse
            if all(cons[dest]["inputs"].values()):
                # add a low for each dest for the con
                for next_dest in cons[dest]["outputs"]:
                    broadcast.append((next_dest, LOW_PULSE, dest))
            else:
                # add high pulse for each dest
                for next_dest in cons[dest]["outputs"]:
                    broadcast.append((next_dest, HIGH_PULSE, dest))
        # print(broadcast)
        # print(cons)
    if press == 1000:
        print(total_low * total_high)
