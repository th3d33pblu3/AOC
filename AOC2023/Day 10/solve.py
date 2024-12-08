def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

NS = '|'
EW = '-'
NE = 'L'
NW = 'J'
SE = 'F'
SW = '7'
N, S, E, W = range(4)
START = 'S'
GROUND = '.'
# MARK = "I"
pipes = []

def next_step(curr_dir: int, curr_loc: tuple[int, int]) -> tuple[int, tuple[int, int]]:
    global pipes, NS, EW, NE, NW, SE, SW, N, S, E, W, START, GROUND

    y, x = curr_loc
    curr_pipe = pipes[y][x]

    if curr_dir == N:
        if curr_pipe == NS:
            return N, (y + 1, x)
        elif curr_pipe == NE:
            return W, (y, x + 1)
        elif curr_pipe == NW:
            return E, (y, x - 1)
        else:
            raise Exception(f"Unknown pipe {curr_pipe=}")
    elif curr_dir == S:
        if curr_pipe == NS:
            return S, (y - 1, x)
        elif curr_pipe == SE:
            return W, (y, x + 1)
        elif curr_pipe == SW:
            return E, (y, x - 1)
        else:
            raise Exception(f"Unknown pipe {curr_pipe=}")
    elif curr_dir == E:
        if curr_pipe == EW:
            return E, (y, x - 1)
        elif curr_pipe == NE:
            return S, (y - 1, x)
        elif curr_pipe == SE:
            return N, (y + 1, x)
        else:
            raise Exception(f"Unknown pipe {curr_pipe=}")
    elif curr_dir == W:
        if curr_pipe == EW:
            return W, (y, x + 1)
        elif curr_pipe == NW:
            return S, (y - 1, x)
        elif curr_pipe == SW:
            return N, (y + 1, x)
        else:
            raise Exception(f"Unknown pipe {curr_pipe=}")
    else:
        raise Exception(f"Unknown direction {curr_dir=}")
    
def find_start_loc() -> tuple[int, int]:
    global pipes, START
    for y, line in enumerate(pipes):
        for x, p in enumerate(line):
            if p == START:
                return y, x
    raise Exception(f"{START=} not found")

def get_start_pipe(start_loc: tuple[int, int]) -> str:
    global pipes, NS, EW, NE, NW, SE, SW, N, S, E, W, START, GROUND

    y, x = start_loc
    if y == 0:
        if x == 0:
            return SE # F
        if x == len(pipes[0]) - 1:
            return SW # 7
        if pipes[y][x - 1] in (EW, SE) and pipes[y][x + 1] in (EW, SW): # left is - or F and right is - or 7
            return EW # -
        else:
            if pipes[y][x - 1] in (EW, SE): # left is - or F
                return SW # 7
            else:
                return SE # F
    if y == len(pipes) - 1:
        if x == 0:
            return NE # L
        if x == len(pipes[0]) - 1:
            return NW # J
        if pipes[y][x - 1] in (EW, NE) and pipes[y][x + 1] in (EW, NW):  # left is - or F and right is - or 7
            return EW # -
        else:
            if pipes[y][x - 1] in (EW, NE):  # left is - or F
                return NW # J
            else:
                return NE # L
    else:
        if pipes[y - 1][x] in (NS, SE, SW): # Top connects down
            if pipes[y + 1][x] in (NS, NE, NW): # Bottom connects too
                return NS
            elif x == 0 or pipes[y][x - 1] not in (EW, NE, SE): # Left does not connect
                return NE
            else:
                return NW
        elif pipes[y + 1][x] in (NS, NE, NW): # Bottom connects
            if x == 0 or pipes[y][x - 1] not in (EW, NE, SE): # Left does not connect
                return SE
            else:
                return SW
        else:
            return EW

def get_random_pipe_dir(pipe: str) -> int:
    global pipes, NS, EW, NE, NW, SE, SW, N, S, E, W
    return N if pipe in (NS, NE, NW) else S

def solve_part_1():
    global pipes
    pipes = [[_ for _ in line] for line in read_input_file_data().splitlines()]
    start_loc = find_start_loc()

    # Replace with correct pipe
    start_pipe = get_start_pipe(start_loc)
    pipes[start_loc[0]][start_loc[1]] = start_pipe

    # Walk the pipe loop
    curr_dir = get_random_pipe_dir(start_pipe)
    curr_loc = start_loc
    steps = 0
    while True:
        curr_dir, curr_loc = next_step(curr_dir, curr_loc)
        steps += 1
        if curr_loc == start_loc:
            break
    return steps // 2

def solve_part_2():
    global pipes, GROUND, MARK
    pipes = [[_ for _ in line] for line in read_input_file_data().splitlines()]
    start_loc = find_start_loc()

    # Create clean pipe map
    y_size = len(pipes)
    x_size = len(pipes[0])
    clean_map = []
    for _ in range(y_size):
        clean_map.append([GROUND] * x_size)

    # Replace with correct pipe
    start_pipe = get_start_pipe(start_loc)
    pipes[start_loc[0]][start_loc[1]] = start_pipe
    clean_map[start_loc[0]][start_loc[1]] = start_pipe

    # Walk the pipe loop to draw the clean map
    curr_dir = get_random_pipe_dir(start_pipe)
    curr_loc = start_loc
    while True:
        clean_map[curr_loc[0]][curr_loc[1]] = pipes[curr_loc[0]][curr_loc[1]]
        curr_dir, curr_loc = next_step(curr_dir, curr_loc)
        if curr_loc == start_loc:
            break
        
    inside = 0
    for line in clean_map:
    # for y, line in enumerate(clean_map):
        isInside = False
        keep = None
        for p in line:
        # for x, p in enumerate(line):
            if p == NS: # |
                isInside = not isInside
            elif p == SE or p == NE: # F or L
                keep = p
            elif p == SW: # 7
                if keep == NE: # L---7
                    isInside = not isInside
            elif p == NW: # J
                if keep == SE: # F---J
                    isInside = not isInside
            elif p == EW: # -
                continue
            elif p == GROUND:
                if isInside:
                    inside += 1
                    # clean_map[y][x] = MARK
            else:
                raise Exception(f"Unknown pipe {p}")
        # print(''.join(line))
    return inside
    
print(solve_part_2())
