def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def solve_part_1():
    file = read_input_file()
    checksum = 0
    for line in file.read().splitlines():
        nums = list(map(int, line.split("\t")))
        nums.sort()
        checksum += nums[-1] - nums[0]
    return checksum

def solve_part_2():
    file = read_input_file()
    result_sum = 0
    for line in file.read().splitlines():
        nums = list(map(int, line.split("\t")))
        nums.sort(reverse=True)
        breaker = False
        for i in range(len(nums)):
            if breaker:
                break
            num = nums[i]
            for x in nums[i + 1 :]:
                if num % x == 0:
                    result_sum += num / x
                    breaker = True
                    break
    return result_sum
    
print(solve_part_2())
