import re

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    data = read_input_file_data()
    samples, _ = data.split('\n\n\n\n')
    cases = samples.split('\n\n')

    count = 0
    for case in cases:
        before, operation, after = case.splitlines()
        opcode, A, B, C = list(map(int, operation.split()))
        bef_reg = list(map(int, re.search(r"(\d, \d, \d, \d)", before).group(0).split(',')))
        aft_reg = list(map(int, re.search(r"(\d, \d, \d, \d)", after).group(0).split(',')))
        
        num_op_codes = 0
        # addr
        if (A <= 3 and B <= 3 and C <= 3 and
            bef_reg[A] + bef_reg[B] == aft_reg[C]):
            num_op_codes += 1
        # addi
        if (A <= 3 and C <= 3 and
            bef_reg[A] + B == aft_reg[C]):
            num_op_codes += 1
        # mulr
        if (A <= 3 and B <= 3 and C <= 3 and
            bef_reg[A] * bef_reg[B] == aft_reg[C]):
            num_op_codes += 1
        # muli
        if (A <= 3 and C <= 3 and
            bef_reg[A] * B == aft_reg[C]):
            num_op_codes += 1
        # banr
        if (A <= 3 and B <= 3 and C <= 3 and
            bef_reg[A] & bef_reg[B] == aft_reg[C]):
            num_op_codes += 1
        # bani
        if (A <= 3 and C <= 3 and
            bef_reg[A] & B == aft_reg[C]):
            num_op_codes += 1
        # banr
        if (A <= 3 and B <= 3 and C <= 3 and
            bef_reg[A] | bef_reg[B] == aft_reg[C]):
            num_op_codes += 1
        # bani
        if (A <= 3 and C <= 3 and
            bef_reg[A] | B == aft_reg[C]):
            num_op_codes += 1
        # setr
        if (A <= 3 and C <= 3 and
            bef_reg[A] == aft_reg[C]):
            num_op_codes += 1
        # seti
        if (C <= 3 and
            A == aft_reg[C]):
            num_op_codes += 1
        # gtir
        if (B <= 3 and C <= 3 and
            aft_reg[C] == (1 if A > bef_reg[B] else 0)):
            num_op_codes += 1
        # gtri
        if (A <= 3 and C <= 3 and
            aft_reg[C] == (1 if bef_reg[A] > B else 0)):
            num_op_codes += 1
        # gtrr
        if (A <= 3 and B <= 3 and C <= 3 and
            aft_reg[C] == (1 if bef_reg[A] > bef_reg[B] else 0)):
            num_op_codes += 1
        # eqir
        if (B <= 3 and C <= 3 and
            aft_reg[C] == (1 if A == bef_reg[B] else 0)):
            num_op_codes += 1
        # eqri
        if (A <= 3 and C <= 3 and
            aft_reg[C] == (1 if bef_reg[A] == B else 0)):
            num_op_codes += 1
        # eqrr
        if (A <= 3 and B <= 3 and C <= 3 and
            aft_reg[C] == (1 if bef_reg[A] == bef_reg[B] else 0)):
            num_op_codes += 1
        
        if num_op_codes >= 3:
            count += 1
    return count

# def figure_out_opcode():
#     data = read_input_file_data()
#     samples, _ = data.split('\n\n\n\n')
#     cases = samples.split('\n\n')

#     for case in cases:
#         before, operation, after = case.splitlines()
#         opcode, A, B, C = list(map(int, operation.split()))
#         bef_reg = list(map(int, re.search(r"(\d, \d, \d, \d)", before).group(0).split(',')))
#         aft_reg = list(map(int, re.search(r"(\d, \d, \d, \d)", after).group(0).split(',')))
        
#         num_op_codes = 0
#         # # addr (9)
#         # if (A <= 3 and B <= 3 and C <= 3 and
#         #     bef_reg[A] + bef_reg[B] == aft_reg[C]):
#         #     num_op_codes += 1
#         # # addi (6)
#         # if (A <= 3 and C <= 3 and
#         #     bef_reg[A] + B == aft_reg[C]):
#         #     num_op_codes += 1
#         # # mulr (8)
#         # if (A <= 3 and B <= 3 and C <= 3 and
#         #     bef_reg[A] * bef_reg[B] == aft_reg[C]):
#         #     num_op_codes += 1
#         # # muli (0)
#         # if (A <= 3 and C <= 3 and
#         #     bef_reg[A] * B == aft_reg[C]):
#         #     num_op_codes += 1
#         # # banr (14)
#         # if (A <= 3 and B <= 3 and C <= 3 and
#         #     bef_reg[A] & bef_reg[B] == aft_reg[C]):
#         #     num_op_codes += 1
#         # # bani (11)
#         # if (A <= 3 and C <= 3 and
#         #     bef_reg[A] & B == aft_reg[C]):
#         #     num_op_codes += 1
#         # # borr (1)
#         # if (A <= 3 and B <= 3 and C <= 3 and
#         #     bef_reg[A] | bef_reg[B] == aft_reg[C]):
#         #     num_op_codes += 1
#         # # bori (10)
#         # if (A <= 3 and C <= 3 and
#         #     bef_reg[A] | B == aft_reg[C]):
#         #     num_op_codes += 1
#         # # setr (7)
#         # if (A <= 3 and C <= 3 and
#         #     bef_reg[A] == aft_reg[C]):
#         #     num_op_codes += 1
#         # # seti (12)
#         # if (C <= 3 and
#         #     A == aft_reg[C]):
#         #     num_op_codes += 1
#         # # gtir (15)
#         # if (B <= 3 and C <= 3 and
#         #     aft_reg[C] == (1 if A > bef_reg[B] else 0)):
#         #     num_op_codes += 1
#         # # gtri (2)
#         # if (A <= 3 and C <= 3 and
#         #     aft_reg[C] == (1 if bef_reg[A] > B else 0)):
#         #     num_op_codes += 1
#         # # gtrr (4)
#         # if (A <= 3 and B <= 3 and C <= 3 and
#         #     aft_reg[C] == (1 if bef_reg[A] > bef_reg[B] else 0)):
#         #     num_op_codes += 1
#         # # eqir (5)
#         # if (B <= 3 and C <= 3 and
#         #     aft_reg[C] == (1 if A == bef_reg[B] else 0)):
#         #     num_op_codes += 1
#         # # eqri (3)
#         # if (A <= 3 and C <= 3 and
#         #     aft_reg[C] == (1 if bef_reg[A] == B else 0)):
#         #     num_op_codes += 1
#         # # eqrr (13)
#         # if (A <= 3 and B <= 3 and C <= 3 and
#         #     aft_reg[C] == (1 if bef_reg[A] == bef_reg[B] else 0)):
#         #     num_op_codes += 1
        
#         # if num_op_codes == 1:
#             # # addr (9)
#             # if (A <= 3 and B <= 3 and C <= 3 and
#             #     bef_reg[A] + bef_reg[B] == aft_reg[C]):
#             #     print(f"opcode: {opcode} represents addr")
#             # # addi (6)
#             # if (A <= 3 and C <= 3 and
#             #     bef_reg[A] + B == aft_reg[C]):
#             #     print(f"opcode: {opcode} represents addi")
#             # # mulr (8)
#             # if (A <= 3 and B <= 3 and C <= 3 and
#             #     bef_reg[A] * bef_reg[B] == aft_reg[C]):
#             #     print(f"opcode: {opcode} represents mulr")
#             # # muli (0)
#             # if (A <= 3 and C <= 3 and
#             #     bef_reg[A] * B == aft_reg[C]):
#             #     print(f"opcode: {opcode} represents muli")
#             # # banr (14)
#             # if (A <= 3 and B <= 3 and C <= 3 and
#             #     bef_reg[A] & bef_reg[B] == aft_reg[C]):
#             #     print(f"opcode: {opcode} represents banr")
#             # # bani (11)
#             # if (A <= 3 and C <= 3 and
#             #     bef_reg[A] & B == aft_reg[C]):
#             #     print(f"opcode: {opcode} represents bani")
#             # # borr (1)
#             # if (A <= 3 and B <= 3 and C <= 3 and
#             #     bef_reg[A] | bef_reg[B] == aft_reg[C]):
#             #     print(f"opcode: {opcode} represents borr")
#             # # bori (10)
#             # if (A <= 3 and C <= 3 and
#             #     bef_reg[A] | B == aft_reg[C]):
#             #     print(f"opcode: {opcode} represents bori")
#             # # setr (7)
#             # if (A <= 3 and C <= 3 and
#             #     bef_reg[A] == aft_reg[C]):
#             #     print(f"opcode: {opcode} represents setr")
#             # # seti (12)
#             # if (C <= 3 and
#             #     A == aft_reg[C]):
#             #     print(f"opcode: {opcode} represents seti")
#             # # gtir (15)
#             # if (B <= 3 and C <= 3 and
#             #     aft_reg[C] == (1 if A > bef_reg[B] else 0)):
#             #     print(f"opcode: {opcode} represents gtir")
#             # # gtri (2)
#             # if (A <= 3 and C <= 3 and
#             #     aft_reg[C] == (1 if bef_reg[A] > B else 0)):
#             #     print(f"opcode: {opcode} represents gtri")
#             # # gtrr (4)
#             # if (A <= 3 and B <= 3 and C <= 3 and
#             #     aft_reg[C] == (1 if bef_reg[A] > bef_reg[B] else 0)):
#             #     print(f"opcode: {opcode} represents gtrr")
#             # # eqir (5)
#             # if (B <= 3 and C <= 3 and
#             #     aft_reg[C] == (1 if A == bef_reg[B] else 0)):
#             #     print(f"opcode: {opcode} represents eqir")
#             # # eqri (3)
#             # if (A <= 3 and C <= 3 and
#             #     aft_reg[C] == (1 if bef_reg[A] == B else 0)):
#             #     print(f"opcode: {opcode} represents eqri")
#             # # eqrr (13)
#             # if (A <= 3 and B <= 3 and C <= 3 and
#             #     aft_reg[C] == (1 if bef_reg[A] == bef_reg[B] else 0)):
#             #     print(f"opcode: {opcode} represents eqrr")
#     return None

def solve_part_2():
    # figure_out_opcode()
    data = read_input_file_data()
    _, program = data.split('\n\n\n\n')
    reg = [0, 0, 0, 0]

    for line in program.splitlines():
        opcode, A, B, C = list(map(int, line.split()))
        match opcode:
            case 0: # muli
                reg[C] = reg[A] * B
            case 1: # borr
                reg[C] = reg[A] | reg[B]
            case 2: # gtri
                reg[C] = 1 if reg[A] > B else 0
            case 3: # eqri
                reg[C] = 1 if reg[A] == B else 0
            case 4: # gtrr
                reg[C] = 1 if reg[A] > reg[B] else 0
            case 5: # eqir
                reg[C] = 1 if A == reg[B] else 0
            case 6: # addi
                reg[C] = reg[A] + B
            case 7: # setr
                reg[C] = reg[A]
            case 8: # mulr
                reg[C] = reg[A] * reg[B]
            case 9: # addr
                reg[C] = reg[A] + reg[B]
            case 10: # bori
                reg[C] = reg[A] | B
            case 11: # bani
                reg[C] = reg[A] & B
            case 12: # seti
                reg[C] = A
            case 13: # eqrr
                reg[C] = 1 if reg[A] == reg[B] else 0
            case 14: # banr
                reg[C] = reg[A] & reg[B]
            case 15: # gtir
                reg[C] = 1 if A > reg[B] else 0
    return reg[0]
    
print(solve_part_2())
