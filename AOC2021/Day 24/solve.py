from collections import defaultdict
def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    # def check_model_number_validity(model_number: int):
    #     assert model_number > 10_000_000_000_000
    #     inputs = list(map(int, str(model_number)))
    #     instructions = read_input_file_data().splitlines()
    #     registers = [0, 0, 0, 0]
    #     register_indices = {'w': 0, 'x': 1, 'y': 2, 'z': 3}
    #     for line in instructions:
    #         parts = line.split()
    #         ins = parts[0]
    #         a_index = register_indices[parts[1]]
    #         if ins == 'inp':
    #             registers[a_index] = inputs.pop(0)
    #         elif ins == 'add':
    #             b = registers[register_indices[parts[2]]] if parts[2] in register_indices else int(parts[2])
    #             registers[a_index] += b
    #         elif ins == 'mul':
    #             b = registers[register_indices[parts[2]]] if parts[2] in register_indices else int(parts[2])
    #             registers[a_index] *= b
    #         elif ins == 'div':
    #             b = registers[register_indices[parts[2]]] if parts[2] in register_indices else int(parts[2])
    #             registers[a_index] //= b
    #         elif ins == 'mod':
    #             b = registers[register_indices[parts[2]]] if parts[2] in register_indices else int(parts[2])
    #             registers[a_index] %= b
    #         elif ins == 'eql':
    #             b = registers[register_indices[parts[2]]] if parts[2] in register_indices else int(parts[2])
    #             registers[a_index] = 1 if registers[register_indices[parts[1]]] == b else 0
    #         else:
    #             raise Exception(f"Unrecognised instruction {parts[0]}")
    #     return registers[register_indices['z']] == 0
    
    # return check_model_number_validity(51983999947999)
    # for n in range(99_999_999_999_999, 11_111_111_111_110, -1):
    #     if '0' in str(n):
    #         continue
    #     model_number = list(map(int, str(n)))
    #     if check_model_number_validity(model_number):
    #         return n

    '''
    Since number is large, question is to be solved through input analysis.
    There is 18 lines of ALU code attributed to each input function.

    inp w       # get input in w
    mul x 0     # clear x
    add x z
    mod x 26    # x = z % 26
    div z (a)   # DIFF (either 1 or 26)
    add x (b)   # DIFF add b to x
    eql x w
    eql x 0     # x = 1 if input != (z % 26) + b else 0
    mul y 0     # clear y
    add y 25
    mul y x
    add y 1     # set y = 25 * x + 1
    mul z y     # if input != (z % 26) + b, z *= 26
    mul y 0     # clear y
    add y w
    add y (c)   # DIFF y = input + c
    mul y x
    add z y

    Analysis:
    Segment  1: a=1  b=11  c=6
    Segment  2: a=1  b=11  c=14
    Segment  3: a=1  b=15  c=13
    Segment  4: a=26 b=-14 c=1
    Segment  5: a=1  b=10  c=6
    Segment  6: a=26 b=0   c=13
    Segment  7: a=26 b=-6  c=6
    Segment  8: a=1  b=13  c=3
    Segment  9: a=26 b=-3  c=8
    Segment 10: a=1  b=13  c=14
    Segment 11: a=1  b=15  c=4
    Segment 12: a=26 b=-2  c=7
    Segment 13: a=26 b=-9  c=15
    Segment 14: a=26 b=-2  c=1

    Conclusion:
    x = 1 if input != (z % 26) + b else 0
    z //= a
    if x == 1:
        z *= 26
        z += input + c

    Other findings:
    Since a is always 1 or 26 and c is always > 0, for z to be 0 at
    the end of the calculation, we need to add input and c to z in a
    way that they sum up to 26.
    Since there is a max of 3 consecutive a=26, max z we need to
    account for is 26**3 = 17576.
    '''
    instructions = read_input_file_data().split('inp w\n')[1:]
    abc = []
    for segment in instructions:
        lines = segment.splitlines()
        a = int(lines[3].split()[2])
        b = int(lines[4].split()[2])
        c = int(lines[14].split()[2])
        abc.append((a, b, c))
    
    VALID_NUMS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    Z_LIMIT = 26**3 # Runtime optimization
    frontier = { 0: 0 } # z: model_number
    for a, b, c in abc:
        new_frontier = defaultdict(int)
        for z, model_number in frontier.items():
            if z > Z_LIMIT:
                continue
            m = (z % 26) + b # The matching input value
            z //= a

            for n in VALID_NUMS:
                if n != m: # x == 1
                    new_z = z * 26 + n + c
                    new_frontier[new_z] = max(new_frontier[new_z], model_number * 10 + n)
                else:
                    new_frontier[z] = max(new_frontier[z], model_number * 10 + n)
        frontier = new_frontier
    return frontier[0]

def solve_part_2():
    # Same solution as part 1 but use min instead of max
    instructions = read_input_file_data().split('inp w\n')[1:]
    abc = []
    for segment in instructions:
        lines = segment.splitlines()
        a = int(lines[3].split()[2])
        b = int(lines[4].split()[2])
        c = int(lines[14].split()[2])
        abc.append((a, b, c))
    
    VALID_NUMS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    Z_LIMIT = 26**3 # Runtime optimization
    frontier = { 0: 0 } # z: model_number
    for a, b, c in abc:
        new_frontier = defaultdict(lambda: 99_999_999_999_999) # Use a large enough value as default
        for z, model_number in frontier.items():
            if z > Z_LIMIT: # Runtime optimization
                continue
            m = (z % 26) + b # The matching input value
            z //= a

            for n in VALID_NUMS:
                if n != m: # x == 1
                    new_z = z * 26 + n + c
                    new_frontier[new_z] = min(new_frontier[new_z], model_number * 10 + n)
                else:
                    new_frontier[z] = min(new_frontier[z], model_number * 10 + n)
        frontier = new_frontier
    return frontier[0]
    
print(solve_part_2())
