def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    map = read_input_file_data().splitlines()
    HEIGHT = len(map)
    WIDTH = len(map[0])
    def find_starting_pos():
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if map[i][j] == '^':
                    return i, j
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4
    
    i, j = find_starting_pos()
    pos = UP
    visited = set()
    while (i >= 0 and i < HEIGHT) and (j >= 0 and j < WIDTH):
        visited.add((i, j))
        if pos == UP:
            if i-1 >=0 and map[i-1][j] == '#':
                pos = RIGHT
            else:
                i -= 1
        elif pos == RIGHT:
            if j+1 < WIDTH and map[i][j+1] == '#':
                pos = DOWN
            else:
                j += 1
        elif pos == DOWN:
            if i+1 < HEIGHT and map[i+1][j] == '#':
                pos = LEFT
            else:
                i += 1
        else:
            if j-1 >= 0 and map[i][j-1] == '#':
                pos = UP
            else:
                j -= 1
    return len(visited)

def solve_part_2():
    map = read_input_file_data().splitlines()
    HEIGHT = len(map)
    WIDTH = len(map[0])
    def find_starting_pos():
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if map[i][j] == '^':
                    return i, j
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    
    i, j = find_starting_pos()
    pos = UP
    visited = set()
    while (i >= 0 and i < HEIGHT) and (j >= 0 and j < WIDTH):
        visited.add((i, j))
        if pos == UP:
            if i-1 >=0 and map[i-1][j] == '#':
                pos = RIGHT
            else:
                i -= 1
        elif pos == RIGHT:
            if j+1 < WIDTH and map[i][j+1] == '#':
                pos = DOWN
            else:
                j += 1
        elif pos == DOWN:
            if i+1 < HEIGHT and map[i+1][j] == '#':
                pos = LEFT
            else:
                i += 1
        else:
            if j-1 >= 0 and map[i][j-1] == '#':
                pos = UP
            else:
                j -= 1

    obstacles = 0
    I, J = find_starting_pos()
    for i0, j0 in visited:
        i, j = I, J
        pos = UP
        loop_places = set()
        while (i >= 0 and i < HEIGHT) and (j >= 0 and j < WIDTH):
            if (i, j, pos) in loop_places:
                obstacles += 1
                break
            loop_places.add((i, j, pos))
            if pos == UP:
                if (i-1 >=0 and map[i-1][j] == '#') or (i-1 == i0 and j == j0):
                    pos = RIGHT
                else:
                    i -= 1
            elif pos == RIGHT:
                if (j+1 < WIDTH and map[i][j+1] == '#') or (i == i0 and j+1 == j0):
                    pos = DOWN
                else:
                    j += 1
            elif pos == DOWN:
                if (i+1 < HEIGHT and map[i+1][j] == '#') or (i+1 == i0 and j == j0):
                    pos = LEFT
                else:
                    i += 1
            else:
                if (j-1 >= 0 and map[i][j-1] == '#') or (i == i0 and j-1 == j0):
                    pos = UP
                else:
                    j -= 1
    
    return obstacles
    
print(solve_part_2())
