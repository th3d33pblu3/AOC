from hashlib import md5

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

PASSWORD = read_input_file_data()
UP = b'U'
DOWN = b'D'
LEFT = b'L'
RIGHT = b'R'

WINNING_CODE = ''

def is_open(c):
    return c in ('b', 'c', 'd', 'e', 'f')

def get_door(code):
    return md5(code).hexdigest()[:4] # UP, DOWN, LEFT, RIGHT

def possible_moves(state):
    global WINNING_CODE
    x, y, code = state
    doors = get_door(code)
    next_moves = set()
    # UP
    if y > 0 and is_open(doors[0]):
        next_moves.add((x, y - 1, code + UP))
    # DOWN
    if y < 3 and is_open(doors[1]):
        next_moves.add((x, y + 1, code + DOWN))
    # LEFT
    if x > 0 and is_open(doors[2]):
        next_moves.add((x - 1, y, code + LEFT))
    # RIGHT
    if x < 3 and is_open(doors[3]):
        next_moves.add((x + 1, y, code + RIGHT))
    for x, y, code in next_moves:
        if x == 3 and y == 3:
            WINNING_CODE = code
    return next_moves

def solve_part_1():
    global WINNING_CODE
    initial_code = PASSWORD.encode()
    states = set()
    states.add((0, 0, initial_code))
    while WINNING_CODE == '':
        next_states = set()
        for state in states:
            next_states = next_states.union(possible_moves(state))
        states = next_states
    return WINNING_CODE

def possible_non_ending_moves(state):
    global WINNING_CODE
    x, y, code = state
    doors = get_door(code)
    next_moves = set()
    # UP
    if y > 0 and is_open(doors[0]):
        next_moves.add((x, y - 1, code + UP))
    # DOWN
    if y < 3 and is_open(doors[1]):
        if x !=3 or y != 2:
            next_moves.add((x, y + 1, code + DOWN))
        else:
            WINNING_CODE = code + DOWN
    # LEFT
    if x > 0 and is_open(doors[2]):
        next_moves.add((x - 1, y, code + LEFT))
    # RIGHT
    if x < 3 and is_open(doors[3]):
        if x !=2 or y != 3:
            next_moves.add((x + 1, y, code + RIGHT))
        else:
            WINNING_CODE = code + RIGHT
    return next_moves

def solve_part_2():
    global WINNING_CODE
    initial_code = PASSWORD.encode()
    states = set()
    states.add((0, 0, initial_code))
    while len(states) > 0:
        next_states = set()
        for state in states:
            next_states = next_states.union(possible_non_ending_moves(state))
        states = next_states
    return len(WINNING_CODE) - len(initial_code)
    
print(solve_part_2())
