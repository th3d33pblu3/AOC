def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def parse_row_col():
    data = read_input_file_data()
    words = data.split()
    row = int(words[-3][:-1])
    col = int(words[-1][:-1])
    return row, col

STARTING_NUMBER = 20151125
MULTIPLE = 252533
MOD = 33554393
TARGET_ROW, TARGET_COL = parse_row_col()

def get_n(row, col):
    # Get the number of numbers up till the diagonal before this diagonal
    prev_diagonal_number = row - 1 + col - 1
    n_sofar = (prev_diagonal_number + 1) * prev_diagonal_number // 2
    # Get the number of numbers in this diagonal up to the row and column number
    n_curr_diag = col
    return n_sofar + n_curr_diag

def solve_part_1():
    num = STARTING_NUMBER
    for _ in range(get_n(TARGET_ROW, TARGET_COL) - 1):
        num = (num * MULTIPLE) % MOD
    return num

def solve_part_2():
    pass
    
print(solve_part_1())
