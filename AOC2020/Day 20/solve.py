import math

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def parse_data():
    data = read_input_file_data().split('\n\n')
    def parse_tile_data(tile_data):
        lines = tile_data.splitlines()
        id = int(lines[0][5:9])
        tiles = lines[1:]
        return (id, tiles)
    return list(map(parse_tile_data, data))

def solve_part_1():
    tiles = parse_data()
    BIT_LENGTH = len(tiles[0][1])
    NUM_TILES = len(tiles)
    MAP_SIZE = int(math.sqrt(NUM_TILES))

    def parse_edges(tile):
        id, tile_map = tile
        xy = [
        #     x                                    y
            ( list(range(BIT_LENGTH)),             [0] * BIT_LENGTH                    ), # Top
            ( [BIT_LENGTH - 1] * BIT_LENGTH,       list(range(BIT_LENGTH))             ), # Right
            ( list(range(BIT_LENGTH - 1, -1, -1)), [BIT_LENGTH - 1] * BIT_LENGTH       ), # Bottom
            ( [0] * BIT_LENGTH,                    list(range(BIT_LENGTH - 1, -1, -1)) )  # Left
        ]

        edge_values = []
        for xs, ys in xy:
            value = 0
            for (x, y) in zip(xs, ys):
                value *= 2
                if tile_map[y][x] == '#':
                    value += 1
            edge_values.append(value)

        return id, tuple(edge_values)
    
    def flip(num):
        return int(bin(num)[2:].zfill(BIT_LENGTH)[::-1], 2)
    
    def move(tile, direction):
        while True:
            id = tile[0]
            val = tile[1][direction]
            inv_val = flip(val)

            # Find connecting tile
            connecting_tile = list(filter(lambda tile: tile[0] != id and (val in tile[1] or inv_val in tile[1]), tiles))
            if len(connecting_tile) == 0:
                return tile
            assert len(connecting_tile) == 1
            tile = connecting_tile[0]

            # Rotate tile accordingly
            id = tile[0]
            tile_edges = tile[1]
            i = tile_edges.index(val) if val in tile_edges else tile_edges.index(inv_val)
            tile_edges = tile_edges[i:] + tile_edges[:i]
            if val in tile_edges: # Because the matching tile should have val_inv instead to match
                tile_edges = (flip(tile_edges[0]), flip(tile_edges[3]), flip(tile_edges[2]), flip(tile_edges[1]))
            target_i = direction + 2 % 4
            pads = 4 - target_i
            tile_edges = tile_edges[pads:] + tile_edges[:pads]
            tile = (id, tile_edges)
    
    tiles = list(map(parse_edges, tiles))
    corner_tile_ids = []
    
    focus_tile = tiles[0]
    # Move to top edge
    focus_tile = move(focus_tile, 0) # (2311, (210, 89, 924, 318)) (3079, (184, 89, 501, 264))

    # Move to top right corner
    focus_tile = move(focus_tile, 1)
    corner_tile_ids.append(focus_tile[0])

    # Move to bottom right corner
    focus_tile = move(focus_tile, 2)
    corner_tile_ids.append(focus_tile[0])

    # Move to bottom left corner
    focus_tile = move(focus_tile, 3)
    corner_tile_ids.append(focus_tile[0])

    # Move to top left corner
    focus_tile = move(focus_tile, 0)
    corner_tile_ids.append(focus_tile[0])

    return math.prod(corner_tile_ids)

def solve_part_2():
    '''
    Input parsing
    '''
    tiles = parse_data()
    BIT_LENGTH = len(tiles[0][1])
    NUM_TILES = len(tiles)
    MAP_SIZE = int(math.sqrt(NUM_TILES))

    '''
    Helper functions
    '''
    def parse_edges(tile):
        id, tile_map = tile
        xy = [
        #     x                                    y
            ( list(range(BIT_LENGTH)),             [0] * BIT_LENGTH                    ), # Top
            ( [BIT_LENGTH - 1] * BIT_LENGTH,       list(range(BIT_LENGTH))             ), # Right
            ( list(range(BIT_LENGTH - 1, -1, -1)), [BIT_LENGTH - 1] * BIT_LENGTH       ), # Bottom
            ( [0] * BIT_LENGTH,                    list(range(BIT_LENGTH - 1, -1, -1)) )  # Left
        ]

        edge_values = []
        for xs, ys in xy:
            value = 0
            for (x, y) in zip(xs, ys):
                value *= 2
                if tile_map[y][x] == '#':
                    value += 1
            edge_values.append(value)

        return id, tuple(edge_values)
    
    def flip(num):
        return int(bin(num)[2:].zfill(BIT_LENGTH)[::-1], 2)
    
    def move(tile, direction, num_steps=float('inf')):
        steps = 0
        while steps < num_steps:
            id = tile[0]
            val = tile[1][direction]
            inv_val = flip(val)

            # Find connecting tile
            connecting_tile = list(filter(lambda tile: tile[0] != id and (val in tile[1] or inv_val in tile[1]), tiles))
            if len(connecting_tile) == 0:
                return tile
            assert len(connecting_tile) == 1
            tile = connecting_tile[0]

            # Rotate tile accordingly
            id = tile[0]
            tile_edges = tile[1]
            i = tile_edges.index(val) if val in tile_edges else tile_edges.index(inv_val)
            tile_edges = tile_edges[i:] + tile_edges[:i]
            if val in tile_edges: # Because the matching tile should have val_inv instead to match
                tile_edges = (flip(tile_edges[0]), flip(tile_edges[3]), flip(tile_edges[2]), flip(tile_edges[1]))
            target_i = direction + 2 % 4
            pads = 4 - target_i
            tile_edges = tile_edges[pads:] + tile_edges[:pads]
            tile = (id, tile_edges)

            # Update steps
            steps += 1
        return tile
    
    '''
    Find top left tile
    '''
    tiles = list(map(parse_edges, tiles))
    focus_tile = tiles[0]
    # Move to top edge
    focus_tile = move(focus_tile, 0) # (2311, (210, 89, 924, 318)) (3079, (184, 89, 501, 264))
    # Move to top left corner
    focus_tile = move(focus_tile, 3)

    '''
    Get all the tiles of the actual map in edge number form
    '''
    map_tiles = []
    row_leading_tile = focus_tile
    for _ in range(MAP_SIZE):
        row_tiles = []
        row_tiles.append(row_leading_tile)

        # Fill row tiles
        curr_tile = row_leading_tile
        for _ in range(MAP_SIZE - 1):
            curr_tile = move(curr_tile, 1, 1)
            row_tiles.append(curr_tile)
        
        # Record row
        map_tiles.append(row_tiles)

        # Prepare for next row
        if _ == MAP_SIZE- 1:
            break
        row_leading_tile = move(row_leading_tile, 2, 1)
    
    '''
    Get all the tiles of the actual map in data form
    '''
    # Get tile dict for quicker reference
    tile_dict = {}
    for tile in parse_data():
        id, data = tile
        edges = parse_edges(tile)[1]
        tile_dict[id] = (data, edges)

    def get_rotated_stripped_tile(tile):
        id, actual_edge_orien = tile
        a, b, c, d = actual_edge_orien
        ap, bp, cp, dp = flip(a), flip(b), flip(c), flip(d)
        tile_data, edge_orien = tile_dict[id]

        if edge_orien == (a, b, c, d): # Same orientation (row, col)
            data = []
            for row in range(1, BIT_LENGTH - 1):
                data.append(tile_data[row][1:-1])
            return data
        elif edge_orien == (b, c, d, a): # Rotated left once (col inv, row)
            data = [['.'] * (BIT_LENGTH - 2) for _ in range(BIT_LENGTH - 2)]
            for i in range(BIT_LENGTH - 2):
                for j in range(BIT_LENGTH - 2):
                    data[i][j] = tile_data[BIT_LENGTH-2-j][i+1]
            data = list(map(lambda row: ''.join(row), data))
            return data
        elif edge_orien == (c, d, a, b): # Rotated 180 degrees (row inv, col inv)
            data = [['.'] * (BIT_LENGTH - 2) for _ in range(BIT_LENGTH - 2)]
            for i in range(BIT_LENGTH - 2):
                for j in range(BIT_LENGTH - 2):
                    data[i][j] = tile_data[BIT_LENGTH-2-i][BIT_LENGTH-2-j]
            data = list(map(lambda row: ''.join(row), data))
            return data
        elif edge_orien == (d, a, b, c): # Rotated right once (col, row inv)
            data = [['.'] * (BIT_LENGTH - 2) for _ in range(BIT_LENGTH - 2)]
            for i in range(BIT_LENGTH - 2):
                for j in range(BIT_LENGTH - 2):
                    data[i][j] = tile_data[j+1][BIT_LENGTH-2-i]
            data = list(map(lambda row: ''.join(row), data))
            return data
        elif edge_orien == (ap, dp, cp, bp): # Flip left-right (row, col inv)
            data = [['.'] * (BIT_LENGTH - 2) for _ in range(BIT_LENGTH - 2)]
            for i in range(BIT_LENGTH - 2):
                for j in range(BIT_LENGTH - 2):
                    data[i][j] = tile_data[i+1][BIT_LENGTH-2-j]
            data = list(map(lambda row: ''.join(row), data))
            return data
        elif edge_orien == (dp, cp, bp, ap): # Flip left-right rotate left (col, row)
            data = [['.'] * (BIT_LENGTH - 2) for _ in range(BIT_LENGTH - 2)]
            for i in range(BIT_LENGTH - 2):
                for j in range(BIT_LENGTH - 2):
                    data[i][j] = tile_data[j+1][i+1]
            data = list(map(lambda row: ''.join(row), data))
            return data
        elif edge_orien == (cp, bp, ap, dp): # Flip up-down (row inv, col)
            data = [['.'] * (BIT_LENGTH - 2) for _ in range(BIT_LENGTH - 2)]
            for i in range(BIT_LENGTH - 2):
                for j in range(BIT_LENGTH - 2):
                    data[i][j] = tile_data[BIT_LENGTH-2-i][j+1]
            data = list(map(lambda row: ''.join(row), data))
            return data
        elif edge_orien == (bp, ap, dp, cp): # Flip left-right rotate right (col inv, row inv)
            data = [['.'] * (BIT_LENGTH - 2) for _ in range(BIT_LENGTH - 2)]
            for i in range(BIT_LENGTH - 2):
                for j in range(BIT_LENGTH - 2):
                    data[i][j] = tile_data[BIT_LENGTH-2-j][BIT_LENGTH-2-i]
            data = list(map(lambda row: ''.join(row), data))
            return data
        else:
            raise Exception("Unknown orientation")
        
    actual_map = []
    for row in map_tiles:
        row_map = []
        for tile in row:
            row_map.append(get_rotated_stripped_tile(tile))
        actual_map.append(row_map)

    '''
    Get combined map
    '''
    combined_map = []
    for row in actual_map:
        for i in range(BIT_LENGTH - 2):
            combined_map.append(''.join(list(map(lambda rows: rows[i], row))))
    COMBINED_MAP_SIZE = len(combined_map)
    
    '''
    Finding sea monsters
                      # 
    #    ##    ##    ###
     #  #  #  #  #  #   
    '''
    sea_monster = [
                                                                                                                                      (0,18), 
        (1, 0),                            (1, 5),(1, 6),                            (1,11),(1,12),                            (1,17),(1,18),(1,19),
               (2, 1),              (2, 4),              (2, 7),              (2,10),              (2,13),              (2,16),
    ]
    SEA_MONSTER_LENGTH = 20
    SEA_MONSTER_HEIGHT = 3

    def is_sea_monster(point):
        i, j = point
        for di, dj in sea_monster:
            if combined_map[i+di][j+dj] != '#':
                return False
        return True
    
    def rotate_map_left():
        nonlocal combined_map
        new_map = [['.'] * COMBINED_MAP_SIZE for _ in range(COMBINED_MAP_SIZE)]
        for i in range(COMBINED_MAP_SIZE):
            for j in range(COMBINED_MAP_SIZE):
                new_map[i][j] = combined_map[COMBINED_MAP_SIZE-1-j][i]
        combined_map = list(map(lambda row: ''.join(row), new_map))
    
    def flip_map():
        nonlocal combined_map
        combined_map = list(map(lambda row: row[::-1], combined_map))
    
    def check_map_rotations_for_sea_monster():
        for _ in range(4):
            sea_monster_points = set()
            for i in range(COMBINED_MAP_SIZE - SEA_MONSTER_HEIGHT + 1):
                for j in range(COMBINED_MAP_SIZE - SEA_MONSTER_LENGTH + 1):
                    if is_sea_monster((i, j)):
                        for di, dj in sea_monster:
                            sea_monster_points.add((i + di, j + dj))
            if sea_monster_points:
                all_hash_points = set()
                for i in range(COMBINED_MAP_SIZE):
                    for j in range(COMBINED_MAP_SIZE):
                        if combined_map[i][j] == '#':
                            all_hash_points.add((i, j))
                return len(all_hash_points.difference(sea_monster_points))
            else:
                rotate_map_left()
        return None
    
    points = check_map_rotations_for_sea_monster()
    if points:
        return points
    flip_map()
    return check_map_rotations_for_sea_monster()

print(solve_part_2())
