from collections import Counter

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

TIE = -1
SPACE = -2

def solve_part_1():
    lines = read_input_file_data().splitlines()
    coordinates = []

    minx = float('inf')
    maxx = 0
    miny = float('inf')
    maxy = 0
    for line in lines:
        line = line.split(', ')
        x = int(line[0])
        y = int(line[1])
        coordinates.append((x, y))
        if x < minx:
            minx = x
        if x > maxx:
            maxx = x
        if y < miny:
            miny = y
        if y > maxy:
            maxy = y

    xsize = maxx + 1 - minx
    ysize = maxy + 1 - miny
    xoffset = minx
    yoffset = miny
    coordinates = [(x - xoffset, y - yoffset) for x, y in coordinates]
    ids = {}
    for i, coordinate in enumerate(coordinates):
        ids[coordinate] = i
    
    grid = []
    for _ in range(xsize):
        grid.append([SPACE] * (ysize))
    
    for coordinate in coordinates:
        grid[coordinate[0]][coordinate[1]] = ids[coordinate]
    
    for x in range(xsize):
        for y in range(ysize):
            min_id = -1
            min_dist = float('inf')
            for coordinate in coordinates:
                dist = abs(x - coordinate[0]) + abs(y - coordinate[1])
                if dist < min_dist:
                    min_dist = dist
                    min_id = ids[coordinate]
                elif dist == min_dist:
                    min_id = TIE
            grid[x][y] = min_id
    
    # Scan 1 round for infinite space ids
    infinite_id = set(grid[0]).union(set(grid[xsize - 1]))
    for y in range(1, ysize - 1):
        infinite_id.add(grid[0][y])
        infinite_id.add(grid[xsize - 1][y])

    counts = Counter()
    for x in range(xsize):
        counts += Counter(grid[x])
    counts = dict(counts)

    max_count = 0
    # max_count_id = -1
    for id in range(len(coordinates)):
        if id in infinite_id:
            continue
        count = counts[id]
        if count > max_count:
            max_count = count
            # max_count_id = id
    return max_count

def solve_part_2():
    lines = read_input_file_data().splitlines()
    coordinates = []

    minx = float('inf')
    maxx = 0
    miny = float('inf')
    maxy = 0
    for line in lines:
        line = line.split(', ')
        x = int(line[0])
        y = int(line[1])
        coordinates.append((x, y))
        if x < minx:
            minx = x
        if x > maxx:
            maxx = x
        if y < miny:
            miny = y
        if y > maxy:
            maxy = y

    xsize = maxx + 1 - minx
    ysize = maxy + 1 - miny
    xoffset = minx
    yoffset = miny
    coordinates = [(x - xoffset, y - yoffset) for x, y in coordinates]
    
    LIMIT = 10000
    safe = 0
    for x in range(xsize):
        for y in range(ysize):
            tdist = 0
            for coordinate in coordinates:
                tdist += abs(x - coordinate[0]) + abs(y - coordinate[1])
            if tdist < LIMIT:
                safe += 1
    return safe
    
print(solve_part_2())
