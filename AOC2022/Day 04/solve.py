def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def get_range(line):
    range1, range2 = line.split(",")
    r1, r2 = range1.split("-")
    r3, r4 = range2.split("-")
    return int(r1), int(r2), int(r3), int(r4)

def solve_part_1():
    file = read_input_file()

    total_count = 0

    for ln in file.readlines():
        r1, r2, r3, r4 = get_range(ln)
        if ((r1 <= r3 and r2 >= r4) or (r1 >= r3 and r2 <= r4)):
            total_count += 1

    return total_count

def solve_part_2():
    file = read_input_file()

    total_count = 0

    for ln in file.readlines():
        r1, r2, r3, r4 = get_range(ln)
        if not ((r2 < r3) or (r4 < r1)):
            total_count += 1

    return total_count


print(solve_part_2())
