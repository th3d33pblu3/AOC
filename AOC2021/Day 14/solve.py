from collections import defaultdict

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    polymer, reactions = read_input_file_data().split('\n\n')
    reactions = [line.split(' -> ') for line in reactions.splitlines()]
    
    # Product dictionary
    products = defaultdict(int)
    for key, val in reactions:
        e1, e2 = key[0], key[1]
        products[key] = (e1+val, val+e2)
    
    # Processing reactants
    reactants = defaultdict(int)
    for i in range(len(polymer)-1):
        pair = polymer[i:i+2]
        reactants[pair] += 1
    
    # Computation using reactant count directly
    for _ in range(10):
        new_reactants = defaultdict(int)
        for reactant in reactants:
            count = reactants[reactant]
            p1, p2 = products[reactant]
            new_reactants[p1] += count
            new_reactants[p2] += count
        reactants = new_reactants
    
    # Element counting
    elements = defaultdict(int)
    for key, val in reactants.items():
        e1, e2 = key[0], key[1]
        elements[e1] += val
        elements[e2] += val
    elements[polymer[0]] += 1 # Make first element double counted
    elements[polymer[-1]] += 1 # Make last element double counted
    for element in elements: # All elements are double counted
        elements[element] //= 2
    
    return max(elements.values()) - min(elements.values())

def solve_part_2():
    polymer, reactions = read_input_file_data().split('\n\n')
    reactions = [line.split(' -> ') for line in reactions.splitlines()]
    
    # Product dictionary
    products = defaultdict(int)
    for key, val in reactions:
        e1, e2 = key[0], key[1]
        products[key] = (e1+val, val+e2)
    
    # Processing reactants
    reactants = defaultdict(int)
    for i in range(len(polymer)-1):
        pair = polymer[i:i+2]
        reactants[pair] += 1
    
    # Computation using reactant count directly
    for _ in range(40):
        new_reactants = defaultdict(int)
        for reactant in reactants:
            count = reactants[reactant]
            p1, p2 = products[reactant]
            new_reactants[p1] += count
            new_reactants[p2] += count
        reactants = new_reactants
    
    # Element counting
    elements = defaultdict(int)
    for key, val in reactants.items():
        e1, e2 = key[0], key[1]
        elements[e1] += val
        elements[e2] += val
    elements[polymer[0]] += 1 # Make first element double counted
    elements[polymer[-1]] += 1 # Make last element double counted
    for element in elements: # All elements are double counted
        elements[element] //= 2
    
    return max(elements.values()) - min(elements.values())
    
print(solve_part_2())
