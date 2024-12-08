def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def solve_part_1():
    file = read_input_file()

    cycle = 1
    value = 1
    strength = 0

    def clock_cycle(cycle):
        nonlocal strength
        if cycle in [20, 60, 100, 140, 180, 220]:
            strength += cycle * value
            print(f"Cycle {cycle} checked")

    for line in file.read().splitlines():
        clock_cycle(cycle)

        info = line.split()
        if info[0] == "noop":
            cycle += 1
        elif info[0] == "addx":
            cycle += 1
            clock_cycle(cycle)
            cycle += 1
            value += int(info[1])
        else:
            raise Exception(f"Unknown operation: {info[0]}")

    return strength

def solve_part_2():
    cycle = 1
    value = 1
    pos = 0
    CRT = ""
    log = ""

    def clock_cycle(cycle):
        nonlocal CRT, pos, log
        if cycle in [40, 80, 120, 160, 200, 240]:
            print(CRT)
            CRT = ""
            pos = 0
            log += f"Cycle {cycle} checked\n"
    
    def display():
        nonlocal CRT, pos
        if (abs(pos - value) <= 1):
            CRT += "#"
        else:
            CRT += "."
        pos += 1

    file = read_input_file()
    for line in file.read().splitlines():
        display()
        clock_cycle(cycle)
        info = line.split()
        if info[0] == "noop":
            cycle += 1
        elif info[0] == "addx":
            cycle += 1
            display()
            clock_cycle(cycle)
            cycle += 1
            value += int(info[1])
        else:
            raise Exception(f"Unknown operation: {info[0]}")

    return log
    
print(solve_part_2())
