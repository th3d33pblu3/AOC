def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    components = [tuple(map(int, line.split('/'))) for line in read_input_file_data().splitlines()]
    max_length = 0
    curr_bridges = {(0, frozenset(), 0)}
    while curr_bridges != set():
        max_length = max(max_length, max([item[2] for item in curr_bridges]))
        new_bridges = set()
        for port, bridge, strength in curr_bridges:
            for i, comp in enumerate(components):
                if i in bridge:
                    continue
                l, r = comp
                if l == port:
                    new_bridges.add((r, bridge.union({i}), strength + l + r))
                elif r == port:
                    new_bridges.add((l, bridge.union({i}), strength + l + r))
        curr_bridges = new_bridges
    return max_length

def solve_part_2():
    components = [tuple(map(int, line.split('/'))) for line in read_input_file_data().splitlines()]
    curr_bridges = {(0, frozenset(), 0)}
    while curr_bridges != set():
        new_bridges = set()
        for port, bridge, strength in curr_bridges:
            for i, comp in enumerate(components):
                if i in bridge:
                    continue
                l, r = comp
                if l == port:
                    new_bridges.add((r, bridge.union({i}), strength + l + r))
                elif r == port:
                    new_bridges.add((l, bridge.union({i}), strength + l + r))
        if new_bridges == set():
            return max([item[2] for item in curr_bridges])
        curr_bridges = new_bridges
    
print(solve_part_2())
