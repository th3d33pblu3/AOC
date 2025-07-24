def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

BLACK = 0
WHITE = 1
DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0)) # UP, RIGHT, DOWN, LEFT

painted_grids = {}
direction = 0
location = (0, 0)

def run_robot():
    global BLACK, WHITE, DIRECTIONS, painted_grids, direction, location

    program = {k: int(v) for k, v in enumerate(read_input_file_data().split(','))}
    LEN = len(program)
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

    is_paint = True
    while pointer < LEN:
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
                program[a] = painted_grids.get(location, BLACK)
            case 4: # 04: output(a)
                # Taking parameters
                mode1 = (instruction % 1000) // 100
                a = get_param_with_mode(mode1)
                pointer += 1
                # Performing operation
                if is_paint:
                    assert a in (0, 1)
                    painted_grids[location] = a # Paint
                    is_paint = False
                else:
                    assert a in (0, 1)
                    if a == 0:
                        direction = (direction - 1) % 4 # Turn left
                    else:
                        direction = (direction + 1) % 4 # Turn right
                    location = (location[0] + DIRECTIONS[direction][0], location[1] + DIRECTIONS[direction][1]) # Move
                    is_paint = True
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
                return
            


def solve_part_1():
    global painted_grids
    run_robot()
    return len(painted_grids)

def solve_part_2():
    global painted_grids
    painted_grids[(0, 0)] = 1 # Start on white
    run_robot()

    # Draw letters
    minx = min([pt[0] for pt in painted_grids])
    maxx = max([pt[0] for pt in painted_grids])
    miny = min([pt[1] for pt in painted_grids])
    maxy = max([pt[1] for pt in painted_grids])

    dx = maxx-minx+1
    dy = maxy-miny+1
    grids = [['.'] * dx for _ in range(dy)]
    for y in range(dy):
        for x in range(dx):
            grids[y][x] = '#' if painted_grids.get((x-minx, maxy-y), BLACK) else ' '
    for row in grids:
        print(''.join(row))
    
print(solve_part_2())
