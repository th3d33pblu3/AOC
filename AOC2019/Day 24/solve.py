def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    states = set()
    curr_state = list(map(list, read_input_file_data().splitlines()))
    curr_key = ''.join(list(map(lambda x: ''.join(x), curr_state)))

    BUG = '#'
    EMPTY = '.'
    WIDTH = len(curr_state[0])
    HEIGHT = len(curr_state)
    DELTAS = ((0, -1), (0, 1), (-1, 0), (1, 0))

    def get_num_adj_bugs(x, y):
        nonlocal curr_state
        count = 0
        for dx, dy in DELTAS:
            (nx, ny) = (x + dx, y + dy)
            if nx < 0 or nx >= WIDTH or ny < 0 or ny >= HEIGHT:
                continue
            if curr_state[ny][nx] == BUG:
                count += 1
        return count
    
    while curr_key not in states:
        states.add(curr_key)
        new_state = [[None] * WIDTH for _ in range(HEIGHT)]
        for x in range(WIDTH):
            for y in range(HEIGHT):
                tile = curr_state[y][x]
                adj_bugs = get_num_adj_bugs(x, y)
                if tile == BUG:
                    new_state[y][x] = BUG if adj_bugs == 1 else EMPTY
                elif tile == EMPTY:
                    new_state[y][x] = BUG if adj_bugs in (1, 2) else EMPTY
        curr_state = new_state
        curr_key = ''.join(list(map(lambda x: ''.join(x), new_state)))
    
    biodiversity_rating = 0
    for i, tile in enumerate(curr_key):
        if tile == BUG:
            biodiversity_rating += pow(2, i)
    return biodiversity_rating

def solve_part_2():
    bugs = set() # (tile, layer)
    # Using the tile numbering as in the question
    tile = 1
    for line in read_input_file_data().splitlines():
        for char in line:
            if char == '#':
                bugs.add((tile, 1))
            tile += 1

    def get_adj_grids(grid):
        tile, layer = grid
        match tile:
            case 1:
                return [(8, layer-1), (2, layer), (6, layer), (12, layer-1)]
            case 2:
                return [(8, layer-1), (3, layer), (7, layer), (1, layer)]
            case 3:
                return [(8, layer-1), (4, layer), (8, layer), (2, layer)]
            case 4:
                return [(8, layer-1), (5, layer), (9, layer), (3, layer)]
            case 5:
                return [(8, layer-1), (14, layer-1), (10, layer), (4, layer)]
            case 6:
                return [(1, layer), (7, layer), (11, layer), (12, layer-1)]
            case 7:
                return [(2, layer), (8, layer), (12, layer), (6, layer)]
            case 8:
                return [(3, layer), (9, layer), (1, layer+1), (2, layer+1), (3, layer+1), (4, layer+1), (5, layer+1), (7, layer)]
            case 9:
                return [(4, layer), (10, layer), (14, layer), (8, layer)]
            case 10:
                return [(5, layer), (14, layer-1), (15, layer), (9, layer)]
            case 11:
                return [(6, layer), (12, layer), (16, layer), (12, layer-1)]
            case 12:
                return [(7, layer), (1, layer+1), (6, layer+1), (11, layer+1), (16, layer+1), (21, layer+1), (17, layer), (11, layer)]
            case 14:
                return [(9, layer), (15, layer), (19, layer), (5, layer+1), (10, layer+1), (15, layer+1), (20, layer+1), (25, layer+1)]
            case 15:
                return [(10, layer), (14, layer-1), (20, layer), (14, layer)]
            case 16:
                return [(11, layer), (17, layer), (21, layer), (12, layer-1)]
            case 17:
                return [(12, layer), (18, layer), (22, layer), (16, layer)]
            case 18:
                return [(21, layer+1), (22, layer+1), (23, layer+1), (24, layer+1), (25, layer+1), (19, layer), (23, layer), (17, layer)]
            case 19:
                return [(14, layer), (20, layer), (24, layer), (18, layer)]
            case 20:
                return [(15, layer), (14, layer-1), (25, layer), (19, layer)]
            case 21:
                return [(16, layer), (22, layer), (18, layer-1), (12, layer-1)]
            case 22:
                return [(17, layer), (23, layer), (18, layer-1), (21, layer)]
            case 23:
                return [(18, layer), (24, layer), (18, layer-1), (22, layer)]
            case 24:
                return [(19, layer), (25, layer), (18, layer-1), (23, layer)]
            case 25:
                return [(20, layer), (14, layer-1), (18, layer-1), (24, layer)]

    def get_num_adj_bugs(grid):
        nonlocal bugs
        adj_grids = get_adj_grids(grid)
        count = 0
        for g in adj_grids:
            if g in bugs:
                count += 1
        return count
    
    for _ in range(200):
        affected_grids = set()
        for bug_grid in bugs:
            affected_grids.update(get_adj_grids(bug_grid))
        new_bugs = set()
        for grid in affected_grids:
            if grid in bugs:
                if get_num_adj_bugs(grid) == 1:
                    new_bugs.add(grid)
            else:
                if get_num_adj_bugs(grid) in (1, 2):
                    new_bugs.add(grid)
        bugs = new_bugs
    return len(bugs)
    
print(solve_part_2())
