from queue import Queue

def read_input_file_data():
    FILE = "puzzle_input.txt"
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
                garden_map[y] = line.replace(START, PLOT)
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

import math
def solve_part_2():
    starting_pos, y_size, x_size, garden_map = parse_input()
    # To solve this question, we need the fact that the map has no rocks on the outer
    # rim and in the center axis from where the start is.
    # This way, to travel to another map, the shortest path is to travel along those
    # axes and the steps required is the same.

    # 1  2  3
    # 4  5  6
    # 7  8  9
    TOP_LEFT  = (0, 0)                      # 1
    TOP       = (0, starting_pos[1])        # 2
    TOP_RIGHT = (0, x_size-1)               # 3
    LEFT      = (starting_pos[0], 0)        # 4
    CENTER    = starting_pos                # 5
    RIGHT     = (starting_pos[0], x_size-1) # 6
    BOT_LEFT  = (y_size-1, 0)               # 7
    BOT       = (y_size-1, starting_pos[1]) # 8
    BOT_RIGHT = (y_size-1, x_size-1)        # 9

    MIN_DIST_POINTS = [
        TOP_LEFT, TOP, TOP_RIGHT,
        LEFT, CENTER, RIGHT,
        BOT_LEFT, BOT, BOT_RIGHT
    ]
    D = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Point shifting from START
    assert (y_size - 1) // 2 == starting_pos[0] and (x_size - 1) // 2 == starting_pos[1]
    HALF_SHIFT = (y_size + 1) // 2
    # Point shifting across map grid
    assert y_size == x_size
    FULL_SHIFT = y_size

    def out_of_range(pos):
        y, x = pos
        return y < 0 or y >= y_size or x < 0 or x >= x_size
    def is_plot(pos):
        y, x = pos
        return garden_map[y % y_size][x % x_size] == PLOT
    def explore(pos) -> tuple[dict[tuple[int, int], int], dict[tuple[int, int], int]]:
        frontier = {pos}
        reachable_steps = {0: 1}
        steps_count = 0
        save1, save2 = None, None # Due to odd and even
        while frontier:
            steps_count += 1
            new_frontier = set()
            for y, x in frontier:
                for dy, dx in D:
                    new_pos = (y+dy, x+dx)
                    if is_plot(new_pos) and not out_of_range(new_pos):
                        new_frontier.add(new_pos)
            frontier = new_frontier
            if frontier == save1: # Last step already fully explores the map
                return reachable_steps, steps_count-1 # max steps
            else:
                save1 = save2
                save2 = frontier
                reachable_steps[steps_count] = len(frontier)
    
    ##################
    # MAIN ALGORITHM #
    ##################
    STEPS = 26501365
    pos_count = 0

    # Initialization
    step_pos_table = {} # point: reachable_steps, max_steps
    for point in MIN_DIST_POINTS:
        step_pos_table[point] = explore(point)
    
    # Center (5)
    point = CENTER
    remaining_steps = STEPS
    reachable_steps, max_steps = step_pos_table[point]
    if remaining_steps >= max_steps:
        pos_count += reachable_steps[max_steps - ((remaining_steps % 2) ^ (max_steps % 2))]
    else:
        pos_count += reachable_steps[remaining_steps]
    
    # Straight line (2, 4, 6, 8)
    for point in [TOP, LEFT, RIGHT, BOT]:
        remaining_steps = STEPS - HALF_SHIFT
        reachable_steps, max_steps = step_pos_table[point]
        # Complete scans
        n = (remaining_steps - max_steps) // FULL_SHIFT
        if n < 0:
            continue
        if FULL_SHIFT % 2 == 0:
            pos_count += n * reachable_steps[max_steps - ((remaining_steps % 2) ^ (max_steps % 2))]
        else:
            pos_count += (
                math.ceil(n / 2) * reachable_steps[max_steps - ((remaining_steps % 2) ^ (max_steps % 2))] +
                math.floor(n / 2) * reachable_steps[max_steps - (((remaining_steps - FULL_SHIFT) % 2) ^ (max_steps % 2))]
            )
        # Remaining scans
        remaining_steps -= n * FULL_SHIFT
        while remaining_steps > 0:
            if remaining_steps >= max_steps:
                pos_count += reachable_steps[max_steps - ((remaining_steps % 2) ^ (max_steps % 2))]
            else:
                pos_count += reachable_steps[remaining_steps]
            remaining_steps -= FULL_SHIFT
    
    # Diagonals (1, 3, 7, 9)
    for point in [TOP_LEFT, TOP_RIGHT, BOT_LEFT, BOT_RIGHT]:
        remaining_steps = STEPS - HALF_SHIFT - HALF_SHIFT
        reachable_steps, max_steps = step_pos_table[point]
        # Complete scans
        n = (remaining_steps - max_steps) // FULL_SHIFT
        if n < 0:
            continue
        if FULL_SHIFT % 2 == 0:
            summation_to_n = (n + 1) * n / 2
            pos_count += summation_to_n * reachable_steps[max_steps - ((remaining_steps % 2) ^ (max_steps % 2))]
        else:
            odd_max, even_max = (n-1, n) if n % 2 == 0 else (n, n-1)
            odd_summation = int((odd_max + 1) / 2 * (((odd_max - 1) / 2) + 1))
            even_summation = int((even_max + 2) / 2 * (((even_max - 2) / 2) + 1))
            pos_count += (
                odd_summation * reachable_steps[max_steps - ((remaining_steps % 2) ^ (max_steps % 2))] +
                even_summation * reachable_steps[max_steps - (((remaining_steps - FULL_SHIFT) % 2) ^ (max_steps % 2))]
            )
        # Remaining scans
        remaining_steps -= n * FULL_SHIFT
        count = n + 1
        while remaining_steps > 0:
            if remaining_steps >= max_steps:
                pos_count += count * reachable_steps[max_steps - ((remaining_steps % 2) ^ (max_steps % 2))]
            else:
                pos_count += count * reachable_steps[remaining_steps]
            remaining_steps -= FULL_SHIFT
            count += 1
    
    return pos_count
    
print(solve_part_2())