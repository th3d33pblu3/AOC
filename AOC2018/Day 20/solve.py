import sys

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    instructions = read_input_file_data()
    doors = {} # (loc): [N, E, S, W]
    DIRS = ('N', 'E', 'S', 'W')
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    START = (0, 0)

    ins_ptr = 0
    def move(location):
        nonlocal doors, instructions, ins_ptr

        ins = instructions[ins_ptr]
        x, y = location
        if ins == '$':
            return
        elif ins in DIRS:
            i = DIRS.index(ins)
            dx, dy = DELTA[i]
            new_location = (x+dx, y+dy)
            doors[location][i] = True
            if new_location not in doors:
                doors[new_location] = [False, False, False, False]
            doors[new_location][(i+2)%4] = True

            ins_ptr += 1
            move(new_location)
            return
        elif ins == '(':
            ins_ptr += 1
            move(location)
            while instructions[ins_ptr] == '|':
                ins_ptr += 1
                move(location)
            assert instructions[ins_ptr] == ')'
            ins_ptr += 1
            move(location)
            return
        elif ins == '|' or ins == ')':
            return
    
    if instructions[0] == '^':
        sys.setrecursionlimit(10000) # allow system to do more recursion
        doors[START] = [False, False, False, False]
        ins_ptr += 1
        move(START)
    
    dist = 0
    frontier = set()
    frontier.add(START)
    reached_rooms = set()
    reached_rooms.add(START)
    while frontier:
        new_frontier = set()
        for location in frontier:
            room_doors = doors[location]
            x, y = location
            for i in range(4):
                if room_doors[i]:
                    dx, dy = DELTA[i]
                    if (x+dx, y+dy) not in reached_rooms:
                        new_frontier.add((x+dx, y+dy))
        reached_rooms.update(new_frontier)
        frontier = new_frontier
        if frontier:
            dist += 1

    return dist
    
def solve_part_2():
    instructions = read_input_file_data()
    doors = {} # (loc): [N, E, S, W]
    DIRS = ('N', 'E', 'S', 'W')
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    START = (0, 0)

    ins_ptr = 0
    def move(location):
        nonlocal doors, instructions, ins_ptr

        ins = instructions[ins_ptr]
        x, y = location
        if ins == '$':
            return
        elif ins in DIRS:
            i = DIRS.index(ins)
            dx, dy = DELTA[i]
            new_location = (x+dx, y+dy)
            doors[location][i] = True
            if new_location not in doors:
                doors[new_location] = [False, False, False, False]
            doors[new_location][(i+2)%4] = True

            ins_ptr += 1
            move(new_location)
            return
        elif ins == '(':
            ins_ptr += 1
            move(location)
            while instructions[ins_ptr] == '|':
                ins_ptr += 1
                move(location)
            assert instructions[ins_ptr] == ')'
            ins_ptr += 1
            move(location)
            return
        elif ins == '|' or ins == ')':
            return
    
    if instructions[0] == '^':
        sys.setrecursionlimit(10000) # allow system to do more recursion
        doors[START] = [False, False, False, False]
        ins_ptr += 1
        move(START)
    
    remaining_dist = 1000 - 1 # find the rooms that can be reach in less than N doors
    frontier = set()
    frontier.add(START)
    reached_rooms = set()
    reached_rooms.add(START)
    while frontier and remaining_dist:
        new_frontier = set()
        for location in frontier:
            room_doors = doors[location]
            x, y = location
            for i in range(4):
                if room_doors[i]:
                    dx, dy = DELTA[i]
                    if (x+dx, y+dy) not in reached_rooms:
                        new_frontier.add((x+dx, y+dy))
        reached_rooms.update(new_frontier)
        frontier = new_frontier
        remaining_dist -= 1
    assert remaining_dist == 0

    return len(set(doors.keys()).difference(reached_rooms))
    
print(solve_part_2())
