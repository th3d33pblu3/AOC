def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def run_program(initial_value, loop_threshold):
    '''
    cpy a d
    cpy 7 c
        # initialize c and d to 7 and a

    cpy 362 b  # P2
    inc d
    dec b
    jnz b -2
    dec c
    jnz c -5
        # d += b * c
        # clears b and c

    cpy d a
    jnz 0 0
    cpy a b    # P1
    cpy 0 a
        # copy d into b
        # clears a

    cpy 2 c
    jnz b 2
    jnz 1 6
    dec b
    dec c
    jnz c -4
    inc a
    jnz 1 -7
        # a += b//2
        # c = 2 if b % 2 == 0 else 1
        # clears b

    cpy 2 b
    jnz c 2
    jnz 1 4
    dec b
    dec c
    jnz 1 -4
    jnz 0 0
    out b
        # output c % 2
        # clears c

    jnz a -19  # goto P1
    jnz 1 -21  # goto P2
    '''
    registers = {'a': initial_value, 'b': 0, 'c': 0, 'd': 0}
    lines = read_input_file_data().splitlines()
    instruction_ptr = 0

    def get_value(s):
        if s in "abcd":
            return registers[s]
        else:
            return int(s)

    expected_output = 0
    def match_output(output):
        nonlocal expected_output, loop_threshold
        if output != expected_output:
            return False
        expected_output = 0 if expected_output else 1 # flip 0 and 1
        loop_threshold -= 1
        return True

    while instruction_ptr < len(lines):
        # Optimization
        if instruction_ptr == 2:
            registers['d'] += 362 * registers['c']
            registers['b'] = 0
            registers['c'] = 0
            instruction_ptr = 8
            continue
        if instruction_ptr == 12:
            registers['a'] += registers['b'] // 2
            registers['c'] = 2 if registers['b'] % 2 == 0 else 1
            registers['b'] = 0
            instruction_ptr = 20
            continue
        if instruction_ptr == 20:
            # print(registers['c'] % 2, end='')
            result = match_output(registers['c'] % 2)
            if not result:
                return False
            if result and loop_threshold == 0:
                return True
            
            registers['c'] = 0
            instruction_ptr = 28
            continue

        words = lines[instruction_ptr].split()
        if words[0] == 'cpy':
            registers[words[2]] = get_value(words[1])
        elif words[0] == 'inc':
            registers[words[1]] += 1
        elif words[0] == 'dec':
            registers[words[1]] -= 1
        elif words[0] == 'jnz':
            if get_value(words[1]) != 0:
                instruction_ptr += get_value(words[2])
                continue
        elif words[0] == 'out':
            # print(f"{registers['b']}", end='')
            result = match_output(registers['b'])
            if not result:
                return False
            if result and loop_threshold == 0:
                return True
        instruction_ptr += 1

def solve():
    a = 1
    while True:
        if run_program(a, 100):
            print(a)
            break
        a += 1
    
solve()
