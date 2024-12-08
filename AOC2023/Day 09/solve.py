def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def extrapolate(nums: list[int]) -> int:
    if nums[0] == 0 and nums[-1] == 0: # Might be buggy
        return 0
    diffs = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
    e_diff = extrapolate(diffs)
    return nums[-1] + e_diff

def solve_part_1():
    output = 0
    for line in read_input_file_data().splitlines():
        nums = list(map(int, line.split()))
        output += extrapolate(nums)
    return output

def extrapolate_back(nums: list[int]):
    if nums[0] == 0 and nums[-1] == 0: # Might be buggy
        return 0
    diffs = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
    e_diff = extrapolate_back(diffs)
    return nums[0] - e_diff

def solve_part_2():
    output = 0
    for line in read_input_file_data().splitlines():
        nums = list(map(int, line.split()))
        output += extrapolate_back(nums)
    return output
    
print(solve_part_2())
