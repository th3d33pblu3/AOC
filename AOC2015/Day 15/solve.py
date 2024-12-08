def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

NUM_INGREDIENTS = 4
LIMIT = 100

def parse_ingredients():
    ingredients = []
    data = read_input_file_data()
    for line in data.splitlines():
        words = line.split()
        capacity = int(words[2][:-1])
        durability = int(words[4][:-1])
        flavour = int(words[6][:-1])
        texture = int(words[8][:-1])
        calories = int(words[10])
        ingredients.append((capacity, durability, flavour, texture, calories))
    return ingredients

def get_all_combi():
    all_combi = []
    for a in range(LIMIT):
        for b in range(LIMIT - a):
            for c in range(LIMIT - a - b):
                d = LIMIT - a - b - c
                all_combi.append((a, b, c, d))
    return all_combi

def solve_part_1():
    ingredients = parse_ingredients()
    all_combi = get_all_combi()

    max_score = 0
    for combi in all_combi:
        cap = dur = flv = txt = 0
        for i, ingredient in enumerate(ingredients):
            cap += ingredient[0] * combi[i]
            dur += ingredient[1] * combi[i]
            flv += ingredient[2] * combi[i]
            txt += ingredient[3] * combi[i]
        cap = max(0, cap)
        dur = max(0, dur)
        flv = max(0, flv)
        txt = max(0, txt)
        score = cap * dur * flv * txt
        max_score = max(max_score, score)
    
    return max_score

def solve_part_2():
    ingredients = parse_ingredients()
    all_combi = get_all_combi()

    max_score = 0
    for combi in all_combi:
        cal = 0
        cap = dur = flv = txt = 0
        for i, ingredient in enumerate(ingredients):
            cap += ingredient[0] * combi[i]
            dur += ingredient[1] * combi[i]
            flv += ingredient[2] * combi[i]
            txt += ingredient[3] * combi[i]
            cal += ingredient[4] * combi[i]

        if cal != 500:
            continue

        cap = max(0, cap)
        dur = max(0, dur)
        flv = max(0, flv)
        txt = max(0, txt)
        score = cap * dur * flv * txt
        max_score = max(max_score, score)
    
    return max_score
    
print(solve_part_2())
