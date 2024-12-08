def read_input_file_data():
    FILE = f"puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def read_test_file_data():
    FILE = f"test_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    chars = read_input_file_data()
    skip = False
    is_garbage = False
    total_score = 0
    curr_group_score = 0
    for char in chars:
        if skip:
            skip = False
        elif char == "!":
            skip = True
        elif char == ">":
            is_garbage = False
        elif is_garbage:
            continue
        elif char == "{":
            curr_group_score += 1
        elif char == "}":
            total_score += curr_group_score
            curr_group_score -= 1
        elif char == "<":
            is_garbage = True
    return total_score

def solve_part_2():
    chars = read_input_file_data()
    skip = False
    is_garbage = False
    total_garbage = 0
    for char in chars:
        if skip:
            skip = False
        elif char == "!":
            skip = True
        elif char == ">":
            is_garbage = False
        elif is_garbage:
            total_garbage += 1
            continue
        elif char == "{":
            pass
        elif char == "}":
            pass
        elif char == "<":
            is_garbage = True
    return total_garbage
    
print(solve_part_2())
