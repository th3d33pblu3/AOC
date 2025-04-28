DEPTH = 3198
TARGET_COORDINATE = (757, 12)
ROCKY = 0
WET = 1
NARROW = 2

geologic_indices = {}
def get_geologic_index(y, x):
    if (y, x) in geologic_indices:
        return geologic_indices[(y, x)]
    
    if (y, x) == (0, 0):
        geologic_indices[(y, x)] = 0
    elif (y, x) == TARGET_COORDINATE:
        geologic_indices[(y, x)] = 0
    elif y == 0:
        geologic_indices[(y, x)] = x * 16807
    elif x == 0:
        geologic_indices[(y, x)] = y * 48271
    else:
        geologic_indices[(y, x)] = get_erosion_level(y, x-1) * get_erosion_level(y-1, x)
    return geologic_indices[(y, x)]

erosion_levels = {}
def get_erosion_level(y, x):
    if (y, x) in erosion_levels:
        return erosion_levels[(y, x)]
    
    erosion_levels[(y, x)] = (get_geologic_index(y, x) + DEPTH) % 20183
    return erosion_levels[(y, x)]

types = {}
def get_type(y, x):
    if (y, x) in types:
        return types[(y, x)]
    
    types[(y, x)] = get_erosion_level(y, x) % 3
    return types[(y, x)]

def solve_part_1():
    ty, tx = TARGET_COORDINATE
    risk_level = 0
    for x in range(tx+1):
        for y in range(ty+1):
            risk_level += get_type(y, x)
    return risk_level

def solve_part_2():
    DELTA = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    TY, TX = TARGET_COORDINATE
    states = {} # Y, X, EQ(0: neither, 1: torch, 2: climbing gear): MIN_TIME
    min_time = float('inf')
    frontier = {(0, 0, 1): 0}
    while frontier:
        new_frontier = {}
        for state, time in frontier.items():
            y, x, eq = state
            if (time >= min_time or # slower path
                time >= min_time + TY - y + TX - x or # cannot reach in time
                y > 7 * TY or x > 7 * TX): # stray too far off
                continue
            if (y, x) == TARGET_COORDINATE:
                if eq == 1: # torch
                    min_time = min(min_time, time)
                    continue
                else:
                    min_time = min(min_time, time + 7)
                    continue
            for i in range(4):
                ny, nx = y + DELTA[i][0], x + DELTA[i][1]
                if ny < 0 or nx < 0:
                    continue
                region = get_type(ny, nx)
                if region == eq: # current eq cannot go
                    neq = 3 - eq - get_type(y, x) # change to equipment for here and there
                    if (y, x, neq) in states and time + 7 >= states[(y, x, neq)]:
                        continue
                    states[(y, x, neq)] = time + 7
                    new_frontier[(y, x, neq)] = time + 7
                else:
                    if (ny, nx, eq) in states and time + 1 >= states[(ny, nx, eq)]:
                        continue
                    states[(ny, nx, eq)] = time + 1
                    new_frontier[(ny, nx, eq)] = time + 1
        frontier = new_frontier
    return min_time

print(solve_part_2())
