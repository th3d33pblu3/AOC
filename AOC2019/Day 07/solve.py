from itertools import permutations

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    PROGRAM = {k: int(v) for k, v in enumerate(read_input_file_data().split(','))}
    def computer(ps, input):
        program = PROGRAM.copy()
        input_src = 0
        pointer = 0
        outputs = []
        while True:
            instruction = program[pointer]
            pointer += 1
            match instruction % 100:
                case 1: # 01: add(a, b) -> c
                    # Taking inputs
                    mode1 = (instruction % 1000) // 100
                    mode2 = (instruction % 10000) // 1000
                    a = program[pointer] if mode1 else program[program[pointer]]
                    pointer += 1
                    b = program[pointer] if mode2 else program[program[pointer]]
                    pointer += 1
                    c = program[pointer]
                    pointer += 1
                    # Performing operation
                    program[c] = a + b
                case 2: # 02: multiply(a, c) -> c
                    # Taking inputs
                    mode1 = (instruction % 1000) // 100
                    mode2 = (instruction % 10000) // 1000
                    a = program[pointer] if mode1 else program[program[pointer]]
                    pointer += 1
                    b = program[pointer] if mode2 else program[program[pointer]]
                    pointer += 1
                    c = program[pointer]
                    pointer += 1
                    # Performing operation
                    program[c] = a * b
                case 3: # 03: input(a)
                    # Taking inputs
                    a = program[pointer]
                    pointer += 1
                    # Performing operation
                    if input_src == 0:
                        program[a] = ps
                        input_src += 1
                    elif input_src == 1:
                        program[a] = input
                        input_src += 1
                    else:
                        raise Exception("Too many inputs required")
                case 4: # 04: output(a)
                    # Taking inputs
                    mode1 = (instruction % 1000) // 100
                    a = program[pointer] if mode1 else program[program[pointer]]
                    pointer += 1
                    # Performing operation
                    outputs.append(a)
                case 5: # 05: jump-if-true
                    # Taking inputs
                    mode1 = (instruction % 1000) // 100
                    mode2 = (instruction % 10000) // 1000
                    a = program[pointer] if mode1 else program[program[pointer]]
                    pointer += 1
                    b = program[pointer] if mode2 else program[program[pointer]]
                    pointer += 1
                    # Performing operation
                    if (a != 0):
                        pointer = b
                case 6: # 06: jump-if-false
                    # Taking inputs
                    mode1 = (instruction % 1000) // 100
                    mode2 = (instruction % 10000) // 1000
                    a = program[pointer] if mode1 else program[program[pointer]]
                    pointer += 1
                    b = program[pointer] if mode2 else program[program[pointer]]
                    pointer += 1
                    # Performing operation
                    if (a == 0):
                        pointer = b
                case 7: # 07: a < b
                    # Taking inputs
                    mode1 = (instruction % 1000) // 100
                    mode2 = (instruction % 10000) // 1000
                    a = program[pointer] if mode1 else program[program[pointer]]
                    pointer += 1
                    b = program[pointer] if mode2 else program[program[pointer]]
                    pointer += 1
                    c = program[pointer]
                    pointer += 1
                    # Performing operation
                    program[c] = 1 if a < b else 0
                case 8: # 08: a == b
                    # Taking inputs
                    mode1 = (instruction % 1000) // 100
                    mode2 = (instruction % 10000) // 1000
                    a = program[pointer] if mode1 else program[program[pointer]]
                    pointer += 1
                    b = program[pointer] if mode2 else program[program[pointer]]
                    pointer += 1
                    c = program[pointer]
                    pointer += 1
                    # Performing operation
                    program[c] = 1 if a == b else 0
                case 99: # 99: terminate
                    return outputs[-1]

    perms = permutations([0, 1, 2, 3, 4])

    max_thrusters = float("-inf")
    best_settings = ()

    for perm in list(perms):
        a, b, c, d, e = perm
        thruster = computer(e, computer(d, computer(c, computer(b, computer(a, 0)))))
        if thruster > max_thrusters:
            max_thrusters = thruster
            best_settings = perm
    print(best_settings)
    return max_thrusters

def solve_part_2():
    PROGRAM = {k: int(v) for k, v in enumerate(read_input_file_data().split(','))}
    perms = permutations(range(5, 10))
    max_thrusters = float("-inf")
    best_settings = ()
    for perm in list(perms):
        a, b, c, d, e = perm
        # Initialize programs and pointers
        programs = [PROGRAM.copy() for _ in range(5)]
        program_pointers = [0] * 5
        inputs: list[list] = [[a, 0], [b], [c], [d], [e]]
        input_save_addresses = [-1] * 5
        waiting = [False] * 5
        terminated = [False] * 5

        def computer(i):
            program = programs[i]
            input: list = inputs[i]
            output: list = inputs[(i + 1) % 5]

            if terminated[i]:
                raise Exception("Terminated computer")
            if waiting[i]:
                if len(inputs[i]) == 0:
                    raise Exception("No more inputs")
                waiting[i] = False
                program[input_save_addresses[i]] = input.pop(0)

            while True:
                instruction = program[program_pointers[i]]
                program_pointers[i] += 1
                match instruction % 100:
                    case 1: # 01: add(a, b) -> c
                        # Taking inputs
                        mode1 = (instruction % 1000) // 100
                        mode2 = (instruction % 10000) // 1000
                        a = program[program_pointers[i]] if mode1 else program[program[program_pointers[i]]]
                        program_pointers[i] += 1
                        b = program[program_pointers[i]] if mode2 else program[program[program_pointers[i]]]
                        program_pointers[i] += 1
                        c = program[program_pointers[i]]
                        program_pointers[i] += 1
                        # Performing operation
                        program[c] = a + b
                    case 2: # 02: multiply(a, c) -> c
                        # Taking inputs
                        mode1 = (instruction % 1000) // 100
                        mode2 = (instruction % 10000) // 1000
                        a = program[program_pointers[i]] if mode1 else program[program[program_pointers[i]]]
                        program_pointers[i] += 1
                        b = program[program_pointers[i]] if mode2 else program[program[program_pointers[i]]]
                        program_pointers[i] += 1
                        c = program[program_pointers[i]]
                        program_pointers[i] += 1
                        # Performing operation
                        program[c] = a * b
                    case 3: # 03: input(a)
                        # Taking inputs
                        a = program[program_pointers[i]]
                        program_pointers[i] += 1
                        # Performing operation
                        try:
                            input_value = input.pop(0)
                            program[a] = input_value
                        except(IndexError):
                            input_save_addresses[i] = a
                            waiting[i] = True
                            return
                    case 4: # 04: output(a)
                        # Taking inputs
                        mode1 = (instruction % 1000) // 100
                        a = program[program_pointers[i]] if mode1 else program[program[program_pointers[i]]]
                        program_pointers[i] += 1
                        # Performing operation
                        output.append(a)
                    case 5: # 05: jump-if-true
                        # Taking inputs
                        mode1 = (instruction % 1000) // 100
                        mode2 = (instruction % 10000) // 1000
                        a = program[program_pointers[i]] if mode1 else program[program[program_pointers[i]]]
                        program_pointers[i] += 1
                        b = program[program_pointers[i]] if mode2 else program[program[program_pointers[i]]]
                        program_pointers[i] += 1
                        # Performing operation
                        if (a != 0):
                            program_pointers[i] = b
                    case 6: # 06: jump-if-false
                        # Taking inputs
                        mode1 = (instruction % 1000) // 100
                        mode2 = (instruction % 10000) // 1000
                        a = program[program_pointers[i]] if mode1 else program[program[program_pointers[i]]]
                        program_pointers[i] += 1
                        b = program[program_pointers[i]] if mode2 else program[program[program_pointers[i]]]
                        program_pointers[i] += 1
                        # Performing operation
                        if (a == 0):
                            program_pointers[i] = b
                    case 7: # 07: a < b
                        # Taking inputs
                        mode1 = (instruction % 1000) // 100
                        mode2 = (instruction % 10000) // 1000
                        a = program[program_pointers[i]] if mode1 else program[program[program_pointers[i]]]
                        program_pointers[i] += 1
                        b = program[program_pointers[i]] if mode2 else program[program[program_pointers[i]]]
                        program_pointers[i] += 1
                        c = program[program_pointers[i]]
                        program_pointers[i] += 1
                        # Performing operation
                        program[c] = 1 if a < b else 0
                    case 8: # 08: a == b
                        # Taking inputs
                        mode1 = (instruction % 1000) // 100
                        mode2 = (instruction % 10000) // 1000
                        a = program[program_pointers[i]] if mode1 else program[program[program_pointers[i]]]
                        program_pointers[i] += 1
                        b = program[program_pointers[i]] if mode2 else program[program[program_pointers[i]]]
                        program_pointers[i] += 1
                        c = program[program_pointers[i]]
                        program_pointers[i] += 1
                        # Performing operation
                        program[c] = 1 if a == b else 0
                    case 99: # 99: terminate
                        terminated[i] = True
                        return
        
        amp = 0
        while not terminated[4]:
            computer(amp)
            amp = (amp + 1) % 5
        thruster = inputs[0][-1]
        if thruster > max_thrusters:
            max_thrusters = thruster
            best_settings = perm
    
    print(best_settings)
    return max_thrusters
    
print(solve_part_2())
