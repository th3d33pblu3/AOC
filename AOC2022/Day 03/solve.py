def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def get_priority(char):
    ascii_value = ord(char)
    if ascii_value <= 90:
        return ascii_value - 38 # - 64 + 26
    else:
        return ascii_value - 96



def solve_part_1():
    file = read_input_file()
    
    def find_common_item(str):
        size = len(str) // 2
        dict = {}
        for char in str[: size]:
            dict[char] = True

        for char in str[size :]:
            if dict.get(char) == True:
                return char

    total_priority = 0

    for ln in file.readlines():
        total_priority += get_priority(find_common_item(ln))

    return total_priority

def solve_part_2():
    file = read_input_file()
    lines = file.readlines()

    def find_common_item(str1, str2, str3):
        dict = {}
        for char in str1:
            dict[char] = 1

        for char in str2:
            if dict.get(char) == 1:
                dict[char] = 2
        
        for char in str3:
            if dict.get(char) == 2:
                return char

    total_priority = 0

    for index in range(0, len(lines), 3):
        total_priority += get_priority(find_common_item(lines[index], lines[index + 1], lines[index + 2]))

    return total_priority


print(solve_part_2())
