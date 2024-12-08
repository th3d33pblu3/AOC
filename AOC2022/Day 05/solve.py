def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def instruction_to_tuple(str):
    s = str.split()
    return (int(s[1]), int(s[3]), int(s[5]))
    
def get_init():
    FILE = "./Day 05/puzzle_init.txt"
    file = open(FILE, "r")
    data = file.readlines()
    num_items = len(data) - 1
    matrix = []
    for _ in range(9):
        matrix.append([])
    for index in range(num_items - 1, -1, -1):
        line = data[index]
        for col in range(1, 35, 4):
            if line[col] != " ":
                matrix[col // 4].append(line[col])
    return matrix

def solve_part_1():
    file = read_input_file()
    data = map(instruction_to_tuple, file.readlines())
    matrix = get_init()

    def move(start, end):
        x = matrix[start - 1].pop()
        matrix[end - 1].append(x)
    
    for num, start, end in data:
        for i in range(num):
            move(start, end)

    result = ""
    for _ in range(9):
        result += matrix[_].pop()

    return result

def solve_part_2():
    file = read_input_file()
    data = map(instruction_to_tuple, file.readlines())
    matrix = get_init()

    def move(num, start, end):
        to_move = matrix[start - 1][-num:]
        matrix[end - 1] = matrix[end - 1] + to_move
        matrix[start - 1] = matrix[start - 1][:-num]
    
    for num, start, end in data:
        move(num, start, end)

    result = ""
    for _ in range(9):
        result += matrix[_].pop()

    return result



print(solve_part_2())
