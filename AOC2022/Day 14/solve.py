from enum import Enum
import numpy as np

def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def find_max_coordinates():
    max_x, max_y = 0, 0
    file = read_input_file()
    for line in file.read().splitlines():
        coordinates = line.split(" -> ")
        for coordinate in coordinates:
            x, y = coordinate.split(",")
            if int(x) > max_x:
                max_x = int(x)
            if int(y) > max_y:
                max_y = int(y)
    return max_x, max_y

class Shapes(Enum):
    SAND = "o"
    AIR = "."
    ROCK = "#"

    def __repr__(self):
        return self.value

def draw_scan(max_x, max_y):
    scan = np.full((max_y + 1, max_x + 1), Shapes.AIR, dtype=Shapes)

    file = read_input_file()
    for line in file.read().splitlines():
        coordinates_str = line.split(" -> ")
        coordinates = list(map(lambda s: tuple(map(int, s.split(","))), coordinates_str))
        current = coordinates[0]
        for coordinate in coordinates:
            scan[min(current[1], coordinate[1]) : max(current[1], coordinate[1]) + 1, min(current[0], coordinate[0]) : max(current[0], coordinate[0]) + 1] = Shapes.ROCK
            current = coordinate
    
    return scan


def solve_part_1():
    # Assumption: sand does not pile up and block the spawn point
    spawn = (0, 500) # y, x
    max_x, max_y = find_max_coordinates()
    scan = draw_scan(max_x + 10, max_y + 10)

    def can_move_down(sand):
        if scan[sand[0] + 1, sand[1]] == Shapes.AIR:
            return True
        else:
            return False

    def move_down(sand):
        sand[0] += 1

    def can_move_left_down(sand):
        if scan[sand[0] + 1, sand[1] - 1] == Shapes.AIR:
            return True
        else:
            return False

    def move_left_down(sand):
        sand[0] += 1
        sand[1] -= 1
    
    def can_move_right_down(sand):
        if scan[sand[0] + 1, sand[1] + 1] == Shapes.AIR:
            return True
        else:
            return False
    
    def move_right_down(sand):
        sand[0] += 1
        sand[1] += 1

    def reset_sand(sand):
        sand[0] = spawn[0]
        sand[1] = spawn[1]

    rest = 0
    try:
        sand = [spawn[0], spawn[1]]
        while(True):
            if can_move_down(sand):
                move_down(sand)
            elif can_move_left_down(sand):
                move_left_down(sand)
            elif can_move_right_down(sand):
                move_right_down(sand)
            else:
                scan[sand[0], sand[1]] = Shapes.SAND
                rest += 1
                reset_sand(sand)

    except Exception as out_of_bounds:
        print(out_of_bounds)
        return rest
    
def solve_part_2():
    spawn = (0, 500) # y, x
    max_x, max_y = find_max_coordinates()
    scan = draw_scan(max(max_x, 500 + max_y + 2) + 1, max_y + 2)
    scan[max_y + 2, :] = Shapes.ROCK

    def can_move_down(sand):
        if scan[sand[0] + 1, sand[1]] == Shapes.AIR:
            return True
        else:
            return False

    def move_down(sand):
        sand[0] += 1

    def can_move_left_down(sand):
        if scan[sand[0] + 1, sand[1] - 1] == Shapes.AIR:
            return True
        else:
            return False

    def move_left_down(sand):
        sand[0] += 1
        sand[1] -= 1
    
    def can_move_right_down(sand):
        if scan[sand[0] + 1, sand[1] + 1] == Shapes.AIR:
            return True
        else:
            return False
    
    def move_right_down(sand):
        sand[0] += 1
        sand[1] += 1

    def reset_sand(sand):
        sand[0] = spawn[0]
        sand[1] = spawn[1]

    rest = 0
    sand = [spawn[0], spawn[1]]
    while(True):
        if can_move_down(sand):
            move_down(sand)
        elif can_move_left_down(sand):
            move_left_down(sand)
        elif can_move_right_down(sand):
            move_right_down(sand)
        else:
            scan[sand[0], sand[1]] = Shapes.SAND
            rest += 1
            if tuple(sand) == spawn:
                np.set_printoptions(linewidth=np.inf, threshold=np.inf)
                write(scan)
                return rest
            reset_sand(sand)

def write(data):
    FILE = "./Day 14/output.txt"
    file = open(FILE, 'w')
    file.write(str(data))
    file.close()
    
print(solve_part_2())
