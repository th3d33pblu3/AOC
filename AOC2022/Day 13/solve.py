import functools
import json

def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def parse(string):
    return json.loads(string)

def compare(left_list, right_list):
    if left_list == right_list:
        return None
    for index in range(len(left_list)):
        left = left_list[index]
        try:
            right = right_list[index]
        except Exception:
            return False

        # print(f"Comparing: {left}, {right}")

        if (type(left) == int and type(right) == int):
            if left < right:
                return True
            if left > right:
                return False
        elif type(left) == int:
            result = compare([left], right)
            if result != None:
                return result
        elif type(right) == int:
            result = compare(left, [right])
            if result != None:
                return result
        else:
            result = compare(left, right)
            if result != None:
                return result
    return True

def solve_part_1():
    file = read_input_file()
    data = file.read().splitlines()
    index = 1
    index_sum = 0
    for i in range(0, len(data), 3):
        left, right = parse(data[i]), parse(data[i + 1])
        print(f"Comparing index: {index}\nLeft : {left}\nRight: {right}")
        if compare(left, right):
            index_sum += index
            print("Result == True")
        else:
            print("Result == False")
        index += 1
    return index_sum

def compareKey(left_list, right_list):
    if left_list == right_list:
        return 0
    for index in range(len(left_list)):
        left = left_list[index]
        try:
            right = right_list[index]
        except Exception:
            return 1

        if (type(left) == int and type(right) == int):
            if left < right:
                return -1
            if left > right:
                return 1
        elif type(left) == int:
            result = compareKey([left], right)
            if result != 0:
                return result
        elif type(right) == int:
            result = compareKey(left, [right])
            if result != 0:
                return result
        else:
            result = compareKey(left, right)
            if result != 0:
                return result
    return -1

def solve_part_2():
    DIVIDER1 = [[2]]
    DIVIDER2 = [[6]]

    file = read_input_file()
    data = file.read().splitlines()
    packets = []
    for i in range(0, len(data), 3):
        left, right = parse(data[i]), parse(data[i + 1])
        packets.append(left)
        packets.append(right)
    packets.append(DIVIDER1)
    packets.append(DIVIDER2)
    packets = sorted(packets, key=functools.cmp_to_key(compareKey))
    for packet in packets:
        print(packet)
    index = 0
    total = 0
    while packets[index] != DIVIDER1:
        index += 1
    index += 1
    total = index
    while packets[index] != DIVIDER2:
        index += 1
    index += 1
    total *= index
    return total
    
print(solve_part_2())
