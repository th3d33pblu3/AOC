import re

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    limits = {'red': 12, 'green': 13, 'blue': 14}
    sum_id = 0
    for id, line in enumerate(read_input_file_data().splitlines()):
        id = id + 1
        sets = re.search(r': (.*)', line).group(1)
        sets = sets.split('; ')

        is_valid = True
        for set in sets:
            colours = set.split(', ')
            for colour_count in colours:
                count, colour = colour_count.split(' ')
                if int(count) > limits[colour]:
                    is_valid = False
                    break
            if not is_valid:
                break
        
        if is_valid:
            sum_id += id

    return sum_id

def solve_part_2():
    power = 0
    for line in read_input_file_data().splitlines():
        sets = re.search(r': (.*)', line).group(1)
        sets = sets.split('; ')

        min_cubes = {'red': 0, 'green': 0, 'blue': 0}
        for set in sets:
            colours = set.split(', ')
            for colour_count in colours:
                count, colour = colour_count.split(' ')
                min_cubes[colour] = max(int(count), min_cubes[colour])
        power += min_cubes['red'] * min_cubes['green'] * min_cubes['blue']

    return power
    
print(solve_part_2())
