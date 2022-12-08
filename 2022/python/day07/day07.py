from uuid import uuid4
from collections import defaultdict
from support import get_input

data = get_input("7", split="\n")

dirsizes = defaultdict(int)

tree = []
for line in data:
    line = line.split()
    if line[1] == "cd":
        if line[2] == "..":
            tree.pop()
        else:
            if line[2] not in dirsizes:
                tree.append(line[2])
            else:
                d = line[2] + str(uuid4())
                tree.append(d)
    elif line[1] == "ls":
        continue
    else:
        if line[0] != "dir":
            for p in tree:
                dirsizes[p] += int(line[0])

print(sum(d for d in dirsizes.values() if d <= 100000))
needed = 30000000 - (70000000 - dirsizes["/"])
print(min(d for d in dirsizes.values() if d > needed))