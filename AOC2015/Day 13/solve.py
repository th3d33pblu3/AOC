from itertools import permutations

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def get_guests_and_happiness_table():
    happiness_table = {}
    guests = []
    data = read_input_file_data()
    for line in data.splitlines():
        words = line.split()

        name = words[0]
        positivity = 1 if words[2] == "gain" else -1
        val = int(words[3]) * positivity
        other_person = words[-1][:-1]

        if name not in guests:
            guests.append(name)
            happiness_table[name] = {}

        happiness_table[name][other_person] = val

    return guests, happiness_table

def get_all_round_table_perms(guests):
    fix_point = guests[0]
    others = guests[1:]
    perms = permutations(others)
    all_perms = []
    for perm in perms:
        perm = list(perm)
        perm.insert(0, fix_point)
        all_perms.append(perm)
    return all_perms

def solve_part_1():
    guests, happiness_table = get_guests_and_happiness_table()
    all_perms = get_all_round_table_perms(guests)

    max_happiness = 0
    for perm in all_perms:
        happiness = happiness_table[perm[-1]][perm[0]] + happiness_table[perm[0]][perm[-1]]
        for index in range(len(perm) - 1):
            happiness += happiness_table[perm[index]][perm[index + 1]] \
                       + happiness_table[perm[index + 1]][perm[index]]
        max_happiness = max(max_happiness, happiness)

    return max_happiness

def solve_part_2():
    guests, happiness_table = get_guests_and_happiness_table()
    perms = permutations(guests)

    max_happiness = 0
    for perm in perms:
        happiness = 0
        for index in range(len(perm) - 1):
            happiness += happiness_table[perm[index]][perm[index + 1]] \
                       + happiness_table[perm[index + 1]][perm[index]]
        max_happiness = max(max_happiness, happiness)

    return max_happiness
    
print(solve_part_2())
