from collections import namedtuple
import re
from support import get_input

test_input = """Blueprint 1:
  Each ore robot costs 4 ore.
  Each clay robot costs 2 ore.
  Each obsidian robot costs 3 ore and 14 clay.
  Each geode robot costs 2 ore and 7 obsidian.

Blueprint 2:
  Each ore robot costs 2 ore.
  Each clay robot costs 3 ore.
  Each obsidian robot costs 3 ore and 8 clay.
  Each geode robot costs 3 ore and 12 obsidian"""
import re, numpy as np

test_input = get_input("19")
print(test_input)

minutes = 24
# Use numpy arrays for state representation
V = lambda *a: np.array(a)

# Key function to represent the state
key = lambda a: tuple(a[0] + a[1]) + tuple(a[1])

# Prune function to keep the best 1000 states
prune = lambda x: sorted({key(x): x for x in x}.values(), key=key)[-1000:]


def parse(line):
    nums = list(map(int, re.findall(r"\d+", line)))
    blueprint = [
        (V(0, 0, 0, nums[1]), V(0, 0, 0, 1)),  # ore robot
        (V(0, 0, 0, nums[2]), V(0, 0, 1, 0)),  # clay robot
        (V(0, 0, nums[4], nums[3]), V(0, 1, 0, 0)),  # obsidian robot
        (V(0, nums[6], 0, nums[5]), V(1, 0, 0, 0)),  # geode robot
        (V(0, 0, 0, 0), V(0, 0, 0, 0)),  # empty robot
    ]
    return blueprint


def possible_next_states(
    current_state: list[(int, int, int, int), (int, int, int, int)], blueprint
):
    current_resources, robots = current_state
    # print(f"current state: {current_state}")
    x = []
    for cost, production in blueprint:
        # print(f"cost:{cost}, production: {production}")
        if all(cost <= current_resources):
            # print(f"making cost:{cost}, production: {production}")
            x.append((current_resources + robots - cost, robots + production))
    return x


# Starting state
initial_state = (V(0, 0, 0, 0), V(0, 0, 0, 1))
blueprints = [parse(block) for block in test_input.split("\n")]
print(blueprints)
max_qualities = []

for index, blueprint in enumerate(blueprints, start=1):
    print("Blueprint", index)
    states = [initial_state]
    for _ in range(minutes):
        print(f"minute {_+1}")
        new_states = []
        for state in states:
            new_states.extend(possible_next_states(state, blueprint))
        states = prune(new_states)
        # if _ == 3:
        #     break
    max_qualities.append((max(ores[0] for ores, _ in states) * index))
print(sum(max_qualities))

initial_state = (V(0, 0, 0, 0), V(0, 0, 0, 1))
blueprints = [parse(block) for block in test_input.split("\n")[:3]]
max_geodes = []

for index, blueprint in enumerate(blueprints, start=1):
    print("Blueprint", index)
    states = [initial_state]
    for _ in range(32):
        print(f"minute {_+1}")
        new_states = []
        for state in states:
            new_states.extend(possible_next_states(state, blueprint))
        states = prune(new_states)
        # if _ == 3:
        #     break
    max_geodes.append((max(ores[0] for ores, _ in states)))
print(max_geodes)
print(np.prod(max_qualities))
