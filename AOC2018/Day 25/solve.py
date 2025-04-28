def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    points = [tuple(map(int, line.split(','))) for line in read_input_file_data().splitlines()]
    NUM_POINTS = len(points)
    constellations = [i for i in range(NUM_POINTS)]

    connection = [[False] * NUM_POINTS for _ in range(NUM_POINTS)]
    for i, point1 in enumerate(points):
        for j, point2 in enumerate(points):
            manhattan_dist = 0
            for dim in range(4):
                manhattan_dist += abs(point1[dim] - point2[dim])
            if manhattan_dist <= 3:
                connection[i][j] = True

    is_merge = True
    while is_merge:
        is_merge = False
        for i in range(NUM_POINTS-1):
            for j in range(i+1, NUM_POINTS):
                if connection[i][j] and (constellations[i] != constellations[j]):
                    is_merge = True
                    new_group = constellations[i]
                    old_group = constellations[j]
                    constellations = [new_group if n == old_group else n for n in constellations]

    return len(set(constellations))

def solve_part_2():
    pass
    
print(solve_part_1())
