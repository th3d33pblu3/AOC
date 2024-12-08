def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"

WALL = "#"
EMPTY = "."

def parse_input():
    blizzards = []
    data = read_input_file_data().splitlines()
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char != WALL and char != EMPTY:
                blizzards.append((x - 1, y - 1, char))
    return blizzards, len(data[0]) - 2, len(data) - 2

# def print_blizzards(blizzards, X_LIMIT, Y_LIMIT):
#     ls = []
#     for y in range(Y_LIMIT):
#         ls.append(["."] * X_LIMIT)
#     for blizzard in blizzards:
#         x, y, dire = blizzard
#         ls[y][x] = dire
#     for i, line in enumerate(ls):
#         ls[i] = "".join(line)
#     print("\n".join(ls))

def solve_part_1():
    blizzards, X_LIMIT, Y_LIMIT = parse_input()
    START = (0, -1)
    GOAL = (X_LIMIT - 1, Y_LIMIT)
    
    def get_moves(pos):
        if pos == START:
            return [START, (0, 0)]
        if pos == (X_LIMIT - 1, Y_LIMIT - 1):
            return [GOAL]
        moves = [pos]
        x, y = pos
        if pos == (0, 0):
            moves.append(START)
        if x != 0:
            moves.append((x - 1, y))
        if x != X_LIMIT - 1:
            moves.append((x + 1, y))
        if y != 0:
            moves.append((x, y - 1))
        if y != Y_LIMIT - 1:
            moves.append((x, y + 1))
        return moves

    def move_blizzards():
        nonlocal blizzards
        new_blizzards = []
        for blizzard in blizzards:
            x, y, direction = blizzard
            if direction == LEFT:
                new_blizzards.append(((x - 1) % X_LIMIT, y, direction))
            elif direction == RIGHT:
                new_blizzards.append(((x + 1) % X_LIMIT, y, direction))
            elif direction == UP:
                new_blizzards.append((x, (y - 1) % Y_LIMIT, direction))
            elif direction == DOWN:
                new_blizzards.append((x, (y + 1) % Y_LIMIT, direction))
        blizzards = new_blizzards

    time = 0
    positions = set()
    positions.add(START)
    while True:
        if GOAL in positions:
            return time
        new_positions = set()
        for pos in positions:
            new_positions.update(get_moves(pos))
        positions.update(new_positions)
        move_blizzards()
        for blizzard in blizzards:
            x, y, direction = blizzard
            if (x, y) in positions:
                positions.remove((x, y))
        time += 1
        
def solve_part_2():
    blizzards, X_LIMIT, Y_LIMIT = parse_input() # 0 to 99, 0 to 34
    START = (0, -1)
    GOAL = (X_LIMIT - 1, Y_LIMIT)
    
    def get_moves(pos):
        if pos == START:
            return [START, (0, 0)]
        if pos == GOAL:
            return [GOAL, (X_LIMIT - 1, Y_LIMIT - 1)]
        moves = [pos]
        x, y = pos
        if pos == (0, 0):
            moves.append(START)
        if pos == (X_LIMIT - 1, Y_LIMIT - 1):
            moves.append(GOAL)
        if x != 0:
            moves.append((x - 1, y))
        if x != X_LIMIT - 1:
            moves.append((x + 1, y))
        if y != 0:
            moves.append((x, y - 1))
        if y != Y_LIMIT - 1:
            moves.append((x, y + 1))
        return moves

    def move_blizzards():
        nonlocal blizzards
        new_blizzards = []
        for blizzard in blizzards:
            x, y, direction = blizzard
            if direction == LEFT:
                new_blizzards.append(((x - 1) % X_LIMIT, y, direction))
            elif direction == RIGHT:
                new_blizzards.append(((x + 1) % X_LIMIT, y, direction))
            elif direction == UP:
                new_blizzards.append((x, (y - 1) % Y_LIMIT, direction))
            elif direction == DOWN:
                new_blizzards.append((x, (y + 1) % Y_LIMIT, direction))
        blizzards = new_blizzards

    time = 0
    positions = set()
    positions.add(START)
    while True:
        if GOAL in positions:
            break
        new_positions = set()
        for pos in positions:
            new_positions.update(get_moves(pos))
        positions.update(new_positions)
        move_blizzards()
        for blizzard in blizzards:
            x, y, direction = blizzard
            if (x, y) in positions:
                positions.remove((x, y))
        time += 1

    positions = set()
    positions.add(GOAL)
    while True:
        if START in positions:
            break
        new_positions = set()
        for pos in positions:
            new_positions.update(get_moves(pos))
        positions.update(new_positions)
        move_blizzards()
        for blizzard in blizzards:
            x, y, direction = blizzard
            if (x, y) in positions:
                positions.remove((x, y))
        time += 1

    positions = set()
    positions.add(START)
    while True:
        if GOAL in positions:
            break
        new_positions = set()
        for pos in positions:
            new_positions.update(get_moves(pos))
        positions.update(new_positions)
        move_blizzards()
        for blizzard in blizzards:
            x, y, direction = blizzard
            if (x, y) in positions:
                positions.remove((x, y))
        time += 1

    return time
    
print(solve_part_2())
