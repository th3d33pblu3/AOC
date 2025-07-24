def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

EMPTY = 0
WALL = 1
BLOCK = 2
PADDLE = 3
BALL = 4

def run_software():
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
                program[a] = input
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
                return outputs

def solve_part_1():
    outputs = run_software()
    grids = [(outputs[i], outputs[i+1], outputs[i+2]) for i in range(0, len(outputs), 3)]
    block_tiles = list(filter(lambda tile: tile[2] == BLOCK, grids))
    return len(block_tiles)

# def play_game():
#     program = {k: int(v) for k, v in enumerate(read_input_file_data().split(','))}
#     program[0] = 2 # Set to 2 to play for free
#     pointer = 0
#     relative_base = 0

#     def get_param_with_mode(mode):
#         match mode:
#             case 0:
#                 return program.get(program.get(pointer, 0), 0)
#             case 1:
#                 return program.get(pointer, 0)
#             case 2:
#                 return program.get(program.get(pointer, 0) + relative_base, 0)
#             case _:
#                 raise Exception("Unknown parameter mode")

#     # Setting up display
#     TILES = [' ', '#', '*', '-', 'o'] # empty, wall, block, paddle, ball
#     display = [[TILES[EMPTY]] * 37 for x in range(20)] # Size of display is 20 by 37
#     def print_display():
#         for line in display:
#             print(''.join(line))

#     score = 0
#     outputs = []
#     while True:
#         instruction = program[pointer]
#         pointer += 1
#         match instruction % 100:
#             case 1: # 01: add(a, b) -> c
#                 # Taking parameters
#                 mode1 = (instruction % 1000) // 100
#                 mode2 = (instruction % 10000) // 1000
#                 mode3 = (instruction % 100000) // 10000
#                 a = get_param_with_mode(mode1)
#                 pointer += 1
#                 b = get_param_with_mode(mode2)
#                 pointer += 1
#                 c = program[pointer] if mode3 == 0 else program[pointer] + relative_base
#                 pointer += 1
#                 # Performing operation
#                 program[c] = a + b
#             case 2: # 02: multiply(a, c) -> c
#                 # Taking parameters
#                 mode1 = (instruction % 1000) // 100
#                 mode2 = (instruction % 10000) // 1000
#                 mode3 = (instruction % 100000) // 10000
#                 a = get_param_with_mode(mode1)
#                 pointer += 1
#                 b = get_param_with_mode(mode2)
#                 pointer += 1
#                 c = program[pointer] if mode3 == 0 else program[pointer] + relative_base
#                 pointer += 1
#                 # Performing operation
#                 program[c] = a * b
#             case 3: # 03: input -> a
#                 # Taking parameters
#                 mode1 = (instruction % 1000) // 100
#                 a = program[pointer] if mode1 == 0 else program[pointer] + relative_base
#                 pointer += 1
#                 # Performing operation
#                 print_display()
#                 print(f"Current score: {score}")
#                 i = input("x for neutral, < to move left, > to move right\n")
#                 if i == 'x':
#                     program[a] = 0
#                 elif i == '<':
#                     program[a] = -1
#                 elif i == '>':
#                     program[a] = 1
#                 else:
#                     print(f"Invalid input {i}")
#                     return
#             case 4: # 04: output(a)
#                 # Taking parameters
#                 mode1 = (instruction % 1000) // 100
#                 a = get_param_with_mode(mode1)
#                 pointer += 1
#                 # Performing operation
#                 outputs.append(a)
#                 # Check output
#                 if len(outputs) == 3:
#                     x, y, n = outputs
#                     if (x, y) == (-1, 0): # update score
#                         score = n
#                     else:
#                         display[y][x] = TILES[n] # update tile
#                     outputs = []
#             case 5: # 05: jump-if-true
#                 # Taking parameters
#                 mode1 = (instruction % 1000) // 100
#                 mode2 = (instruction % 10000) // 1000
#                 a = get_param_with_mode(mode1)
#                 pointer += 1
#                 b = get_param_with_mode(mode2)
#                 pointer += 1
#                 # Performing operation
#                 if (a != 0):
#                     pointer = b
#             case 6: # 06: jump-if-false
#                 # Taking parameters
#                 mode1 = (instruction % 1000) // 100
#                 mode2 = (instruction % 10000) // 1000
#                 a = get_param_with_mode(mode1)
#                 pointer += 1
#                 b = get_param_with_mode(mode2)
#                 pointer += 1
#                 # Performing operation
#                 if (a == 0):
#                     pointer = b
#             case 7: # 07: a < b
#                 # Taking parameters
#                 mode1 = (instruction % 1000) // 100
#                 mode2 = (instruction % 10000) // 1000
#                 mode3 = (instruction % 100000) // 10000
#                 a = get_param_with_mode(mode1)
#                 pointer += 1
#                 b = get_param_with_mode(mode2)
#                 pointer += 1
#                 c = program[pointer] if mode3 == 0 else program[pointer] + relative_base
#                 pointer += 1
#                 # Performing operation
#                 program[c] = 1 if a < b else 0
#             case 8: # 08: a == b
#                 # Taking parameters
#                 mode1 = (instruction % 1000) // 100
#                 mode2 = (instruction % 10000) // 1000
#                 mode3 = (instruction % 100000) // 10000
#                 a = get_param_with_mode(mode1)
#                 pointer += 1
#                 b = get_param_with_mode(mode2)
#                 pointer += 1
#                 c = program[pointer] if mode3 == 0 else program[pointer] + relative_base
#                 pointer += 1
#                 # Performing operation
#                 program[c] = 1 if a == b else 0
#             case 9: # 09: rb += a
#                 # Taking parameters
#                 mode1 = (instruction % 1000) // 100
#                 a = get_param_with_mode(mode1)
#                 pointer += 1
#                 # Performing operation
#                 relative_base += a
#             case 99: # 99: terminate
#                 return score

def auto_play_game():
    program = {k: int(v) for k, v in enumerate(read_input_file_data().split(','))}
    program[0] = 2 # Set to 2 to play for free
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

    # Track ball and paddle
    paddle_pos = None
    ball_pos = None

    score = 0
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
                if ball_pos[0] < paddle_pos[0]:
                    program[a] = -1
                elif ball_pos[0] > paddle_pos[0]:
                    program[a] = 1
                else:
                    program[a] = 0
            case 4: # 04: output(a)
                # Taking parameters
                mode1 = (instruction % 1000) // 100
                a = get_param_with_mode(mode1)
                pointer += 1
                # Performing operation
                outputs.append(a)
                # Check output
                if len(outputs) == 3:
                    x, y, n = outputs
                    if (x, y) == (-1, 0): # update score
                        score = n
                    else:
                        if n == PADDLE: # track paddle
                            paddle_pos = (x, y)
                        elif n == BALL: # track ball
                            ball_pos = (x, y)
                    outputs = [] # clear output
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
                return score

def solve_part_2():
    return auto_play_game()
    
print(solve_part_2())
