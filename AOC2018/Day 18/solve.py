def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

OPEN = '.'
TREE = '|'
LBYD = '#'

def solve_part_1():
    land = read_input_file_data().splitlines()
    COORDINATES = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, +1), (1, -1), (1, 0), (1, 1)]
    def get_adj(row, col, target_type):
        count = 0
        for dr, dc in COORDINATES:
            if row + dr >= 0 and row + dr < 50 and col + dc >= 0 and col + dc < 50:
                if land[row + dr][col + dc] == target_type:
                    count += 1
        return count

    time = 0
    while time < 10:
        new_land = [['?' for _ in range(50)] for _ in range(50)]
        for row in range(50):
            for col in range(50):
                if land[row][col] == OPEN:
                    trees = get_adj(row, col, TREE)
                    if trees >= 3:
                        new_land[row][col] = TREE
                    else:
                        new_land[row][col] = OPEN
                elif land[row][col] == TREE:
                    lumberyards = get_adj(row, col, LBYD)
                    if lumberyards >= 3:
                        new_land[row][col] = LBYD
                    else:
                        new_land[row][col] = TREE
                elif land[row][col] == LBYD:
                    trees = get_adj(row, col, TREE)
                    lumberyards = get_adj(row, col, LBYD)
                    if trees > 0 and lumberyards > 0:
                        new_land[row][col] = LBYD
                    else:
                        new_land[row][col] = OPEN
        land = new_land
        time += 1

    trees = 0
    lumberyards = 0
    for row in range(50):
        for col in range(50):
            if land[row][col] == TREE:
                trees += 1
            elif land[row][col] == LBYD:
                lumberyards += 1
    return trees * lumberyards

def solve_part_2():
    land = read_input_file_data().splitlines()
    state_key = ''.join(land)
    states = {} # curr_state : prev_state

    COORDINATES = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, +1), (1, -1), (1, 0), (1, 1)]
    def get_adj(row, col, target_type):
        count = 0
        for dr, dc in COORDINATES:
            if row + dr >= 0 and row + dr < 50 and col + dc >= 0 and col + dc < 50:
                if land[row + dr][col + dc] == target_type:
                    count += 1
        return count

    iterations = 1_000_000_000
    while iterations > 0:
        new_land = [['?' for _ in range(50)] for _ in range(50)]
        for row in range(50):
            for col in range(50):
                if land[row][col] == OPEN:
                    trees = get_adj(row, col, TREE)
                    if trees >= 3:
                        new_land[row][col] = TREE
                    else:
                        new_land[row][col] = OPEN
                elif land[row][col] == TREE:
                    lumberyards = get_adj(row, col, LBYD)
                    if lumberyards >= 3:
                        new_land[row][col] = LBYD
                    else:
                        new_land[row][col] = TREE
                elif land[row][col] == LBYD:
                    trees = get_adj(row, col, TREE)
                    lumberyards = get_adj(row, col, LBYD)
                    if trees > 0 and lumberyards > 0:
                        new_land[row][col] = LBYD
                    else:
                        new_land[row][col] = OPEN

        new_state_key = ''.join([''.join(line) for line in new_land])
        if new_state_key in states:
            # iteration for current change
            curr_state_key = new_state_key
            iterations -= 1

            # calculate loops
            loop_size = 0
            # manually move by 1
            curr_state_key = state_key
            loop_size += 1
            # calculate loop size
            while curr_state_key != new_state_key:
                curr_state_key = states[curr_state_key]
                loop_size += 1
            iterations %= loop_size

            # backtrack to find right state
            final_state_key = ''

            backtracks = loop_size - iterations
            if backtracks == 0:
                final_state_key = new_state_key
            elif backtracks == 1:
                final_state_key = state_key
            else:
                curr_state_key = state_key
                backtracks -= 1
                for _ in range(backtracks):
                    curr_state_key = states[curr_state_key]
                final_state_key = curr_state_key
            
            # calculate value and return
            trees = final_state_key.count(TREE)
            lumberyards = final_state_key.count(LBYD)
            return trees * lumberyards
            
        else:
            states[new_state_key] = state_key
            land = new_land
            state_key = new_state_key
            iterations -= 1

    trees = 0
    lumberyards = 0
    for row in range(50):
        for col in range(50):
            if land[row][col] == TREE:
                trees += 1
            elif land[row][col] == LBYD:
                lumberyards += 1
    return trees * lumberyards
    
print(solve_part_2())
