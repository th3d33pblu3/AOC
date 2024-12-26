def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    data = read_input_file_data()
    lava_map = [list(map(int, line)) for line in data.splitlines()]

    HEIGHT = len(lava_map)
    WIDTH = len(lava_map[0])
    starting_pos = set()
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if lava_map[i][j] == 0:
                starting_pos.add((i, j))
    
    def get_score(p):
        pos = {p}

        def get_next_height(height, pos):
            new_pos = set()
            for i, j in pos:
                if i-1 >= 0 and lava_map[i-1][j] == height:
                    new_pos.add((i-1, j))
                if i+1 < HEIGHT and lava_map[i+1][j] == height:
                    new_pos.add((i+1, j))
                if j-1 >= 0 and lava_map[i][j-1] == height:
                    new_pos.add((i, j-1))
                if j+1 < WIDTH and lava_map[i][j+1] == height:
                    new_pos.add((i, j+1))
            return new_pos
        
        for height in range(1, 10):
            pos = get_next_height(height, pos)
        return len(pos)
    
    return sum(list(map(get_score, starting_pos)))

def solve_part_2():
    data = read_input_file_data()
    lava_map = [list(map(int, line)) for line in data.splitlines()]

    HEIGHT = len(lava_map)
    WIDTH = len(lava_map[0])
    pos = {}
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if lava_map[i][j] == 0:
                pos[(i, j)] = 1
    
    def get_next_height(height, pos):
        new_pos = {}
        for i, j in pos.keys():
            if i-1 >= 0 and lava_map[i-1][j] == height:
                new_pos[(i-1, j)] = new_pos.get((i-1, j), 0) + pos[(i, j)]
            if i+1 < HEIGHT and lava_map[i+1][j] == height:
                new_pos[(i+1, j)] = new_pos.get((i+1, j), 0) + pos[(i, j)]
            if j-1 >= 0 and lava_map[i][j-1] == height:
                new_pos[(i, j-1)] = new_pos.get((i, j-1), 0) + pos[(i, j)]
            if j+1 < WIDTH and lava_map[i][j+1] == height:
                new_pos[(i, j+1)] = new_pos.get((i, j+1), 0) + pos[(i, j)]
        return new_pos
    
    for height in range(1, 10):
        pos = get_next_height(height, pos)
    
    return sum(pos.values())
    
print(solve_part_2())
