def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    SIZE = 71
    bytes = list(map(lambda line: tuple(map(int, line.split(','))), read_input_file_data().splitlines()))
    space = [[0] * SIZE for _ in range(SIZE)]
    for byte in bytes[:1024]:
        i, j = byte
        space[i][j] = -1
    
    frontier = set()
    frontier.add((0, 0))
    space[0][0] = -1 # Prevent going back to starting location with step 0
    steps = 0
    while len(frontier) != 0:
        steps += 1
        new_frontier = set()
        for i0, j0 in frontier:
            i, j = i0-1, j0
            if i >= 0 and space[i][j] == 0:
                space[i][j] = steps
                new_frontier.add((i, j))
            i, j = i0+1, j0
            if i < SIZE and space[i][j] == 0:
                space[i][j] = steps
                new_frontier.add((i, j))
            i, j = i0, j0-1
            if j >=0 and space[i][j] == 0:
                space[i][j] = steps
                new_frontier.add((i, j))
            i, j = i0, j0+1
            if j < SIZE and space[i][j] == 0:
                space[i][j] = steps
                new_frontier.add((i, j))
        frontier = new_frontier
    return space[SIZE - 1][SIZE - 1]

def solve_part_2():
    SIZE = 71
    bytes = list(map(lambda line: tuple(map(int, line.split(','))), read_input_file_data().splitlines()))
    space = [[0] * SIZE for _ in range(SIZE)]
    for byte in bytes[:1024]: # Drop first 1024 bytes
        i, j = byte
        space[i][j] = -1
    space[0][0] = -1 # Prevent going back to starting location with step 0

    def end_reachable() -> bool:
        END = (SIZE - 1, SIZE - 1)
        visited = set()
        frontier = set()
        frontier.add((0, 0))
        while len(frontier) != 0:
            visited.update(frontier)
            if END in visited:
                return True
            new_frontier = set()
            for i0, j0 in frontier:
                i, j = i0-1, j0
                if i >= 0 and space[i][j] == 0 and (i, j) not in visited:
                    new_frontier.add((i, j))
                i, j = i0+1, j0
                if i < SIZE and space[i][j] == 0 and (i, j) not in visited:
                    new_frontier.add((i, j))
                i, j = i0, j0-1
                if j >=0 and space[i][j] == 0 and (i, j) not in visited:
                    new_frontier.add((i, j))
                i, j = i0, j0+1
                if j < SIZE and space[i][j] == 0 and (i, j) not in visited:
                    new_frontier.add((i, j))
            frontier = new_frontier
        return False

    byte_pointer = 1023
    current_byte = bytes[byte_pointer]
    while end_reachable():
        byte_pointer += 1
        current_byte = bytes[byte_pointer]
        space[current_byte[0]][current_byte[1]] = -1
    print(byte_pointer) # 2979
    return ','.join(tuple(map(str, current_byte)))
    
print(solve_part_2())
