def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    data = read_input_file_data().splitlines()[2:]
    def process_line(line: str):
        items = line.split()
        # Node
        node_details = items[0].split('-')
        x, y = int(node_details[1][1:]), int(node_details[2][1:])
        # Used
        used = int(items[2][:-1])
        # Avail
        avail = int(items[3][:-1])
        return (x, y, used, avail)

    nodes = list(map(process_line, data))

    viable_pairs = 0
    length = len(nodes)
    for i in range(length):
        for j in range(length):
            if i == j:
                continue
            # (x, y, used, avail)
            A = nodes[i]
            B = nodes[j]
            if A[2] != 0 and A[2] <= B[3]:
                viable_pairs += 1
                print(A, B)

    return viable_pairs

def solve_part_2():
    X_LEN = 33
    Y_LEN = 31
    grid_map = [[-1] * Y_LEN for i in range(X_LEN)]

    data = read_input_file_data().splitlines()[2:]
    for line in data:
        items = line.split()
        # Node
        node_details = items[0].split('-')
        x, y = int(node_details[1][1:]), int(node_details[2][1:])
        # Used
        used = int(items[2][:-1])
        # Avail
        avail = int(items[3][:-1])
        # grid_map[x][y] = f"{used}/{used + avail}"

        # Map style
        if used == 0:
            grid_map[x][y] = '_'
        elif used + avail > 100:
            grid_map[x][y] = '#'
        else:
            grid_map[x][y] = '.'
    grid_map[0][0] = 'S'
    grid_map[X_LEN - 1][0] = 'G'
    
    for x in range(X_LEN):
        print(''.join(grid_map[x]))
    
    # ONLY x3-y28 is very free (avail = 88T)
    '''
    x_max = 32
    y_max = 30
    By inspecting the data, we see that 
        - ONLY node-x3-y28 is very free
        - other nodes are mostly used
        - there is a wall of large files at y = 20 (except node-x0-y20)
    This means we need to keep using this ONLY free tile to move data from node-x32-y0 to node-x0-y0

    Move empty slot to x = 0 requires 3 steps
    Moving it to y = 0 required 28 steps
    Moving it to x = 31 required 31 steps
    Take 1 step towards goal
    For every other step forward, we need 5 steps to do the shifting.
    Since we need to move a total of 32 steps, this means we need another 31*5=155 steps worth of rotation

    Total steps = 3 + 28 + 31 + 1 + 155 = 218
    '''
    return 218

print(solve_part_2())
