def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    points, instructions = read_input_file_data().split('\n\n')
    points = set([tuple(map(int, point.split(','))) for point in points.splitlines()])
    instructions = [(line[11], int(line.split('=')[1])) for line in instructions.splitlines()]

    def fold_point(point, axis, n):
        x, y = point
        if axis == 'x':
            if x > n:
                return (n - (x - n), y)
            else:
                return (x, y)
        else: # axis == 'y'
            if y > n:
                return (x, n - (y - n))
            else:
                return (x, y)

    axis, n = instructions[0]
    points = set(map(lambda point: fold_point(point, axis, n), points))
    return len(points)

def solve_part_2():
    points, instructions = read_input_file_data().split('\n\n')
    points = set([tuple(map(int, point.split(','))) for point in points.splitlines()])
    instructions = [(line[11], int(line.split('=')[1])) for line in instructions.splitlines()]

    def fold_point(point, axis, n):
        x, y = point
        if axis == 'x':
            if x > n:
                return (n - (x - n), y)
            else:
                return (x, y)
        else: # axis == 'y'
            if y > n:
                return (x, n - (y - n))
            else:
                return (x, y)

    for axis, n in instructions:
        points = set(map(lambda point: fold_point(point, axis, n), points))
    
    transformed = list(zip(*points))
    x_min = min(transformed[0])
    x_max = max(transformed[0])
    y_min = min(transformed[1])
    y_max = max(transformed[1])

    image = [['.'] * (x_max - x_min + 1) for _ in range(y_max - y_min + 1)]
    for x, y in points:
        image[y-y_min][x-x_min] = '#'
    
    return '\n'.join(list(map(lambda line: ''.join(line), image)))
    
print(solve_part_2())
