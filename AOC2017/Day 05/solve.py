def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def get_list():
    file = read_input_file()
    data = file.read().splitlines()
    ls = list(map(int, data))
    return ls

def solve_part_1():
    ls = get_list()
    index = 0
    steps = 0
    try:
        while True:
            num = ls[index]
            ls[index] = num + 1
            index += num
            steps += 1
    except:
        return steps

def solve_part_2():
    ls = get_list()
    index = 0
    steps = 0
    try:
        while True:
            num = ls[index]
            ls[index] = num + 1 if num < 3 else num - 1
            index += num
            steps += 1
    except:
        return steps
    
print(solve_part_2())
