def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    freq = 0
    for line in read_input_file_data().splitlines():
        if line[0] == "+":
            freq += int(line[1:])
        else:
            freq -= int(line[1:])
    return freq

def solve_part_2():
    freq = 0
    visited = set()
    visited.add(0)
    lines = read_input_file_data().splitlines()
    while True:
        for line in lines:
            if line[0] == "+":
                freq += int(line[1:])
            else:
                freq -= int(line[1:])
            if freq in visited:
                return freq
            else:
                visited.add(freq)
    
print(solve_part_2())
