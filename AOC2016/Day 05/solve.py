import hashlib

def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def solve_part_1():
    file = read_input_file()
    header = file.read()

    GOAL = "00000"
    PASSWORD_LENGTH = 8
    KEY_INDEX = 6 - 1
    target_length = len(GOAL)
    number = 0
    result = ""
    while len(result) < PASSWORD_LENGTH:
        number += 1
        hash = hashlib.md5((header + str(number)).encode()).hexdigest()
        first_five = hash[0:target_length]
        if first_five == GOAL:
            result += hash[KEY_INDEX]
    return result # 1a3099aa

def solve_part_2():
    file = read_input_file()
    header = file.read()

    GOAL = "00000"
    PASSWORD_LENGTH = 8
    POS_INDEX = 6 - 1
    KEY_INDEX = 7 - 1
    target_length = len(GOAL)
    number = 0
    result = ["_"] * 8
    while "_" in result:
        number += 1
        hash = hashlib.md5((header + str(number)).encode()).hexdigest()
        first_five = hash[0:target_length]
        if first_five == GOAL:
            pos = hash[POS_INDEX]
            if pos.isnumeric():
                pos = int(pos)
                if pos in range(8) and result[pos] == "_":
                    result[pos] = hash[KEY_INDEX]
    return ''.join(result) # 694190cd
    
print(solve_part_2())
