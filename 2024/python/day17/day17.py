test_input = """Register A: 0
Register B: 2024
Register C: 43690

Program: 4,0"""

import re

with open("input.txt") as fh:
    test_input = fh.read()

pat_reg = re.compile(r"([ABC]): (\d+)")
pat_prog = re.compile(r"(\d+)")

reg, prog = test_input.split("\n\n")
registers = {}
for l in reg.splitlines():
    r, v = pat_reg.findall(l)[0]
    registers[r] = int(v)

prog = tuple(map(int, pat_prog.findall(prog)))
out = []
instruct_ptr = 0
print(reg)
print(prog)


# operand_ptr = 1
def combo_op(oper, register=registers):
    combo_operands = {0: 0, 1: 1, 2: 2, 3: 3, 4: "A", 5: "B", 6: "C"}
    if oper == 7:
        return None
    elif oper <= 3:
        return oper
    return register[combo_operands[oper]]


# 0 adv, targ A, div by 2 ^ combo op, store A
# 1 bxl, bitwise OR, targ B, literal operand, store B
# 2 bst, module 8 of combo operand, store B
# 3 jnz, jump to literal op, set instruction ptr,
# 4 bxc, bitwsie XOR of B and C, reads operand but ignores it, store B
# 5 out, combo operand modulo 8, if multiple nums, csv
# 6 bdv, same as 0 (adv), store in B
# 7 cdv, same as 0 (adv), store in C

read = True

while read:
    if instruct_ptr >= len(prog):
        break
    op, oper = prog[instruct_ptr : instruct_ptr + 2]
    print(op, oper, registers)
    match op:
        case 0:
            registers["A"] = int(registers["A"] / (2 ** combo_op(oper)))
        case 1:
            registers["B"] = int(registers["B"]) ^ oper
        case 2:
            registers["B"] = combo_op(oper) % 8
        case 3:
            if registers["A"] != 0:
                instruct_ptr = oper
            else:
                instruct_ptr += 2
        case 4:
            registers["B"] = registers["B"] ^ registers["C"]
        case 5:
            v = combo_op(oper) % 8
            print(v)
            out.extend(list(map(str, str(v))))
            print(out)
        case 6:
            registers["B"] = int(registers["A"] / (2 ** combo_op(oper)))
        case 7:
            registers["C"] = int(registers["A"] / (2 ** combo_op(oper)))
        case _:
            print(f"breaking {op}")
            break
    if op != 3:
        instruct_ptr += 2
    # input()
print(registers)
print(",".join(out))


a, b, c, *prog = [int(n) for n in re.findall("(\d+)", open("input.txt").read())]


def run(prog, a):
    ip, b, c, out = 0, 0, 0, []
    while ip >= 0 and ip < len(prog):
        lit, combo = prog[ip + 1], [0, 1, 2, 3, a, b, c, 99999][prog[ip + 1]]
        match prog[ip]:
            case 0:
                a = int(a / 2**combo)  # adv
            case 1:
                b = b ^ lit  # bxl
            case 2:
                b = combo % 8  # bst
            case 3:
                ip = ip if a == 0 else lit - 2  # jnz
            case 4:
                b = b ^ c  # bxc
            case 5:
                out.append(combo % 8)  # out
            case 6:
                b = int(a / 2**combo)  # bdv
            case 7:
                c = int(a / 2**combo)  # cdv
        ip += 2
    return out


print("Part 1:", ",".join(str(n) for n in run(prog, a)))
print(prog)
target = prog[::-1]


def find_a(a=0, depth=0):
    print(a)
    if depth == len(target):
        return a
    for i in range(8):
        output = run(prog, a * 8 + i)
        if output and output[0] == target[depth]:
            if result := find_a((a * 8 + i), depth + 1):
                return result
    return 0


print("Part 2:", find_a())
