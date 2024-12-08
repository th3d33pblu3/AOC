import hashlib

def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def solve_part_1():
    file = read_input_file()
    header = file.read()
    GOAL = "00000"
    target_length = len(GOAL)
    number = 0
    result = None
    while result != GOAL:
        number += 1
        hash = hashlib.md5((header + str(number)).encode())
        result = hash.hexdigest()[0:target_length]

    return number # 346386

def solve_part_2():
    file = read_input_file()
    header = file.read()
    GOAL = "000000"
    target_length = len(GOAL)
    number = 0
    result = None
    while result != GOAL:
        number += 1
        hash = hashlib.md5((header + str(number)).encode())
        result = hash.hexdigest()[0:target_length]

    return number # 9958218
    
print(solve_part_2())


