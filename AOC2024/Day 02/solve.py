def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    def is_safe(l):
        if len(l) <= 1:
            return True
        sign = 1 if l[1] - l[0] > 0 else -1
        for i in range(1, len(l)):
            diff = (l[i] - l[i-1]) * sign
            if diff < 1 or diff > 3:
                return False
        return True
    
    safe_lines = 0
    for line in read_input_file_data().splitlines():
        nums = list(map(int, line.split()))
        if is_safe(nums):
            safe_lines += 1
    return safe_lines

def solve_part_2():
    def is_safe(l):
        if len(l) <= 1:
            return True
        sign = 1 if l[1] - l[0] > 0 else -1
        for i in range(1, len(l)):
            diff = (l[i] - l[i-1]) * sign
            if diff < 1 or diff > 3:
                return False
        return True

    safe_lines = 0
    for line in read_input_file_data().splitlines():
        nums = list(map(int, line.split()))
        sign = 1 if nums[1] - nums[0] > 0 else -1
        for i in range(1, len(nums)):
            diff = (nums[i] - nums[i-1]) * sign
            if diff < 1 or diff > 3:
                nums2 = nums.copy()
                nums2.pop(i)
                if is_safe(nums2):
                    safe_lines += 1
                else:
                    nums3 = nums.copy()
                    nums3.pop(i-1)
                    if is_safe(nums3):
                        safe_lines += 1
                    else:
                        nums4 = nums.copy()
                        nums4.pop(0)
                        if is_safe(nums4):
                            safe_lines += 1
                break
        else:
            safe_lines += 1
    return safe_lines
    
print(solve_part_2())
