def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    registers = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
    lines = read_input_file_data().splitlines()
    length = len(lines)
    toggled = [False for _ in range(length)]
    instruction_ptr = 0

    def get_value(s):
        if s in "abcd":
            return registers[s]
        else:
            return int(s)

    while instruction_ptr < length:
        words = lines[instruction_ptr].split()
        if not toggled[instruction_ptr]: # Untoggled instructions
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
            elif words[0] == 'tgl':
                i = get_value(words[1]) + instruction_ptr
                if i < 0 or i >= length: # Continue if out of range
                    instruction_ptr += 1
                    continue
                toggled[i] = not toggled[i]
        else: # Toggled instructions
            # one-argument
            if words[0] == 'inc':
                registers[words[1]] -= 1
            elif words[0] == 'dec':
                registers[words[1]] += 1
            elif words[0] == 'tgl':
                registers[words[1]] += 1
            # two-argument
            elif words[0] == 'jnz':
                if words[2] not in "abcd": # Skip invalid instruction
                    instruction_ptr += 1
                    continue
                registers[words[2]] = get_value(words[1])
            elif words[0] == 'cpy':
                if get_value(words[1]) != 0:
                    instruction_ptr += get_value(words[2])
                    continue
        instruction_ptr += 1
    
    return registers['a']

def solve_part_2():
    '''
    cpy a b
    dec b
    cpy a d
    cpy 0 a
    cpy b c
    inc a
    dec c
    jnz c -2 # copy c into a
    dec d
    jnz d -5 # add d*b into a
    dec b
    cpy b c
    cpy c d # set b-1 into b, c and d
    dec d
    inc c
    jnz d -2 # add d into c
    tgl c
    cpy -16 c
    jnz 1 c
    cpy 90 c
    jnz 81 d
    inc a
    inc d
    jnz d -2
    inc c
    jnz c -5
    '''
    registers = {'a': 12, 'b': 0, 'c': 0, 'd': 0}
    lines = read_input_file_data().splitlines()
    length = len(lines)
    toggled = [False for _ in range(length)]
    instruction_ptr = 0

    def get_value(s):
        if s in "abcd":
            return registers[s]
        else:
            return int(s)

    while instruction_ptr < length:
        # Optimization lines 4-9 using multiply
        if instruction_ptr == 4 and not toggled[4] and not toggled[5] and not toggled[6] and not toggled[7] and not toggled[8] and not toggled[9]:
            # add b * d into a then set c and d to 0
            registers['a'] += registers['b'] * registers['d']
            registers['c'] = 0
            registers['d'] = 0
            instruction_ptr = 10
            continue

        words = lines[instruction_ptr].split()
        if not toggled[instruction_ptr]: # Untoggled instructions
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
            elif words[0] == 'tgl':
                i = get_value(words[1]) + instruction_ptr
                if i < 0 or i >= length: # Continue if out of range
                    instruction_ptr += 1
                    continue
                toggled[i] = not toggled[i]
        else: # Toggled instructions
            # one-argument
            if words[0] == 'inc':
                registers[words[1]] -= 1
            elif words[0] == 'dec':
                registers[words[1]] += 1
            elif words[0] == 'tgl':
                registers[words[1]] += 1
            # two-argument
            elif words[0] == 'jnz':
                if words[2] not in "abcd": # Skip invalid instruction
                    instruction_ptr += 1
                    continue
                registers[words[2]] = get_value(words[1])
            elif words[0] == 'cpy':
                if get_value(words[1]) != 0:
                    instruction_ptr += get_value(words[2])
                    continue
        instruction_ptr += 1
    
    return registers['a']
    
print(solve_part_2())
