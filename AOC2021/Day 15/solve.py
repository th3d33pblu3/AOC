import numpy as np
import queue

def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def get_matrix():
    file = read_input_file()
    data = file.readlines()

    height = len(data)
    width = len(data[0]) - 1

    weights = np.full((height, width), 0)

    for i in range(height):
        line = data[i]
        for x in range(width):
            weights[i][x] = int(line[x])
    
    return height, width, weights

def get_big_matrix():
    file = read_input_file()
    data = file.readlines()

    height = len(data)
    width = len(data[0]) - 1

    weights = np.full((height, width), 0)

    for i in range(height):
        line = data[i]
        for x in range(width):
            weights[i][x] = int(line[x])

    # height, width, weights
    extended_weights = weights.copy()
    for i in range(1, 9):
        weights = weights + 1
        weights = np.where(weights > 9, weights - 9, weights)
        extended_weights = np.hstack((extended_weights, weights.copy()))

    big_height = height * 5
    big_width = width * 5

    big_matrix = extended_weights[:, 0 : big_width]
    for i in range(1, 5):
        x = extended_weights[:, i * width : big_width + i * width]
        big_matrix = np.vstack((big_matrix, x))
    
    return big_height, big_width, big_matrix


def solve_part_1():
    # Initialization
    height, width, weights = get_matrix()
    best_sol = np.full((height, width), np.inf)

    pos = (0, 0)
    pq = queue.PriorityQueue()

    # Pre-processing
    best_sol[0][0] = 0
    pq.put((weights[0][1], (0, 1)))
    pq.put((weights[1][0], (1, 0)))

    # Get-moves
    def get_moves(pos):
        h = pos[0]
        w = pos[1]
        curr_val = best_sol[h][w]

        left = w - 1
        right = w + 1
        up = h - 1
        down = h + 1

        moves = []
        if left >= 0 and best_sol[h][left] == np.inf:
            moves.append((curr_val + weights[h][left], (h, left)))
        if up >= 0 and best_sol[up][w] == np.inf:
            moves.append((curr_val + weights[up][w], (up, w)))
        if right < width and best_sol[h][right] == np.inf:
            moves.append((curr_val + weights[h][right], (h, right)))
        if down < height and best_sol[down][w] == np.inf:
            moves.append((curr_val + weights[down][w], (down, w)))

        return moves

    while (pos != (height - 1, width - 1)):
        next = pq.get()
        while (next[0] >= best_sol[next[1][0]][next[1][1]]):
            next = pq.get()

        best_sol[next[1][0]][next[1][1]] = next[0]
        pos = next[1]

        new_moves = get_moves(pos)
        for move in new_moves:
            pq.put(move)

    print(best_sol)
    return best_sol[pos[0]][pos[1]]

def solve_part_2():
    # Initialization
    height, width, weights = get_big_matrix()
    best_sol = np.full((height, width), np.inf)

    pos = (0, 0)
    pq = queue.PriorityQueue()

    # Pre-processing
    best_sol[0][0] = 0
    pq.put((weights[0][1], (0, 1)))
    pq.put((weights[1][0], (1, 0)))

    # Get-moves
    def get_moves(pos):
        h = pos[0]
        w = pos[1]
        curr_val = best_sol[h][w]

        left = w - 1
        right = w + 1
        up = h - 1
        down = h + 1

        moves = []
        if left >= 0 and best_sol[h][left] == np.inf:
            moves.append((curr_val + weights[h][left], (h, left)))
        if up >= 0 and best_sol[up][w] == np.inf:
            moves.append((curr_val + weights[up][w], (up, w)))
        if right < width and best_sol[h][right] == np.inf:
            moves.append((curr_val + weights[h][right], (h, right)))
        if down < height and best_sol[down][w] == np.inf:
            moves.append((curr_val + weights[down][w], (down, w)))

        return moves

    while (pos != (height - 1, width - 1)):
        next = pq.get()
        while (next[0] >= best_sol[next[1][0]][next[1][1]]):
            next = pq.get()

        best_sol[next[1][0]][next[1][1]] = next[0]
        pos = next[1]

        new_moves = get_moves(pos)
        for move in new_moves:
            pq.put(move)

    print(best_sol)
    return best_sol[pos[0]][pos[1]]

print(solve_part_2())
