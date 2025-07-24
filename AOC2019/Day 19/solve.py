def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

DATA = {k: int(v) for k, v in enumerate(read_input_file_data().split(','))}

def drone_system(x, y):
    program = DATA.copy()
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

    is_X = True
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
                program[a] = x if is_X else y
                is_X = False
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
                return outputs[0]

def solve_part_1():
    count = 0
    for x in range(50):
        for y in range(50):
            if drone_system(x, y):
                count += 1
    return count

def solve_part_2():
    # # Inspect shape
    # grids = [['.'] * 50 for _ in range(50)]
    # for x in range(50):
    #     for y in range(50):
    #         if drone_system(x, y):
    #             grids[y][x] = '#'
    # for line in grids:
    #     print(''.join(line))
    '''
    From the print, we can see that the ratio of y to x is roughly 2:1.
    We should first find a good estimate of the possible range where
    the 100*100 can fit, then we tweak it back towards the origin.
    '''
    def can_fit(x, y):
        return drone_system(x, y) and drone_system(x+99, y+99) and drone_system(x+99, y) and drone_system(x, y+99)
    
    # Find a spot where spaceship can fit
    n = 1
    while not can_fit(n, 2*n):
        n *= 2
    # Find a more fine tuned spot where the spaceship can fit
    low = n // 2
    high = n
    while high - low > 1:
        mid = (low + high) // 2
        if can_fit(mid, 2*mid):
            high = mid
        else:
            low = mid
    # Find precise spot
    x, y = high, 2*high
    while True:
        if can_fit(x-1, y-2):
            x -= 1
            y -= 2
        elif can_fit(x-1, y):
            x -= 1
        elif can_fit(x, y-1):
            y -= 1
        else:
            return x * 10000 + y
    
print(solve_part_2())
