def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

N = 0
E = 1
S = 2
W = 3

def solve_part_1():
    instructions = list(map(lambda line: (line[0], int(line[1:])), read_input_file_data().splitlines()))
    face = E
    y = 0 # North-South
    x = 0 # East-West
    for ins, n in instructions:
        if ins == 'N':
            y += n
        elif ins == 'S':
            y -= n
        elif ins == 'E':
            x += n
        elif ins == 'W':
            x -= n
        elif ins == 'L':
            face = (face - n//90) % 4
        elif ins == 'R':
            face = (face + n//90) % 4
        elif ins == 'F':
            if face == N:
                y += n
            elif face == S:
                y -= n
            elif face == E:
                x += n
            elif face == W:
                x -= n
    return abs(y) + abs(x)

def solve_part_2():
    instructions = list(map(lambda line: (line[0], int(line[1:])), read_input_file_data().splitlines()))
    wy = 1 # North-South
    wx = 10 # East-West
    sy = 0
    sx = 0
    for ins, n in instructions:
        if ins == 'N':
            wy += n
        elif ins == 'S':
            wy -= n
        elif ins == 'E':
            wx += n
        elif ins == 'W':
            wx -= n
        elif ins == 'L':
            if n == 90:
                temp = wx
                wx = -wy
                wy = temp
            elif n == 180:
                wy = -wy
                wx = -wx
            elif n == 270:
                temp = wy
                wy = -wx
                wx = temp
        elif ins == 'R':
            if n == 90:
                temp = wy
                wy = -wx
                wx = temp
            elif n == 180:
                wy = -wy
                wx = -wx
            elif n == 270:
                temp = wx
                wx = -wy
                wy = temp
        elif ins == 'F':
            sy += wy * n
            sx += wx * n
    return abs(sy) + abs(sx)
    
print(solve_part_2())
