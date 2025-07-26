def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    nums = list(map(int, read_input_file_data().splitlines()))
    PREV_NUMS = 25
    for i, n in enumerate(nums[PREV_NUMS:]):
        prev_nums = nums[i:i+PREV_NUMS]
        flag = False
        for j, x in enumerate(prev_nums[:-1]):
            if n - x in prev_nums[j+1:]:
                flag = True
                break
        if not flag:
            return n

def solve_part_2():
    INVALID_NUM = 1309761972
    nums = list(map(int, read_input_file_data().splitlines()))
    curr_sum = nums[0] + nums[1]
    low = 0
    high = 2
    while curr_sum != INVALID_NUM:
        if curr_sum < INVALID_NUM:
            curr_sum += nums[high]
            high += 1
        else:
            curr_sum -= nums[low]
            low += 1
    return max(nums[low:high]) + min(nums[low:high])
    
print(solve_part_2())
