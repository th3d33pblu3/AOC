import math
from queue import Queue

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def parse_reactions():
    data = read_input_file_data()
    reactions = {} # output : (quantity, [(input, quantity)...])
    for line in data.splitlines():
        input_str, output_str = line.split(' => ')

        input_list = []
        inputs = input_str.split(', ')
        for input_item in inputs:
            quantity, chemical = input_item.split()
            quantity = int(quantity)
            input_list.append((chemical, quantity))

        outputs = output_str.split()
        output, quantity = outputs[1], int(outputs[0])

        reactions[output] = (quantity, input_list)
    return reactions

FUEL = 'FUEL'
ORE = 'ORE'

def solve_part_1(fuels=1):
    reactions = parse_reactions()
    chemicals = {key: 0 for key in reactions.keys()}
    chemicals[FUEL] = -fuels
    chemicals[ORE] = 0
    q = Queue()
    q.put(FUEL)
    while not q.empty():
        chemical = q.get()
        count = chemicals[chemical]
        if (chemical == ORE) or (count >= 0):
            continue
        # Make chemical
        output_quantity, inputs = reactions[chemical]
        multiplier = math.ceil(abs(count) / output_quantity)
        chemicals[chemical] += multiplier * output_quantity
        for input_chemical, input_quantity in inputs:
            chemicals[input_chemical] -= multiplier * input_quantity
            if chemicals[input_chemical] < 0 and input_chemical != ORE:
                q.put(input_chemical)
    return abs(chemicals[ORE])

def solve_part_2():
    part_1 = solve_part_1(1)
    TRILLION = 1_000_000_000_000
    low = TRILLION // part_1 # from part 1, we can definitely produce this many fuel
    high = TRILLION
    while high - low > 1:
        mid = (high + low) // 2
        ores_required = solve_part_1(mid)
        if ores_required > TRILLION:
            high = mid
        else:
            low = mid
    return low
    
print(solve_part_2())
