def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def solve_part_1():
    file = read_input_file()
    valid = 0
    invalid = 0
    for line in file.read().splitlines():
        a, b, c = line.split()
        ls = [int(a), int(b), int(c)]
        ls.sort()
        if ((ls[0] + ls[1]) > ls[2]):
            valid += 1
        else:
            invalid += 1
    return valid


def solve_part_2():
    file = read_input_file()
    valid = 0
    invalid = 0
    lines = file.read().splitlines()
    for index in range(0, len(lines), 3):
        l1, l2, l3 = lines[index : index + 3]
        a, b, c = l1.split()
        d, e, f = l2.split()
        g, h, i = l3.split()
        ls = [int(a), int(d), int(g)]
        ls.sort()
        if ((ls[0] + ls[1]) > ls[2]):
            valid += 1
        else:
            invalid += 1
        ls = [int(b), int(e), int(h)]
        ls.sort()
        if ((ls[0] + ls[1]) > ls[2]):
            valid += 1
        else:
            invalid += 1
        ls = [int(c), int(f), int(i)]
        ls.sort()
        if ((ls[0] + ls[1]) > ls[2]):
            valid += 1
        else:
            invalid += 1
    return valid
    
print(solve_part_2())
