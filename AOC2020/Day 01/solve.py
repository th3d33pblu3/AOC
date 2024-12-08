def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    nums = set(map(int, read_input_file_data().splitlines()))
    SUM = 2020
    for num in nums:
        if SUM - num in nums:
            return num * (SUM - num)

def solve_part_2():
    nums = set(map(int, read_input_file_data().splitlines()))
    SUM = 2020
    for num1 in nums:
        for num2 in nums:
            for num3 in nums:
                if num1 != num2 and num2 != num3 and num1 != num3:
                    if num1 + num2 + num3 == SUM:
                        return num1 * num2 * num3
    
print(solve_part_2())
