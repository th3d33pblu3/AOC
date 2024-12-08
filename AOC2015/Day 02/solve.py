def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def solve_part_1():
    file = read_input_file()
    total_area = 0
    for line in file.readlines():
        x, y, z = map(int, line.split("x"))
        a = x * y
        b = y * z
        c = x * z
        total_area += 2 * a + 2 * b + 2 * c + min(a, b, c)
    
    return total_area

def solve_part_2():
    file = read_input_file()
    total_length = 0
    for line in file.readlines():
        x, y, z = map(int, line.split("x"))
        total_length += (x + y + z - max(x, y, z)) * 2 + (x * y * z)
    
    return total_length
    
print(solve_part_2())
