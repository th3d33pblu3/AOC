def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

UP = "U"
DOWN = "D"
LEFT = "L"
RIGHT = "R"

def solve_part_1():
    wires = read_input_file_data().splitlines()
    
    wire1_paths = set()
    segments = wires[0].split(",")
    x = 0
    y = 0
    for segment in segments:
        direction = segment[0]
        steps = int(segment[1:])
        for _ in range(steps):
            if direction == UP:
                y += 1
            elif direction == DOWN:
                y -= 1
            elif direction == LEFT:
                x -= 1
            elif direction == RIGHT:
                x += 1
            else:
                raise Exception(f"Unknown direction: {direction}")
            wire1_paths.add((x, y))

    wire2_paths = set()
    segments = wires[1].split(",")
    x = 0
    y = 0
    for segment in segments:
        direction = segment[0]
        steps = int(segment[1:])
        for _ in range(steps):
            if direction == UP:
                y += 1
            elif direction == DOWN:
                y -= 1
            elif direction == LEFT:
                x -= 1
            elif direction == RIGHT:
                x += 1
            else:
                raise Exception(f"Unknown direction: {direction}")
            wire2_paths.add((x, y))

    intersections = wire1_paths.intersection(wire2_paths)
    min_dist = 9999999999999
    for point in intersections:
        min_dist = min(min_dist, abs(point[0]) + abs(point[1]))
    
    return min_dist

def solve_part_2():
    wires = read_input_file_data().splitlines()

    wire_times1 = {}
    wire1_paths = set()
    segments = wires[0].split(",")
    x = 0
    y = 0
    time = 0
    for segment in segments:
        direction = segment[0]
        steps = int(segment[1:])
        for _ in range(steps):
            if direction == UP:
                y += 1
            elif direction == DOWN:
                y -= 1
            elif direction == LEFT:
                x -= 1
            elif direction == RIGHT:
                x += 1
            else:
                raise Exception(f"Unknown direction: {direction}")
            time += 1
            wire1_paths.add((x, y))
            if wire_times1.get((x, y)) == None:
                wire_times1[(x, y)] = time

    wire_times2 = {}
    wire2_paths = set()
    segments = wires[1].split(",")
    x = 0
    y = 0
    time = 0
    for segment in segments:
        direction = segment[0]
        steps = int(segment[1:])
        for _ in range(steps):
            if direction == UP:
                y += 1
            elif direction == DOWN:
                y -= 1
            elif direction == LEFT:
                x -= 1
            elif direction == RIGHT:
                x += 1
            else:
                raise Exception(f"Unknown direction: {direction}")
            time += 1
            wire2_paths.add((x, y))
            if wire_times2.get((x, y)) == None:
                wire_times2[(x, y)] = time

    intersections = wire1_paths.intersection(wire2_paths)
    min_time = 9999999999999
    for point in intersections:
        min_time = min(wire_times1[point] + wire_times2[point], min_time)
    
    return min_time
    
print(solve_part_2())
