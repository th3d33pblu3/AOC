import math

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    data = read_input_file_data().splitlines()
    time = int(data[0])
    buses = list(map(lambda n: -1 if n == 'x' else int(n), data[1].split(',')))
    
    id = None
    earliest = float('inf')
    for bus in buses:
        if bus == -1:
            continue
        arrival_time = math.ceil(time / bus) * bus
        if arrival_time < earliest:
            earliest = arrival_time
            id = bus
    return id * (earliest - time)


def solve_part_2():
    data = read_input_file_data().splitlines()
    buses = [] # bus, offset
    for offset, bus in enumerate(data[1].split(',')):
        if bus == 'x':
            continue
        id = int(bus)
        buses.append((id, (id - offset) % id))

    # Chinese Remainder Theorem (works because buses are prime)
    mi, ri = list(zip(*buses))
    common_modulo_M = math.prod(mi)
    Mi = [common_modulo_M // m for m in mi]
    xi = [pow(M, -1, m) for M, m in zip(Mi, mi)]
    x = sum([math.prod(rMx) for rMx in zip(ri, Mi, xi)]) % common_modulo_M
    return x
    
print(solve_part_2())
