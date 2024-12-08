from queue import Queue

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def read_test_file_data():
    FILE = "test_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def get_connections():
    connections = {}
    for line in read_input_file_data().splitlines():
        left, right = line.split(" <-> ")
        start_id = int(left)
        end_ids = tuple(map(int, right.split(", ")))
        connections[start_id] = end_ids
    return connections

def solve_part_1():
    connections = get_connections()
    STARTING_ID = 0
    count = 0
    frontier = Queue()
    visited = set()
    frontier.put(STARTING_ID)
    while frontier.qsize() != 0:
        curr_id = frontier.get()
        if curr_id in visited:
            continue
        count += 1
        visited.add(curr_id)
        for id in connections[curr_id]:
            if id not in visited:
                frontier.put(id)
    return count


def solve_part_2():
    connections = get_connections()
    all_ids = set(connections.keys())
    count = 0
    frontier = Queue()
    while len(all_ids) != 0:
        if frontier.qsize() == 0:
            curr_id = next(iter(all_ids))
            count += 1
        else:
            curr_id = frontier.get()
        if curr_id not in all_ids:
            continue
        else:
            all_ids.remove(curr_id)
        for id in connections[curr_id]:
            if id in all_ids:
                frontier.put(id)
    return count
    
print(solve_part_2())
