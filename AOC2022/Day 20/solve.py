from collections import Counter

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def read_test_file_data():
    FILE = "test_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def parse_list():
    global LS_SIZE
    ls = []
    for line in read_input_file_data().splitlines():
        ls.append(int(line))
    LS_SIZE = len(ls)
    return ls

def parse_test_list():
    global LS_SIZE
    ls = []
    for line in read_test_file_data().splitlines():
        ls.append(int(line))
    LS_SIZE = len(ls)
    return ls

LS_SIZE = None

def solve_part_1():
    global LS_SIZE
    nums = parse_list()
    indices = [_ for _ in range(LS_SIZE)]

    for num_pos, num in enumerate(nums):
        if num == 0:
            continue
        num_index = indices[num_pos]
        num_new_index = (num_index + num) % (LS_SIZE - 1)
        if num_new_index == 0:
            num_new_index = LS_SIZE - 1
        if num_index == num_new_index:
            continue
        move_index = 1 if num_index > num_new_index else -1
        left = min(num_index, num_new_index)
        right = max(num_index, num_new_index)
        for index_pos, index in enumerate(indices):
            if left <= index <= right:
                indices[index_pos] = (indices[index_pos] + move_index) % LS_SIZE
        indices[num_pos] = num_new_index

    zipped_ls = list(zip(nums, indices))
    zipped_ls.sort(key = lambda tup: tup[1])
    sorted_ls = list(map(lambda tup: tup[0], zipped_ls))
        
    zero_pos = sorted_ls.index(0)
    pos1 = (zero_pos + 1000) % LS_SIZE
    pos2 = (zero_pos + 2000) % LS_SIZE
    pos3 = (zero_pos + 3000) % LS_SIZE
    sum_nums = sorted_ls[pos1] + sorted_ls[pos2] + sorted_ls[pos3]
    return sum_nums

def mix(nums, indices):
    for num_pos, num in enumerate(nums):
        if num == 0:
            continue
        num_index = indices[num_pos]
        num_new_index = (num_index + num) % (LS_SIZE - 1)
        if num_new_index == 0:
            num_new_index = LS_SIZE - 1
        if num_index == num_new_index:
            continue
        move_index = 1 if num_index > num_new_index else -1
        left = min(num_index, num_new_index)
        right = max(num_index, num_new_index)
        for index_pos, index in enumerate(indices):
            if left <= index <= right:
                indices[index_pos] = (indices[index_pos] + move_index) % LS_SIZE
        indices[num_pos] = num_new_index
    return indices

def solve_part_2():
    DECRYPTION_KEY = 811589153
    TIMES_TO_MIX = 10

    nums = parse_list()
    actual_nums = [num * DECRYPTION_KEY for num in nums]
    indices = [_ for _ in range(LS_SIZE)]
    for _ in range(TIMES_TO_MIX):
        indices = mix(actual_nums, indices)
    
    zipped_ls = list(zip(actual_nums, indices))
    zipped_ls.sort(key = lambda tup: tup[1])
    sorted_ls = list(map(lambda tup: tup[0], zipped_ls))
        
    zero_pos = sorted_ls.index(0)
    pos1 = (zero_pos + 1000) % LS_SIZE
    pos2 = (zero_pos + 2000) % LS_SIZE
    pos3 = (zero_pos + 3000) % LS_SIZE
    sum_nums = sorted_ls[pos1] + sorted_ls[pos2] + sorted_ls[pos3]
    return sum_nums
    
print(solve_part_2())
