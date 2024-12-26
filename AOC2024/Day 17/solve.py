def get_data():
    RA = 52042868
    RB = 0
    RC = 0
    program = [2,4,1,7,7,5,0,3,4,4,1,7,5,5,3,0]
    return RA, RB, RC, program

def solve_part_1():
    RA, RB, RC, program = get_data()
    pointer = 0
    output = []

    def read_literal_operand():
        nonlocal pointer
        v = program[pointer]
        pointer += 1
        return v
    
    def read_combo_operand():
        nonlocal pointer
        v = program[pointer]
        pointer += 1
        match v:
            case 0 | 1 | 2 | 3:
                return v
            case 4:
                return RA
            case 5:
                return RB
            case 6:
                return RC
            case 7:
                raise Exception("Illegal combo operand")
            case _:
                raise Exception(f"Unknown operand {v}")
    
    def run_instruction():
        nonlocal pointer, RA, RB, RC
        v = program[pointer]
        pointer += 1
        match v:
            case 0: # adv
                operand = read_combo_operand()
                RA = RA // (2 ** operand)
            case 1: # bxl
                operand = read_literal_operand()
                RB = RB ^ operand
            case 2: # bst
                operand = read_combo_operand()
                RB = operand % 8
            case 3: # jnz
                if RA == 0:
                    pointer += 1
                else:
                    operand = read_literal_operand()
                    pointer = operand
            case 4: # bxc
                pointer += 1
                RB = RB ^ RC
            case 5: # out
                operand = read_combo_operand()
                output.append(operand % 8)
            case 6: # bdv
                operand = read_combo_operand()
                RB = RA // (2 ** operand)
            case 7: # cdv
                operand = read_combo_operand()
                RC = RA // (2 ** operand)
            case _:
                raise Exception(f"Unknown instruction {v}")
    
    PTR_LIMIT = len(program)
    while pointer < PTR_LIMIT:
        run_instruction()
    return ','.join(list(map(str, output)))

def solve_part_2():
    '''
    # Program: 2,4,1,7,7,5,0,3,4,4,1,7,5,5,3,0

    2,4 RB = RA % 8
    1,7	RB ^= 7
    7,5	RC = RA >> RB
    0,3	RA >> 3
    4,4	RB ^= RC
    1,7	RB ^= 7
    5,5	print(RB % 8)
    3,0	jump to start if RA != 0

    Take last 3 bits of RA, flip them and store in RB as x. (2,4)(1,7)
    Remove x bits from RA and store last 3 bits in RC.                (7,5)          (1,7)
    Delete last 3 bits from RA.                                            (0,3)
    Print RB ^ RC.                                                              (4,4)     (5,5)
    Repeat.                                                                                    (3,0)

    Since we need to print a program of length 16, A needs to have 16 3-bit numbers.
    '''
    def make_RA(l):
        n = 0
        for i in l:
            n = (n << 3) + i
        return n
    
    def read_literal_operand():
        nonlocal pointer
        v = program[pointer]
        pointer += 1
        return v
    
    def read_combo_operand():
        nonlocal pointer
        v = program[pointer]
        pointer += 1
        match v:
            case 0 | 1 | 2 | 3:
                return v
            case 4:
                return RA
            case 5:
                return RB
            case 6:
                return RC
            case 7:
                raise Exception("Illegal combo operand")
            case _:
                raise Exception(f"Unknown operand {v}")
    
    def run_instruction():
        nonlocal pointer, RA, RB, RC
        v = program[pointer]
        pointer += 1
        match v:
            case 0: # adv   : RA >> c_operand
                operand = read_combo_operand()
                RA = RA // (2 ** operand)
            case 1: # bxl   : RB ^ l_operand
                operand = read_literal_operand()
                RB = RB ^ operand
            case 2: # bst   : RB = c_operand % 8
                operand = read_combo_operand()
                RB = operand % 8
            case 3: # jnz   : jump to l_oeprand if RA not 0
                if RA == 0:
                    pointer += 1
                else:
                    operand = read_literal_operand()
                    pointer = operand
            case 4: # bxc   : RB ^ RC
                pointer += 1
                RB = RB ^ RC
            case 5: # out   : print(c_operand % 8)
                operand = read_combo_operand()
                output.append(operand % 8)
            case 6: # bdv   : RB >> c_operand
                operand = read_combo_operand()
                RB = RA // (2 ** operand)
            case 7: # cdv   : RC >> c_operand
                operand = read_combo_operand()
                RC = RA // (2 ** operand)
            case _:
                raise Exception(f"Unknown instruction {v}")

    program = [2,4,1,7,7,5,0,3,4,4,1,7,5,5,3,0]
    PTR_LIMIT = len(program)
    values = [i for i in range(8)]
    frontier = set()
    frontier.add((7,)) # First number has to be 7 so that it can output 0 as the last number of the program
    for index in range(PTR_LIMIT-1): # We need 15 more numbers
        new_frontier = set()
        for nums in frontier:
            for x in values:
                new_num = (*nums, x)
                RA = make_RA(new_num)
                RB = RC = 0
                pointer = 0
                output = []
                while pointer < PTR_LIMIT:
                    run_instruction()
                if output == program[PTR_LIMIT - 2 - index:]:
                    new_frontier.add(new_num)
        frontier = new_frontier
    return min(list(map(make_RA, frontier)))
    
print(solve_part_2())
