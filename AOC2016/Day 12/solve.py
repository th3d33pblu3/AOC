def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    lines = read_input_file_data().splitlines()
    instruction_ptr = 0

    def get_value(s):
        if s in "abcd":
            return registers[s]
        else:
            return int(s)

    while instruction_ptr < len(lines):
        words = lines[instruction_ptr].split()
        if words[0] == 'cpy':
            registers[words[2]] = get_value(words[1])
        elif words[0] == 'inc':
            registers[words[1]] += 1
        elif words[0] == 'dec':
            registers[words[1]] -= 1
        elif words[0] == 'jnz':
            if get_value(words[1]) != 0:
                instruction_ptr += get_value(words[2])
                continue
        instruction_ptr += 1
    
    return registers['a']


def solve_part_2():
    registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
    lines = read_input_file_data().splitlines()
    instruction_ptr = 0

    def get_value(s):
        if s in "abcd":
            return registers[s]
        else:
            return int(s)

    while instruction_ptr < len(lines):
        words = lines[instruction_ptr].split()
        if words[0] == 'cpy':
            registers[words[2]] = get_value(words[1])
        elif words[0] == 'inc':
            registers[words[1]] += 1
        elif words[0] == 'dec':
            registers[words[1]] -= 1
        elif words[0] == 'jnz':
            if get_value(words[1]) != 0:
                instruction_ptr += get_value(words[2])
                continue
        instruction_ptr += 1
    
    return registers['a']
    
print(solve_part_2())
