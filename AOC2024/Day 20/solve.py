def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    WALL = '#'
    maze_data = read_input_file_data().splitlines()
    HEIGHT, WIDTH = len(maze_data), len(maze_data[0])

    START = None
    END = None
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if maze_data[i][j] == 'S':
                START = (i, j)
            elif maze_data[i][j] == 'E':
                END = (i, j)
    assert START != None and END != None

    def is_in_maze(i, j):
        return i > 0 and i < HEIGHT-1 and j > 0 and j < WIDTH-1

    # Min time to each tile (Only single path from START to END)
    frontier = START
    steps = 0
    visited = { START: 0 }
    while frontier != None:
        new_frontier = None
        steps += 1
        i, j = frontier
        if i-1 > 0 and maze_data[i-1][j] != WALL and (i-1, j) not in visited:
            new_frontier = (i-1, j)
            visited[(i-1, j)] = steps
        elif i+1 < HEIGHT-1 and maze_data[i+1][j] != WALL and (i+1, j) not in visited:
            new_frontier = (i+1, j)
            visited[(i+1, j)] = steps
        elif j-1 > 0 and maze_data[i][j-1] != WALL and (i, j-1) not in visited:
            new_frontier = (i, j-1)
            visited[(i, j-1)] = steps
        elif j+1 < WIDTH-1 and maze_data[i][j+1] != WALL and (i, j+1) not in visited:
            new_frontier = (i, j+1)
            visited[(i, j+1)] = steps
        frontier = new_frontier

    # Cheat
    count_cheats_save_100 = 0
    # time_saved_cheats = {}
    for (i, j), steps in visited.items():
        for si, sj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
            if not is_in_maze(si, sj) or maze_data[si][sj] != WALL: # ignore invalid cheat_start
                continue
            for ei, ej in ((si-1, sj), (si+1, sj), (si, sj-1), (si, sj+1)):
                cheat_end = (ei, ej)
                if ei == i and ej == j: # ignore cheat ends that go back to same spot
                    continue
                if not is_in_maze(ei, ej) or maze_data[ei][ej] == WALL: # ignore invalid cheat_end
                    continue
                # Valid cheat
                new_steps = steps + 2
                if visited[cheat_end] - new_steps >= 100: # Cheat saved more than 100 picoseconds
                    count_cheats_save_100 += 1

    #             # For checking
    #             time_saved = visited[cheat_end] - new_steps
    #             if time_saved > 0:
    #                 if time_saved not in time_saved_cheats:
    #                     time_saved_cheats[time_saved] = set()
    #                 time_saved_cheats[time_saved].add((i, j, ei, ej))
    
    # time_saved_list = list(time_saved_cheats.keys())
    # time_saved_list.sort()
    # for time in time_saved_list:
    #     print(f"There are {len(time_saved_cheats[time])} that save {time} picoseconds.")
    return count_cheats_save_100

def solve_part_2():
    WALL = '#'
    maze_data = read_input_file_data().splitlines()
    HEIGHT, WIDTH = len(maze_data), len(maze_data[0])

    START = None
    END = None
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if maze_data[i][j] == 'S':
                START = (i, j)
            elif maze_data[i][j] == 'E':
                END = (i, j)
    assert START != None and END != None

    # Min time to each tile (Only single path from START to END)
    frontier = START
    steps = 0
    visited = set((START,))
    step_locs = { 0: START }
    while frontier != None:
        steps += 1
        i, j = frontier
        for ni, nj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
            if ni > 0 and ni < HEIGHT-1 and nj > 0 and nj < WIDTH-1 and maze_data[ni][nj] != WALL and (ni, nj) not in visited:
                frontier = (ni, nj)
                visited.add((ni, nj))
                step_locs[steps] = (ni, nj)
                break
        else:
            frontier = None
    assert step_locs[steps - 1] == END # steps is being incremented to after END

    # Cheat
    MIN_TIME_SAVED = 100
    CHEAT_DURATION = 20
    loc_by_step = [step_locs[s] for s in range(steps)]
    count = 0
    for s, (i, j) in enumerate(loc_by_step[:steps - MIN_TIME_SAVED]):
        for t, (ei, ej) in enumerate(loc_by_step[s + MIN_TIME_SAVED:], start = s + MIN_TIME_SAVED):
            dist = abs(i - ei) + abs(j - ej)
            if dist <= CHEAT_DURATION and t - s - dist >= MIN_TIME_SAVED:
                count += 1
    return count
    
print(solve_part_2())
