import re

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    ins = read_input_file_data()
    pattern = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
    result = re.findall(pattern, ins)
    total = 0
    for x, y in result:
        total += int(x) * int(y)
    return total

def solve_part_2():
    def get_muls(text):
        pattern = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"
        result = re.findall(pattern, text)
        total = 0
        for x, y in result:
            total += int(x) * int(y)
        return total

    total = 0
    ins = read_input_file_data()
    segs = ins.split("do()")
    for seg in segs:
        text = seg.split("don't()")[0]
        total += get_muls(text)
    return total
    
print(solve_part_2())
