from support import get_input
from itertools import cycle
jets = [1 if l == '>' else -1 for l in get_input("17")]
well = set([-1j,1-1j,2-1j,3-1j,4-1j,5-1j,6-1j])
highest = -1
piece_index = 4
jet_index = -1
p1, p2 = 0, 0
history = dict()
limit = 1_000_000_000_000
pieces = [[2+0j,3+0j,4+0j,5+0j], 
          [3+0j,2+1j,3+1j,4+1j,3+2j],
          [2+0j,3+0j,4+0j,4+1j,4+2j],
          [2+0j,2+1j,2+2j,2+3j],
          [2+0j,3+0j,2+1j,3+1j]]   

cycle_jets = cycle(jets)
for i, rock in enumerate(cycle(pieces)):
    
    seen = (i % 5, jet_index)
    if seen in history:
        period = i - history[seen][0]
        print(history)
        if i % period == limit % period:
            print(period)
            p2 = history[seen][1] + (highest+1 - history[seen][1])*(((limit-i)//period)+1)
            break
    else:
        history[seen] = i, highest+1

    if i == 2022:
        p1 = highest+1 

    piece_index = i % 5
    
    for j, jet in enumerate(cycle_jets):
        jet_index = j % 40
        piece = [x+jet for x in rock]
        if any([(x.real < 0) or (x in well) or (x.real > 6) for x in piece]):
            piece = [x-jet for x in piece]
        piece = [x-1j for x in piece]
        if any([x in well for x in piece]):
            well |= set([x+1j for x in piece])
            highest = max(highest, int(piece[-1].imag)+1)
            break

print(p1,p2)     