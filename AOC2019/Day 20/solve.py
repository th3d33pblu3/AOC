def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def process_maze():
    data = read_input_file_data().splitlines()
    x_min = 2
    x_max = len(data[0]) - 3 # inclusive
    y_min = 2
    y_max = len(data) - 3 # inclusive
    
    cx_min = cx_max = cy_min = cy_max = -1
    for y, line in enumerate(data):
        x = line.find('# ')
        if x >= x_max or x == -1:
            continue
        cx_min = cx_min if cx_min != -1 else x + 1
        cx_max = cx_max if cx_max != -1 else line.find(' #', 2)
        cy_min = cy_min if cy_min != -1 else y
        cy_max = y

    assert cx_min != -1 and cx_max != -1 and cy_min != -1 and cy_max != -1
    return (x_min, x_max, y_min, y_max), (cx_min, cx_max, cy_min, cy_max)

def solve_part_1():
    maze = read_input_file_data().splitlines()
    (x_min, x_max, y_min, y_max), (cx_min, cx_max, cy_min, cy_max) = process_maze()

    # ---------- Register all teleporters -----------
    teleporters = {}
    unpaired_teleporters = {}
    # Top edge
    y = y_min
    for x in range(x_min + 1, x_max): # Teleporter cannot be at corners
        if maze[y][x] == '.':
            label = maze[y-2][x] + maze[y-1][x]
            if label in unpaired_teleporters:
                other_loc = unpaired_teleporters.pop(label)
                teleporters[(x, y)] = other_loc
                teleporters[other_loc] = (x, y)
            else:
                unpaired_teleporters[label] = (x, y)
    # Bottom edge
    y = y_max
    for x in range(x_min + 1, x_max): # Teleporter cannot be at corners
        if maze[y][x] == '.':
            label = maze[y+1][x] + maze[y+2][x]
            if label in unpaired_teleporters:
                other_loc = unpaired_teleporters.pop(label)
                teleporters[(x, y)] = other_loc
                teleporters[other_loc] = (x, y)
            else:
                unpaired_teleporters[label] = (x, y)
    # Left edge
    x = x_min
    for y in range(y_min + 1, y_max): # Teleporter cannot be at corners
        if maze[y][x] == '.':
            label = maze[y][x-2] + maze[y][x-1]
            if label in unpaired_teleporters:
                other_loc = unpaired_teleporters.pop(label)
                teleporters[(x, y)] = other_loc
                teleporters[other_loc] = (x, y)
            else:
                unpaired_teleporters[label] = (x, y)
    # Right edge
    x = x_max
    for y in range(y_min + 1, y_max): # Teleporter cannot be at corners
        if maze[y][x] == '.':
            label = maze[y][x+1] + maze[y][x+2]
            if label in unpaired_teleporters:
                other_loc = unpaired_teleporters.pop(label)
                teleporters[(x, y)] = other_loc
                teleporters[other_loc] = (x, y)
            else:
                unpaired_teleporters[label] = (x, y)
    # Center top edge
    y = cy_min - 1
    for x in range(cx_min + 1, cx_max): # Teleporter cannot be at corners
        if maze[y][x] == '.':
            label = maze[y+1][x] + maze[y+2][x]
            if label in unpaired_teleporters:
                other_loc = unpaired_teleporters.pop(label)
                teleporters[(x, y)] = other_loc
                teleporters[other_loc] = (x, y)
            else:
                unpaired_teleporters[label] = (x, y)
    # Center bottom edge
    y = cy_max + 1
    for x in range(cx_min + 1, cx_max): # Teleporter cannot be at corners
        if maze[y][x] == '.':
            label = maze[y-2][x] + maze[y-1][x]
            if label in unpaired_teleporters:
                other_loc = unpaired_teleporters.pop(label)
                teleporters[(x, y)] = other_loc
                teleporters[other_loc] = (x, y)
            else:
                unpaired_teleporters[label] = (x, y)
    # Center left edge
    x = cx_min - 1
    for y in range(cy_min + 1, cy_max): # Teleporter cannot be at corners
        if maze[y][x] == '.':
            label = maze[y][x+1] + maze[y][x+2]
            if label in unpaired_teleporters:
                other_loc = unpaired_teleporters.pop(label)
                teleporters[(x, y)] = other_loc
                teleporters[other_loc] = (x, y)
            else:
                unpaired_teleporters[label] = (x, y)
    # Center ight edge
    x = cx_max + 1
    for y in range(cy_min + 1, cy_max): # Teleporter cannot be at corners
        if maze[y][x] == '.':
            label = maze[y][x-2] + maze[y][x-1]
            if label in unpaired_teleporters:
                other_loc = unpaired_teleporters.pop(label)
                teleporters[(x, y)] = other_loc
                teleporters[other_loc] = (x, y)
            else:
                unpaired_teleporters[label] = (x, y)

    # ---------- Register start and end ----------
    START = unpaired_teleporters['AA']
    END = unpaired_teleporters['ZZ']

    # ---------- Flood maze ----------
    DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    frontier = set()
    frontier.add(START)
    steps = 0
    while frontier:
        steps += 1
        new_frontier = set()
        for (x, y) in frontier:
            if (x, y) in teleporters:
                if teleporters[(x, y)] not in visited: # Teleport to new location
                    new_frontier.add((teleporters[(x, y)]))
            for dx, dy in DELTAS:
                nx, ny = x + dx, y + dy
                if (nx, ny) == END: # Reached end, exit and return
                    return steps
                if (nx, ny) in visited: # Visited before, ignore
                    continue
                if ((nx < x_min) or (nx > x_max) or (ny < y_min) or (ny > y_max) or     # Out of range from side, ignore
                    (nx >= cx_min and nx <= cx_max and ny >= cy_min and ny <= cy_max)): # Out of range in center, ignore
                    continue
                if maze[ny][nx] == '#': # Hit wall, ignore
                    continue
                new_frontier.add((nx, ny)) # Walk to new location
        visited.update(frontier)
        frontier = new_frontier

def solve_part_2():
    maze = read_input_file_data().splitlines()
    (x_min, x_max, y_min, y_max), (cx_min, cx_max, cy_min, cy_max) = process_maze()

    # ---------- Register all teleporters -----------
    teleporters = {}
    unpaired_teleporters = {}
    # Top edge
    y = y_min
    for x in range(x_min + 1, x_max): # Teleporter cannot be at corners
        if maze[y][x] == '.':
            label = maze[y-2][x] + maze[y-1][x]
            if label in unpaired_teleporters:
                other_loc = unpaired_teleporters.pop(label)
                teleporters[(x, y)] = (other_loc, -1)
                teleporters[other_loc] = ((x, y), 1)
            else:
                unpaired_teleporters[label] = (x, y)
    # Bottom edge
    y = y_max
    for x in range(x_min + 1, x_max): # Teleporter cannot be at corners
        if maze[y][x] == '.':
            label = maze[y+1][x] + maze[y+2][x]
            if label in unpaired_teleporters:
                other_loc = unpaired_teleporters.pop(label)
                teleporters[(x, y)] = (other_loc, -1)
                teleporters[other_loc] = ((x, y), 1)
            else:
                unpaired_teleporters[label] = (x, y)
    # Left edge
    x = x_min
    for y in range(y_min + 1, y_max): # Teleporter cannot be at corners
        if maze[y][x] == '.':
            label = maze[y][x-2] + maze[y][x-1]
            if label in unpaired_teleporters:
                other_loc = unpaired_teleporters.pop(label)
                teleporters[(x, y)] = (other_loc, -1)
                teleporters[other_loc] = ((x, y), 1)
            else:
                unpaired_teleporters[label] = (x, y)
    # Right edge
    x = x_max
    for y in range(y_min + 1, y_max): # Teleporter cannot be at corners
        if maze[y][x] == '.':
            label = maze[y][x+1] + maze[y][x+2]
            if label in unpaired_teleporters:
                other_loc = unpaired_teleporters.pop(label)
                teleporters[(x, y)] = (other_loc, -1)
                teleporters[other_loc] = ((x, y), 1)
            else:
                unpaired_teleporters[label] = (x, y)
    # Center top edge
    y = cy_min - 1
    for x in range(cx_min + 1, cx_max): # Teleporter cannot be at corners
        if maze[y][x] == '.':
            label = maze[y+1][x] + maze[y+2][x]
            if label in unpaired_teleporters:
                other_loc = unpaired_teleporters.pop(label)
                teleporters[(x, y)] = (other_loc, 1)
                teleporters[other_loc] = ((x, y), -1)
            else:
                unpaired_teleporters[label] = (x, y)
    # Center bottom edge
    y = cy_max + 1
    for x in range(cx_min + 1, cx_max): # Teleporter cannot be at corners
        if maze[y][x] == '.':
            label = maze[y-2][x] + maze[y-1][x]
            if label in unpaired_teleporters:
                other_loc = unpaired_teleporters.pop(label)
                teleporters[(x, y)] = (other_loc, 1)
                teleporters[other_loc] = ((x, y), -1)
            else:
                unpaired_teleporters[label] = (x, y)
    # Center left edge
    x = cx_min - 1
    for y in range(cy_min + 1, cy_max): # Teleporter cannot be at corners
        if maze[y][x] == '.':
            label = maze[y][x+1] + maze[y][x+2]
            if label in unpaired_teleporters:
                other_loc = unpaired_teleporters.pop(label)
                teleporters[(x, y)] = (other_loc, 1)
                teleporters[other_loc] = ((x, y), -1)
            else:
                unpaired_teleporters[label] = (x, y)
    # Center ight edge
    x = cx_max + 1
    for y in range(cy_min + 1, cy_max): # Teleporter cannot be at corners
        if maze[y][x] == '.':
            label = maze[y][x-2] + maze[y][x-1]
            if label in unpaired_teleporters:
                other_loc = unpaired_teleporters.pop(label)
                teleporters[(x, y)] = (other_loc, 1)
                teleporters[other_loc] = ((x, y), -1)
            else:
                unpaired_teleporters[label] = (x, y)

    # ---------- Register start and end ----------
    START = (*unpaired_teleporters['AA'], 0)
    END = (*unpaired_teleporters['ZZ'], 0)

    # ---------- Flood maze ----------
    MAX_LEVEL_DEPTH = 100 # Set this manually to determine recursion strength
    DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    frontier = set()
    frontier.add(START)
    steps = 0
    while frontier:
        steps += 1
        new_frontier = set()
        for (x, y, level) in frontier:
            if (x, y) in teleporters:
                new_loc, dlevel = teleporters[(x, y)]
                new_level = level + dlevel
                if (*new_loc, new_level) not in visited and new_level >= 0 and new_level <= MAX_LEVEL_DEPTH:
                    new_frontier.add((*new_loc, new_level)) # Teleport to new location
            for dx, dy in DELTAS:
                nx, ny = x + dx, y + dy
                if (nx, ny, level) == END: # Reached end, exit and return
                    return steps
                if (nx, ny, level) in visited: # Visited before, ignore
                    continue
                if ((nx < x_min) or (nx > x_max) or (ny < y_min) or (ny > y_max) or     # Out of range from side, ignore
                    (nx >= cx_min and nx <= cx_max and ny >= cy_min and ny <= cy_max)): # Out of range in center, ignore
                    continue
                if maze[ny][nx] == '#': # Hit wall, ignore
                    continue
                new_frontier.add((nx, ny, level)) # Walk to new location
        visited.update(frontier)
        frontier = new_frontier
    
print(solve_part_2())
