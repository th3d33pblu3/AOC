import math
import numpy as np

def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def get_nums():
    return list(map(int, read_input_file().read().splitlines()[0].split("\t")))

def solve_part_1():
    nums = np.array(get_nums())
    number_of_banks = len(nums)
    seen_before = {}
    
    steps = 0
    while seen_before.get(tuple(nums)) == None:
        seen_before[tuple(nums)] = True

        max_index = np.argmax(nums)
        blocks_to_distribute = nums[max_index]
        nums[max_index] = 0

        high = math.ceil(blocks_to_distribute / number_of_banks)
        low = math.floor(blocks_to_distribute / number_of_banks)
        num_banks_receive_high = blocks_to_distribute % number_of_banks
        num_banks_receive_low = number_of_banks - num_banks_receive_high

        index = (max_index + 1) % number_of_banks
        while num_banks_receive_high > 0:
            nums[index] += high
            index = (index + 1) % number_of_banks
            num_banks_receive_high -= 1
        while num_banks_receive_low > 0:
            nums[index] += low
            index = (index + 1) % number_of_banks
            num_banks_receive_low -= 1

        steps += 1

    return steps

def solve_part_2():
    nums = np.array(get_nums())
    number_of_banks = len(nums)
    seen_before = {}
    
    steps = 0
    while seen_before.get(tuple(nums)) == None:
        seen_before[tuple(nums)] = steps

        max_index = np.argmax(nums)
        blocks_to_distribute = nums[max_index]
        nums[max_index] = 0

        high = math.ceil(blocks_to_distribute / number_of_banks)
        low = math.floor(blocks_to_distribute / number_of_banks)
        num_banks_receive_high = blocks_to_distribute % number_of_banks
        num_banks_receive_low = number_of_banks - num_banks_receive_high

        index = (max_index + 1) % number_of_banks
        while num_banks_receive_high > 0:
            nums[index] += high
            index = (index + 1) % number_of_banks
            num_banks_receive_high -= 1
        while num_banks_receive_low > 0:
            nums[index] += low
            index = (index + 1) % number_of_banks
            num_banks_receive_low -= 1

        steps += 1

    return steps - seen_before[tuple(nums)]
    
print(solve_part_2())
