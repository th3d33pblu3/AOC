def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    '''
    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
        | 0 | A |
        +---+---+
    '''
    NUMPAD = {
        'A': (0, 0),
        '0': (1, 0),
        '1': (2, 1),
        '2': (1, 1),
        '3': (0, 1),
        '4': (2, 2),
        '5': (1, 2),
        '6': (0, 2),
        '7': (2, 3),
        '8': (1, 3),
        '9': (0, 3)
    }
    '''
        +---+---+
        | ^ | A |
    +---+---+---+
    | < | v | > |
    +---+---+---+
    '''
    DIRPAD = {
        'A': (0, 1),
        '^': (1, 1),
        '<': (2, 0),
        'v': (1, 0),
        '>': (0, 0)
    }

    def enter_code(code) -> int:
        # print(code)
        dirpad1_ins = ''
        numpad_pos = (0, 0)
        for btn in code:
            dirpad1_ins += press_num_pad(btn, numpad_pos)
            numpad_pos = NUMPAD[btn]
        # print(dirpad1_ins)
        
        dirpad2_ins = ''
        dirpad1_pos = (0, 1)
        for btn in dirpad1_ins:
            dirpad2_ins += press_dirpad(btn, dirpad1_pos)
            dirpad1_pos = DIRPAD[btn]
        # print(dirpad2_ins)

        my_ins = ''
        dirpad2_pos = (0, 1)
        for btn in dirpad2_ins:
            my_ins += press_dirpad(btn, dirpad2_pos)
            dirpad2_pos = DIRPAD[btn]
        # print(my_ins)
        return len(my_ins)
    
    def press_num_pad(btn, numpad_pos):
        tx, ty = NUMPAD[btn]
        sx, sy = numpad_pos
        if ty >= sy and tx >= sx:
            # top left
            if sy == 0 and tx == 2: # to prevent error
                return '^' * (ty - sy) + '<' * (tx - sx) + 'A'
            else: # optimization
                return '<' * (tx - sx) + '^' * (ty - sy) + 'A'
        elif ty >= sy and tx < sx:
            # top right
            return '^' * (ty - sy) + '>' * (sx - tx) + 'A'
        elif ty < sy and tx >= sx:
            # bottom left
            return 'v' * (sy - ty) + '<' * (tx - sx) + 'A'
        elif ty < sy and tx < sx:
            # bottom right
            if ty == 0 and sx == 2: # to prevent error
                return '>' * (sx - tx) + 'v' * (sy - ty) + 'A'
            else: # optimization
                return 'v' * (sy - ty) + '>' * (sx - tx) + 'A'
        else:
            raise Exception("Unexpected error")

    def press_dirpad(btn, dirpad_pos):
        tx, ty = DIRPAD[btn]
        sx, sy = dirpad_pos
        if ty >= sy and tx >= sx:
            # top left
            return '^' * (ty - sy) + '<' * (tx - sx) + 'A'
        elif ty >= sy and tx < sx:
            # top right # to prevent error
            return '>' * (sx - tx) + '^' * (ty - sy) + 'A'
        elif ty < sy and tx >= sx:
            # bottom left # to prevent error
            return 'v' * (sy - ty) + '<' * (tx - sx) + 'A'
        elif ty < sy and tx < sx:
            # bottom right
            return '>' * (sx - tx) + 'v' * (sy - ty) + 'A'
        else:
            raise Exception("Unexpected error")

    codes = read_input_file_data().splitlines()
    total_complexity = 0
    for code in codes:
        length = enter_code(code)
        total_complexity += int(code[:-1]) * length
        # print(code, length, int(code[:-1]))
    return total_complexity

def solve_part_2():
    '''
    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
        | 0 | A |
        +---+---+
    '''
    NUMPAD = {
        'A': (0, 0),
        '0': (1, 0),
        '1': (2, 1),
        '2': (1, 1),
        '3': (0, 1),
        '4': (2, 2),
        '5': (1, 2),
        '6': (0, 2),
        '7': (2, 3),
        '8': (1, 3),
        '9': (0, 3)
    }
    '''
        +---+---+
        | ^ | A |
    +---+---+---+
    | < | v | > |
    +---+---+---+
    '''
    DIRPAD = {
        'A': (0, 1),
        '^': (1, 1),
        '<': (2, 0),
        'v': (1, 0),
        '>': (0, 0)
    }
    NUM_DIRPAD_ROBOTS = 25

    '''
    Take not that when moving to digonal grids, the order of the
    combination of the 2 directions matters. The more optimal one
    is the one that leaves the next robot closer to 'A'.
    '''

    def get_first_robot_ins(btn, curr_robot_pos):
        '''
        Get the DIRPAD instructions from the next robot to press
        the given NUMPAD button from the given robot position.
        '''
        tx, ty = NUMPAD[btn]
        sx, sy = curr_robot_pos
        if ty >= sy and tx >= sx:
            # top left
            if sy == 0 and tx == 2: # to prevent error
                return '^' * (ty - sy) + '<' * (tx - sx) + 'A'
            else: # optimization
                return '<' * (tx - sx) + '^' * (ty - sy) + 'A'
        elif ty >= sy and tx < sx:
            # top right
            return '^' * (ty - sy) + '>' * (sx - tx) + 'A'
        elif ty < sy and tx >= sx:
            # bottom left
            return 'v' * (sy - ty) + '<' * (tx - sx) + 'A'
        elif ty < sy and tx < sx:
            # bottom right
            if ty == 0 and sx == 2: # to prevent error
                return '>' * (sx - tx) + 'v' * (sy - ty) + 'A'
            else: # optimization
                return 'v' * (sy - ty) + '>' * (sx - tx) + 'A'
        else:
            raise Exception("Unexpected error")

    robot_moves = {} # Use memoization to speed things up
    def get_next_robot_ins(btn, curr_robot_pos):
        '''
        Get the DIRPAD instructions from the next robot to press
        the given DIRPAD button from the given robot position.
        Uses memoization to save time.
        '''
        key = (*curr_robot_pos, btn)
        if key in robot_moves:
            return robot_moves[key]

        tx, ty = DIRPAD[btn]
        sx, sy = curr_robot_pos
        ins = None
        if ty >= sy and tx >= sx:
            # top left
            ins = '<' * (tx - sx) + '^' * (ty - sy) + 'A'
        elif ty >= sy and tx < sx:
            # top right # to prevent error
            if sx == 2:
                ins = '>' * (sx - tx) + '^' * (ty - sy) + 'A'
            else: # optimization
                ins = '^' * (ty - sy) + '>' * (sx - tx) + 'A'
        elif ty < sy and tx >= sx:
            # bottom left # to prevent error
            if tx == 2:
                ins = 'v' * (sy - ty) + '<' * (tx - sx) + 'A'
            else: # optimization
                ins = '<' * (tx - sx) + 'v' * (sy - ty) + 'A'
        elif ty < sy and tx < sx:
            # bottom right
            ins = 'v' * (sy - ty) + '>' * (sx - tx) + 'A'
        else:
            raise Exception("Unexpected error")
        robot_moves[key] = ins
        return ins
    
    '''
    Determine the required number of instructions by me for a given 
    DIRPAD robot to press the given DIRPAD button from the given
    robot position.
    Uses memoization to save time.
    '''
    robot_btn_lens = [{} for _ in range(NUM_DIRPAD_ROBOTS)]
    last_robot_ins_len = {} # Setup base case
    keys, values = DIRPAD.keys(), DIRPAD.values()
    for key in keys:
        for value in values:
            last_robot_ins_len[(*value, key)] = len(get_next_robot_ins(key, value))
    robot_btn_lens[-1] = last_robot_ins_len

    def enter_code(code) -> int:
        first_robot_ins = ''
        numpad_pos = NUMPAD['A']
        for btn in code:
            first_robot_ins += get_first_robot_ins(btn, numpad_pos)
            numpad_pos = NUMPAD[btn]
            
        robot_positions = [DIRPAD['A'] for _ in range(NUM_DIRPAD_ROBOTS)]
        def get_ins_len(r, ins):
            robot_btn_len = robot_btn_lens[r]
            ins_len = 0
            for btn in ins:
                key = (*robot_positions[r], btn)
                if key not in robot_btn_len:
                    next_robot_ins = get_next_robot_ins(btn, robot_positions[r])
                    btn_len = get_ins_len(r+1, next_robot_ins)
                    robot_btn_len[key] = btn_len
                ins_len += robot_btn_len[key]
                robot_positions[r] = DIRPAD[btn]
            return ins_len

        return get_ins_len(0, first_robot_ins)
    
    codes = read_input_file_data().splitlines()
    total_complexity = 0
    for code in codes:
        length = enter_code(code)
        total_complexity += int(code[:-1]) * length
    return total_complexity
    
print(solve_part_2())
