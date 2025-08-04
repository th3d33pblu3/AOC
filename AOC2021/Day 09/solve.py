def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    heightmap = [list(map(int, line)) for line in read_input_file_data().splitlines()]
    WIDTH = len(heightmap[0])
    HEIGHT = len(heightmap)
    DELTAS = ((-1, 0), (1, 0), (0, -1), (0, 1))

    risk_level = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            val = heightmap[y][x]
            is_low = True
            for dx, dy in DELTAS:
                nx, ny = x + dx, y + dy
                if 0 <= nx and nx < WIDTH and 0 <= ny and ny < HEIGHT:
                    val2 = heightmap[ny][nx]
                    if val2 <= val:
                        is_low = False
                        break
            if is_low:
                risk_level += val + 1
    return risk_level

def solve_part_2():
    heightmap = [list(map(int, line)) for line in read_input_file_data().splitlines()]
    WIDTH = len(heightmap[0])
    HEIGHT = len(heightmap)
    DELTAS = ((-1, 0), (1, 0), (0, -1), (0, 1))

    seen_points = set()
    basin_sizes = []

    def get_neighbours(x, y):
        neighbours = []
        for dx, dy in DELTAS:
            nx, ny = x + dx, y + dy
            if 0 <= nx and nx < WIDTH and 0 <= ny and ny < HEIGHT:
                neighbours.append((nx, ny))
        return neighbours

    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (x, y) in seen_points or heightmap[y][x] == 9:
                continue
            frontier = set()
            frontier.add((x, y))
            seen = set()
            curr_size = 0
            while frontier:
                new_frontier = set()
                for (x, y) in frontier:
                    if (x, y) in seen or heightmap[y][x] == 9:
                        continue
                    curr_size += 1
                    neighbours = get_neighbours(x, y)
                    new_frontier.update(neighbours)
                seen.update(frontier)
                frontier = new_frontier
            seen_points.update(seen)
            basin_sizes.append(curr_size)
    
    basin_sizes.sort()
    a, b, c = basin_sizes[-3:]
    return a * b * c
    
print(solve_part_2())
