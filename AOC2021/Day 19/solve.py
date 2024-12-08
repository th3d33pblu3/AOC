def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    scanners = [[tuple(map(int, coordinates.split(','))) for coordinates in sc.splitlines()[1:]] for sc in read_input_file_data().split('\n\n')]
    

def solve_part_2():
    pass
    
print(solve_part_1())
