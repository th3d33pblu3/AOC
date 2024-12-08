import re

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    lines = read_input_file_data().splitlines()
    sum = 0
    for line in lines:
        nums = re.findall(r'\d', line)
        sum += int(nums[0] + nums[-1])
    return sum

mapper = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
def convert(text: str):
    if text.isdigit():
        return int(text)
    return mapper[text]

def solve_part_2():
    lines = read_input_file_data().splitlines()
    sum = 0
    for line in lines:
        nums = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
        print(nums)
        first = convert(nums[0])
        last = convert(nums[-1])
        sum += (first * 10) + last
        print((first * 10) + last)
    return sum
    
print(solve_part_2())
