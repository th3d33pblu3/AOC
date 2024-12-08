import numpy as np
import re

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    SIZE = 1000
    fabric = np.zeros((SIZE, SIZE), dtype=np.int32)
    for line in read_input_file_data().splitlines():
        id, x_start, y_start, width, height = list(map(int, re.split(r'\D{1,}', line)[1:]))
        fabric[y_start : y_start + height, x_start : x_start + width] += 1
    return np.count_nonzero(fabric[fabric > 1])

def solve_part_2():
    SIZE = 1000
    fabric = np.zeros((SIZE, SIZE), dtype=np.int32)
    lines = read_input_file_data().splitlines()
    for line in lines:
        id, x_start, y_start, width, height = list(map(int, re.split(r'\D{1,}', line)[1:]))
        fabric[y_start : y_start + height, x_start : x_start + width] += 1
    for line in lines:
        id, x_start, y_start, width, height = list(map(int, re.split(r'\D{1,}', line)[1:]))
        if np.count_nonzero(fabric[y_start : y_start + height, x_start : x_start + width] != 1) == 0:
            return id
    
print(solve_part_2())
