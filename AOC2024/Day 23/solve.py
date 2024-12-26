from itertools import combinations

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    connections = {}
    for line in read_input_file_data().splitlines():
        a, b = line.split("-")
        if a in connections:
            connections[a].add(b)
        else:
            connections[a] = set()
            connections[a].add(b)
        if b in connections:
            connections[b].add(a)
        else:
            connections[b] = set()
            connections[b].add(a)
    
    triplets = set()
    for comp, others in connections.items():
        L = len(others)
        others = list(others)
        for i in range(L-1):
            c1 = others[i]
            for j in range(i+1, L):
                c2 = others[j]
                if c1 in connections[c2]:
                    l = [comp, c1, c2]
                    l.sort()
                    triplets.add(tuple(l))

    count = 0
    for t1, t2, t3 in triplets:
        if t1[0] == 't' or t2[0] == 't' or t3[0] == 't':
            count += 1
    return count

def solve_part_2():
    connections = {}
    for line in read_input_file_data().splitlines():
        a, b = line.split("-")
        if a in connections:
            connections[a].add(b)
        else:
            connections[a] = set()
            connections[a].add(b)
        if b in connections:
            connections[b].add(a)
        else:
            connections[b] = set()
            connections[b].add(a)
    
    # Every computer is connected to 13 other computers
    # Previous attemps found sets of size 12. Try to look for sets of size 13/14
    largest_set = set()
    for comp, others in connections.items():
        for i in range(len(others), len(largest_set) - 1, -1):
            combis = combinations(others, i)
            for combi in combis:
                # check if combi is valid
                choose2 = combinations(combi, 2)
                for a, b in choose2:
                    if a not in connections[b]:
                        break
                else:
                    # Valid combi
                    cs = set(combi)
                    cs.add(comp)
                    largest_set = cs
                    break # All other combis are of only the same size
    largest_set = list(largest_set)
    largest_set.sort()
    return ','.join(largest_set)
    
print(solve_part_2())
