def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def parse_line(line):
    ins, n = line.split()
    n = int(n)
    return ins, n

def solve_part_1():
    instructions = list(map(parse_line, read_input_file_data().splitlines()))
    dist = 0
    depth = 0
    for ins, n in instructions:
        if ins == 'forward':
            dist += n
        elif ins == 'down':
            depth += n
        elif ins == 'up':
            depth -= n
    return dist * depth

def solve_part_2():
    instructions = list(map(parse_line, read_input_file_data().splitlines()))
    aim = 0
    dist = 0
    depth = 0
    for ins, n in instructions:
        if ins == 'forward':
            dist += n
            depth += aim * n
        elif ins == 'down':
            aim += n
        elif ins == 'up':
            aim -= n
    return dist * depth
    
print(solve_part_2())
