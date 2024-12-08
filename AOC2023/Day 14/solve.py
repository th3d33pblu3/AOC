def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

WALL = '#'
ROCK = 'O'
SPACE = '.'

def solve_part_1():
    rocks = read_input_file_data().splitlines()
    y_length = len(rocks)
    x_length = len(rocks[0])

    t_load = 0
    for x in range(x_length):
        northmost = y_length
        stacked_rocks = 0
        for y in range(y_length):
            c = rocks[y][x]
            if c == WALL:
                northmost = y_length - y - 1
                stacked_rocks = 0
            elif c == ROCK:
                t_load += northmost - stacked_rocks
                stacked_rocks += 1
    return t_load

def solve_part_2():
    rocks = [[c for c in line] for line in read_input_file_data().splitlines()]
    y_length = len(rocks)
    x_length = len(rocks[0])

    def tilt_north():
        for x in range(x_length):
            piled_rocks = 0
            for y in range(y_length - 1, -1, -1):
                if rocks[y][x] == ROCK:
                    piled_rocks += 1
                    rocks[y][x] = SPACE
                elif rocks[y][x] == WALL:
                    y_temp = y + 1
                    while piled_rocks != 0:
                        rocks[y_temp][x] = ROCK
                        y_temp += 1
                        piled_rocks -= 1
            if piled_rocks != 0:
                y_temp = 0
                while piled_rocks != 0:
                    rocks[y_temp][x] = ROCK
                    y_temp += 1
                    piled_rocks -= 1

    def tilt_west():
        for y in range(y_length):
            piled_rocks = 0
            for x in range(x_length - 1, -1, -1):
                if rocks[y][x] == ROCK:
                    piled_rocks += 1
                    rocks[y][x] = SPACE
                elif rocks[y][x] == WALL:
                    x_temp = x + 1
                    while piled_rocks != 0:
                        rocks[y][x_temp] = ROCK
                        x_temp += 1
                        piled_rocks -= 1
            if piled_rocks != 0:
                x_temp = 0
                while piled_rocks != 0:
                    rocks[y][x_temp] = ROCK
                    x_temp += 1
                    piled_rocks -= 1

    def tilt_south():
        for x in range(x_length):
            piled_rocks = 0
            for y in range(y_length):
                if rocks[y][x] == ROCK:
                    piled_rocks += 1
                    rocks[y][x] = SPACE
                elif rocks[y][x] == WALL:
                    y_temp = y - 1
                    while piled_rocks != 0:
                        rocks[y_temp][x] = ROCK
                        y_temp -= 1
                        piled_rocks -= 1
            if piled_rocks != 0:
                y_temp = y_length - 1
                while piled_rocks != 0:
                    rocks[y_temp][x] = ROCK
                    y_temp -= 1
                    piled_rocks -= 1

    def tilt_east():
        for y in range(y_length):
            piled_rocks = 0
            for x in range(x_length):
                if rocks[y][x] == ROCK:
                    piled_rocks += 1
                    rocks[y][x] = SPACE
                elif rocks[y][x] == WALL:
                    x_temp = x - 1
                    while piled_rocks != 0:
                        rocks[y][x_temp] = ROCK
                        x_temp -= 1
                        piled_rocks -= 1
            if piled_rocks != 0:
                x_temp = x_length - 1
                while piled_rocks != 0:
                    rocks[y][x_temp] = ROCK
                    x_temp -= 1
                    piled_rocks -= 1

    def get_load():
        t_load = 0
        for x in range(x_length):
            for y in range(y_length):
                if rocks[y][x] == ROCK:
                    t_load += y_length - y
        return t_load

    def print_rocks():
        for _ in rocks:
            print(''.join(_))

    # for n in range(1, 1000000000 + 1):
    #     tilt_north()
    #     tilt_west()
    #     tilt_south()
    #     tilt_east()
    #     if n % 100 == 0:
    #         print(n, ": ", get_load())
    
    # From output analysis
    # Loop-size ~= 1700
    remainders = {   0 :  100084,
                   100 :  100043,
                   200 :  100011,
                   300 :  100016,
                   400 :  100034,
                   500 :  100064,
                   600 :  100086,
                   700 :  100084,
                   800 :  100084,
                   900 :  100071,
                  1000 :  100025,
                  1100 :  100008,
                  1200 :  100024,
                  1300 :  100047,
                  1400 :  100079,
                  1500 :  100086,
                  1600 :  100086}

    return remainders[1000000000 % 1700]

print(solve_part_2())
