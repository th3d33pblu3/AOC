def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

A_START  = 722
B_START  = 354
A_FACTOR = 16807
B_FACTOR = 48271
DIV      = 2147483647

def solve_part_1():
    a = A_START
    b = B_START
    count = 0
    for _ in range(40_000_000):
        a, b = (a * A_FACTOR) % DIV, (b * B_FACTOR) % DIV
        if a % 65536 == b % 65536: # Last 16 bits
            count += 1
    return count

def solve_part_2():
    a = A_START
    b = B_START
    count = 0
    for _ in range(5_000_000):
        while True:
            a = (a * A_FACTOR) % DIV
            if a % 4 == 0:
                break
        while True:
            b = (b * B_FACTOR) % DIV
            if b % 8 == 0:
                break
        if a % 65536 == b % 65536: # Last 16 bits
            count += 1
    return count
    
print(solve_part_2())
