def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    program = {k: int(v) for k, v in enumerate(read_input_file_data().split(','))}
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
                program[a] = 1 # Passing 1 to the input
            case 4: # 04: output(a)
                # Taking inputs
                mode1 = (instruction % 1000) // 100
                a = program[pointer] if mode1 else program[program[pointer]]
                pointer += 1
                # Performing operation
                outputs.append(a)
            case 99: # 99: terminate
                return outputs

def solve_part_2():
    program = {k: int(v) for k, v in enumerate(read_input_file_data().split(','))}
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
                program[a] = 5 # Passing 5 to the input
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
                return outputs
    
print(solve_part_2())
