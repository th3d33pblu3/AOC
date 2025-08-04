def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def parse_data():
    data = read_input_file_data().split('\n\n')
    nums = list(map(int, data[0].split(',')))
    boards = list(map(lambda board: list(map(lambda line: list(map(int, line.split())), board.splitlines())), data[1:]))
    return nums, boards

def solve_part_1():
    nums, boards = parse_data() 
    NUM_BOARDS = len(boards)
    board_markings = [[[False] * 5 for _ in range(5)] for _ in range(NUM_BOARDS)]

    def mark_board(board_index, num):
        nonlocal board_markings
        board = boards[board_index]
        for row, line in enumerate(board):
            for col, n in enumerate(line):
                if n == num:
                    board_markings[board_index][row][col] = True
                    is_win = True
                    for r in range(5):
                        if not board_markings[board_index][r][col]:
                            is_win = False
                            break
                    if is_win:
                        return is_win
                    is_win = True
                    for c in range(5):
                        if not board_markings[board_index][row][c]:
                            is_win = False
                            break
                    return is_win
        return False
    
    for num in nums:
        for board_index in range(NUM_BOARDS):
            is_win = mark_board(board_index, num)
            if is_win:
                sum_unmarked = 0
                for r in range(5):
                    for c in range(5):
                        if not board_markings[board_index][r][c]:
                            sum_unmarked += boards[board_index][r][c]
                return sum_unmarked * num

def solve_part_2():
    nums, boards = parse_data() 
    NUM_BOARDS = len(boards)
    board_markings = [[[False] * 5 for _ in range(5)] for _ in range(NUM_BOARDS)]
    is_board_won = [False] * NUM_BOARDS

    def mark_board(board_index, num):
        nonlocal board_markings
        board = boards[board_index]
        for row, line in enumerate(board):
            for col, n in enumerate(line):
                if n == num:
                    board_markings[board_index][row][col] = True
                    is_win = True
                    for r in range(5):
                        if not board_markings[board_index][r][col]:
                            is_win = False
                            break
                    if is_win:
                        return is_win
                    is_win = True
                    for c in range(5):
                        if not board_markings[board_index][row][c]:
                            is_win = False
                            break
                    return is_win
        return False
    
    for num in nums:
        for board_index in range(NUM_BOARDS):
            if is_board_won[board_index]:
                continue
            is_win = mark_board(board_index, num)
            if is_win:
                is_board_won[board_index] = True
                if all(is_board_won):
                    sum_unmarked = 0
                    for r in range(5):
                        for c in range(5):
                            if not board_markings[board_index][r][c]:
                                sum_unmarked += boards[board_index][r][c]
                    return sum_unmarked * num
    
print(solve_part_2())
