from itertools import combinations

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def parse_containers():
    data = read_input_file_data()
    containers = []
    for line in data.splitlines():
        containers.append(int(line))
    return containers

def solve_part_1():
    LIMIT = 150
    containers = parse_containers()
    total_exact_fits = 0
    for i in range(1, len(containers)):
        combis = combinations(containers, i)
        exact_fits = len(list(filter(lambda x: sum(x) == LIMIT, combis)))
        total_exact_fits += exact_fits
    return total_exact_fits

def solve_part_2():
    LIMIT = 150
    containers = parse_containers()
    for i in range(1, len(containers)):
        combis = combinations(containers, i)
        exact_fits = len(list(filter(lambda x: sum(x) == LIMIT, combis)))
        if exact_fits != 0:
            return exact_fits
    
print(solve_part_2())
