import re
import math
import numpy as np

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    data = read_input_file_data()
    def parse_machine(desc: str):
        lines = desc.splitlines()
        A = (int(re.search(r"X\+([0-9]*)", lines[0]).group(1)), int(re.search(r"Y\+([0-9]*)", lines[0]).group(1)))
        B = (int(re.search(r"X\+([0-9]*)", lines[1]).group(1)), int(re.search(r"Y\+([0-9]*)", lines[1]).group(1)))
        target = (int(re.search(r"X=([0-9]*)", lines[2]).group(1)), int(re.search(r"Y=([0-9]*)", lines[2]).group(1)))
        return (A, B, target)
    
    machines = list(map(parse_machine, data.split("\n\n")))
    tokens = 0
    for machine in machines:
        A, B, target = machine
        Ax, Ay = A
        Bx, By = B
        X, Y = target
        # Brute force solution
        for a in range(100):
            if X - (Ax * a) > 0 and (X - (Ax * a)) % Bx == 0:
                b = (X - (Ax * a)) // Bx
                if (Ay * a) + (By * b) == Y:
                    tokens += 3 * a + b
                    break
    return tokens

def solve_part_2():
    data = read_input_file_data()
    def parse_machine(desc: str):
        lines = desc.splitlines()
        A = (int(re.search(r"X\+([0-9]*)", lines[0]).group(1)), int(re.search(r"Y\+([0-9]*)", lines[0]).group(1)))
        B = (int(re.search(r"X\+([0-9]*)", lines[1]).group(1)), int(re.search(r"Y\+([0-9]*)", lines[1]).group(1)))
        target = (int(re.search(r"X=([0-9]*)", lines[2]).group(1)) + 10000000000000, int(re.search(r"Y=([0-9]*)", lines[2]).group(1)) + 10000000000000)
        return (A, B, target)

    machines = list(map(parse_machine, data.split("\n\n")))
    tokens = 0
    for machine in machines:
        A, B, target = machine
        Ax, Ay = A
        Bx, By = B
        X, Y = target
        # Solve Ma * x = Mb
        Ma = np.array([[Ax, Bx], [Ay, By]])
        Mb = np.array([X, Y])
        a, b = tuple(map(round, np.linalg.solve(Ma, Mb)))
        if a >= 0 and b >= 0 and Ax * a + Bx * b == X and Ay * a + By * b == Y:
            tokens += 3 * int(a) + int(b)
    return tokens
    
print(solve_part_2())
