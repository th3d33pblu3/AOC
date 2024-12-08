def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

SAFE = '.'
TRAP = '^'

def count_safe_tiles(row: str):
    return row.count(SAFE)

def get_next_row(prev_row):
    prev_row = SAFE + prev_row + SAFE
    new_row = ''
    for i in range(1, len(prev_row) - 1):
        new_row += TRAP if (prev_row[i - 1] == TRAP) ^ (prev_row[i + 1] == TRAP) else SAFE
    return new_row

def solve_part_1():
    curr_row = read_input_file_data()
    safe_tiles_count = count_safe_tiles(curr_row)
    for _ in range(40 - 1):
        curr_row = get_next_row(curr_row)
        safe_tiles_count += count_safe_tiles(curr_row)
    return safe_tiles_count

def solve_part_2(): # 19991126
    INITIAL_ROW = read_input_file_data()
    curr_row = INITIAL_ROW
    safe_tiles_count = count_safe_tiles(curr_row)
    for _ in range(400000 - 1):
        curr_row = get_next_row(curr_row)
        safe_tiles_count += count_safe_tiles(curr_row)
    return safe_tiles_count
    
print(solve_part_2())
