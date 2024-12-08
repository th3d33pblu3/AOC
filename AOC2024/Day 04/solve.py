def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    board = read_input_file_data().splitlines()
    HEIGHT = len(board)
    WIDTH = len(board[0])
    count = 0
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if board[i][j] == 'X':
                if i-3 >= 0                     and board[i-1][j]   == 'M' and board[i-2][j]   == 'A' and board[i-3][j]   == 'S': # N
                    count += 1
                if i-3 >= 0     and j+3 < WIDTH and board[i-1][j+1] == 'M' and board[i-2][j+2] == 'A' and board[i-3][j+3] == 'S': # NE
                    count += 1
                if j+3 < WIDTH                  and board[i][j+1]   == 'M' and board[i][j+2]   == 'A' and board[i][j+3]   == 'S': # E
                    count += 1
                if i+3 < HEIGHT and j+3 < WIDTH and board[i+1][j+1] == 'M' and board[i+2][j+2] == 'A' and board[i+3][j+3] == 'S': # SE
                    count += 1
                if i+3 < HEIGHT                 and board[i+1][j]   == 'M' and board[i+2][j]   == 'A' and board[i+3][j]   == 'S': # S
                    count += 1
                if i+3 < HEIGHT and j-3 >= 0    and board[i+1][j-1] == 'M' and board[i+2][j-2] == 'A' and board[i+3][j-3] == 'S': # SW
                    count += 1
                if j-3 >= 0                     and board[i][j-1]   == 'M' and board[i][j-2]   == 'A' and board[i][j-3]   == 'S': # W
                    count += 1
                if i-3 >=0      and j-3 >= 0    and board[i-1][j-1] == 'M' and board[i-2][j-2] == 'A' and board[i-3][j-3] == 'S': # NW
                    count += 1
    return count

def solve_part_2():
    board = read_input_file_data().splitlines()
    HEIGHT = len(board)
    WIDTH = len(board[0])
    count = 0
    for i in range(1, HEIGHT - 1):
        for j in range(1, WIDTH - 1):
            if board[i][j] == 'A' and \
                ((board[i-1][j-1] == 'M' and board[i+1][j+1] == 'S') or (board[i-1][j-1] == 'S' and board[i+1][j+1] == 'M')) and \
                ((board[i-1][j+1] == 'M' and board[i+1][j-1] == 'S') or (board[i-1][j+1] == 'S' and board[i+1][j-1] == 'M')):
                count += 1
    return count
    
print(solve_part_2())
