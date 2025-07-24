import sys

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4

def solve_part_1():
    # Repair droid program
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

    def get_output(input):
        nonlocal program, pointer, relative_base
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
                    program[a] = input
                case 4: # 04: output(a)
                    # Taking parameters
                    mode1 = (instruction % 1000) // 100
                    a = get_param_with_mode(mode1)
                    pointer += 1
                    # Performing operation
                    return a # return output
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
                    break

    def reverse(direction):
        if direction == NORTH:
            return SOUTH
        elif direction == SOUTH:
            return NORTH
        elif direction == WEST:
            return EAST
        elif direction == EAST:
            return WEST
        else:
            raise Exception(f"Unknown direciton {direction}")

    # Explore area
    starting_loc = (0, 0)
    area_map = {} # (x, y): [north, south, west, east]
    oxygen_system_loc = None
    DIRECTIONS = [NORTH, SOUTH, WEST, EAST]
    DELTAS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def explore(location):
        nonlocal area_map, oxygen_system_loc
        if location in area_map:
            return
        area_map[location] = [False, False, False, False]
        for i, direction in enumerate(DIRECTIONS):
            output = get_output(direction)
            match output:
                case 0:
                    continue
                case 1:
                    area_map[location][i] = True
                    new_loc = (location[0] + DELTAS[i][0], location[1] + DELTAS[i][1])
                    explore(new_loc)
                    get_output(reverse(direction))
                case 2:
                    area_map[location][i] = True
                    new_loc = (location[0] + DELTAS[i][0], location[1] + DELTAS[i][1])
                    oxygen_system_loc = new_loc
                    explore(new_loc)
                    get_output(reverse(direction))

    explore(starting_loc)

    # Find shortest dist to oxygen system
    dist = 0
    visited = set()
    frontier = set()
    frontier.add(starting_loc)
    while frontier:
        if oxygen_system_loc in frontier:
            return dist
        dist += 1
        new_frontier = set()
        for location in frontier:
            for i, _ in enumerate(DIRECTIONS):
                if area_map[location][i]:
                    new_loc = (location[0] + DELTAS[i][0], location[1] + DELTAS[i][1])
                    if new_loc not in visited:
                        new_frontier.add(new_loc)
        visited.update(frontier)
        frontier = new_frontier

def solve_part_2():
    # Repair droid program
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

    def get_output(input):
        nonlocal program, pointer, relative_base
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
                    program[a] = input
                case 4: # 04: output(a)
                    # Taking parameters
                    mode1 = (instruction % 1000) // 100
                    a = get_param_with_mode(mode1)
                    pointer += 1
                    # Performing operation
                    return a # return output
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
                    break

    def reverse(direction):
        if direction == NORTH:
            return SOUTH
        elif direction == SOUTH:
            return NORTH
        elif direction == WEST:
            return EAST
        elif direction == EAST:
            return WEST
        else:
            raise Exception(f"Unknown direciton {direction}")

    # Explore area
    starting_loc = (0, 0)
    area_map = {} # (x, y): [north, south, west, east]
    oxygen_system_loc = None
    DIRECTIONS = [NORTH, SOUTH, WEST, EAST]
    DELTAS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def explore(location):
        nonlocal area_map, oxygen_system_loc
        if location in area_map:
            return
        area_map[location] = [False, False, False, False]
        for i, direction in enumerate(DIRECTIONS):
            output = get_output(direction)
            match output:
                case 0:
                    continue
                case 1:
                    area_map[location][i] = True
                    new_loc = (location[0] + DELTAS[i][0], location[1] + DELTAS[i][1])
                    explore(new_loc)
                    get_output(reverse(direction))
                case 2:
                    area_map[location][i] = True
                    new_loc = (location[0] + DELTAS[i][0], location[1] + DELTAS[i][1])
                    oxygen_system_loc = new_loc
                    explore(new_loc)
                    get_output(reverse(direction))

    explore(starting_loc)

    # Find shortest dist to oxygen system
    duration = 0
    visited = set()
    frontier = set()
    frontier.add(oxygen_system_loc)
    while frontier:
        new_frontier = set()
        for location in frontier:
            for i, _ in enumerate(DIRECTIONS):
                if area_map[location][i]:
                    new_loc = (location[0] + DELTAS[i][0], location[1] + DELTAS[i][1])
                    if new_loc not in visited:
                        new_frontier.add(new_loc)
        if new_frontier:
            duration += 1
        visited.update(frontier)
        frontier = new_frontier
    return duration
    
print(solve_part_2())
