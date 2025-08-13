def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def parse_data():
    lines = read_input_file_data().splitlines()
    graph = {}
    for line in lines:
        src, data = line.split(': ')
        if src not in graph:
            graph[src] = set()
        for item in data.split():
            if item not in graph:
                graph[item] = set()
            graph[src].add(item)
            graph[item].add(src)
    return graph

def solve_part_1():
    graph = parse_data()
    nodes = list(graph.keys())
    paths = set()
    for a in nodes:
        for b in graph[a]:
            if a < b:
                paths.add((a, b))
            else:
                paths.add((b, a))
    
    frontier = {nodes[0]}
    visited = set()
    n = 0 # Roughly how many branches it takes to cover whole graph
    while frontier:
        n += 1
        new_frontier = set()
        for node in frontier:
            new_frontier.update(graph[node])
        new_frontier.difference_update(visited)
        visited.update(frontier)
        frontier = new_frontier

    def branch(steps):
        nonlocal graph, nodes, paths
        path_counter = {}
        for start_node in nodes:
            frontier = {start_node}
            visited = set()
            curr_steps = steps
            while frontier and curr_steps > 0:
                new_frontier = set()
                for node in frontier:
                    for neighbour in graph[node]:
                        if neighbour not in visited:
                            path = (node, neighbour) if node < neighbour else (neighbour, node)
                            path_counter[path] = path_counter.get(path, 0) + 1
                            new_frontier.add(neighbour)
                visited.update(frontier)
                frontier = new_frontier
                curr_steps -= 1
        path_count = list(map(lambda i: (i[1], i[0]), list(path_counter.items())))
        path_count.sort(reverse=True)
        return path_count
    
    def remove_connection(a, b):
        nonlocal graph, paths
        graph[a].remove(b)
        graph[b].remove(a)
        paths.remove((a, b) if a < b else (b, a))
    
    def add_connection(a, b):
        nonlocal graph, paths
        graph[a].add(b)
        graph[b].add(a)
        paths.add((a, b) if a < b else (b, a))

    def check_connectivity(a, b):
        nonlocal graph
        frontier = {a}
        visited = set()
        while frontier:
            new_frontier = set()
            for n in frontier:
                new_frontier.update(graph[n])
            new_frontier.difference_update(visited)
            visited.update(frontier)
            frontier = new_frontier
        return b in visited
    
    def get_connected_size(start_node):
        nonlocal graph
        frontier = {start_node}
        visited = {start_node}
        while frontier:
            new_frontier = set()
            for node in frontier:
                new_frontier.update(graph[node])
            new_frontier.difference_update(visited)
            visited.update(frontier)
            frontier = new_frontier
        return len(visited)

    SAMPLE_SIZE = 10
    possible_wires = list(map(lambda item: item[1], branch(n*2//3)[:SAMPLE_SIZE]))
    print(possible_wires)
    for i in range(SAMPLE_SIZE):
        for j in range(SAMPLE_SIZE):
            for k in range(SAMPLE_SIZE):
                if i == j or j == k or i == k:
                    continue
                a1, b1 = possible_wires[i]
                a2, b2 = possible_wires[j]
                a3, b3 = possible_wires[k]
                remove_connection(a1, b1)
                remove_connection(a2, b2)
                remove_connection(a3, b3)
                if not check_connectivity(a1, b1):
                    print(f"Disconnected wires: {a1}/{b1}, {a2}/{b2}, {a3}/{b3}")
                    x = get_connected_size(a1)
                    y = get_connected_size(b1)
                    return x * y
                else:
                    add_connection(a1, b1)
                    add_connection(a2, b2)
                    add_connection(a3, b3)
    return None

print(solve_part_1())
