import math

def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

input = int(read_input_file().read())

def solve_part_1():
    def get_ring_number(num):
        ring = math.floor(math.sqrt(num - 1)) + 1
        if ring % 2 == 0:
            ring += 1
        return ring

    num = input
    if num == 1:
        return 0
    ring_number = get_ring_number(num) # 1, 3, 5, 7, 9 etc
    pos_on_ring = num - (ring_number - 2) ** 2 - 1 # starts with 0
    quarter_ring_length = ring_number - 1 # 1 less than ring_number
    pos_on_quarter_ring = pos_on_ring % quarter_ring_length # starts with 0
    axis_pos_on_quarter_ring = quarter_ring_length / 2 - 1
    move_to_axis_steps = abs(pos_on_quarter_ring - axis_pos_on_quarter_ring)
    move_along_axis_to_middle_steps = (ring_number - 1) / 2

    steps = move_to_axis_steps + move_along_axis_to_middle_steps
    return steps

def solve_part_2():
    limit = input

    written = {(0, 0): 1, (1, 0): 1}

    def update(x, y):
        nonlocal written
        num = 0
        ls_of_pos = [(x - 1, y + 1), (x    , y + 1), (x + 1, y + 1),
                     (x - 1,     y),                 (x + 1, y    ),
                     (x - 1, y - 1), (x    , y - 1), (x + 1, y - 1)]
        for pos in ls_of_pos:
            if written.get(pos) != None:
                num += written.get(pos)
        written[(x, y)] = num
        return num

    x = 1
    y = 0
    num = 1
    quarter_ring_length = 2
    while num < limit:
        # UP
        for _ in range(quarter_ring_length - 1):
            y += 1
            num = update(x, y)
            if num > limit:
                return num
        # LEFT
        for _ in range(quarter_ring_length):
            x -= 1
            num = update(x, y)
            if num > limit:
                return num
        # DOWN
        for _ in range(quarter_ring_length):
            y -= 1
            num = update(x, y)
            if num > limit:
                return num
        # RIGHT
        for _ in range(quarter_ring_length + 1):
            x += 1
            num = update(x, y)
            if num > limit:
                return num
        quarter_ring_length += 2
    
print(solve_part_2())
