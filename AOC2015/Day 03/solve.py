def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def solve_part_1():
    file = read_input_file()
    data = file.read()

    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"
    x = 0
    y = 0
    houses = {}

    houses[(x, y)] = 1

    def move(arrow):
        nonlocal x, y
        if arrow == UP:
            y += 1
        elif arrow == DOWN:
            y -= 1
        elif arrow == LEFT:
            x -= 1
        elif arrow == RIGHT:
            x += 1
        else:
            raise Exception("Unknown direction occurred")

    for arrow in data:
        move(arrow)
        if houses.get((x, y)) != None:
            houses[(x, y)] += 1
        else:
            houses[(x, y)] = 1
    
    return len(houses)


def solve_part_2():
    file = read_input_file()
    data = file.read()

    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"

    IS_SANTA = True

    santa = [0, 0]
    robot = [0, 0]
    current = santa
    houses = {}
    houses[(0, 0)] = 2

    def swap():
        nonlocal current, IS_SANTA
        if IS_SANTA:
            IS_SANTA = False
            current = robot
        else:
            IS_SANTA = True
            current = santa

    def get_tuple():
        return (current[0], current[1])

    def move(arrow):
        nonlocal current
        if arrow == UP:
            current[1] += 1
        elif arrow == DOWN:
            current[1] -= 1
        elif arrow == LEFT:
            current[0] -= 1
        elif arrow == RIGHT:
            current[0] += 1
        else:
            raise Exception("Unknown direction occurred")

    for arrow in data:
        move(arrow)
        tup = get_tuple()
        if houses.get(tup) != None:
            houses[tup] += 1
        else:
            houses[tup] = 1
        swap()
    
    return len(houses)
    
print(solve_part_2())
