def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    nums = list(map(int, read_input_file_data().splitlines()))
    increased = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            increased += 1
    return increased

def solve_part_2():
    nums = list(map(int, read_input_file_data().splitlines()))
    increased = 0
    for i in range(4, len(nums) + 1):
        if sum(nums[i-3:i]) > sum(nums[i-4:i-1]):
            increased += 1
    return increased
    
print(solve_part_2())
