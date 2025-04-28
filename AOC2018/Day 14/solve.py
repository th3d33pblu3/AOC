def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    NUM_RECIPES = int(read_input_file_data())
    scoreboard = [3, 7]
    elf1 = 0
    elf2 = 1

    while len(scoreboard) < NUM_RECIPES + 10:
        s1 = scoreboard[elf1]
        s2 = scoreboard[elf2]
        new_recipe = s1 + s2
        if new_recipe < 10:
            scoreboard.append(new_recipe)
        else:
            scoreboard.extend([1, new_recipe - 10])
        elf1 = (elf1 + 1 + s1) % len(scoreboard)
        elf2 = (elf2 + 1 + s2) % len(scoreboard)
    
    return ''.join(map(str, scoreboard[NUM_RECIPES : NUM_RECIPES + 10]))

def solve_part_2():
    RECIPE_PATTERN = [int(s) for s in read_input_file_data()]
    PATTERN_LEN = len(RECIPE_PATTERN)
    scoreboard = [3, 7]
    elf1 = 0
    elf2 = 1

    while True:
        s1 = scoreboard[elf1]
        s2 = scoreboard[elf2]
        new_recipe = s1 + s2
        if new_recipe < 10:
            scoreboard.append(new_recipe)
            if len(scoreboard) >= PATTERN_LEN and scoreboard[-PATTERN_LEN:] == RECIPE_PATTERN:
                return len(scoreboard) - PATTERN_LEN
        else:
            scoreboard.extend([1, new_recipe - 10])
            if len(scoreboard) >= PATTERN_LEN and scoreboard[-PATTERN_LEN:] == RECIPE_PATTERN:
                return len(scoreboard) - PATTERN_LEN
            if len(scoreboard) - 1 >= PATTERN_LEN and scoreboard[-PATTERN_LEN-1 : -1] == RECIPE_PATTERN:
                return len(scoreboard) - 1 - PATTERN_LEN
        elf1 = (elf1 + 1 + s1) % len(scoreboard)
        elf2 = (elf2 + 1 + s2) % len(scoreboard)
    
print(solve_part_2())
