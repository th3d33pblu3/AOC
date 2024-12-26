def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    WALL = '#'
    BOX = 'O'
    EMPTY = '.'
    UP = '^'
    DOWN = 'v'
    LEFT = '<'
    RIGHT = '>'

    unparsed_map, movements = read_input_file_data().split("\n\n")
    def parse_map(unparsed_map: str):
        robot_pos = None
        warehouse_map = [list(line) for line in unparsed_map.splitlines()]
        WIDTH = len(warehouse_map[0])
        for i in range(len(warehouse_map)):
            for j in range(WIDTH):
                if warehouse_map[i][j] == '@':
                    robot_pos = (i, j)
                    warehouse_map[i][j] = EMPTY
                    return warehouse_map, robot_pos

    warehouse_map, robot_pos = parse_map(unparsed_map)

    def move(dir):
        nonlocal warehouse_map, robot_pos
        i, j = robot_pos
        if dir == UP:
            target_pos = (i-1, j)
        elif dir == DOWN:
            target_pos = (i+1, j)
        elif dir == LEFT:
            target_pos = (i, j-1)
        elif dir == RIGHT:
            target_pos = (i, j+1)
        else:
            raise Exception(f"Unknown direction {dir}")
        ti, tj = target_pos
        if warehouse_map[ti][tj] == EMPTY:
            robot_pos = target_pos
            return
        elif warehouse_map[ti][tj] == WALL:
            return
        elif warehouse_map[ti][tj] == BOX:
            first_empty = None
            ci, cj = target_pos
            while True:
                curr_sel = warehouse_map[ci][cj]
                if curr_sel == WALL:
                    break
                elif curr_sel == EMPTY:
                    first_empty = (ci, cj)
                    break
                elif curr_sel == BOX:
                    if dir == UP:
                        ci -= 1
                    elif dir == DOWN:
                        ci += 1
                    elif dir == LEFT:
                        cj -= 1
                    elif dir == RIGHT:
                        cj += 1
                else:
                    raise Exception(f"Unknown target {curr_sel}")
            if first_empty != None:
                warehouse_map[first_empty[0]][first_empty[1]] = BOX
                warehouse_map[target_pos[0]][target_pos[1]] = EMPTY
                robot_pos = target_pos
                return
            else:
                return
    
    for direction in movements.replace('\n', ''):
        move(direction)
    
    def calculate_GPS(warehouse_map):
        total_gps = 0
        WIDTH = len(warehouse_map[0])
        for i in range(len(warehouse_map)):
            for j in range(WIDTH):
                if warehouse_map[i][j] == BOX:
                    total_gps += i * 100 + j
        return total_gps
    return calculate_GPS(warehouse_map)

def solve_part_2():
    WALL = '#'
    BOX_LEFT = '['
    BOX_RIGHT = ']'
    EMPTY = '.'
    UP = '^'
    DOWN = 'v'
    LEFT = '<'
    RIGHT = '>'

    unparsed_map, movements = read_input_file_data().split("\n\n")
    def parse_map(unparsed_map: str):
        ROBOT = '@'
        BOX = 'O'
        def extend(line):
            new_line = []
            for x in line:
                if x == WALL:
                    new_line.append(WALL)
                    new_line.append(WALL)
                elif x == BOX:
                    new_line.append(BOX_LEFT)
                    new_line.append(BOX_RIGHT)
                elif x == EMPTY:
                    new_line.append(EMPTY)
                    new_line.append(EMPTY)
                elif x == ROBOT:
                    new_line.append(ROBOT)
                    new_line.append(EMPTY)
            return new_line

        robot_pos = None
        warehouse_map = [extend(list(line)) for line in unparsed_map.splitlines()]
        WIDTH = len(warehouse_map[0])
        for i in range(len(warehouse_map)):
            for j in range(WIDTH):
                if warehouse_map[i][j] == ROBOT:
                    robot_pos = (i, j)
                    warehouse_map[i][j] = EMPTY
                    return warehouse_map, robot_pos

    warehouse_map, robot_pos = parse_map(unparsed_map)

    def move(dir):
        nonlocal robot_pos
        i, j = robot_pos
        if dir == UP:
            target_pos = (i-1, j)
        elif dir == DOWN:
            target_pos = (i+1, j)
        elif dir == LEFT:
            target_pos = (i, j-1)
        elif dir == RIGHT:
            target_pos = (i, j+1)
        else:
            raise Exception(f"Unknown direction {dir}")
        ti, tj = target_pos
        if warehouse_map[ti][tj] == EMPTY:
            robot_pos = target_pos
            return
        elif warehouse_map[ti][tj] == WALL:
            return
        elif warehouse_map[ti][tj] == BOX_LEFT:
            if can_move_box((ti, tj), (ti, tj+1), dir):
                move_box((ti, tj), (ti, tj+1), dir)
                robot_pos = target_pos
                return
            else:
                return
        elif warehouse_map[ti][tj] == BOX_RIGHT:
            if can_move_box((ti, tj-1), (ti, tj), dir):
                move_box((ti, tj-1), (ti, tj), dir)
                robot_pos = target_pos
                return
            else:
                return
    
    def can_move_box(box_left, box_right, dir) -> bool:
        if dir == LEFT or dir == RIGHT:
            ci, cj = box_left if dir == LEFT else box_right
            increment = -1 if dir == LEFT else 1
            while True:
                curr_sel = warehouse_map[ci][cj]
                if curr_sel == WALL:
                    return False
                elif curr_sel == EMPTY:
                    return True
                else: # BOX_LEFT or BOX_RIGHT
                    cj += increment
        else:
            increment = -1 if dir == UP else 1
            i = box_left[0] + increment
            j1, j2 = box_left[1], box_right[1]
            return can_move_item(warehouse_map[i][j1], (i, j1), dir) and can_move_item(warehouse_map[i][j2], (i, j2), dir)
    
    def can_move_item(item, pos, dir):
        if item == WALL:
            return False
        elif item == EMPTY:
            return True
        elif item == BOX_LEFT:
            return can_move_box(pos, (pos[0], pos[1] + 1), dir)
        elif item == BOX_RIGHT:
            return can_move_box((pos[0], pos[1] - 1), pos, dir)
            
    def move_box(box_left, box_right, dir):
        nonlocal warehouse_map
        if dir == LEFT:
            warehouse_map[box_right[0]][box_right[1]] = EMPTY
            ci, cj = box_left
            while warehouse_map[ci][cj] != EMPTY:
                if warehouse_map[ci][cj] == BOX_LEFT:
                    warehouse_map[ci][cj] = BOX_RIGHT
                elif warehouse_map[ci][cj] == BOX_RIGHT:
                    warehouse_map[ci][cj] = BOX_LEFT
                else:
                    raise Exception(f"Unmovable object {warehouse_map[ci][cj]}")
                cj -= 1
            warehouse_map[ci][cj] = BOX_LEFT
            return
        elif dir == RIGHT:
            warehouse_map[box_left[0]][box_left[1]] = EMPTY
            ci, cj = box_right
            while warehouse_map[ci][cj] != EMPTY:
                if warehouse_map[ci][cj] == BOX_LEFT:
                    warehouse_map[ci][cj] = BOX_RIGHT
                elif warehouse_map[ci][cj] == BOX_RIGHT:
                    warehouse_map[ci][cj] = BOX_LEFT
                else:
                    raise Exception(f"Unmovable object {warehouse_map[ci][cj]}")
                cj += 1
            warehouse_map[ci][cj] = BOX_RIGHT
            return
        elif dir == UP or dir == DOWN:
            i = box_left[0]
            j1, j2 = box_left[1], box_right[1]
            # Make current box space empty
            warehouse_map[i][j1] = EMPTY
            warehouse_map[i][j2] = EMPTY
            # Make target space empty
            i += -1 if dir == UP else 1
            if warehouse_map[i][j1] == BOX_LEFT:
                move_box((i, j1), (i, j1+1), dir)
            elif warehouse_map[i][j1] == BOX_RIGHT:
                move_box((i, j1-1), (i, j1), dir)
            if warehouse_map[i][j2] == BOX_LEFT:
                move_box((i, j2), (i, j2+1), dir)
            elif warehouse_map[i][j2] == BOX_RIGHT:
                # move_box((i, j2-1), (i, j2), dir)
                raise Exception("THIS BOX SHOULD BE MOVED!")
            # Move to target
            warehouse_map[i][j1] = BOX_LEFT
            warehouse_map[i][j2] = BOX_RIGHT
    
    for direction in movements.replace('\n', ''):
        move(direction)
    
    def calculate_GPS(warehouse_map):
        total_gps = 0
        WIDTH = len(warehouse_map[0])
        for i in range(len(warehouse_map)):
            for j in range(WIDTH):
                if warehouse_map[i][j] == BOX_LEFT:
                    total_gps += i * 100 + j
        return total_gps
    return calculate_GPS(warehouse_map)
    
print(solve_part_2())
