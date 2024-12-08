from itertools import combinations
from functools import reduce
from operator import mul

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def parse_input_list():
    return list(map(lambda x: int(x), read_input_file_data().splitlines()))

def get_quantum_entanglement(presents: tuple) -> int:
    return reduce(mul, presents)

def solve_part_1():
    presents_list = parse_input_list()
    total_weight = sum(presents_list)
    assert total_weight % 3 == 0
    target_weight = total_weight // 3

    curr_size = len(presents_list)
    min_quantum_entanglement = get_quantum_entanglement(tuple(presents_list))
    for i in range(1, len(presents_list) // 3 + 1):
        combis = combinations(presents_list, i)
        for combi in combis:
            if sum(combi) == target_weight and len(combi) <= curr_size:
                curr_size = len(combi)
                min_quantum_entanglement = min(min_quantum_entanglement, get_quantum_entanglement(combi))
    return min_quantum_entanglement

def solve_part_2():
    presents_list = parse_input_list()
    total_weight = sum(presents_list)
    assert total_weight % 4 == 0
    target_weight = total_weight // 4

    curr_size = len(presents_list)
    min_quantum_entanglement = get_quantum_entanglement(tuple(presents_list))
    for i in range(1, len(presents_list) // 4 + 1):
        combis = combinations(presents_list, i)
        for combi in combis:
            if sum(combi) == target_weight and len(combi) <= curr_size:
                curr_size = len(combi)
                min_quantum_entanglement = min(min_quantum_entanglement, get_quantum_entanglement(combi))
    return min_quantum_entanglement

    
print(solve_part_2())
