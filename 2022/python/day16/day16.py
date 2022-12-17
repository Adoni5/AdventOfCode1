test_input = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""
import numpy as np
import re
from pprint import pprint
from support import get_input
from functools import cache

test_input = get_input("16")

pat = re.compile(r"([A-Z]{2}|\d+)")
valves = {}
for line in test_input.splitlines():
    l = pat.findall(line)
    valves[l[0]] = {"flow": int(l[1]), "tunnels": l[2:], "paths": {}}

pprint(valves)
keys = sorted([x for x in list(valves.keys()) if valves[x]['flow'] != 0])
print(keys)

def bfs(frontier, end):
    depth = 1
    while True:
        next_frontier = set()
        for x in frontier:
            if x == end:
                return depth
            for y in valves[x]['tunnels']:
                next_frontier.add(y)
        frontier = next_frontier
        depth += 1


for k in keys + ['AA']:
    for k2 in keys:
        if k2 != k:
            valves[k]['paths'][k2] = bfs(valves[k]['tunnels'], k2)

pprint(valves)


def part1():
    best = 0
    def search(opened, flowed, current_room, depth_to_go):
        nonlocal best
        if flowed > best:
            best = flowed

        if depth_to_go <= 0:
            return

        if current_room not in opened:
            search(opened.union([current_room]), flowed + valves[current_room]['flow'] * depth_to_go, current_room, depth_to_go - 1)
        else:
            for k in [x for x in valves[current_room]['paths'].keys() if x not in opened]:
                search(opened, flowed, k, depth_to_go - valves[current_room]['paths'][k])

    search(set(['AA']), 0, 'AA', 29)
    print(best)

part1()

def part2():
    best = 0
    def search(opened, flowed, current_room, depth_to_go, elephants_turn):
        nonlocal best
        if flowed > best:
            best = flowed

        if depth_to_go <= 0:
            return

        if current_room not in opened:
            search(opened.union([current_room]), flowed + valves[current_room]['flow'] * depth_to_go, current_room, depth_to_go - 1, elephants_turn)
            if not elephants_turn:
                search(set([current_room]).union(opened), flowed + valves[current_room]['flow'] * depth_to_go, 'AA', 25, True)
        else:
            for k in [x for x in valves[current_room]['paths'].keys() if x not in opened]:
                search(opened, flowed, k, depth_to_go - valves[current_room]['paths'][k], elephants_turn)

    search(set(['AA']), 0, 'AA', 25, False)
    print(best)
part2()
