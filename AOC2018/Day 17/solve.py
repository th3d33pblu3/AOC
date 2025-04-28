import re

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def process_data():
    data = read_input_file_data().splitlines()
    clay = set()
    for line in data:
        if line[0] == 'x':
            x = int(re.search(r"x=(\d+),", line).group(1))
            y1 = int(re.search(r"y=(\d+)", line).group(1))
            y2 = int(re.search(r"\.\.(\d+)", line).group(1))
            for y in range(y1, y2+1):
                clay.add((x, y))
        else:
            y = int(re.search(r"y=(\d+),", line).group(1))
            x1 = int(re.search(r"x=(\d+)", line).group(1))
            x2 = int(re.search(r"\.\.(\d+)", line).group(1))
            for x in range(x1, x2+1):
                clay.add((x, y))
    return clay

def solve_part_1():
    clay = process_data()
    miny = min(map(lambda p: p[1], clay))
    maxy = max(map(lambda p: p[1], clay))

    water = set()
    frontier = set()
    frontier.add((500, 0))
    while frontier:
        x, y = frontier.pop()
        if y > maxy: # ignore
            continue
        if (x, y) in clay: # ignore paths that now get filled up
            continue
        # try to flow down
        if (x, y+1) not in clay:
            water.add((x, y+1))
            frontier.add((x, y+1))
        else: # hit clay tile
            # check left
            xl = x-1
            while (xl, y) not in clay and (xl, y+1) in clay:
                water.add((xl, y))
                xl -= 1
            left_sealed = (xl, y) in clay # hit clay tile on left
            # check right
            xr = x+1
            while (xr, y) not in clay and (xr, y+1) in clay:
                water.add((xr, y))
                xr += 1
            right_sealed = (xr, y) in clay

            if left_sealed and right_sealed: # found sink
                for xt in range(xl+1, xr): # fill sink
                    clay.add((xt, y))
                    if (xt, y-1) in water:
                        frontier.add((xt, y-1)) # backtrack
            else:
                if not left_sealed:
                    water.add((xl, y))
                    frontier.add((xl, y))
                if not right_sealed:
                    water.add((xr, y))
                    frontier.add((xr, y))
    
    return len(set(filter(lambda p: p[1] >= miny and p[1] <= maxy, water)))

def solve_part_2():
    clay = process_data()
    miny = min(map(lambda p: p[1], clay))
    maxy = max(map(lambda p: p[1], clay))

    water = set()
    # retained_water = 0
    frontier = set()
    frontier.add((500, 0))
    while frontier:
        x, y = frontier.pop()
        if y > maxy: # ignore
            continue
        if (x, y) in clay: # ignore paths that now get filled up
            continue
        # try to flow down
        if (x, y+1) not in clay:
            water.add((x, y+1))
            frontier.add((x, y+1))
        else: # hit clay tile
            # check left
            xl = x-1
            while (xl, y) not in clay and (xl, y+1) in clay:
                water.add((xl, y))
                xl -= 1
            left_sealed = (xl, y) in clay # hit clay tile on left
            # check right
            xr = x+1
            while (xr, y) not in clay and (xr, y+1) in clay:
                water.add((xr, y))
                xr += 1
            right_sealed = (xr, y) in clay

            if left_sealed and right_sealed: # found sink
                for xt in range(xl+1, xr): # fill sink
                    clay.add((xt, y))
                    # retained_water += 1
                    if (xt, y-1) in water:
                        frontier.add((xt, y-1)) # backtrack
            else:
                if not left_sealed:
                    water.add((xl, y))
                    frontier.add((xl, y))
                if not right_sealed:
                    water.add((xr, y))
                    frontier.add((xr, y))

    # return retained_water
    return len(set(filter(lambda p: p[0] >= miny and p[0] <= maxy, clay.intersection(water))))
    
print(solve_part_2())
