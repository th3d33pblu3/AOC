def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

class Dir:
    UP    = 0
    RIGHT = 1
    DOWN  = 2
    LEFT  = 3

def solve_part_1():
    data = read_input_file_data().splitlines()
    HEIGHT = len(data)
    WIDTH = len(data[0])
    infected = {}
    for r in range(HEIGHT):
        for c in range(WIDTH):
            if data[r][c] == '#':
                infected[(r, c)] = True
    
    curr_pos = (HEIGHT // 2, WIDTH // 2)
    curr_dir = Dir.UP
    count = 0
    for _ in range(10000):
        is_infected = infected.get(curr_pos, False)
        # Turn
        curr_dir = (curr_dir + 1) % 4 if is_infected else (curr_dir - 1) % 4
        # Flip infection
        infected[curr_pos] = not is_infected
        if not is_infected: # Track count
            count += 1
        # Move
        r, c = curr_pos
        match curr_dir:
            case Dir.UP:
                curr_pos = (r-1, c)
            case Dir.RIGHT:
                curr_pos = (r, c+1)
            case Dir.DOWN:
                curr_pos = (r+1, c)
            case Dir.LEFT:
                curr_pos = (r, c-1)
    return count

class Status:
    CLEAN    = 0
    WEAKENED = 1
    INFECTED = 2
    FLAGGED  = 3

def solve_part_2():
    data = read_input_file_data().splitlines()
    HEIGHT = len(data)
    WIDTH = len(data[0])
    status = {}
    for r in range(HEIGHT):
        for c in range(WIDTH):
            if data[r][c] == '#':
                status[(r, c)] = Status.INFECTED
    
    curr_pos = (HEIGHT // 2, WIDTH // 2)
    curr_dir = Dir.UP
    count = 0
    for _ in range(10000000):
        curr_status = status.get(curr_pos, Status.CLEAN)
        # Turn
        match curr_status:
            case Status.CLEAN:    # Turn left
                curr_dir = (curr_dir - 1) % 4
            case Status.WEAKENED: # Does not turn
                pass
            case Status.INFECTED: # Turn right
                curr_dir = (curr_dir + 1) % 4
            case Status.FLAGGED:  # Reverse
                curr_dir = (curr_dir + 2) % 4
        # Flip infection
        status[curr_pos] = (curr_status + 1) % 4
        if curr_status == Status.WEAKENED: # Track count
            count += 1
        # Move
        r, c = curr_pos
        match curr_dir:
            case Dir.UP:
                curr_pos = (r-1, c)
            case Dir.RIGHT:
                curr_pos = (r, c+1)
            case Dir.DOWN:
                curr_pos = (r+1, c)
            case Dir.LEFT:
                curr_pos = (r, c-1)
    return count
    
print(solve_part_2())
