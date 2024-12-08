from tqdm import tqdm
import math

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def parse_input():
    return int(read_input_file_data())

def solve_part_1():
    min_present_count = parse_input()
    min_elves_num_sum = min_present_count // 10

    houses = [1] * min_elves_num_sum
    houses[0] = 0
    for i in tqdm(range(2, min_elves_num_sum)):
        for j in range(i, min_elves_num_sum, i):
            houses[j] += i
    for house, house_elves_num_sum in enumerate(houses):
        if house_elves_num_sum >= min_elves_num_sum:
            return house

def solve_part_2():
    min_present_count = parse_input()
    min_house = min_present_count // 10

    houses = [0] * min_house
    for i in tqdm(range(1, min_house)):
        for j in range(1, 51):
            if i * j < min_house:
                houses[i * j] += i * 11
    for house, house_elves_num_sum in enumerate(houses):
        if house_elves_num_sum >= min_present_count:
            return house
    
print(solve_part_2())
