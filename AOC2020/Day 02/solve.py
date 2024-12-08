from collections import Counter

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    valid = 0
    for line in read_input_file_data().splitlines():
        ins = line.split()
        min_count, max_count = tuple(map(int, ins[0].split("-")))
        char = ins[1][0]
        password = ins[2]

        counter = Counter(password)
        char_count = counter.get(char)
        if char_count == None:
            char_count = 0
        if min_count <= char_count <= max_count:
            valid += 1
    return valid

def solve_part_2():
    valid = 0
    for line in read_input_file_data().splitlines():
        ins = line.split()
        pos1, pos2 = tuple(map(int, ins[0].split("-")))
        char = ins[1][0]
        password = ins[2]

        count = 0
        if password[pos1 - 1] == char:
            count += 1
        if password[pos2 - 1] == char:
            count += 1
        if count == 1:
            valid += 1
    return valid
    
print(solve_part_2())
