import re

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    registers = {}
    instructions = read_input_file_data().splitlines()
    sounds = []

    def get_value(r: str):
        if re.match('^[-]?[0-9]+$', r):
            return int(r)
        else:
            return registers.get(r, 0)
    
    ptr = 0
    while True:
        ins = instructions[ptr]
        words = ins.split()
        match words[0]:
            case 'snd':
                sounds.append(get_value(words[1]))
            case 'set':
                registers[words[1]] = get_value(words[2])
            case 'add':
                registers[words[1]] = registers.get(words[1], 0) + get_value(words[2])
            case 'mul':
                registers[words[1]] = registers.get(words[1], 0) * get_value(words[2])
            case 'mod':
                registers[words[1]] = registers.get(words[1], 0) % get_value(words[2])
            case 'rcv':
                if get_value(words[1]) != 0:
                    return sounds[-1]
            case 'jgz':
                if get_value(words[1]) > 0:
                    ptr += get_value(words[2])
                    continue
            case _:
                raise Exception(f"Unknown instruction {ins}")
        ptr += 1

def solve_part_2():
    p1_snd_count = 0
    curr_program = 0
    other_program = 1

    instructions = read_input_file_data().splitlines()
    registers = [{'p': 0}, {'p': 1}]
    buffers = [[], []]
    is_waiting = [False, False]
    ptr = [0, 0]

    def get_value(r: str):
        nonlocal curr_program
        if re.match('^[-]?[0-9]+$', r):
            return int(r)
        else:
            return registers[curr_program].get(r, 0)
    
    while True:
        ins = instructions[ptr[curr_program]]
        words = ins.split()
        match words[0]:
            case 'snd':
                buffers[other_program].append(get_value(words[1]))
                is_waiting[other_program] = False
                if curr_program == 1:
                    p1_snd_count += 1
            case 'set':
                registers[curr_program][words[1]] = get_value(words[2])
            case 'add':
                registers[curr_program][words[1]] = registers[curr_program].get(words[1], 0) + get_value(words[2])
            case 'mul':
                registers[curr_program][words[1]] = registers[curr_program].get(words[1], 0) * get_value(words[2])
            case 'mod':
                registers[curr_program][words[1]] = registers[curr_program].get(words[1], 0) % get_value(words[2])
            case 'rcv':
                if len(buffers[curr_program]) != 0: # If there is something to receive
                    registers[curr_program][words[1]] = buffers[curr_program].pop(0)
                else: # Nothing to receive
                    is_waiting[curr_program] = True
                    if is_waiting[other_program]: # If other program also cannot execute, terminate
                        break
                    # Other program can execute
                    curr_program, other_program = other_program, curr_program
                    continue
            case 'jgz':
                if get_value(words[1]) > 0:
                    ptr[curr_program] += get_value(words[2])
                    continue
            case _:
                raise Exception(f"Unknown isntruction {ins}")
        ptr[curr_program] += 1
    return p1_snd_count
    
print(solve_part_2())
