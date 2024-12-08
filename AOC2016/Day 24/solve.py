from itertools import permutations

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def get_shortest_dist():
    layout = read_input_file_data().splitlines()
    HEIGHT = len(layout)
    WIDTH = len(layout[0])
    # for i in range(HEIGHT):
    #     for j in range(WIDTH):
    #         if layout[i][j] != '#' and layout[i][j] != '.':
    #             print(f"{layout[i][j]}: ({i}, {j})")
    '''
    4: (1, 131)
    6: (9, 23)
    0: (9, 153)
    1: (17, 167)
    7: (21, 7)
    3: (31, 171)
    5: (41, 1)
    2: (41, 139)
    '''
    LOCATIONS = { 0: (9, 153),
                  1: (17, 167),
                  2: (41, 139),
                  3: (31, 171),
                  4: (1, 131),
                  5: (41, 1),
                  6: (9, 23),
                  7: (21, 7) }
    
    def BFS(start):
        nonlocal layout
        output = [-1 for _ in range(8)]
        dist = [[-1] * WIDTH for _ in range(HEIGHT)]

        steps = 0
        frontier = {start}
        while frontier != set():
            new_frontier = set()
            for loc in frontier:
                x, y = loc
                if dist[x][y] !=  -1: # already visited
                    continue
                if layout[x][y] == '#': # blocked
                    continue
                if layout[x][y] != '.': # key location
                    output[int(layout[x][y])] = steps
                # expanding frontier
                dist[x][y] = steps
                if x-1 >= 0:
                    new_frontier.add((x-1, y))
                if x+1 < HEIGHT:
                    new_frontier.add((x+1, y))
                if y-1 >= 0:
                    new_frontier.add((x, y-1))
                if y+1 < WIDTH:
                    new_frontier.add((x, y+1))   
            frontier = new_frontier
            steps += 1
        return output
    
    return [BFS(LOCATIONS[i]) for i in range(8)]

def solve_part_1():
    SHORTEST_DIST = get_shortest_dist()

    min_dist = float('infinity')
    for perm in list(permutations(range(1, 8))):
        dist = SHORTEST_DIST[0][perm[0]] # Start at 0
        for i in range(1, 7):
            dist += SHORTEST_DIST[perm[i-1]][perm[i]]
        if dist < min_dist:
            min_dist = dist

    return min_dist

def solve_part_2():
    SHORTEST_DIST = get_shortest_dist()

    min_dist = float('infinity')
    for perm in list(permutations(range(1, 8))):
        dist = SHORTEST_DIST[0][perm[0]] # Start at 0
        for i in range(1, 7):
            dist += SHORTEST_DIST[perm[i-1]][perm[i]]
        dist += SHORTEST_DIST[perm[6]][0]
        if dist < min_dist:
            min_dist = dist

    return min_dist
    
print(solve_part_2())
