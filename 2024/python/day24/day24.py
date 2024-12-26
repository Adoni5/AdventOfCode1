test_input = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""
import re
from operator import and_, or_, xor
from collections import deque

with open("input.txt") as fh:
    test_input = fh.read()

gates, state = test_input.split("\n\n")
pat = re.compile(r"([xy]\d{2}): (\d+)")
gates = dict(pat.findall(gates))
gates = {k: int(v) for k, v in gates.items()}
ops = {"AND": and_, "OR": or_, "XOR": xor}
pat = re.compile(r"(.{3}) ([ANDXOR]+) (.{3}).*(.{3})")

q = deque(pat.findall(state))
while q:
    b1, op, b2, store = q.popleft()
    if b1 in gates and b2 in gates:
        gates[store] = ops[op](gates[b1], gates[b2])
    else:
        q.append((b1, op, b2, store))

z_bits = tuple(sorted((k, v) for k, v in gates.items() if k.startswith("z")))
print(int("".join(tuple(str(v) for k, v in z_bits[::-1])), 2))

x_bits = tuple(sorted((k, v) for k, v in gates.items() if k.startswith("x")))
print(int("".join(tuple(str(v) for k, v in x_bits[::-1])), 2))
x_sum = int("".join(tuple(str(v) for k, v in x_bits[::-1])), 2)


y_bits = tuple(sorted((k, v) for k, v in gates.items() if k.startswith("y")))
print(int("".join(tuple(str(v) for k, v in y_bits[::-1])), 2))
y_sum = int("".join(tuple(str(v) for k, v in y_bits[::-1])), 2)


def find_first_z_output(gates, start_wire, visited=None):
    """
    Recursively follows gates that use 'start_wire' as an input,
    until it finds a gate whose output begins with 'z'.
    Returns that 'zXX' output wire, or None if not found.
    """
    if visited is None:
        visited = set()
    if start_wire in visited:
        return None
    visited.add(start_wire)

    for inp1, gate_type, inp2, out_wire in gates:
        # If this gate uses start_wire as an input, follow its output
        if start_wire in (inp1, inp2):
            if out_wire.startswith("z"):
                # Found a z-wire
                return out_wire
            # Otherwise, keep looking
            result = find_first_z_output(gates, out_wire, visited)
            if result:
                return result

    return None


def find_swaps(gates, x_value, y_value, final_output="z45"):
    """
    Perform the 8-swap logic for a ripple-carry adder where
    gates are tuples (inp1, gate_type, inp2, out_wire).

    Steps:
      (1) Identify 3 gates that produce zXX but aren't XOR (excluding final_output).
      (2) Identify 3 gates that use XOR but none of their I/O is x, y, or z.
      -> We now have 6 gates in total from (1) and (2).

      (3) From these 6 gates, if any is an XOR with non-z output,
          recursively follow that output to the first zXX and swap out_wire -> zXX - 1.
          Limit to exactly 2 swaps total.

      (4) Compare the circuit's final output (mock or real) vs. x+y,
          count leading zero bits in their XOR => N => last two swaps = (xN, yN).

    Returns a dict:
      {
        'step1_gates': [...],
        'step2_gates': [...],
        'two_recursive_swaps': [...],
        'last_two_swaps': (xN, yN)
      }
    """
    # -----------------------------
    # Step 1) Identify 3 gates: produce zXX but not XOR, excluding final_output
    # -----------------------------
    step1_gates = []
    for gate in gates:
        (inp1, gate_type, inp2, out_wire) = gate
        if out_wire.startswith("z") and out_wire != final_output:
            if gate_type != "XOR":
                step1_gates.append(gate)

    # -----------------------------
    # Step 2) Identify 3 gates: use XOR but none of their I/O wires start with x, y, or z
    # -----------------------------
    step2_gates = []
    for gate in gates:
        (inp1, gate_type, inp2, out_wire) = gate
        if gate_type == "XOR":
            wires = [inp1, inp2, out_wire]
            if not any(w[0] in ("x", "y", "z") for w in wires):
                step2_gates.append(gate)

    # Combine the 6 gates (if you find exactly 3 in each list)
    six_wrong_gates = step1_gates + step2_gates
    print(six_wrong_gates)
    # -----------------------------
    # Step 3) Among those 6 gates, find 2 XOR => zXX swaps
    # -----------------------------
    two_recursive_swaps = []
    for gate in six_wrong_gates:
        (inp1, gate_type, inp2, out_wire) = gate
        if gate_type == "XOR" and not out_wire.startswith("z"):
            z_found = find_first_z_output(gates, out_wire)
            if z_found is not None:
                # Example: z_found='z09' => swap (out_wire, 'z08')
                try:
                    z_num = int(z_found[1:])
                    two_recursive_swaps.append((out_wire, f"z{z_num - 1}"))
                except ValueError:
                    pass

    # -----------------------------
    # Step 4) Compare final output vs. x+y to get last two swaps
    # -----------------------------
    correct_value = x_value + y_value

    # For real usage, you’d evaluate the circuit’s actual final_output here
    # We'll do a placeholder and assume circuit_value = correct_value
    circuit_value = correct_value

    mismatch = correct_value ^ circuit_value
    max_bits = max(correct_value.bit_length(), circuit_value.bit_length(), 1)
    bin_str = format(mismatch, f"0{max_bits}b")

    leading_zero_count = 0
    for ch in bin_str:
        if ch == "0":
            leading_zero_count += 1
        else:
            break

    # Final two swaps = (xN, yN)
    last_two_swaps = (f"x{leading_zero_count}", f"y{leading_zero_count}")

    return {
        "step1_gates": step1_gates,
        "step2_gates": step2_gates,
        "two_recursive_swaps": two_recursive_swaps,
        "last_two_swaps": last_two_swaps,
    }


# ----------------------------------------------------------------------------
# Example usage
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    # Example gates: (inp1, operation, inp2, output)
    # Let's call find_swaps with x=5, y=7, final_output='z45'
    results = find_swaps(
        pat.findall(state), x_value=x_sum, y_value=y_sum, final_output="z45"
    )

    print("Step 1 Gates (zXX but not XOR, excluding z45):")
    for g in results["step1_gates"]:
        print("  ", g)

    print("\nStep 2 Gates (XOR but no x,y,z in any I/O):")
    for g in results["step2_gates"]:
        print("  ", g)

    print("\nTwo Recursive Swaps (just for the 6 gates above):")
    for s in results["two_recursive_swaps"]:
        print("  ", s)

    print("\nLast Two Swaps (xN, yN):", results["last_two_swaps"])

wires = {}
operations = []


def process(op, op1, op2):
    if op == "AND":
        return op1 & op2
    elif op == "OR":
        return op1 | op2
    elif op == "XOR":
        return op1 ^ op2


highest_z = "z00"
data = open("input.txt").read().split("\n")
for line in data:
    if ":" in line:
        wire, value = line.split(": ")
        wires[wire] = int(value)
    elif "->" in line:
        op1, op, op2, _, res = line.split(" ")
        operations.append((op1, op, op2, res))
        if res[0] == "z" and int(res[1:]) > int(highest_z[1:]):
            highest_z = res

wrong = set()
for op1, op, op2, res in operations:
    if res[0] == "z" and op != "XOR" and res != highest_z:
        wrong.add(res)
    if (
        op == "XOR"
        and res[0] not in ["x", "y", "z"]
        and op1[0] not in ["x", "y", "z"]
        and op2[0] not in ["x", "y", "z"]
    ):
        wrong.add(res)
    if op == "AND" and "x00" not in [op1, op2]:
        for subop1, subop, subop2, subres in operations:
            if (res == subop1 or res == subop2) and subop != "OR":
                wrong.add(res)
    if op == "XOR":
        for subop1, subop, subop2, subres in operations:
            if (res == subop1 or res == subop2) and subop == "OR":
                wrong.add(res)

while len(operations):
    op1, op, op2, res = operations.pop(0)
    if op1 in wires and op2 in wires:
        wires[res] = process(op, wires[op1], wires[op2])
    else:
        operations.append((op1, op, op2, res))

bits = [str(wires[wire]) for wire in sorted(wires, reverse=True) if wire[0] == "z"]
print(int("".join(bits), 2))
print(",".join(sorted(wrong)))
