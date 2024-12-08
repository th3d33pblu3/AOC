def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    total_fuel = 0
    for line in read_input_file_data().splitlines():
        total_fuel += max(int(line) // 3 - 2, 0)
    return total_fuel

def solve_part_2():
    total_fuel = 0
    for line in read_input_file_data().splitlines():
        curr_fuel = int(line)
        while curr_fuel > 0:
            curr_fuel = max(curr_fuel // 3 - 2, 0)
            total_fuel += curr_fuel 
    return total_fuel

print(solve_part_2())
