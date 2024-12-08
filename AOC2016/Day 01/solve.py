from enum import Enum

def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

class Directions(Enum):
    NORTH = ( 0,  1)
    SOUTH = ( 0, -1)
    EAST  = ( 1,  0)
    WEST  = (-1,  0)
    LEFT  = "L"
    RIGHT = "R"

def rotate(facing, dir):
    if facing == Directions.NORTH:
        if dir == Directions.LEFT.value:
            return Directions.WEST
        else:
            return Directions.EAST
    elif facing == Directions.SOUTH:
        if dir == Directions.LEFT.value:
            return Directions.EAST
        else:
            return Directions.WEST
    elif facing == Directions.EAST:
        if dir == Directions.LEFT.value:
            return Directions.NORTH
        else:
            return Directions.SOUTH
    elif facing == Directions.WEST:
        if dir == Directions.LEFT.value:
            return Directions.SOUTH
        else:
            return Directions.NORTH

def solve_part_1():
    pos = [0, 0]
    facing = Directions.NORTH
    file = read_input_file()
    instructions = file.read().split(", ")
    for instruction in instructions:
        dir = instruction[0]
        steps = int(instruction[1:])
        facing = rotate(facing, dir)
        x, y = facing.value[0] * steps, facing.value[1] * steps
        pos[0] += x
        pos[1] += y
    print(pos)
    return abs(pos[0]) + abs(pos[1])


def solve_part_2():
    visited = {(0, 0): 1}
    pos = [0, 0]
    facing = Directions.NORTH
    file = read_input_file()
    instructions = file.read().split(", ")
    for instruction in instructions:
        dir = instruction[0]
        steps = int(instruction[1:])
        facing = rotate(facing, dir)
        for step in range(1, steps + 1):
            pos[0] += facing.value[0]
            pos[1] += facing.value[1]
            coord = tuple(pos)
            if visited.get(coord) != None:
                print(pos)
                return abs(pos[0]) + abs(pos[1])
            visited[coord] = 1
    
print(solve_part_2())
