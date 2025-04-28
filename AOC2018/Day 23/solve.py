import re
from pulp import *

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def get_nanobots():
    data = read_input_file_data()
    nanobots = [list(map(int, re.findall(r'-?\d+', line))) for line in data.splitlines()]
    return nanobots

def solve_part_1():
    nanobots = get_nanobots()
    strongest_bot = nanobots[0]
    for bot in nanobots:
        if bot[3] > strongest_bot[3]:
            strongest_bot = bot
    x, y, z, r = strongest_bot
    return len(list(filter(lambda bot: abs(bot[0] - x) + abs(bot[1] - y) + abs(bot[2] - z) <= r, nanobots)))

def solve_part_2():
    '''
    Setup
    '''
    nanobots = get_nanobots()

    # Bounds
    min_x = min(bx - br for bx, _, _, br in nanobots)
    max_x = max(bx + br for bx, _, _, br in nanobots)
    min_y = min(by - br for _, by, _, br in nanobots)
    max_y = max(by + br for _, by, _, br in nanobots)
    min_z = min(bz - br for _, _, bz, br in nanobots)
    max_z = max(bz + br for _, _, bz, br in nanobots)
    M = 5 * (10**8) # value to bound the points

    # Declare decision variables
    x = LpVariable('x', lowBound=min_x, upBound=max_x, cat=LpContinuous)
    y = LpVariable('y', lowBound=min_y, upBound=max_y, cat=LpContinuous)
    z = LpVariable('z', lowBound=min_z, upBound=max_z, cat=LpContinuous)

    in_range = {}
    dx = {}
    dy = {}
    dz = {}

    # Set up Phase 1 (maximize coverage)
    prob1 = LpProblem("Phase1_Maximize_Coverage", LpMaximize)
    # Set up Phase 2 (minimize distance)
    prob2 = LpProblem("Phase2_Minimize_Distance", LpMinimize)

    # Add constraints common to both phases
    for i, (bx, by, bz, br) in enumerate(nanobots):
        in_range[i] = LpVariable(f"in_range_{i}", cat=LpBinary)
        dx[i] = LpVariable(f"dx_{i}", lowBound=0, cat=LpContinuous)
        dy[i] = LpVariable(f"dy_{i}", lowBound=0, cat=LpContinuous)
        dz[i] = LpVariable(f"dz_{i}", lowBound=0, cat=LpContinuous)

        for prob in (prob1, prob2):
            # linearize |x - bx|, |y - by|, |z - bz|
            prob += dx[i] >= x - bx
            prob += dx[i] >= bx - x
            prob += dy[i] >= y - by
            prob += dy[i] >= by - y
            prob += dz[i] >= z - bz
            prob += dz[i] >= bz - z
            # in_range flag with big-M relaxation
            prob += dx[i] + dy[i] + dz[i] <= br + M * (1 - in_range[i])

    '''
    Phase 1
    '''
    # Phase 1 objective: maximize number of bots in range
    prob1 += lpSum(in_range.values()), "MaximizeCoverage"
    # Solve Phase 1
    prob1.solve(PULP_CBC_CMD(msg=False))
    # Extract results
    best_count = int(value(lpSum(in_range.values())))
    print(f"Best coverage found: {best_count}") # 985

    '''
    Phase 2
    '''
    # Bind coverage count in Phase 2
    prob2 += lpSum(in_range.values()) == best_count, "FixCoverage"

    # Add variables and constraints to measure distance to origin
    d0x = LpVariable("d0x", lowBound=0, cat=LpContinuous)
    d0y = LpVariable("d0y", lowBound=0, cat=LpContinuous)
    d0z = LpVariable("d0z", lowBound=0, cat=LpContinuous)
    prob2 += d0x >= x
    prob2 += d0x >= -x
    prob2 += d0y >= y
    prob2 += d0y >= -y
    prob2 += d0z >= z
    prob2 += d0z >= -z

    # Phase 2 objective: minimize Manhattan distance to origin
    prob2 += d0x + d0y + d0z, "MinimizeDistance"
    # Solve Phase 2
    prob2.solve(PULP_CBC_CMD(msg=False))
    # Extract
    optimal_point = (int(value(x)), int(value(y)), int(value(z))) # (53492544, 46716342, 24067217)
    optimal_distance = int(value(d0x + d0y + d0z)) # 124276103
    print(f"Optimal point: {optimal_point}, Distance to origin: {optimal_distance}")
    return optimal_distance

print(solve_part_2())
