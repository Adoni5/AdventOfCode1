test_input = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""
from collections import defaultdict


with open("input.txt") as fh:
    test_input = fh.read().strip()
conns = defaultdict(set)
for line in test_input.strip().splitlines():
    nod1, nod2 = line.split("-")
    conns[nod1].add(nod2)
    conns[nod2].add(nod1)

networks = set()

for host in conns:
    peers = conns[host]
    for peer in peers:
        other_peers = conns[peer]
        if len(comm := peers.intersection(other_peers)):
            for c in iter(comm):
                net = tuple(sorted([host, peer, c]))
                networks.add(net)

print(sum((any(comp.startswith("t") for comp in n) for n in networks)))


while True:
    new_networks = set()
    for network in networks:
        host, *peers = network
        host_peers, *peer_peers = [conns[h] for h in network]
        if len(comm := host_peers.intersection(*peer_peers)):
            for c in iter(comm):
                net = tuple(sorted(list(network) + [c]))
                new_networks.add(net)
    if len(new_networks) == 0:
        break
    net_len = len(next(iter(new_networks)))
    print(f"Found {len(new_networks)} networks of length {net_len}")
    networks = new_networks

largest_network = next(iter(networks))
net_len = len(largest_network)
password = ",".join(largest_network)
print(password)
