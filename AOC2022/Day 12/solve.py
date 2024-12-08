import numpy as np

def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def get_elevation(char):
    return ord(char) - ord('a')

def get_map():
    elevation_map = []
    start = ()
    end = ()
    file = read_input_file()
    for row, line in enumerate(file.read().splitlines()):
        line_elevation = []
        for column, char in enumerate(line):
            if char == 'S':
                line_elevation.append(get_elevation('a'))
                start = (row, column)
            elif char == 'E':
                line_elevation.append(get_elevation('z'))
                end = (row, column)
            else:
                line_elevation.append(get_elevation(char))
        elevation_map.append(line_elevation)

    return elevation_map, start, end

def solve_part_1():
    elevation_map, start, end = get_map()
    height = len(elevation_map)
    width = len(elevation_map[0])
    steps = np.full((height, width), np.inf)
    steps[start[0], start[1]] = 0
    frontier = [start]

    def get_moves(pos):
        moves = []
        if pos[0] > 0:
            moves.append((pos[0] - 1, pos[1]))
        if pos[1] > 0:
            moves.append((pos[0], pos[1] - 1))
        if pos[0] < height - 1:
            moves.append((pos[0] + 1, pos[1]))
        if pos[1] < width - 1:
            moves.append((pos[0], pos[1] + 1))
        return moves

    def can_move(pos, move):
        pos_elevation = elevation_map[pos[0]][pos[1]]
        move_elevation = elevation_map[move[0]][move[1]]
        if move_elevation <= pos_elevation + 1:
            return True
        return False

    def should_move(pos, move):
        pos_step = steps[pos[0]][pos[1]]
        move_step = steps[move[0]][move[1]]
        if move_step > pos_step + 1:
            return True
        return False

    while len(frontier) > 0:
        pos = frontier.pop(0)
        moves = get_moves(pos)
        for move in moves:
            if can_move(pos, move) and should_move(pos, move):
                steps[move[0], move[1]] = steps[pos[0], pos[1]] + 1
                frontier.append(move)

    return steps[end[0], end[1]]


def solve_part_2():
    """
    Move from E to all the elevation 'a'.
    """
    elevation_map, _, start = get_map()
    height = len(elevation_map)
    width = len(elevation_map[0])
    steps = np.full((height, width), np.inf)
    steps[start[0], start[1]] = 0
    frontier = [start]

    def get_moves(pos):
        moves = []
        if pos[0] > 0:
            moves.append((pos[0] - 1, pos[1]))
        if pos[1] > 0:
            moves.append((pos[0], pos[1] - 1))
        if pos[0] < height - 1:
            moves.append((pos[0] + 1, pos[1]))
        if pos[1] < width - 1:
            moves.append((pos[0], pos[1] + 1))
        return moves

    def can_move(pos, move):
        """
        Moving logic must be reversed
        """
        pos_elevation = elevation_map[pos[0]][pos[1]]
        move_elevation = elevation_map[move[0]][move[1]]
        if move_elevation >= pos_elevation - 1:           # Changed
            return True
        return False

    def should_move(pos, move):
        pos_step = steps[pos[0]][pos[1]]
        move_step = steps[move[0]][move[1]]
        if move_step > pos_step + 1:
            return True
        return False

    while len(frontier) > 0:
        pos = frontier.pop(0)
        moves = get_moves(pos)
        for move in moves:
            if can_move(pos, move) and should_move(pos, move):
                steps[move[0], move[1]] = steps[pos[0], pos[1]] + 1
                frontier.append(move)

    min_a = np.inf
    for row in range(height):
        for col in range(width):
            elevation = elevation_map[row][col]
            if elevation == 0:
                min_a = min(min_a, steps[row, col])
    return min_a

print(solve_part_2())
