def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    heat_map = [[int(c) for c in line] for line in read_input_file_data().splitlines()]
    LENGTH = len(heat_map)
    WIDTH = len(heat_map[0])

    


def solve_part_2():
    pass
    
print(solve_part_1())
