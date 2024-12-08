def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def solve_part_1():
    file = read_input_file()
    max_sum = 0
    curr_sum = 0
    for ln in file.readlines():
        if ln == "\n":
            if curr_sum > max_sum:
                max_sum = curr_sum
            curr_sum = 0
        else:
            curr_sum += int(ln)
    return max_sum

def solve_part_2():
    file = read_input_file()
    max_sum = [0, 0, 0]
    curr_sum = 0
    for ln in file.readlines():
        if ln == "\n":
            if curr_sum > max_sum[2]:
                max_sum[0] = max_sum[1]
                max_sum[1] = max_sum[2]
                max_sum[2] = curr_sum
            elif curr_sum > max_sum[1]:
                max_sum[0] = max_sum[1]
                max_sum[1] = curr_sum
            elif curr_sum > max_sum[0]:
                max_sum[0] = curr_sum
            curr_sum = 0
        else:
            curr_sum += int(ln)
    return sum(max_sum)

print(solve_part_2())
