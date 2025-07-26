def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    # Parsing data
    active_cubes = set()
    data = read_input_file_data().splitlines()
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == '#':
                active_cubes.add((x, y, 0))
    
    # Defining helper functions
    NEIGHBOUR_DELTA = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                NEIGHBOUR_DELTA.append((dx, dy, dz))
    NEIGHBOUR_DELTA.remove((0, 0, 0))

    def get_active_neighbours(cube):
        nonlocal active_cubes, NEIGHBOUR_DELTA
        x, y, z = cube
        active_neighbour_count = 0
        for dx, dy, dz in NEIGHBOUR_DELTA:
            if (x+dx, y+dy, z+dz) in active_cubes:
                active_neighbour_count += 1
        return active_neighbour_count
    
    def get_neighbours(cube):
        return set(map(lambda delta: (cube[0]+delta[0], cube[1]+delta[1], cube[2]+delta[2]), NEIGHBOUR_DELTA))
    
    # Actual computation
    for _ in range(6):
        frontier = set()
        for cube in active_cubes:
            frontier.add(cube)
            frontier.update(get_neighbours(cube))
        
        new_active_cubes = set()
        for cube in frontier:
            active_neighbour_count = get_active_neighbours(cube)
            if cube in active_cubes:
                if active_neighbour_count in (2, 3):
                    new_active_cubes.add(cube)
            else:
                if active_neighbour_count == 3:
                    new_active_cubes.add(cube)
        active_cubes = new_active_cubes
    
    return len(active_cubes)

def solve_part_2():
    # Parsing data
    active_cubes = set()
    data = read_input_file_data().splitlines()
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == '#':
                active_cubes.add((x, y, 0, 0))
    
    # Defining helper functions
    NEIGHBOUR_DELTA = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in range(-1, 2):
                    NEIGHBOUR_DELTA.append((dx, dy, dz, dw))
    NEIGHBOUR_DELTA.remove((0, 0, 0, 0))

    def get_active_neighbours(cube):
        nonlocal active_cubes, NEIGHBOUR_DELTA
        x, y, z, w = cube
        active_neighbour_count = 0
        for dx, dy, dz, dw in NEIGHBOUR_DELTA:
            if (x+dx, y+dy, z+dz, w+dw) in active_cubes:
                active_neighbour_count += 1
        return active_neighbour_count
    
    def get_neighbours(cube):
        return set(map(lambda delta: (cube[0]+delta[0], cube[1]+delta[1], cube[2]+delta[2], cube[3]+delta[3]), NEIGHBOUR_DELTA))
    
    # Actual computation
    for _ in range(6):
        frontier = set()
        for cube in active_cubes:
            frontier.add(cube)
            frontier.update(get_neighbours(cube))
        
        new_active_cubes = set()
        for cube in frontier:
            active_neighbour_count = get_active_neighbours(cube)
            if cube in active_cubes:
                if active_neighbour_count in (2, 3):
                    new_active_cubes.add(cube)
            else:
                if active_neighbour_count == 3:
                    new_active_cubes.add(cube)
        active_cubes = new_active_cubes
    
    return len(active_cubes)
    
print(solve_part_2())
