from collections import deque

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    programs = [chr(ord('a') + i) for i in range(16)]
    instructions = read_input_file_data().split(',')
    for ins in instructions:
        match ins[0]:
            case 's': # spin
                deq = deque(programs)
                deq.rotate(int(ins[1:]))
                programs = list(deq)
            case 'x': # exchange
                X, Y = tuple(map(int, ins[1:].split('/')))
                programs[X], programs[Y] = programs[Y], programs[X]
            case 'p': # partner
                X, Y = ins[1:].split('/')
                xi = programs.index(X)
                yi = programs.index(Y)
                programs[xi], programs[yi] = programs[yi], programs[xi]
            case _:
                raise Exception(f"Unexpected instruction {ins}")
    return ''.join(programs)

def solve_part_2():
    DANCE_MOVES = read_input_file_data().split(',')
    def dance(p):
        programs = list(p)
        for ins in DANCE_MOVES:
            match ins[0]:
                case 's': # spin
                    deq = deque(programs)
                    deq.rotate(int(ins[1:]))
                    programs = list(deq)
                case 'x': # exchange
                    X, Y = tuple(map(int, ins[1:].split('/')))
                    programs[X], programs[Y] = programs[Y], programs[X]
                case 'p': # partner
                    X, Y = ins[1:].split('/')
                    xi = programs.index(X)
                    yi = programs.index(Y)
                    programs[xi], programs[yi] = programs[yi], programs[xi]
                case _:
                    raise Exception(f"Unexpected instruction {ins}")
        return ''.join(programs)
    
    programs = ''.join([chr(ord('a') + i) for i in range(16)])
    dance_results = {}
    while programs not in dance_results:
        next_programs = dance(programs)
        dance_results[programs] = next_programs
        programs = next_programs

    CYCLE_START = programs
    cycle_length = 0
    while True:
        cycle_length += 1
        programs = dance_results[programs]
        if programs == CYCLE_START:
            break
    
    # Actual counting
    programs = ''.join([chr(ord('a') + i) for i in range(16)])
    remaining_dances = 1_000_000_000
    while programs != CYCLE_START:
        programs = dance_results[programs]
        remaining_dances -= 1
    remaining_dances %= cycle_length

    for _ in range(remaining_dances):
        programs = dance_results[programs]
    return programs

print(solve_part_2())
