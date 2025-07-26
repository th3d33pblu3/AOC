def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    nums = list(map(int, read_input_file_data().split(',')))
    nums.reverse()
    for i in range(len(nums), 2020):
        if nums.count(nums[0]) == 1: # First time the number is spoken
            nums.insert(0, 0)
        else: # How many turns apart
            nums.insert(0, nums.index(nums[0], 1))
    return nums[0]

def solve_part_2():
    starting_nums = list(map(int, read_input_file_data().split(',')))
    last_pos = {}
    for i, n in enumerate(starting_nums[:-1]):
        last_pos[n] = i
    last_spoken_num = starting_nums[-1]
    index = len(starting_nums)
    while index < 30_000_000:
        if last_spoken_num in last_pos:
            diff = index - last_pos[last_spoken_num] - 1
            last_pos[last_spoken_num] = index-1
            last_spoken_num = diff
        else:
            last_pos[last_spoken_num] = index-1
            last_spoken_num = 0
        index += 1
    return last_spoken_num
    
print(solve_part_2())
