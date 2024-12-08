from collections import deque

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    password = list("abcdefgh")

    instructions = read_input_file_data().splitlines()
    for line in instructions:
        ins = line.split()
        match (ins[0]):
            case "swap":
                match (ins[1]):
                    case "position": # swap position X with position Y
                        X = int(ins[2])
                        Y = int(ins[5])
                        password[X], password[Y] = password[Y], password[X]
                    case "letter": # swap letter X with letter Y
                        X = ins[2]
                        Y = ins[5]
                        xi = password.index(X)
                        yi = password.index(Y)
                        password[xi], password[yi] = password[yi], password[xi]
                    case _:
                        raise Exception(f"Unknown swap {ins}")
            case "rotate":
                match (ins[3]):
                    case "step" | "steps": # rotate left/right X step
                        dir = -1 if ins[1] == "left" else 1
                        X = int(ins[2])
                        deq = deque(password)
                        deq.rotate(X * dir)
                        password = list(deq)
                    case "position": # rotate based on position of letter X
                        X = ins[6]
                        xi = password.index(X)
                        rot = 1 + xi + (1 if xi >= 4 else 0)
                        deq = deque(password)
                        deq.rotate(rot)
                        password = list(deq)
                    case _:
                        raise Exception(f"Unknown rotate {ins}")
            case "reverse": # reverse positions X through Y
                X = int(ins[2])
                Y = int(ins[4])
                password[X:Y+1] = password[X:Y+1][::-1]
            case "move": # move position X to position Y
                X = int(ins[2])
                Y = int(ins[5])
                letter = password.pop(X)
                password.insert(Y, letter)
            case _:
                raise Exception(f"Unknown instruction {ins}")

    return ''.join(password)

def solve_part_2():
    password = list("fbgdceah")
    
    instructions = read_input_file_data().splitlines()
    instructions.reverse()
    for line in instructions:
        ins = line.split()
        match (ins[0]):
            case "swap":
                match (ins[1]):
                    case "position": # swap position X with position Y
                        X = int(ins[2])
                        Y = int(ins[5])
                        password[X], password[Y] = password[Y], password[X]
                    case "letter": # swap letter X with letter Y
                        X = ins[2]
                        Y = ins[5]
                        xi = password.index(X)
                        yi = password.index(Y)
                        password[xi], password[yi] = password[yi], password[xi]
                    case _:
                        raise Exception(f"Unknown swap {ins}")
            case "rotate":
                match (ins[3]):
                    case "step" | "steps": # rotate left/right X step
                        dir = 1 if ins[1] == "left" else -1 # rotate in different direction
                        X = int(ins[2])
                        deq = deque(password)
                        deq.rotate(X * dir)
                        password = list(deq)
                    case "position": # rotate based on position of letter X
                        X = ins[6]
                        xi = password.index(X)

                        # need to rotate X to the original position
                        '''
                        How it originally got rotated
                        0 -> 1 (+1)
                        1 -> 3 (+2)
                        2 -> 5 (+3)
                        3 -> 7 (+4)
                        4 -> 2 (+6)
                        5 -> 4 (+7)
                        6 -> 6 (+8)
                        7 -> 0 (+9)

                        Reverse
                        0 -> 7 (+7)
                        1 -> 0 (-1)
                        2 -> 4 (+2)
                        3 -> 1 (-2)
                        4 -> 5 (+1)
                        5 -> 2 (-3)
                        6 -> 6 (+0)
                        7 -> 3 (-4)
                        '''
                        reverse_index = { 0: 7, 1: -1, 2: 2, 3: -2, 4: 1, 5: -3, 6: 0, 7: -4 }
                        rot = reverse_index[xi]
                        deq = deque(password)
                        deq.rotate(rot)
                        password = list(deq)
                    case _:
                        raise Exception(f"Unknown rotate {ins}")
            case "reverse": # reverse positions X through Y
                X = int(ins[2])
                Y = int(ins[4])
                password[X:Y+1] = password[X:Y+1][::-1]
            case "move": # move position X to position Y
                X = int(ins[2])
                Y = int(ins[5])
                letter = password.pop(Y) # Move from Y to X instead
                password.insert(X, letter)
            case _:
                raise Exception(f"Unknown instruction {ins}")

    return ''.join(password)
    
print(solve_part_2())
