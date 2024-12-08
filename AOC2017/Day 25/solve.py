def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

class States:
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5

class Dir:
    LEFT = -1
    RIGHT = 1

def solve():
    tape = {}
    cursor = 0
    state = States.A
    steps = 12683008

    def take_step():
        nonlocal tape, cursor, state
        match state:
            case States.A:
                if tape.get(cursor, 0) == 0:
                    tape[cursor] = 1
                    cursor += Dir.RIGHT
                    state = States.B
                else:
                    tape[cursor] = 0
                    cursor += Dir.LEFT
                    state = States.B
            case States.B:
                if tape.get(cursor, 0) == 0:
                    tape[cursor] = 1
                    cursor += Dir.LEFT
                    state = States.C
                else:
                    tape[cursor] = 0
                    cursor += Dir.RIGHT
                    state = States.E
            case States.C:
                if tape.get(cursor, 0) == 0:
                    tape[cursor] = 1
                    cursor += Dir.RIGHT
                    state = States.E
                else:
                    tape[cursor] = 0
                    cursor += Dir.LEFT
                    state = States.D
            case States.D:
                if tape.get(cursor, 0) == 0:
                    tape[cursor] = 1
                    cursor += Dir.LEFT
                    state = States.A
                else:
                    tape[cursor] = 1
                    cursor += Dir.LEFT
                    state = States.A
            case States.E:
                if tape.get(cursor, 0) == 0:
                    tape[cursor] = 0
                    cursor += Dir.RIGHT
                    state = States.A
                else:
                    tape[cursor] = 0
                    cursor += Dir.RIGHT
                    state = States.F
            case States.F:
                if tape.get(cursor, 0) == 0:
                    tape[cursor] = 1
                    cursor += Dir.RIGHT
                    state = States.E
                else:
                    tape[cursor] = 1
                    cursor += Dir.RIGHT
                    state = States.A

    for _ in range(steps):
        take_step()
    return sum(tape.values())
    
print(solve())
