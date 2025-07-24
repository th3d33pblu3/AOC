def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    NUM_COMPUTERS = 50
    program = {k: int(v) for k, v in enumerate(read_input_file_data().split(','))}

    inputs: list[list] = [[i] for i in range(NUM_COMPUTERS)]
    programs = [program.copy() for _ in range(NUM_COMPUTERS)]
    pointers = [0 for _ in range(NUM_COMPUTERS)]
    outputs: list[list] = [[] for _ in range(NUM_COMPUTERS)]
    relative_bases = [0 for _ in range(NUM_COMPUTERS)]

    def computer(id):
        nonlocal inputs, programs, pointers, outputs
        program = programs[id]
        pointer = pointers[id]
        output = outputs[id]
        relative_base = relative_bases[id]

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
                program[a] = inputs[id].pop(0) if inputs[id] else -1
            case 4: # 04: output(a)
                # Taking parameters
                mode1 = (instruction % 1000) // 100
                a = get_param_with_mode(mode1)
                pointer += 1
                # Performing operation
                output.append(a)
                if len(output) == 3:
                    i = output.pop(0)
                    x = output.pop(0)
                    y = output.pop(0)
                    if i == 255:
                        return y
                    inputs[i].append(x)
                    inputs[i].append(y)
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
                pass
        pointers[id] = pointer # Update stored pointer
        relative_bases[id] = relative_base # Update relative base

    y = None
    while y == None:
        for id in range(NUM_COMPUTERS):
            output = computer(id)
            if output != None:
                y = output
                break
    return y

def solve_part_2():
    NUM_COMPUTERS = 50
    program = {k: int(v) for k, v in enumerate(read_input_file_data().split(','))}

    inputs: list[list] = [[i] for i in range(NUM_COMPUTERS)]
    programs = [program.copy() for _ in range(NUM_COMPUTERS)]
    pointers = [0 for _ in range(NUM_COMPUTERS)]
    outputs: list[list] = [[] for _ in range(NUM_COMPUTERS)]
    relative_bases = [0 for _ in range(NUM_COMPUTERS)]
    idle_states = [False for _ in range(NUM_COMPUTERS)]

    NAT = [-1, -1]

    def computer(id):
        nonlocal inputs, programs, pointers, outputs, idle_states, NAT
        program = programs[id]
        pointer = pointers[id]
        output = outputs[id]
        relative_base = relative_bases[id]

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
                if not inputs[id]:
                    idle_states[id] = True
                program[a] = inputs[id].pop(0) if inputs[id] else -1
            case 4: # 04: output(a)
                # Taking parameters
                mode1 = (instruction % 1000) // 100
                a = get_param_with_mode(mode1)
                pointer += 1
                # Performing operation
                output.append(a)
                if len(output) == 3:
                    idle_states[id] = False
                    i = output.pop(0)
                    x = output.pop(0)
                    y = output.pop(0)
                    if i == 255:
                        NAT[0] = x
                        NAT[1] = y
                        # print(f"Computer {id} sent NAT a packet with X={x} Y={y}") # Debug printing message
                    else:
                        inputs[i].append(x)
                        inputs[i].append(y)
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
                pass
        pointers[id] = pointer # Update stored pointer
        relative_bases[id] = relative_base # Update relative base

    last_sent_y = None
    while True:
        for _ in range(1000):
            for id in range(NUM_COMPUTERS):
                computer(id)
        if not all(idle_states):
            continue
        # Idle, send from NAT
        if last_sent_y == NAT[1]:
            break
        inputs[0].append(NAT[0])
        inputs[0].append(NAT[1])
        last_sent_y = NAT[1]
    return last_sent_y
    
print(solve_part_2())
