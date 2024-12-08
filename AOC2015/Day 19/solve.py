import re

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def parse_input_file_data():
    data = read_input_file_data()
    lines = data.splitlines()
    mappings = lines[:-2]
    mappings = list(map(lambda x: tuple(x.split(" => ")), mappings))
    org_str = lines[-1]
    return mappings, org_str

def solve_part_1():
    mappings, org_str = parse_input_file_data()
    unique = set()
    for old, new in mappings:
        index = 0
        left = ""
        right = org_str
        while old in right:
            index = right.index(old)
            left += right[:index]
            replacement = right[index : index + len(old)]
            right = right[index + len(old):]
            unique.add(left + new + right)
            left += replacement
    return len(unique)

def map_elements(molecules: str):
    CHANGES = [("Al", "A"), ("Ca", "C"), ("Mg", "M"), ("Si", "S"), ("Th", "T"), ("Ti", "U"), ("Rn", "("), ("Ar", ")")]
    for old, new in CHANGES:
        molecules = molecules.replace(old, new)
    return molecules

def map_placeholders(molecules: str):
    CHANGES = [('(F)', '!'), ('(M)', '@'), ('(A)', '#'), ('(FYM)', '$'), ('(MYF)', '%'), ('(FYF)', '^'), ('(FYFYF)', '&')]
    for old, new in CHANGES:
        molecules = molecules.replace(old, new)
    return molecules

def parse_input_file_data_advanced() -> tuple[str, list, list, list]:
    data = read_input_file_data()
    lines = data.splitlines()
    medicine = map_elements(lines[-1])
    mappings = lines[:-2]
    e_mappings = []
    limit_mappings = []
    base_mappings = []
    for line in mappings:
        left, right = tuple(line.split(" => "))
        if left == "e":
            e_mappings.append((left, map_elements(right)))
        elif "Rn" in right:
            limit_mappings.append((map_elements(left), map_placeholders(map_elements(right))))
        else:
            base_mappings.append((map_elements(left), map_elements(right)))
    
    return medicine, base_mappings, limit_mappings, e_mappings

def solve_part_2():

    MEDICINE, base_mappings, limit_mappings, e_mappings = parse_input_file_data_advanced()

    LIMIT_ROOTS = {"F", "M", "A", "FYM", "MYF", "FYF", "FYFYF"}
    E_ROOTS = {"HF", "NA", "OM"}
    NUM_Y_TO_ROOT_LEN = {0: 1, 1: 3, 2: 5}
    LEFT = "("
    RIGHT = ")"
    DUMMY = "_"
    MAPPINGS = base_mappings + limit_mappings
    
    def find_within_limits(molecules: str) -> tuple[int, int]: # Indices includes the LIMITS themselves
        assert LEFT in molecules
        open_close = 1
        starting_index = molecules.index(LEFT)
        ending_index = starting_index + 1
        while open_close > 0:
            element = molecules[ending_index]
            if element == LEFT:
                open_close += 1
            elif element == RIGHT:
                open_close -= 1
            ending_index += 1
        return starting_index, ending_index

    def remove_limits(molecules: str) -> tuple[str, int]:
        total_steps = 0
        molecules_no_limit = ""
        index = 0
        while index < len(molecules):
            if molecules[index] == LEFT:
                starting_index, ending_index = find_within_limits(molecules[index:])
                steps = solve_steps_in_limits(molecules[index:][starting_index + 1: ending_index - 1])
                total_steps += steps
                molecules_no_limit += DUMMY
                index += ending_index
                continue
            else:
                molecules_no_limit += molecules[index]
            index += 1
        return molecules_no_limit, total_steps

    def solve_steps_in_limits(molecules: str) -> int:
        molecules_no_limits, steps = remove_limits(molecules)
        num_y = molecules_no_limits.count("Y")
        root_len = NUM_Y_TO_ROOT_LEN[num_y]
        steps_to_reduce_to_root = len(molecules_no_limits) - root_len
        return steps + steps_to_reduce_to_root

    molecules_no_limits, steps_sofar = remove_limits(MEDICINE)
    steps_to_reduce_to_e = steps_sofar + len(molecules_no_limits) - 1
    return steps_to_reduce_to_e
    
print(solve_part_2())
