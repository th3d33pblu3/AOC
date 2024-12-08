def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def solve_part_1():
    file = read_input_file()

    ESCAPE = "\\"
    DOUBLE_QUOTE = "\""

    total_minus = 0
    for line in file.read().splitlines():
        minus = 0
        i = 1
        while i < len(line) - 1:
            if line[i] == ESCAPE:
                if (line[i + 1] == ESCAPE or line[i + 1] == DOUBLE_QUOTE):
                    i += 1
                    minus += 1
                elif line[i + 1] == "x":
                    i += 3
                    minus += 3
            i += 1
        total_minus += minus + 2
    return total_minus # 1333

def solve_part_2():
    file = read_input_file()

    ESCAPE = "\\"
    DOUBLE_QUOTE = "\""

    total_plus = 0
    for line in file.read().splitlines():
        plus = 0
        for char in line:
            if (char == ESCAPE or char == DOUBLE_QUOTE):
                plus += 1
        total_plus += plus + 2
    return total_plus # 2046
    
print(solve_part_2())
