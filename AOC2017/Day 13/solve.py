def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

DEPTH = 89

def get_range_depths():
    range_depths = [-1] * DEPTH
    for line in read_input_file_data().splitlines():
        depth, range = tuple(map(int, line.split(": ")))
        range_depths[depth] = range
    return range_depths

def solve_part_1():
    range_depths = get_range_depths()
    severity = 0
    for i in range(DEPTH):
        if range_depths[i] != -1:
            if i % (range_depths[i] * 2 - 2) == 0:
                severity += i * range_depths[i]
    return severity

def get_cycle_depths():
    range_depths = get_range_depths()
    for i in range(DEPTH):
        if range_depths[i] != -1:
            range_depths[i] = range_depths[i] * 2 - 2
    return range_depths

def solve_part_2():
    cycle_depths = get_cycle_depths()
    wait = 0
    while True:
        is_passable = True
        for i in range(DEPTH):
            if cycle_depths[i] != -1:
                if (i + wait) % cycle_depths[i] == 0:
                    is_passable = False
                    break
        if is_passable:
            return wait
        else:
            wait += 1
    
print(solve_part_2())
