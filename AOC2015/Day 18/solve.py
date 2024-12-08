def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def parse_lights():
    data = read_input_file_data()
    lights = []
    for line in data.splitlines():
        row = []
        words = list(line)
        for light in words:
            if light == ".":
                row.append(False)
            else:
                row.append(True)
        lights.append(row)
    return lights

LIMIT = 100
    
def get_next_status(row: int, col: int, lights: list[list[int]]) -> bool:
    on_count = 0

    for i in [-1, 0, 1]:
        new_row = row + i
        for j in [-1, 0, 1]:
            new_col = col + j
            if new_row >= 0 and new_row < LIMIT and new_col >= 0 and new_col < LIMIT and (i != 0 or j != 0):
                if lights[new_row][new_col]:
                    on_count += 1
    
    curr_state_on = lights[row][col]
    if curr_state_on:
        return on_count == 2 or on_count == 3
    else:
        return on_count == 3

def step(lights):
    new_lights = []
    for row in range(LIMIT):
        new_row = []
        for col in range(LIMIT):
            new_row.append(get_next_status(row, col, lights))
        new_lights.append(new_row)
    return new_lights

def solve_part_1():
    lights = parse_lights()
    for _ in range(100):
        lights = step(lights)
    return sum(map(lambda row: row.count(True), lights))

def on_corners(lights):
    lights[0][0] = True
    lights[0][LIMIT - 1] = True
    lights[LIMIT - 1][0] = True
    lights[LIMIT - 1][LIMIT - 1] = True
    return lights

def solve_part_2():
    lights = parse_lights()
    lights = on_corners(lights)
    for _ in range(100):
        lights = step(lights)
        lights = on_corners(lights)
    return sum(map(lambda row: row.count(True), lights))
    
print(solve_part_2())
