from queue import Queue

def read_input_file_data():
    FILE = "puzzle_input.txt"
    FILE = "sample.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

PLOT = '.'
ROCK = '#'
START = 'S'

def parse_input():
    garden_map = read_input_file_data().splitlines()
    for y, line in enumerate(garden_map):
        for x, c in enumerate(line):
            if c == START:
                line.replace(START, PLOT)
                return (y, x), len(garden_map), len(garden_map[0]), garden_map
    raise Exception("No starting position found.")

def solve_part_1():
    starting_pos, y_size, x_size, garden_map = parse_input()

    D = [(0, 1),
         (1, 0),
         (0, -1),
         (-1, 0)]
    def can_move(y, x):
        if y<0 or y>=y_size or x<0 or x>=x_size:
            return False
        return garden_map[y][x] == PLOT
        # return garden_map[y%y_size][x%x_size] == PLOT

    STEPS = 64
    # STEPS = 10
    visited_pos0 = {starting_pos}
    visited_pos1 = set()
    frontier = {starting_pos}
    for _ in range(STEPS):
        new_frontier = set()
        for y, x in frontier:
            for dy, dx in D:
                if can_move(y+dy, x+dx):
                    new_frontier.add((y+dy, x+dx))
        frontier = new_frontier.difference(visited_pos1)
        new_frontier.update(visited_pos1)
        visited_pos1 = visited_pos0
        visited_pos0 = new_frontier
    return len(visited_pos0)

def solve_part_2():
    starting_pos, y_size, x_size, garden_map = parse_input()
    D = [(1, 0),
         (-1, 0),
         (0, 1),
         (0, -1)]
    def out_of_range(pos):
        y, x = pos
        return y < 0 or y >= y_size or x < 0 or x >= x_size
    def is_plot(pos):
        y, x = pos
        return garden_map[y % y_size][x % x_size] == PLOT
    def explore(pos) -> tuple[dict[tuple[int, int], int], dict[tuple[int, int], int]]:
        frontier = {pos}
        pos_steps = {pos: 0}
        exit_steps = {}
        steps_count = 0
        while len(frontier) != 0:
            steps_count += 1
            new_frontier = set()
            for y, x in frontier:
                for dy, dx in D:
                    new_pos = (y+dy, x+dx)
                    if is_plot(new_pos):
                        if out_of_range(new_pos): # New position is a valid exit
                            # assert new_pos not in exit_steps # DEBUG
                            exit_steps[new_pos] = steps_count
                        elif new_pos not in pos_steps: # Unexplored step
                            pos_steps[new_pos] = steps_count
                            new_frontier.add(new_pos)
            frontier = new_frontier
        return pos_steps, exit_steps
    def correct_exit_pos(exit_pos):
        y, x = exit_pos
        return y % y_size, x % x_size
    def get_new_map_pos(map_pos, exit_pos):
        y, x = exit_pos
        if y < 0:
            return map_pos[0] - 1, map_pos[1]
        elif y >= y_size:
            return map_pos[0] + 1, map_pos[1]
        elif x < 0:
            return map_pos[0], map_pos[1] - 1
        elif x >= x_size:
            return map_pos[0], map_pos[1] + 1
        else:
            raise Exception(f"Unrecognized exit {exit_pos}")
    
    # Primary initialization
    STEPS = 26501365
    STEPS = 50
    explored_pos_steps = {} # pos: pos_steps, exit_steps
    pos_largest_steps = {}  # pos: largest_step_count (int)

    pos_steps, exit_steps = explore(starting_pos)
    explored_pos_steps[starting_pos] = (pos_steps, exit_steps)
    pos_largest_steps[starting_pos] = max(pos_steps.values())
    exits = exit_steps.keys()
    for exit in exits:
        exit_pos = (exit[0] % y_size, exit[1] % x_size)
        explored_pos_steps[exit_pos] = explore(exit_pos)
        pos_largest_steps[exit_pos] = max(explored_pos_steps[exit_pos][0].values())
    
    even_count, odd_count = 0, 0
    for pos in pos_steps:
        if (pos[0] + pos[1]) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    # Secondary initialization
    even_odd_pos_count = even_count, odd_count

    # Algorithm
    map_even_odd = {} # map_pos: (0: even, 1: odd)
    explored_map = {} # (map_pos, pos): steps

    pos_frontier = Queue()
    pos_frontier.put(((0, 0), starting_pos, STEPS)) # map_pos, pos, steps
    unfinished_frontier = Queue()
    while not pos_frontier.empty():
        map_pos, pos, steps = pos_frontier.get()

        # Search trimming
        if (map_pos, pos) in explored_map:
            if explored_map[(map_pos, pos)] >= steps:
                continue
        explored_map[(map_pos, pos)] = steps

        # Walk in map
        if steps >= pos_largest_steps[pos]: # Can walk finish
            map_even_odd[map_pos] = (pos[0] + pos[1] + steps) % 2
        else: # Cannot walk finish
            unfinished_frontier.put((map_pos, pos, steps))
        
        # Find exits and new positions
        exit_steps = explored_pos_steps[pos][1]
        for exit in exit_steps:
            required_steps = exit_steps[exit]
            if required_steps > steps:
                continue
            new_map_pos = get_new_map_pos(map_pos, exit)
            pos_frontier.put((new_map_pos, correct_exit_pos(exit), steps - required_steps))

    map_positions: dict[tuple[int, int], set] = {}
    while not unfinished_frontier.empty():
        map_pos, pos, steps = unfinished_frontier.get()
        if map_pos in map_even_odd: # If already walked finish by some exploration
            continue
        if map_pos not in map_positions:
            map_positions[map_pos] = set()
        pos_steps = explored_pos_steps[pos][0]

        to_update = set(filter(lambda p: pos_steps[p] <= steps and (pos_steps[p] % 2) == (steps % 2), pos_steps))
        map_positions[map_pos].update(to_update)

    sum_pos = 0
    for map_pos in map_even_odd:
        sum_pos += even_odd_pos_count[map_even_odd[map_pos]]
    for map_pos in map_positions:
        map_type = (map_pos[0] + map_pos[1]) % 2
        for pos in map_positions[map_pos]:
            assert (pos[0] + pos[1]) % 2 == map_type
        sum_pos += len(map_positions[map_pos])
    return sum_pos
    
print(solve_part_1())
