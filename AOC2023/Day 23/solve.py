def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

LEFT = '<'
RIGHT = '>'
UP = '^'
DOWN = 'v'
WALL = '#'
ROAD = '.'

def solve_part_1():
    hike_map = read_input_file_data().splitlines()
    START = (0, 1)
    END = (len(hike_map) - 1, len(hike_map[0]) -2)
    assert hike_map[START[0]][START[1]] == ROAD and hike_map[END[0]][END[1]] == ROAD

    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    opp_dir = {
        (1, 0): (-1, 0),
        (0, 1): (0, -1),
        (-1, 0): (1, 0),
        (0, -1): (0, 1)
    }
    steps = 0
    positions = {(START[0], START[1], (-1, 0))} # Invalid direction being going up
    while positions:
        new_positions = set()
        for y, x, invalid_dir in positions:
            current_tile = hike_map[y][x]
            if current_tile != ROAD:
                if current_tile == LEFT:
                    new_positions.add((y, x - 1, (0, 1)))
                elif current_tile == RIGHT:
                    new_positions.add((y, x + 1, (0, -1)))
                elif current_tile == UP:
                    new_positions.add((y - 1, x, (1, 0)))
                elif current_tile == DOWN:
                    new_positions.add((y + 1, x, (-1, 0)))
                else:
                    raise Exception(f"Invalid tile {current_tile}")
            else:
                for dir in DIRECTIONS:
                    if dir == invalid_dir:
                        continue
                    target_tile = hike_map[y + dir[0]][x + dir[1]]
                    if target_tile == WALL:
                        continue
                    elif target_tile == RIGHT and dir == (0, -1):
                        continue
                    elif target_tile == DOWN and dir == (-1, 0):
                        continue
                    elif y + dir[0] == END[0] and x + dir[1] == END[1]:
                        continue
                    else:
                        new_positions.add((y + dir[0], x + dir[1], opp_dir[dir]))
        positions = new_positions
        steps += 1
    return steps

def solve_part_2():
    hike_map = read_input_file_data().splitlines()
    START = (0, 1)
    END = (len(hike_map) - 1, len(hike_map[0]) -2)
    assert hike_map[START[0]][START[1]] == ROAD and hike_map[END[0]][END[1]] == ROAD

    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    opp_dir = {
        (1, 0): (-1, 0),
        (0, 1): (0, -1),
        (-1, 0): (1, 0),
        (0, -1): (0, 1)
    }

    # Find intersections on the map
    intersections = []
    for y in range(START[0]+1, END[0]):
        for x in range(START[1], END[1]+1):
            if hike_map[y][x] == WALL:
                continue
            num_possible_paths = 0
            for dy, dx in DIRECTIONS:
                if hike_map[y+dy][x+dx] != WALL:
                    num_possible_paths += 1
            if num_possible_paths >= 3:
                intersections.append((y, x))

    # Creating route table
    route_table = {}
    for intersection in intersections:
        route_table[intersection] = {}

    frontier = set()
    for y, x in intersections:
        frontier.add((y, x, None, (y, x)))
    
    # Handling START and END
    intersections.append(START)
    intersections.append(END)
    route_table[START] = {}
    # route_table[END] does not need to be defined since it should not go anywhere from there

    # Flooding to fill route table
    steps = 0
    while frontier:
        steps += 1
        new_frontier = set()
        for y, x, invalid_dir, source in frontier:
            for dir in DIRECTIONS:
                if dir == invalid_dir:
                    continue
                ny, nx = y + dir[0], x + dir[1]
                if hike_map[ny][nx] != WALL:
                    if (ny, nx) in intersections:
                        route_table[source][(ny, nx)] = steps
                        if (ny, nx) == START: # Back tracing for START so that do not need to deal with index out of bounds
                            route_table[START][source] = steps
                    else:
                        new_frontier.add((ny, nx, opp_dir[dir], source))
        frontier = new_frontier

    def get_max_route_dist(path, acc_dist):
        if path[-1] == END:
            return acc_dist
        
        last_intersection = path[-1]
        distance_table = route_table[last_intersection]
        
        max_route_dist = 0
        for next_intersection in distance_table:
            if next_intersection not in path:
                max_route_dist = max(max_route_dist, get_max_route_dist(path + [next_intersection], acc_dist + distance_table[next_intersection]))
        return max_route_dist
    
    return get_max_route_dist([START], 0)
    
print(solve_part_2())
