import re

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def read_map_file_data() -> list:
    FILE = "puzzle_map.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def parse_instructions() -> list:
    return re.split(r'(L|R)', read_input_file_data())

class InstructionHandler:
    def __init__(self) -> None:
        self.instructions = parse_instructions()
        self.curr_index = 0
        self.max_index = len(self.instructions)
        
    def get_next_instruction(self) -> str:
        if self.curr_index == self.max_index:
            return None
        instruction = self.instructions[self.curr_index]
        self.curr_index += 1
        return instruction

PATH = "."
WALL = "#"
WARP_SPACE = " "

MAP_COLUMNS = None
MAP_ROWS = None

CUBE_MAP_SIZE = None
CUBE_MAX_INDEX = None

def parse_map():
    global MAP_COLUMNS, MAP_ROWS
    puzzle_map = []
    max_columns = 0
    for line in read_map_file_data().splitlines():
        line_map = []
        for char in line:
            if char == " ":
                line_map.append(WARP_SPACE)
            elif char == ".":
                line_map.append(PATH)
            elif char == "#":
                line_map.append(WALL)
            else:
                raise Exception(f"Unknown map marking. {char}")
        max_columns = max(max_columns, len(line_map))
        puzzle_map.append(line_map)
    for row in puzzle_map:
        if len(row) < max_columns:
            row.extend([WARP_SPACE] * (max_columns - len(row)))
    MAP_COLUMNS = max_columns
    MAP_ROWS = len(puzzle_map)
    return puzzle_map

def parse_cube_map():
    global CUBE_MAP_SIZE, CUBE_MAX_INDEX
    CUBE_MAP_SIZE = 50
    CUBE_MAX_INDEX = CUBE_MAP_SIZE - 1
    puzzle_cube_map = []
    map_data_lines = read_map_file_data().splitlines()

    face1 = []
    face2 = []
    for line in map_data_lines[: CUBE_MAP_SIZE]:
        face1.append(line[CUBE_MAP_SIZE : CUBE_MAP_SIZE * 2])
        face2.append(line[CUBE_MAP_SIZE * 2 :])
    puzzle_cube_map.append(face1)
    puzzle_cube_map.append(face2)
    
    face3 = []
    for line in map_data_lines[CUBE_MAP_SIZE : CUBE_MAP_SIZE * 2]:
        face3.append(line[CUBE_MAP_SIZE :])
    puzzle_cube_map.append(face3)

    face4 = []
    face5 = []
    for line in map_data_lines[CUBE_MAP_SIZE * 2 : CUBE_MAP_SIZE * 3]:
        face4.append(line[: CUBE_MAP_SIZE])
        face5.append(line[CUBE_MAP_SIZE :])
    puzzle_cube_map.append(face4)
    puzzle_cube_map.append(face5)

    face6 = []
    for line in map_data_lines[CUBE_MAP_SIZE * 3 :]:
        face6.append(line[:])
    puzzle_cube_map.append(face6)

    return puzzle_cube_map

cube_map_links = ((1, 2, 3, 5),
                  (4, 2, 0, 5),
                  (1, 4, 3, 0),
                  (4, 5, 0, 2),
                  (1, 5, 3, 2),
                  (4, 1, 0, 3))

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

TURN_LEFT = "L"
TURN_RIGHT = "R"

def turn_dir(curr_dir, instruction):
    if instruction == TURN_LEFT:
        return (curr_dir - 1) % 4
    elif instruction == TURN_RIGHT:
        return (curr_dir + 1) % 4
    else:
        raise Exception(f"Unknown turning direction: {instruction}")

def move(puzzle_map, curr_pos, curr_dir, steps):
    row, col = curr_pos
    if curr_dir == RIGHT:
        while steps > 0:
            next_col = (col + 1) % MAP_COLUMNS
            next_pos = puzzle_map[row][next_col]
            steps -= 1
            while next_pos == WARP_SPACE:
                next_col = (next_col + 1) % MAP_COLUMNS
                next_pos = puzzle_map[row][next_col]
            assert steps >= 0
            if next_pos == PATH:
                col = next_col
            elif next_pos == WALL:
                break
            else:
                raise Exception(f"Wrong warping.")
    elif curr_dir == DOWN:
        while steps > 0:
            next_row = (row + 1) % MAP_ROWS
            next_pos = puzzle_map[next_row][col]
            steps -= 1
            while next_pos == WARP_SPACE:
                next_row = (next_row + 1) % MAP_ROWS
                next_pos = puzzle_map[next_row][col]
            assert steps >= 0
            if next_pos == PATH:
                row = next_row
            elif next_pos == WALL:
                break
            else:
                raise Exception(f"Wrong warping.")
    elif curr_dir == LEFT:
        while steps > 0:
            next_col = (col - 1) % MAP_COLUMNS
            next_pos = puzzle_map[row][next_col]
            steps -= 1
            while next_pos == WARP_SPACE:
                next_col = (next_col - 1) % MAP_COLUMNS
                next_pos = puzzle_map[row][next_col]
            assert steps >= 0
            if next_pos == PATH:
                col = next_col
            elif next_pos == WALL:
                break
            else:
                raise Exception(f"Wrong warping.")
    elif curr_dir == UP:
        while steps > 0:
            next_row = (row - 1) % MAP_ROWS
            next_pos = puzzle_map[next_row % MAP_ROWS][col]
            steps -= 1
            while next_pos == WARP_SPACE:
                next_row = (next_row - 1) % MAP_ROWS
                next_pos = puzzle_map[next_row % MAP_ROWS][col]
            assert steps >= 0
            if next_pos == PATH:
                row = next_row
            elif next_pos == WALL:
                break
            else:
                raise Exception(f"Wrong warping.")
    else:
        raise Exception(f"Unknown direction {curr_dir}")
    return (row, col)
            
def solve_part_1():
    puzzle_map = parse_map()
    puzzle_instructions = InstructionHandler()
    curr_pos = (0, puzzle_map[0].index(PATH)) # row, column
    curr_dir = RIGHT
    instruction = puzzle_instructions.get_next_instruction()
    while instruction != None:
        if instruction.isnumeric():
            steps = int(instruction)
            curr_pos = move(puzzle_map, curr_pos, curr_dir, steps)
        else:
            curr_dir = turn_dir(curr_dir, instruction)
        instruction = puzzle_instructions.get_next_instruction()
    end_row, end_col = curr_pos
    end_dir = curr_dir
    return (end_row + 1) * 1000 + (end_col + 1) * 4 + end_dir

def get_next_pos_across_face(curr_face, curr_row, curr_col, curr_dir):
    next_connecting_face = cube_map_links[curr_face][curr_dir]
    next_connecting_dir = cube_map_links[next_connecting_face].index(curr_face)
    if curr_dir == RIGHT:
        if next_connecting_dir == RIGHT:
            next_row = CUBE_MAX_INDEX - curr_row
            next_col = CUBE_MAX_INDEX
            next_dir = LEFT
        elif next_connecting_dir == DOWN:
            next_row = CUBE_MAX_INDEX
            next_col = curr_row
            next_dir = UP
        elif next_connecting_dir == LEFT:
            next_row = curr_row
            next_col = 0
            next_dir = RIGHT
        elif next_connecting_dir == UP:
            next_row = 0
            next_col = CUBE_MAX_INDEX - curr_row
            next_dir = DOWN
    elif curr_dir == DOWN:
        if next_connecting_dir == RIGHT:
            next_row = curr_col
            next_col = CUBE_MAX_INDEX
            next_dir = LEFT
        elif next_connecting_dir == DOWN:
            next_row = CUBE_MAX_INDEX
            next_col = CUBE_MAX_INDEX - curr_col
            next_dir = UP
        elif next_connecting_dir == LEFT:
            next_row = CUBE_MAX_INDEX - curr_col
            next_col = 0
            next_dir = RIGHT
        elif next_connecting_dir == UP:
            next_row = 0
            next_col = curr_col
            next_dir = DOWN
    elif curr_dir == LEFT:
        if next_connecting_dir == RIGHT:
            next_row = curr_row
            next_col = CUBE_MAX_INDEX
            next_dir = LEFT
        elif next_connecting_dir == DOWN:
            next_row = CUBE_MAX_INDEX
            next_col = CUBE_MAX_INDEX - curr_row
            next_dir = UP
        elif next_connecting_dir == LEFT:
            next_row = CUBE_MAX_INDEX - curr_row
            next_col = 0
            next_dir = RIGHT
        elif next_connecting_dir == UP:
            next_row = 0
            next_col = curr_row
            next_dir = DOWN
    elif curr_dir == UP:
        if next_connecting_dir == RIGHT:
            next_row = CUBE_MAX_INDEX - curr_col
            next_col = CUBE_MAX_INDEX
            next_dir = LEFT
        elif next_connecting_dir == DOWN:
            next_row = CUBE_MAX_INDEX
            next_col = curr_col
            next_dir = UP
        elif next_connecting_dir == LEFT:
            next_row = curr_col
            next_col = 0
            next_dir = RIGHT
        elif next_connecting_dir == UP:
            next_row = 0
            next_col = CUBE_MAX_INDEX - curr_col
            next_dir = DOWN
    else:
        raise Exception(f"Unknown direction: {curr_dir}")
    return next_connecting_face, next_row, next_col, next_dir

def cube_move(puzzle_map, curr_face, curr_row, curr_col, curr_dir, steps):
    for _ in range(steps):
        next_face = curr_face
        next_dir = curr_dir
        if curr_dir == RIGHT:
            next_row = curr_row
            next_col = curr_col + 1
        elif curr_dir == DOWN:
            next_row = curr_row + 1
            next_col = curr_col
        elif curr_dir == LEFT:
            next_row = curr_row
            next_col = curr_col - 1
        elif curr_dir == UP:
            next_row = curr_row - 1
            next_col = curr_col
        else:
            raise Exception(f"Unknown direction: {curr_dir}") 
        if next_row < 0 or next_row >= CUBE_MAP_SIZE or next_col < 0 or next_col >= CUBE_MAP_SIZE:
            next_face, next_row, next_col, next_dir = get_next_pos_across_face(curr_face, curr_row, curr_col, curr_dir)
        if puzzle_map[next_face][next_row][next_col] == WALL:
            break
        else:
            curr_face = next_face
            curr_row = next_row
            curr_col = next_col
            curr_dir = next_dir
        
    return curr_face, curr_row, curr_col, curr_dir

class Logger:
    def __init__(self, file_name="output.txt") -> None:
        self.file_name = file_name
        self.file = None

    def log(self, data):
        self.file.write(data)

    def open(self):
        self.file = open(self.file_name, 'a')

    def close(self):
        self.file.close()

def solve_part_2():
    puzzle_instructions = InstructionHandler()
    puzzle_cube_map = parse_cube_map()
    curr_face = 0
    curr_row = 0
    curr_col = 0
    curr_dir = RIGHT
    instruction = puzzle_instructions.get_next_instruction()
    logger = Logger()
    logger.open()
    while instruction != None:
        logger.log(f"{curr_face}, {curr_row}, {curr_col}, {curr_dir}, {instruction}\n")
        if instruction.isnumeric():
            steps = int(instruction)
            curr_face, curr_row, curr_col, curr_dir = cube_move(puzzle_cube_map, curr_face, curr_row, curr_col, curr_dir, steps)
        else:
            curr_dir = turn_dir(curr_dir, instruction)
        instruction = puzzle_instructions.get_next_instruction()
    if curr_face == 0:
        curr_col += CUBE_MAP_SIZE
    elif curr_face == 1:
        curr_col += CUBE_MAP_SIZE * 2
    elif curr_face == 2:
        curr_row += CUBE_MAP_SIZE
        curr_col += CUBE_MAP_SIZE
    elif curr_face == 3:
        curr_row += CUBE_MAP_SIZE * 2
    elif curr_face == 4:
        curr_row += CUBE_MAP_SIZE * 2
        curr_col += CUBE_MAP_SIZE
    elif curr_face == 5:
        curr_row += CUBE_MAP_SIZE * 3
    else:
        raise Exception(f"Unknown cube face: {curr_face}")

    logger.close()
    return (curr_row + 1) * 1000 + (curr_col + 1) * 4 + curr_dir
    
print(solve_part_2())
