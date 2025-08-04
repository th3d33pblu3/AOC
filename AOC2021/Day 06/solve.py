def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    nums = list(map(int, read_input_file_data().split(',')))
    fishes = {}
    for i in range(9):
        fishes[i] = nums.count(i)
    
    for _ in range(80):
        new_fishes = {}
        for i in range(1, 9):
            new_fishes[i-1] = fishes[i]
        new_fishes[6] += fishes[0]
        new_fishes[8] = fishes[0]
        fishes = new_fishes
    return sum(fishes.values())

def solve_part_2():
    nums = list(map(int, read_input_file_data().split(',')))
    fishes = {}
    for i in range(9):
        fishes[i] = nums.count(i)
    
    for _ in range(256):
        new_fishes = {}
        for i in range(1, 9):
            new_fishes[i-1] = fishes[i]
        new_fishes[6] += fishes[0]
        new_fishes[8] = fishes[0]
        fishes = new_fishes
    return sum(fishes.values())
    
print(solve_part_2())
