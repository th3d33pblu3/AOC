def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def parse_aunts():
    data = read_input_file_data()
    aunts = [None] # So that each aunt is at the right index
    for line in data.splitlines():
        words = line.split()
        values = words[2:]
        aunt = {}
        i = 0
        while i < len(values):
            item = values[i][:-1]
            i += 1
            num = int(values[i]) if (i == len(values) - 1) else int(values[i][:-1])
            i += 1
            aunt[item] = num
        aunts.append(aunt)
    return aunts

CORRECT_AUNT_SUE = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

def solve_part_1():
    aunts = parse_aunts()
    for i in range(1, len(aunts)):
        aunt = aunts[i]
        is_correct_aunt = True
        for item in aunt.keys():
            if aunt[item] != CORRECT_AUNT_SUE[item]:
                is_correct_aunt = False
                break
        if is_correct_aunt:
            return i

def solve_part_2():
    aunts = parse_aunts()
    for i in range(1, len(aunts)):
        aunt = aunts[i]
        is_correct_aunt = True
        for item in aunt.keys():
            if item == "cats" or item == "trees":
                if aunt[item] <= CORRECT_AUNT_SUE[item]:
                    is_correct_aunt = False
                    break
            elif item == "pomeranians" or item == "goldfish":
                if aunt[item] >= CORRECT_AUNT_SUE[item]:
                    is_correct_aunt = False
                    break
            else:
                if aunt[item] != CORRECT_AUNT_SUE[item]:
                    is_correct_aunt = False
                    break
        if is_correct_aunt:
            return i
    
print(solve_part_2())
