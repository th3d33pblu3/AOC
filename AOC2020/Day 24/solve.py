def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    instructions = read_input_file_data().splitlines()
    tiles = set()
    for line in instructions:
        ne, se = 0, 0
        ins_len = len(line)
        ptr = 0
        while ptr < ins_len:
            char = line[ptr]
            ptr += 1
            if char == 'e':
                ne += 1
                se += 1
            elif char == 'w':
                ne -= 1
                se -= 1
            elif char == 'n':
                char2 = line[ptr]
                ptr += 1
                if char2 == 'e':
                    ne += 1
                elif char2 == 'w':
                    se -= 1
            elif char == 's':
                char2 = line[ptr]
                ptr += 1
                if char2 == 'e':
                    se += 1
                elif char2 == 'w':
                    ne -= 1
        # Restructuring coordinates
        key = (ne, se)
        if key in tiles:
            tiles.remove(key)
        else:
            tiles.add(key)
    return len(tiles)

def solve_part_2():
    instructions = read_input_file_data().splitlines()
    tiles = set()
    for line in instructions:
        ne, se = 0, 0
        ins_len = len(line)
        ptr = 0
        while ptr < ins_len:
            char = line[ptr]
            ptr += 1
            if char == 'e':
                ne += 1
                se += 1
            elif char == 'w':
                ne -= 1
                se -= 1
            elif char == 'n':
                char2 = line[ptr]
                ptr += 1
                if char2 == 'e':
                    ne += 1
                elif char2 == 'w':
                    se -= 1
            elif char == 's':
                char2 = line[ptr]
                ptr += 1
                if char2 == 'e':
                    se += 1
                elif char2 == 'w':
                    ne -= 1
        # Restructuring coordinates
        key = (ne, se)
        if key in tiles:
            tiles.remove(key)
        else:
            tiles.add(key)

    # Define helper functions
    DELTAS = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1)]
    def get_neighbours(tile):
        return list(map(lambda delta: (delta[0]+tile[0], delta[1]+tile[1]), DELTAS))
    def count_adj_black(tile):
        nonlocal black_tiles
        neighbours = get_neighbours(tile)
        count = 0
        for neighbour in neighbours:
            if neighbour in black_tiles:
                count += 1
        return count
    
    # Computation
    black_tiles = tiles
    for _ in range(100):
        frontier = set()
        for tile in black_tiles:
            frontier.update(get_neighbours(tile))
        
        new_black_tiles = set()
        for tile in frontier:
            adj_black = count_adj_black(tile)
            if tile in black_tiles: # black tile
                if adj_black in (1, 2):
                    new_black_tiles.add(tile)
            else: # white tile
                if adj_black == 2:
                    new_black_tiles.add(tile)
        
        black_tiles = new_black_tiles
    return len(black_tiles)
    
print(solve_part_2())
