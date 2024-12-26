def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    maze = read_input_file_data().splitlines()
    starting_pos = (len(maze)-2, 1)
    ending_pos = (1, len(maze[0])-2)
    assert maze[starting_pos[0]][starting_pos[1]] == 'S'
    assert maze[ending_pos[0]][ending_pos[1]] == 'E'
    maze[starting_pos[0]] = maze[starting_pos[0]].replace("S", ".")
    maze[ending_pos[0]] = maze[ending_pos[0]].replace("E", ".")

    N, E, S, W = 0, 1, 2, 3
    WALL, EMPTY = '#', '.'
    HEIGHT, WIDTH = len(maze), len(maze[0])
    best_scores = {(starting_pos[0], starting_pos[1], E): 0}
    frontier = set()
    frontier.add((starting_pos[0], starting_pos[1], E))

    while len(frontier) != 0:
        new_frontier = set()
        for i, j, dir in frontier:
            if (i, j) == ending_pos:
                continue
            score = best_scores[(i, j, dir)] # must exist

            # Move
            new_pos = None
            if dir == N and i-1 >= 0 and maze[i-1][j] != WALL:
                new_pos = (i-1, j, dir)
            elif dir == E and j+1 < WIDTH and maze[i][j+1] != WALL:
                new_pos = (i, j+1, dir)
            elif dir == S and i+1 < HEIGHT and maze[i+1][j] != WALL:
                new_pos = (i+1, j, dir)
            elif dir == W and j-1 >= 0 and maze[i][j-1] != WALL:
                new_pos = (i, j-1, dir)

            if new_pos != None:
                new_score = score + 1
                if new_pos not in best_scores or new_score < best_scores[new_pos]:
                    new_frontier.add(new_pos)
                    best_scores[new_pos] = new_score
            
            # Rotate
            new_pos1, new_pos2 = ((i, j, E), (i, j, W)) if dir in (N, S) else ((i, j, N), (i, j, S))
            new_score = score + 1000
            if new_pos1 not in best_scores or new_score < best_scores[new_pos1]:
                new_frontier.add(new_pos1)
                best_scores[new_pos1] = new_score
            if new_pos2 not in best_scores or new_score < best_scores[new_pos2]:
                new_frontier.add(new_pos2)
                best_scores[new_pos2] = new_score
        
        frontier = new_frontier
    
    return min(best_scores.get((*ending_pos, N), None), best_scores.get((*ending_pos, E), None))

def solve_part_2():
    maze = read_input_file_data().splitlines()
    starting_pos = (len(maze)-2, 1)
    ending_pos = (1, len(maze[0])-2)
    assert maze[starting_pos[0]][starting_pos[1]] == 'S'
    assert maze[ending_pos[0]][ending_pos[1]] == 'E'
    maze[starting_pos[0]] = maze[starting_pos[0]].replace("S", ".")
    maze[ending_pos[0]] = maze[ending_pos[0]].replace("E", ".")

    N, E, S, W = 0, 1, 2, 3
    WALL, EMPTY = '#', '.'
    HEIGHT, WIDTH = len(maze), len(maze[0])
    best_scores = {(starting_pos[0], starting_pos[1], E): 0}
    frontier = set()
    frontier.add((starting_pos[0], starting_pos[1], E))

    while len(frontier) != 0:
        new_frontier = set()
        for i, j, dir in frontier:
            if (i, j) == ending_pos:
                continue
            score = best_scores[(i, j, dir)] # must exist

            # Move
            new_pos = None
            if dir == N and i-1 >= 0 and maze[i-1][j] != WALL:
                new_pos = (i-1, j, dir)
            elif dir == E and j+1 < WIDTH and maze[i][j+1] != WALL:
                new_pos = (i, j+1, dir)
            elif dir == S and i+1 < HEIGHT and maze[i+1][j] != WALL:
                new_pos = (i+1, j, dir)
            elif dir == W and j-1 >= 0 and maze[i][j-1] != WALL:
                new_pos = (i, j-1, dir)

            if new_pos != None:
                new_score = score + 1
                if new_pos not in best_scores or new_score < best_scores[new_pos]:
                    new_frontier.add(new_pos)
                    best_scores[new_pos] = new_score
            
            # Rotate
            new_pos1, new_pos2 = ((i, j, E), (i, j, W)) if dir in (N, S) else ((i, j, N), (i, j, S))
            new_score = score + 1000
            if new_pos1 not in best_scores or new_score < best_scores[new_pos1]:
                new_frontier.add(new_pos1)
                best_scores[new_pos1] = new_score
            if new_pos2 not in best_scores or new_score < best_scores[new_pos2]:
                new_frontier.add(new_pos2)
                best_scores[new_pos2] = new_score
        
        frontier = new_frontier

    # Backtracking
    frontier = set()
    ending1, ending2 = (*ending_pos, E), (*ending_pos, N)
    score1, score2 = best_scores[ending1], best_scores[ending2]
    if score1 <= score2:
        frontier.add((*ending1, score1))
    if score2 <= score1:
        frontier.add((*ending2, score2))
    
    best_tiles = set()
    while len(frontier) != 0:
        new_frontier = set()
        for i, j, dir, score in frontier:
            best_tiles.add((i, j))
            if (i, j) == starting_pos:
                continue

            # Move
            new_pos = None
            if dir == S and i-1 >= 0 and maze[i-1][j] != WALL:
                new_pos = (i-1, j, dir, score - 1)
            elif dir == W and j+1 < WIDTH and maze[i][j+1] != WALL:
                new_pos = (i, j+1, dir, score - 1)
            elif dir == N and i+1 < HEIGHT and maze[i+1][j] != WALL:
                new_pos = (i+1, j, dir, score - 1)
            elif dir == E and j-1 >= 0 and maze[i][j-1] != WALL:
                new_pos = (i, j-1, dir, score - 1)

            if new_pos != None:
                if score - 1 == best_scores[new_pos[:3]]:
                    new_frontier.add(new_pos)
            
            # Rotate
            new_score = score - 1000
            new_pos1, new_pos2 = ((i, j, E), (i, j, W)) if dir in (N, S) else ((i, j, N), (i, j, S))
            if new_pos1 in best_scores and new_score == best_scores[new_pos1]:
                new_frontier.add((*new_pos1, new_score))
            if new_pos2 in best_scores and new_score == best_scores[new_pos2]:
                new_frontier.add((*new_pos2, new_score))
        
        frontier = new_frontier
    
    return len(best_tiles)
    
print(solve_part_2())
