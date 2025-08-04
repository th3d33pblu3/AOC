import statistics

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    nums = list(map(int, read_input_file_data().split(',')))
    best_pos = int(statistics.median(nums))
    return sum([abs(n - best_pos) for n in nums])

def solve_part_2():
    nums = list(map(int, read_input_file_data().split(',')))
    best_pos = int(statistics.mean(nums))
    steps = [abs(n - best_pos) for n in nums]
    return sum([n * (n + 1) // 2 for n in steps])
    
print(solve_part_2())
