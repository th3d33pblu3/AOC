def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    connections = {}
    for line in read_input_file_data().splitlines():
        l, r = line.split('-')
        if l not in connections:
            connections[l] = set()
        if r not in connections:
            connections[r] = set()
        connections[l].add(r)
        connections[r].add(l)
    
    small_caves = list(filter(lambda cave: cave.islower() and cave != 'start' and cave != 'end', connections.keys()))
    frontier = [(loc, [False] * len(small_caves)) for loc in connections['start']]
    paths = 0
    while frontier:
        new_frontier = []
        for curr_loc, caves_visited in frontier:
            if curr_loc == 'start':
                continue
            elif curr_loc == 'end':
                paths += 1
                continue
            if curr_loc.islower(): # Small cave
                index = small_caves.index(curr_loc)
                if caves_visited[index]: # Already visited small cave before
                    continue
                else: # First time visiting small cave
                    caves_visited[index] = True
                    # Visit next caves
                    for new_loc in connections[curr_loc]:
                        new_frontier.append((new_loc, caves_visited.copy()))
            else: # Big cave
                # Visit next caves
                for new_loc in connections[curr_loc]:
                    new_frontier.append((new_loc, caves_visited.copy()))
        frontier = new_frontier
    return paths

def solve_part_2():
    connections = {}
    for line in read_input_file_data().splitlines():
        l, r = line.split('-')
        if l not in connections:
            connections[l] = set()
        if r not in connections:
            connections[r] = set()
        connections[l].add(r)
        connections[r].add(l)
    
    small_caves = list(filter(lambda cave: cave.islower() and cave != 'start' and cave != 'end', connections.keys()))
    frontier = [(loc, [False] * len(small_caves), False) for loc in connections['start']]
    paths = 0
    while frontier:
        new_frontier = []
        for curr_loc, caves_visited, double_visited in frontier:
            if curr_loc == 'start':
                continue
            elif curr_loc == 'end':
                paths += 1
                continue
            if curr_loc.islower(): # Small cave
                index = small_caves.index(curr_loc)
                if caves_visited[index]: # Already visited small cave before
                    if double_visited: # Already used up chance to double visit
                        continue
                    else: # Visit small cave again
                        double_visited = True
                        # Visit next caves
                        for new_loc in connections[curr_loc]:
                            new_frontier.append((new_loc, caves_visited.copy(), double_visited))
                else: # First time visiting small cave
                    caves_visited[index] = True
                    # Visit next caves
                    for new_loc in connections[curr_loc]:
                        new_frontier.append((new_loc, caves_visited.copy(), double_visited))
            else: # Big cave
                # Visit next caves
                for new_loc in connections[curr_loc]:
                    new_frontier.append((new_loc, caves_visited.copy(), double_visited))
        frontier = new_frontier
    return paths
    
print(solve_part_2())
