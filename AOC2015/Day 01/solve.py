def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def solve_part_1():
    file = read_input_file()
    data = file.read()

    UP = "("
    DOWN = ")"

    floor = 0
    for char in data:
        if char == UP:
            floor += 1
        elif char == DOWN:
            floor -= 1
        else:
            raise Exception("Unknown command")
    return floor

def solve_part_2():
    file = read_input_file()
    data = file.read()

    UP = "("
    DOWN = ")"

    floor = 0
    for idx, char in enumerate(data, start=1):
        if char == UP:
            floor += 1
        elif char == DOWN:
            floor -= 1
        else:
            raise Exception("Unknown command")

        if floor == -1:
            return idx
    
print(solve_part_2())
