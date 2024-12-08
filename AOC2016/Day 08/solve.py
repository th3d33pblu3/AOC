import numpy as np

def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def solve_part_1():
    screen = np.full((6, 50), False, dtype=bool)
    file = read_input_file()
    for line in file.read().splitlines():
        ins = line.split()
        if ins[0] == "rect":
            nums = ins[1].split("x")
            x = int(nums[0])
            y = int(nums[1])
            screen[:y, :x] = True
        elif ins[1] == "row":
            row = int(ins[2].split("=")[1])
            roll_value = int(ins[4])
            screen[row] = np.roll(screen[row], roll_value)
        else: # ins[1] == "column"
            col = int(ins[2].split("=")[1])
            roll_value = int(ins[4])
            screen[:, col] = np.roll(screen[:, col], roll_value)

    return np.count_nonzero(screen)

def solve_part_2():
    screen = np.full((6, 50), False)
    file = read_input_file()
    for line in file.read().splitlines():
        ins = line.split()
        if ins[0] == "rect":
            nums = ins[1].split("x")
            x = int(nums[0])
            y = int(nums[1])
            screen[:y, :x] = True
        elif ins[1] == "row":
            row = int(ins[2].split("=")[1])
            roll_value = int(ins[4])
            screen[row] = np.roll(screen[row], roll_value)
        else: # ins[1] == "column"
            col = int(ins[2].split("=")[1])
            roll_value = int(ins[4])
            screen[:, col] = np.roll(screen[:, col], roll_value)
    screen = screen.tolist()
    screen = list(map(lambda line: list(map(lambda bool: "#" if bool else ".", line)), screen))
    for i in range(0, 50, 5):
        for row in screen:
            print(row[i : i + 5])
        print()

    return "AFBUPZBJPS"
    
print(solve_part_2())
