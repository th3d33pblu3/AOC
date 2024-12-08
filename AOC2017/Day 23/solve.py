import re

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    instructions = read_input_file_data().splitlines()
    LIMIT = len(instructions)
    registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}
    ptr = 0

    def get_value(r: str):
        if re.match('^[-]?[0-9]+$', r):
            return int(r)
        else:
            return registers.get(r, 0)

    mul_count = 0
    while ptr < LIMIT:
        ins, X, Y = instructions[ptr].split()
        match ins:
            case 'set':
                registers[X] = get_value(Y)
            case 'sub':
                registers[X] -= get_value(Y)
            case 'mul':
                registers[X] *= get_value(Y)
                mul_count += 1
            case 'jnz':
                if get_value(X) != 0:
                    ptr += get_value(Y)
                    continue
        ptr += 1
    return mul_count

def solve_part_2():
    instructions = read_input_file_data().splitlines()
    LIMIT = len(instructions)
    registers = {'a': 1, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}
    ptr = 0

    def get_value(r: str):
        if re.match('^[-]?[0-9]+$', r):
            return int(r)
        else:
            return registers.get(r, 0)

    '''
    set b 81
    set c b
    jnz a 2
    jnz 1 5
    mul b 100
    add b +100000
    set c b
    add c +17000
    # a=1, b=108100, c=125100

    set f 1     # (3) [line  8]
    set d 2
    set e 2     # (2) [line 10]
    set g d     # (1) [line 11]
    mul g e
    sub g b
    jnz g 2     # if g == 0: set f=0 
    set f 0     # if d is factor of b (and d != b): set f = 0
    add e +1
    set g e
    sub g b
    jnz g -8    # GOTO (1) [g != 0]

    add d +1    # [line 20]
    set g d
    sub g b
    jnz g -13   # GOTO (2) [g != 0] 

    jnz f 2
    add h +1

    set g b
    sub g c
    jnz g 2     # Continue [g != 0]
    jnz 1 3     # Exit
    add b +17
    jnz 1 -23   # GOTO (3)
    '''
    while ptr < LIMIT:
        # Optimization
        if ptr == 0:
            assert registers['a'] == 1
            registers['b'] = 108100
            registers['c'] = 125100
            ptr = 8
            continue
        if ptr == 11:
            b = registers['b']
            for d in range(registers['d'], b): # lines 20-23
                if b / d == b // d and b != d:
                    registers['f'] = 0 # if d is a factor of b (and b != d)
                    break
            registers['e'] = registers['b']
            registers['g'] = 0
            registers['d'] = registers['b'] - 1 # lines 20-23
            ptr = 24
            continue

        ins, X, Y = instructions[ptr].split()
        match ins:
            case 'set':
                registers[X] = get_value(Y)
            case 'sub':
                registers[X] -= get_value(Y)
            case 'mul':
                registers[X] *= get_value(Y)
            case 'jnz':
                if get_value(X) != 0:
                    ptr += get_value(Y)
                    continue
        ptr += 1
    return registers['h']
    
print(solve_part_2())
