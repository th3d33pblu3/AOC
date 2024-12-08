from queue import Queue

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    dir_coor = tuple[int, int, int]
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

    mirrors = read_input_file_data().splitlines()
    y_size = len(mirrors)
    x_size = len(mirrors[0])
    energized = []
    for _ in range(y_size):
        energized.append([0] * x_size)

    def is_in_range(dc: dir_coor) -> bool:
        _, y, x = dc
        return x >= 0 and y >= 0 and x < x_size and y < y_size
    def is_completed(dc: dir_coor) -> bool:
        if not is_in_range(dc):
            return True
        dir, y, x = dc
        return energized[y][x] & (1 << dir) != 0
    def mark_energized(dc: dir_coor):
        dir, y, x = dc
        energized[y][x] |= 1 << dir
    def next(dc: dir_coor) -> list[dir_coor]:
        # if not is_in_range(dc):
        #     return []
        dir, y, x = dc
        c = mirrors[y][x]
        if c == '.':
            if dir == LEFT:
                return [(dir, y, x-1)]
            elif dir == RIGHT:
                return [(dir, y, x+1)]
            elif dir == UP:
                return [(dir, y-1, x)]
            elif dir == DOWN:
                return [(dir, y+1, x)]
        elif c == '/':
            if dir == LEFT:
                return [(DOWN, y+1, x)]
            elif dir == RIGHT:
                return [(UP, y-1, x)]
            elif dir == UP:
                return [(RIGHT, y, x+1)]
            elif dir == DOWN:
                return [(LEFT, y, x-1)]
        elif c == '\\':
            if dir == LEFT:
                return [(UP, y-1, x)]
            elif dir == RIGHT:
                return [(DOWN, y+1, x)]
            elif dir == UP:
                return [(LEFT, y, x-1)]
            elif dir == DOWN:
                return [(RIGHT, y, x+1)]
        elif c == '|':
            if dir == LEFT:
                return [(UP, y-1, x), (DOWN, y+1, x)]
            elif dir == RIGHT:
                return [(UP, y-1, x), (DOWN, y+1, x)]
            elif dir == UP:
                return [(dir, y-1, x)]
            elif dir == DOWN:
                return [(dir, y+1, x)]
        elif c == '-':
            if dir == LEFT:
                return [(dir, y, x-1)]
            elif dir == RIGHT:
                return [(dir, y, x+1)]
            elif dir == UP:
                return [(LEFT, y, x-1), (RIGHT, y, x+1)]
            elif dir == DOWN:
                return [(LEFT, y, x-1), (RIGHT, y, x+1)]
        raise Exception("Unknown character")

    unsettled_directions = Queue()
    unsettled_directions.put((RIGHT, 0, 0))
    while not unsettled_directions.empty():
        dc = unsettled_directions.get()
        mark_energized(dc)
        new_dcs = next(dc)
        for dc in new_dcs:
            if not is_completed(dc):
                unsettled_directions.put(dc)
    
    counter = 0
    for y in range(y_size):
        for x in range(x_size):
            if energized[y][x] != 0:
                counter += 1
    return counter

def solve_part_2():
    dir_coor = tuple[int, int, int]
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

    mirrors = read_input_file_data().splitlines()
    y_size = len(mirrors)
    x_size = len(mirrors[0])
    energized = None
    def reset_energized():
        nonlocal energized
        energized = []
        for _ in range(y_size):
            energized.append([0] * x_size)
    def is_in_range(dc: dir_coor) -> bool:
        _, y, x = dc
        return x >= 0 and y >= 0 and x < x_size and y < y_size
    def is_completed(dc: dir_coor) -> bool:
        if not is_in_range(dc):
            return True
        dir, y, x = dc
        return energized[y][x] & (1 << dir) != 0
    def mark_energized(dc: dir_coor):
        dir, y, x = dc
        energized[y][x] |= 1 << dir
    def next(dc: dir_coor) -> list[dir_coor]:
        dir, y, x = dc
        c = mirrors[y][x]
        if c == '.':
            if dir == LEFT:
                return [(dir, y, x-1)]
            elif dir == RIGHT:
                return [(dir, y, x+1)]
            elif dir == UP:
                return [(dir, y-1, x)]
            elif dir == DOWN:
                return [(dir, y+1, x)]
        elif c == '/':
            if dir == LEFT:
                return [(DOWN, y+1, x)]
            elif dir == RIGHT:
                return [(UP, y-1, x)]
            elif dir == UP:
                return [(RIGHT, y, x+1)]
            elif dir == DOWN:
                return [(LEFT, y, x-1)]
        elif c == '\\':
            if dir == LEFT:
                return [(UP, y-1, x)]
            elif dir == RIGHT:
                return [(DOWN, y+1, x)]
            elif dir == UP:
                return [(LEFT, y, x-1)]
            elif dir == DOWN:
                return [(RIGHT, y, x+1)]
        elif c == '|':
            if dir == LEFT:
                return [(UP, y-1, x), (DOWN, y+1, x)]
            elif dir == RIGHT:
                return [(UP, y-1, x), (DOWN, y+1, x)]
            elif dir == UP:
                return [(dir, y-1, x)]
            elif dir == DOWN:
                return [(dir, y+1, x)]
        elif c == '-':
            if dir == LEFT:
                return [(dir, y, x-1)]
            elif dir == RIGHT:
                return [(dir, y, x+1)]
            elif dir == UP:
                return [(LEFT, y, x-1), (RIGHT, y, x+1)]
            elif dir == DOWN:
                return [(LEFT, y, x-1), (RIGHT, y, x+1)]
        raise Exception("Unknown character")

    def find_counter(dc: dir_coor) -> int:
        reset_energized()
        unsettled_directions = Queue()
        unsettled_directions.put(dc)
        while not unsettled_directions.empty():
            dc = unsettled_directions.get()
            mark_energized(dc)
            new_dcs = next(dc)
            for dc in new_dcs:
                if not is_completed(dc):
                    unsettled_directions.put(dc)
        
        counter = 0
        for y in range(y_size):
            for x in range(x_size):
                if energized[y][x] != 0:
                    counter += 1
        return counter
    
    max_counter = 0
    # Right column
    dir = LEFT
    x = x_size - 1
    for y in range(y_size):
        max_counter = max(max_counter, find_counter((dir, y, x)))
    # Left column
    dir = RIGHT
    x = 0
    for y in range(y_size):
        max_counter = max(max_counter, find_counter((dir, y, x)))
    # Bottom row
    dir = UP
    y = y_size - 1
    for x in range(x_size):
        max_counter = max(max_counter, find_counter((dir, y, x)))
    # Top row
    dir = DOWN
    y = 0
    for x in range(x_size):
        max_counter = max(max_counter, find_counter((dir, y, x)))
    return max_counter

    
print(solve_part_2())
