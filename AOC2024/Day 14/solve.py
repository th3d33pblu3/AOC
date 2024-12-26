import re

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    def parse_robot(desc):
        p = tuple(map(int, re.search(r"p=([0-9]*,[0-9]*)", desc).group(1).split(',')))
        v = tuple(map(int, re.search(r"v=(-?[0-9]*,-?[0-9]*)", desc).group(1).split(',')))
        return p, v

    robots = list(map(parse_robot, read_input_file_data().splitlines()))
    WIDTH = 101
    HEIGHT = 103
    TIME = 100

    quad1 = 0
    quad2 = 0
    quad3 = 0
    quad4 = 0
    for robot in robots:
        p, v = robot
        final_p = ((p[0] + (v[0] * TIME)) % WIDTH, (p[1] + (v[1] * TIME)) % HEIGHT)
        if final_p[0] < WIDTH // 2 and final_p[1] < HEIGHT // 2:
            quad1 += 1
        elif final_p[0] >= (WIDTH + 1) // 2 and final_p[1] < HEIGHT // 2:
            quad2 += 1
        elif final_p[0] < WIDTH // 2 and final_p[1] >= (HEIGHT + 1) // 2:
            quad3 += 1
        elif final_p[0] >= (WIDTH + 1) // 2 and final_p[1] >= (HEIGHT + 1) // 2:
            quad4 += 1
    return quad1 * quad2 * quad3 * quad4

def solve_part_2():
    def parse_robot(desc):
        p = tuple(map(int, re.search(r"p=([0-9]*,[0-9]*)", desc).group(1).split(',')))
        v = tuple(map(int, re.search(r"v=(-?[0-9]*,-?[0-9]*)", desc).group(1).split(',')))
        return p, v

    robots = list(map(parse_robot, read_input_file_data().splitlines()))
    WIDTH = 101
    HEIGHT = 103

    time = 0
    skips = ''
    while True:
        skips: str = input("Type a number to skip or press 'x' to stop\n")
        if skips == 'x':
            break
        if skips.isdigit():
            skips = int(skips)
            time += skips
            print(f"Skipped {skips}")
        else:
            time += 1
            print(f"Next second")
        robot_map = [[0] * WIDTH for _ in range(HEIGHT)]

        for robot in robots:
            p, v = robot
            x, y = (p[0] + (v[0] * time)) % WIDTH, (p[1] + (v[1] * time)) % HEIGHT
            robot_map[y][x] += 1
        for line in robot_map:
            print(''.join(list(map(lambda x: '.' if x == 0 else '#', line))))
        print(f"Current time: {time}")
    return time # 8159
    # Interesting patterns start to appear at time 22 with intervals of 103
    
print(solve_part_2())
