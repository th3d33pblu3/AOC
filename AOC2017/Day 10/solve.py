from functools import reduce

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    SIZE = 256
    lengths = list(map(int, read_input_file_data().split(",")))
    nums = [i for i in range(SIZE)]

    def reverse_range(start, end):
        nums_copy = nums.copy()
        true_end = end % SIZE
        i = start % SIZE
        j = (end - 1) % SIZE
        while i != true_end:
            nums[i] = nums_copy[j]
            i = (i + 1) % SIZE
            j = (j - 1 + SIZE) % SIZE

    current_pos = 0
    skip_size = 0
    for length in lengths:
        start, end = current_pos, current_pos + length
        reverse_range(start, end)
        current_pos = (current_pos + length + skip_size) % SIZE
        skip_size += 1
    return nums[0] * nums[1]

def solve_part_2():
    SIZE = 256
    ROUNDS = 64
    lengths = list(map(ord, read_input_file_data()))
    lengths.extend([17, 31, 73, 47, 23])
    nums = [i for i in range(SIZE)]

    def reverse_range(start, end):
        nums_copy = nums.copy()
        true_end = end % SIZE
        i = start % SIZE
        j = (end - 1) % SIZE
        while i != true_end:
            nums[i] = nums_copy[j]
            i = (i + 1) % SIZE
            j = (j - 1 + SIZE) % SIZE

    current_pos = 0
    skip_size = 0
    for _ in range(ROUNDS):
        for length in lengths:
            start, end = current_pos, current_pos + length
            reverse_range(start, end)
            current_pos = (current_pos + length + skip_size) % SIZE
            skip_size = (skip_size + 1) % SIZE

    hash = ""
    for block_num in range(len(nums) // 16):
        block = nums[block_num * 16 : (block_num + 1) * 16]
        hex_val = hex(reduce(lambda a, b: a ^ b, block))[2:]
        if len(hex_val) < 2:
            hex_val = "0" + hex_val
        hash += hex_val
    return hash
    
print(solve_part_2())