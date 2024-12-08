def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    codes = list(map(int, read_input_file_data().split(",")))
    codes[1] = 12
    codes[2] = 2
    index = 0

    def read_next():
        nonlocal index
        num = codes[index]
        index += 1
        return num

    while index < len(codes):
        opcode = read_next()
        if opcode == 1:
            num1 = read_next()
            num2 = read_next()
            pos = read_next()
            codes[pos] = codes[num1] + codes[num2]
        elif opcode == 2:
            num1 = read_next()
            num2 = read_next()
            pos = read_next()
            codes[pos] = codes[num1] * codes[num2]
        elif opcode == 99:
            break
        else:
            raise Exception(f"Unexpected opcode: {opcode}")
    return codes[0]

def solve_part_2():
    TARGET = 19690720
    for noun in range(100):
        for verb in range(100):
            codes = list(map(int, read_input_file_data().split(",")))
            codes[1] = noun
            codes[2] = verb
            index = 0

            def read_next():
                nonlocal index
                num = codes[index]
                index += 1
                return num

            while index < len(codes):
                opcode = read_next()
                if opcode == 1:
                    num1 = read_next()
                    num2 = read_next()
                    pos = read_next()
                    codes[pos] = codes[num1] + codes[num2]
                elif opcode == 2:
                    num1 = read_next()
                    num2 = read_next()
                    pos = read_next()
                    codes[pos] = codes[num1] * codes[num2]
                elif opcode == 99:
                    break
                else:
                    raise Exception(f"Unexpected opcode: {opcode}")
            if codes[0] == TARGET:
                return 100 * noun + verb
    
print(solve_part_2())
