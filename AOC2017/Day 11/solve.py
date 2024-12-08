from collections import Counter

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    data = read_input_file_data()
    counts = Counter(data.split(","))
    north_count = counts.get('n')
    south_count = counts.get('s')
    ne_count    = counts.get('ne')
    nw_count    = counts.get('nw')
    se_count    = counts.get('se')
    sw_count    = counts.get('sw')

    ne_diff    = ne_count- sw_count
    nw_diff    = nw_count - se_count
    south_diff = south_count - north_count

    if (ne_diff < 0 or nw_diff < 0 or south_diff < 0):
        loops = abs(min(ne_diff, nw_diff, south_diff))
        ne_diff    += loops
        nw_diff    += loops
        south_diff += loops

    if (ne_diff > 0 and nw_diff > 0):
        north_steps = min(ne_diff, nw_diff)
        ne_diff    -= north_steps
        nw_diff    -= north_steps
        south_diff -= north_steps

    return abs(ne_diff) + abs(nw_diff) + abs(south_diff)

def solve_part_2():
    """
    Relations:
    N + SE + SW = 0
    S + NE + NW = 0

    N + SE = NE
    N + SW = NW
    S + NE = SE
    S + NW = SW

    NE + NW = N
    SE + SW = S

    """
    counter = {'n': 0, 's': 0, 'ne': 0, 'nw': 0, 'se': 0, 'sw': 0}
    opp_dirs = {'n': 's', 's': 'n', 'ne': 'sw', 'nw': 'se', 'se': 'nw', 'sw': 'ne'}

    max_dist = 0

    for dir in read_input_file_data().split(","):
        opp_dir = opp_dirs[dir]
        if counter[opp_dir] > 0:
            counter[opp_dir] -= 1
        else:
            counter[dir] += 1
        if counter['ne'] > 0 and counter['nw'] > 0: # NE + NW = N
            counter['ne'] -= 1
            counter['nw'] -= 1
            if counter['s'] > 0:
                counter['s'] -= 1
            else:
                counter['n'] += 1
        elif counter['se'] > 0 and counter['sw'] > 0: # SE + SW = S
            counter['se'] -= 1
            counter['sw'] -= 1
            if counter['n'] > 0:
                counter['n'] -= 1
            else:
                counter['s'] += 1
        elif counter['n'] > 0 and counter['se'] > 0 and counter['sw'] > 0: # N + SE + SW = 0
            counter['n']  -= 1
            counter['se'] -= 1
            counter['sw'] -= 1
        elif counter['s'] > 0 and counter['ne'] > 0 and counter['nw'] > 0: # S + NE + NW = 0
            counter['s']  -= 1
            counter['ne'] -= 1
            counter['nw'] -= 1
        elif counter['n'] > 0 and counter['se'] > 0: # N + SE = NE
            counter['n']  -= 1
            counter['se'] -= 1
            if counter['sw'] > 0:
                counter['sw'] -= 1
            else:
                counter['ne'] += 1
        elif counter['n'] > 0 and counter['sw'] > 0: # N + SW = NW
            counter['n']  -= 1
            counter['sw'] -= 1
            if counter['se'] > 0:
                counter['se'] -= 1
            else:
                counter['nw'] += 1
        elif counter['s'] > 0 and counter['ne'] > 0: # S + NE = SE
            counter['s']  -= 1
            counter['ne'] -= 1
            if counter['nw'] > 0:
                counter['nw'] -= 1
            else:
                counter['se'] += 1
        elif counter['s'] > 0 and counter['nw'] > 0: # S + NW = SW
            counter['s']  -= 1
            counter['nw'] -= 1
            if counter['ne'] > 0:
                counter['ne'] -= 1
            else:
                counter['sw'] += 1
        
        dist = sum(counter.values())
        if dist > max_dist:
            max_dist = dist
    return max_dist
    
print(solve_part_2())
