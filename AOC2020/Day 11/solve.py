def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'

def solve_part_1():
    seats = list(map(lambda line: [char for char in line], read_input_file_data().splitlines()))
    key = ''.join(list(map(lambda row: ''.join(row), seats)))
    HEIGHT = len(seats)
    WIDTH = len(seats[0])

    DELTA = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    def get_adj_occupied(x, y):
        nonlocal seats
        count = 0
        for dx, dy in DELTA:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= WIDTH or ny < 0 or ny >= HEIGHT:
                continue
            if seats[ny][nx] == OCCUPIED:
                count += 1
        return count

    seen_states = set()
    while key not in seen_states:
        seen_states.add(key)
        new_seats = [[FLOOR] * WIDTH for _ in range(HEIGHT)]
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if seats[y][x] == FLOOR:
                    continue
                elif seats[y][x] == EMPTY:
                    num_adj_occupied = get_adj_occupied(x, y)
                    if num_adj_occupied == 0:
                        new_seats[y][x] = OCCUPIED
                    else:
                        new_seats[y][x] = EMPTY
                else:
                    num_adj_occupied = get_adj_occupied(x, y)
                    if num_adj_occupied >= 4:
                        new_seats[y][x] = EMPTY
                    else:
                        new_seats[y][x] = OCCUPIED
        seats = new_seats
        key = ''.join(list(map(lambda row: ''.join(row), seats)))
    return key.count(OCCUPIED)

def solve_part_2():
    seats = list(map(lambda line: [char for char in line], read_input_file_data().splitlines()))
    key = ''.join(list(map(lambda row: ''.join(row), seats)))
    HEIGHT = len(seats)
    WIDTH = len(seats[0])

    DELTA = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    def get_adj_occupied(x, y):
        nonlocal seats
        count = 0
        for dx, dy in DELTA:
            nx = x + dx
            ny = y + dy
            while nx >= 0 and nx < WIDTH and ny >= 0 and ny < HEIGHT and seats[ny][nx] == FLOOR:
                nx += dx
                ny += dy
            if nx < 0 or nx >= WIDTH or ny < 0 or ny >= HEIGHT:
                continue
            if seats[ny][nx] == OCCUPIED:
                count += 1
        return count

    seen_states = set()
    while key not in seen_states:
        seen_states.add(key)
        new_seats = [[FLOOR] * WIDTH for _ in range(HEIGHT)]
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if seats[y][x] == FLOOR:
                    continue
                elif seats[y][x] == EMPTY:
                    num_adj_occupied = get_adj_occupied(x, y)
                    if num_adj_occupied == 0:
                        new_seats[y][x] = OCCUPIED
                    else:
                        new_seats[y][x] = EMPTY
                else:
                    num_adj_occupied = get_adj_occupied(x, y)
                    if num_adj_occupied >= 5:
                        new_seats[y][x] = EMPTY
                    else:
                        new_seats[y][x] = OCCUPIED
        seats = new_seats
        key = ''.join(list(map(lambda row: ''.join(row), seats)))
    return key.count(OCCUPIED)
    
print(solve_part_2())
