def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def process_data():
    area_map = read_input_file_data().splitlines()
    starting_location = None
    num_keys = 0
    for y, line in enumerate(area_map):
        for x, char in enumerate(line):
            if char == '@':
                starting_location = (x, y)
                line.replace('@', '.')
            elif 'a' <= char <= 'z':
                num_keys += 1
    return area_map, starting_location, num_keys

def solve_part_1():
    area_map, starting_location, num_keys = process_data()
    DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    start_state = (starting_location, (False,) * num_keys)
    states = { start_state: 0 }
    frontier = set()
    frontier.add(start_state)

    while frontier:
        new_frontier = set()
        for state in frontier:
            loc, keys = state
            steps = states[state]
            for i in range(4):
                dx, dy = loc[0] + DELTAS[i][0], loc[1] + DELTAS[i][1]
                char = area_map[dy][dx]
                if char == '#':
                    continue
                elif char == '.':
                    new_state = ((dx, dy), keys)
                    if new_state not in states:
                        states[new_state] = steps + 1
                        new_frontier.add(new_state)
                elif 'a' <= char and char <= 'z':
                    new_keys = list(keys)
                    new_keys[ord(char) - ord('a')] = True
                    new_keys = tuple(new_keys)
                    new_state = ((dx, dy), new_keys)
                    if new_state not in states:
                        states[new_state] = steps + 1
                        new_frontier.add(new_state)
                    if all(new_keys):
                        return states[new_state]
                elif 'A' <= char and char <= 'Z':
                    if not keys[ord(char) - ord('A')]:
                        continue
                    new_state = ((dx, dy), keys)
                    if new_state not in states:
                        states[new_state] = steps + 1
                        new_frontier.add(new_state)
        frontier = new_frontier
    return None

def solve_part_2():
    area_map, starting_location, num_keys = process_data()
    DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Re-process map center
    x, y = starting_location
    area_map[y-1] = area_map[y-1][:x-1] + '.#.' + area_map[y-1][x+2:]
    area_map[y]   = area_map[y  ][:x-1] + '###' + area_map[y  ][x+2:]
    area_map[y+1] = area_map[y+1][:x-1] + '.#.' + area_map[y+1][x+2:]
    starting_locations = ((x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1))
    map_limits = ((0, 0, x, y), (x+1, 0, len(area_map[0]), y), (0, y+1, x, len(area_map)), (x+1, y+1, len(area_map[0]), len(area_map)))

    # Split map into 4 quadrants
    quadrants = []
    for starting_location, (minx, miny, maxx, maxy) in zip(starting_locations, map_limits):
        keys = set()
        doors = set()
        for x in range(minx, maxx):
            for y in range(miny, maxy):
                char = area_map[y][x]
                if 'a' <= char and char <= 'z':
                    keys.add((char, (x, y)))
                elif 'A' <= char and char <= 'Z':
                    doors.add((char, (x, y)))
        keys = list(keys)
        keys.sort()
        doors = list(doors)
        doors.sort()
        quadrants.append((starting_location, (minx, miny, maxx, maxy), keys, doors))

    # Process quadrants
    locations = {}
    node_steps = {}
    for i, (starting_location, _, keys, doors) in enumerate(quadrants):
        # Record nodes
        quadrant_nodes = {}
        quadrant_nodes[str(i)] = starting_location
        for key, (x, y) in keys:
            quadrant_nodes[key] = (x, y)
        for door, (x, y) in doors:
            quadrant_nodes[door] = (x, y)
        # Combine to main nodes list
        locations.update(quadrant_nodes)
        
        # Find steps between nodes
        for node, (x, y) in quadrant_nodes.items():
            curr_node_steps = {}
            visited = set()
            frontier = set()
            frontier.add((x, y))
            steps = 0
            while frontier:
                steps += 1
                new_frontier = set()
                for (x, y) in frontier:
                    for (dx, dy) in DELTAS:
                        new_loc = (x + dx, y + dy)
                        if new_loc in visited:
                            continue
                        char = area_map[new_loc[1]][new_loc[0]]
                        if char == '#':
                            continue
                        elif char == '.':
                            new_frontier.add(new_loc)
                        else:
                            curr_node_steps[char] = min(curr_node_steps.get(char, float('inf')), steps)
                visited.update(frontier)
                frontier = new_frontier
            node_steps[node] = curr_node_steps

    # Actual computation
    min_steps = float('inf')
    start_state = (tuple(map(str, range(4))), (False,) * num_keys)
    states = { start_state: 0 }
    frontier = set()
    frontier.add(start_state)
    while frontier:
        new_frontier = set()
        for state in frontier:
            nodes, keys = state
            curr_steps = states[state]
            for dn in range(4):
                node = nodes[dn]
                for char, steps in node_steps[node].items():
                    if 'a' <= char and char <= 'z':
                        new_nodes = tuple(n if n != node else char for n in nodes)
                        new_keys = list(keys)
                        new_keys[ord(char) - ord('a')] = True
                        new_keys = tuple(new_keys)
                        new_state = (new_nodes, new_keys)
                        if new_state not in states:
                            states[new_state] = curr_steps + steps
                            new_frontier.add(new_state)
                        else:
                            old_steps = states[new_state]
                            new_steps = curr_steps + steps
                            if old_steps > new_steps:
                                states[new_state] = new_steps
                                new_frontier.add(new_state)
                        if all(new_keys):
                            min_steps = min(min_steps, states[new_state])
                    elif 'A' <= char and char <= 'Z':
                        if not keys[ord(char) - ord('A')]:
                            continue
                        new_nodes = tuple(n if n != node else char for n in nodes)
                        new_state = (new_nodes, keys)
                        if new_state not in states:
                            states[new_state] = curr_steps + steps
                            new_frontier.add(new_state)
                        else:
                            old_steps = states[new_state]
                            new_steps = curr_steps + steps
                            if old_steps > new_steps:
                                states[new_state] = new_steps
                                new_frontier.add(new_state)
        frontier = new_frontier
    return min_steps
    
print(solve_part_2())
