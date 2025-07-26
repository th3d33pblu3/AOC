import math

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    c1, c2 = list(map(int, read_input_file_data().splitlines()))
    N = 20201227

    value, loop_size = 1, 0
    while value != c1:
        value = value * 7 % N
        loop_size += 1
    
    return pow(c2, loop_size, N)

def solve_part_2():
    pass
    
print(solve_part_1())
