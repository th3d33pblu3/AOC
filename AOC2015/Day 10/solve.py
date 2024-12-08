def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    data = read_input_file_data()

    def make_round(num_str):
        new_str = ""
        start = num_str[0]
        count = 1
        for char in num_str[1:]:
            if char == start:
                count += 1
            else:
                new_str += str(count) + start
                start = char
                count = 1
        new_str += str(count) + start
        return new_str

    for _ in range(40):
        data = make_round(data)

    return len(data)

def solve_part_2(): # 4666278
    data = read_input_file_data()

    def make_round(num_str):
        new_str = ""
        start = num_str[0]
        count = 1
        for char in num_str[1:]:
            if char == start:
                count += 1
            else:
                new_str += str(count) + start
                start = char
                count = 1
        new_str += str(count) + start
        return new_str

    for _ in range(50):
        data = make_round(data)

    return len(data)
    
print(solve_part_2())
