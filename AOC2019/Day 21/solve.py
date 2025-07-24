def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def springdroid(input: list):
    program = {k: int(v) for k, v in enumerate(read_input_file_data().split(','))}
    pointer = 0
    relative_base = 0

    def get_param_with_mode(mode):
        match mode:
            case 0:
                return program.get(program.get(pointer, 0), 0)
            case 1:
                return program.get(pointer, 0)
            case 2:
                return program.get(program.get(pointer, 0) + relative_base, 0)
            case _:
                raise Exception("Unknown parameter mode")

    outputs = []
    while True:
        instruction = program[pointer]
        pointer += 1
        match instruction % 100:
            case 1: # 01: add(a, b) -> c
                # Taking parameters
                mode1 = (instruction % 1000) // 100
                mode2 = (instruction % 10000) // 1000
                mode3 = (instruction % 100000) // 10000
                a = get_param_with_mode(mode1)
                pointer += 1
                b = get_param_with_mode(mode2)
                pointer += 1
                c = program[pointer] if mode3 == 0 else program[pointer] + relative_base
                pointer += 1
                # Performing operation
                program[c] = a + b
            case 2: # 02: multiply(a, c) -> c
                # Taking parameters
                mode1 = (instruction % 1000) // 100
                mode2 = (instruction % 10000) // 1000
                mode3 = (instruction % 100000) // 10000
                a = get_param_with_mode(mode1)
                pointer += 1
                b = get_param_with_mode(mode2)
                pointer += 1
                c = program[pointer] if mode3 == 0 else program[pointer] + relative_base
                pointer += 1
                # Performing operation
                program[c] = a * b
            case 3: # 03: input -> a
                # Taking parameters
                mode1 = (instruction % 1000) // 100
                a = program[pointer] if mode1 == 0 else program[pointer] + relative_base
                pointer += 1
                # Performing operation
                if outputs:
                    print(''.join(map(chr, outputs)))
                    outputs = []
                program[a] = input.pop(0)
            case 4: # 04: output(a)
                # Taking parameters
                mode1 = (instruction % 1000) // 100
                a = get_param_with_mode(mode1)
                pointer += 1
                # Performing operation
                outputs.append(a)
            case 5: # 05: jump-if-true
                # Taking parameters
                mode1 = (instruction % 1000) // 100
                mode2 = (instruction % 10000) // 1000
                a = get_param_with_mode(mode1)
                pointer += 1
                b = get_param_with_mode(mode2)
                pointer += 1
                # Performing operation
                if (a != 0):
                    pointer = b
            case 6: # 06: jump-if-false
                # Taking parameters
                mode1 = (instruction % 1000) // 100
                mode2 = (instruction % 10000) // 1000
                a = get_param_with_mode(mode1)
                pointer += 1
                b = get_param_with_mode(mode2)
                pointer += 1
                # Performing operation
                if (a == 0):
                    pointer = b
            case 7: # 07: a < b
                # Taking parameters
                mode1 = (instruction % 1000) // 100
                mode2 = (instruction % 10000) // 1000
                mode3 = (instruction % 100000) // 10000
                a = get_param_with_mode(mode1)
                pointer += 1
                b = get_param_with_mode(mode2)
                pointer += 1
                c = program[pointer] if mode3 == 0 else program[pointer] + relative_base
                pointer += 1
                # Performing operation
                program[c] = 1 if a < b else 0
            case 8: # 08: a == b
                # Taking parameters
                mode1 = (instruction % 1000) // 100
                mode2 = (instruction % 10000) // 1000
                mode3 = (instruction % 100000) // 10000
                a = get_param_with_mode(mode1)
                pointer += 1
                b = get_param_with_mode(mode2)
                pointer += 1
                c = program[pointer] if mode3 == 0 else program[pointer] + relative_base
                pointer += 1
                # Performing operation
                program[c] = 1 if a == b else 0
            case 9: # 09: rb += a
                # Taking parameters
                mode1 = (instruction % 1000) // 100
                a = get_param_with_mode(mode1)
                pointer += 1
                # Performing operation
                relative_base += a
            case 99: # 99: terminate
                print(''.join(map(chr, outputs[:-1] if outputs[-1] > 127 else outputs)))
                return outputs[-1]

def interactive_springdroid():
    program = {k: int(v) for k, v in enumerate(read_input_file_data().split(','))}
    pointer = 0
    relative_base = 0

    def get_param_with_mode(mode):
        match mode:
            case 0:
                return program.get(program.get(pointer, 0), 0)
            case 1:
                return program.get(pointer, 0)
            case 2:
                return program.get(program.get(pointer, 0) + relative_base, 0)
            case _:
                raise Exception("Unknown parameter mode")

    inputs = []
    outputs = []
    while True:
        instruction = program[pointer]
        pointer += 1
        match instruction % 100:
            case 1: # 01: add(a, b) -> c
                # Taking parameters
                mode1 = (instruction % 1000) // 100
                mode2 = (instruction % 10000) // 1000
                mode3 = (instruction % 100000) // 10000
                a = get_param_with_mode(mode1)
                pointer += 1
                b = get_param_with_mode(mode2)
                pointer += 1
                c = program[pointer] if mode3 == 0 else program[pointer] + relative_base
                pointer += 1
                # Performing operation
                program[c] = a + b
            case 2: # 02: multiply(a, c) -> c
                # Taking parameters
                mode1 = (instruction % 1000) // 100
                mode2 = (instruction % 10000) // 1000
                mode3 = (instruction % 100000) // 10000
                a = get_param_with_mode(mode1)
                pointer += 1
                b = get_param_with_mode(mode2)
                pointer += 1
                c = program[pointer] if mode3 == 0 else program[pointer] + relative_base
                pointer += 1
                # Performing operation
                program[c] = a * b
            case 3: # 03: input -> a
                # Taking parameters
                mode1 = (instruction % 1000) // 100
                a = program[pointer] if mode1 == 0 else program[pointer] + relative_base
                pointer += 1
                # Performing operation
                if not inputs:
                    ascii_inputs = input(''.join(map(chr, outputs)))
                    outputs = []
                    inputs = [ord(char) for char in ascii_inputs + '\n']
                program[a] = inputs.pop(0)
            case 4: # 04: output(a)
                # Taking parameters
                mode1 = (instruction % 1000) // 100
                a = get_param_with_mode(mode1)
                pointer += 1
                # Performing operation
                outputs.append(a)
            case 5: # 05: jump-if-true
                # Taking parameters
                mode1 = (instruction % 1000) // 100
                mode2 = (instruction % 10000) // 1000
                a = get_param_with_mode(mode1)
                pointer += 1
                b = get_param_with_mode(mode2)
                pointer += 1
                # Performing operation
                if (a != 0):
                    pointer = b
            case 6: # 06: jump-if-false
                # Taking parameters
                mode1 = (instruction % 1000) // 100
                mode2 = (instruction % 10000) // 1000
                a = get_param_with_mode(mode1)
                pointer += 1
                b = get_param_with_mode(mode2)
                pointer += 1
                # Performing operation
                if (a == 0):
                    pointer = b
            case 7: # 07: a < b
                # Taking parameters
                mode1 = (instruction % 1000) // 100
                mode2 = (instruction % 10000) // 1000
                mode3 = (instruction % 100000) // 10000
                a = get_param_with_mode(mode1)
                pointer += 1
                b = get_param_with_mode(mode2)
                pointer += 1
                c = program[pointer] if mode3 == 0 else program[pointer] + relative_base
                pointer += 1
                # Performing operation
                program[c] = 1 if a < b else 0
            case 8: # 08: a == b
                # Taking parameters
                mode1 = (instruction % 1000) // 100
                mode2 = (instruction % 10000) // 1000
                mode3 = (instruction % 100000) // 10000
                a = get_param_with_mode(mode1)
                pointer += 1
                b = get_param_with_mode(mode2)
                pointer += 1
                c = program[pointer] if mode3 == 0 else program[pointer] + relative_base
                pointer += 1
                # Performing operation
                program[c] = 1 if a == b else 0
            case 9: # 09: rb += a
                # Taking parameters
                mode1 = (instruction % 1000) // 100
                a = get_param_with_mode(mode1)
                pointer += 1
                # Performing operation
                relative_base += a
            case 99: # 99: terminate
                print(''.join(map(chr, outputs[:-1] if outputs[-1] > 127 else outputs)))
                return outputs[-1]


def solve_part_1():
    # Readonly registers: A, B, C, D (each stand for 1, 2, 3, 4 grids away)
    # Writable registers: T, J
    # Instruction types : AND, OR, NOT

    # Landing spot after jump is 4 grids away
    # Jump if A/B/C is hole (False) and D is land (True)
    '''
    NOT A J
    NOT B T
    OR  T J
    NOT C T
    OR  T J
    AND D J
    WALK
    '''
    # return interactive_springdroid()
    inputs = list(map(ord, "NOT A J\nNOT B T\nOR T J\nNOT C T\nOR T J\nAND D J\nWALK\n"))
    return springdroid(inputs)

def solve_part_2():
    # Readonly registers: A, B, C, D, E, F, G, H, I (each stand for 1, 2, 3, 4, 5, 6, 7, 8, 9 grids away)
    # Writable registers: T, J
    # Instruction types : AND, OR, NOT
    '''
    CASE 1: C is False
    Jump if D and H are True

    CASE 2: B is False
    Jump if D is True

    CASE 3: A is False
    Jump

    OR the 3 cases together
    '''
    '''
    NOT C J
    AND D J
    AND H J
    NOT B T
    AND D T
    OR  T J
    NOT A T
    OR  T J
    RUN
    '''
    # return interactive_springdroid()
    inputs = list(map(ord, "NOT C J\nAND D J\nAND H J\nNOT B T\nAND D T\nOR T J\nNOT A T\nOR T J\nRUN\n"))
    return springdroid(inputs)
    
print(solve_part_2())
