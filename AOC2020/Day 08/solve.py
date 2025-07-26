def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def parse_instructions():
    def parse_line(line):
        ins, n = line.split()
        return (ins, int(n))
    instructions = [parse_line(line) for line in read_input_file_data().splitlines()]
    return instructions

def solve_part_1():
    instructions = parse_instructions()
    acc = 0
    ptr = 0
    seen_pointers = set()
    while ptr not in seen_pointers:
        seen_pointers.add(ptr)
        ins, n = instructions[ptr]
        if ins == 'acc':
            acc += n
            ptr += 1
        elif ins == 'jmp':
            ptr += n
        elif ins == 'nop':
            ptr += 1
    return acc

def solve_part_2():
    instructions = parse_instructions()
    LENGTH = len(instructions)
    def check_termination():
        nonlocal instructions, LENGTH
        acc = 0
        ptr = 0
        seen_pointers = set()
        while ptr not in seen_pointers:
            if ptr < 0 or ptr >= LENGTH:
                return True, acc
            seen_pointers.add(ptr)
            ins, n = instructions[ptr]
            if ins == 'acc':
                acc += n
                ptr += 1
            elif ins == 'jmp':
                ptr += n
            elif ins == 'nop':
                ptr += 1
        return False, acc
    for i in range(LENGTH):
        ins, n = instructions[i]
        if ins == 'acc':
            continue
        instructions[i] = ('jmp', n) if ins == 'nop' else ('nop', n)
        is_terminate, acc = check_termination()
        instructions[i] = (ins, n)
        if is_terminate:
            return acc
    
print(solve_part_2())
