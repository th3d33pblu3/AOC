def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def get_num_list():
    data = read_input_file_data()
    return [int(c) for c in data]

BASE_LIST = [0, 1, 0, -1]

def solve_part_1():
    nums = get_num_list()
    LENGTH = len(nums)
    for _ in range(100):
        nums = [abs(sum([n * BASE_LIST[((j+1)//(i+1)) % 4] for (j, n) in enumerate(nums)])) % 10 for i in range(LENGTH)]
    return ''.join(list(map(str, nums[:8])))

def solve_part_2():
    # Setup
    nums = get_num_list()
    num_list_length = len(nums) * 10000
    offset = int(''.join(list(map(str, nums[:7]))))
    assert offset >= (num_list_length // 2) + 1
    nums = (nums * 10000)[offset:]
    SIZE = len(nums)
    
    # Looping 100 times
    for _ in range(100):
        for i in range(SIZE - 2, -1, -1):
            nums[i] = (nums[i] + nums[i+1]) % 10
    
    return ''.join(list(map(str, nums[:8])))
    
print(solve_part_2())