def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def solve_part_1():
    file = read_input_file()
    code = ""
    num = 5
    for line in file.read().splitlines():
        for char in line:
            if char == "U":
                if num not in [1, 2, 3]:
                    num -= 3
            elif char == "D":
                if num not in [7, 8, 9]:
                    num += 3
            elif char == "L":
                if num not in [1, 4, 7]:
                    num -= 1
            elif char == "R":
                if num not in [3, 6, 9]:
                    num += 1
        code += str(num)
    return code

def solve_part_2():
    #     1
    #   2 3 4
    # 5 6 7 8 9
    #   A B C
    #     D

    # Remapped
    #       03
    #    07 08 09
    # 11 12 13 14 15
    #    17 18 19
    #       23
    unmapping = { 3: "1",
                  7: "2",
                  8: "3",
                  9: "4",
                 11: "5",
                 12: "6",
                 13: "7",
                 14: "8",
                 15: "9",
                 17: "A",
                 18: "B",
                 19: "C",
                 23: "D"}

    file = read_input_file()
    code = ""
    num = 11
    for line in file.read().splitlines():
        for char in line:
            if char == "U":
                if num not in [11, 7, 3, 9, 15]:
                    num -= 5
            elif char == "D":
                if num not in [11, 17, 23, 19, 15]:
                    num += 5
            elif char == "L":
                if num not in [3, 7, 11, 17, 23]:
                    num -= 1
            elif char == "R":
                if num not in [3, 9, 15, 19, 23]:
                    num += 1
        code += unmapping[num]
    return code
    
print(solve_part_2())
