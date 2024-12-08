def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    orders, ins = read_input_file_data().split('\n\n')
    rules = set()
    for line in orders.splitlines():
        rules.add(tuple(map(int, line.split('|'))))

    total = 0
    def is_valid(nums):
        for i in range(1, len(nums)):
            for j in range(i):
                if (nums[j], nums[i]) not in rules:
                    return False
        return True
    for line in ins.splitlines():
        nums = list(map(int, line.split(',')))
        if is_valid(nums):
            mid = (len(nums) - 1) // 2
            total += nums[mid]
    return total

def solve_part_2():
    orders, ins = read_input_file_data().split('\n\n')
    rules = set()
    for line in orders.splitlines():
        rules.add(tuple(map(int, line.split('|'))))

    total = 0
    def is_valid(nums):
        for i in range(1, len(nums)):
            for j in range(i):
                if (nums[j], nums[i]) not in rules:
                    return False
        return True
    def order_correctly(nums):
        while not is_valid(nums):
            for i in range(1, len(nums)):
                for j in range(i):
                    if (nums[j], nums[i]) not in rules:
                        temp = nums[j]
                        nums[j] = nums[i]
                        nums[i] = temp
        return nums
    for line in ins.splitlines():
        nums = list(map(int, line.split(',')))
        if not is_valid(nums):
            nums = order_correctly(nums)
            mid = (len(nums) - 1) // 2
            total += nums[mid]
    return total
    
print(solve_part_2())
