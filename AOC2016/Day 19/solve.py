from math import log2, floor

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    # Referenced from https://en.wikipedia.org/wiki/Josephus_problem
    # f(n)=2(n-2^{{\lfloor \log _{2}(n)\rfloor }})+1
    n = int(read_input_file_data())
    return 2 * (n - pow(2, floor(log2(n)))) + 1


def solve_part_2():
    '''
    Solve by pattern finding.
    Starting from 3, let current value be a marker.
    From current marker to next marker (3 * current marker), +1 until winner is current marker, then +2 until winner is next marker
    '''
    n = int(read_input_file_data())
    if n == 1 or n == 2:
        return 1
    if n == 3:
        return 3
    
    smaller_marker = 3
    bigger_marker = 3 * smaller_marker
    while bigger_marker < n:
        smaller_marker = bigger_marker
        bigger_marker = 3 * smaller_marker

    increment = n - smaller_marker
    if increment <= smaller_marker:
        return increment
    else:
        return smaller_marker + (increment - smaller_marker) * 2

print(solve_part_2())
