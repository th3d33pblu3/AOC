def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    heat_map = [list(map(int, line)) for line in read_input_file_data().splitlines()]
    HEIGHT = len(heat_map)
    WIDTH = len(heat_map[0])
    UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3

    def get_heat_loss(row, col, steps, dir):
        heat_loss = 0
        if dir == UP:
            for i in range(1, steps+1):
                heat_loss += heat_map[row-i][col]
        elif dir == RIGHT:
            for i in range(1, steps+1):
                heat_loss += heat_map[row][col+i]
        elif dir == DOWN:
            for i in range(1, steps+1):
                heat_loss += heat_map[row+i][col]
        elif dir == LEFT:
            for i in range(1, steps+1):
                heat_loss += heat_map[row][col-i]
        else:
            raise Exception("Unknown direction")
        return heat_loss

    states = { (0, 0, None): 0 }
    frontier = set()
    for row in range(1, 4):
        frontier.add((row, 0, DOWN, get_heat_loss(0, 0, row, DOWN)))
    for col in range(1, 4):
        frontier.add((0, col, RIGHT, get_heat_loss(0, 0, col, RIGHT)))
    
    while frontier:
        new_frontier = set()
        for row, col, last_dir, heat_loss in frontier:
            # If visited with lower heat loss
            if ((row, col, last_dir) in states and heat_loss >= states[(row, col, last_dir)] or
                (row, col, (last_dir + 2) % 4) in states and heat_loss >= states[(row, col, (last_dir + 2) % 4)]):
                continue

            # Not visited or found path with lower heat loss
            states[(row, col, last_dir)] = heat_loss

            # Reached end, no longer need to branch
            if row == HEIGHT - 1 and col == WIDTH - 1:
                continue

            # Branching
            if last_dir in (UP, DOWN):
                for d in range(1, 4):
                    if col - d >= 0:
                        new_frontier.add((row, col - d, LEFT, heat_loss + get_heat_loss(row, col, d, LEFT)))
                    if col + d < WIDTH:
                        new_frontier.add((row, col + d, RIGHT, heat_loss + get_heat_loss(row, col, d, RIGHT)))
            elif last_dir in (LEFT, RIGHT):
                for d in range(1, 4):
                    if row - d >= 0:
                        new_frontier.add((row - d, col, UP, heat_loss + get_heat_loss(row, col, d, UP)))
                    if row + d < HEIGHT:
                        new_frontier.add((row + d, col, DOWN, heat_loss + get_heat_loss(row, col, d, DOWN)))
            
        frontier = new_frontier
    
    return min(states[(HEIGHT-1, WIDTH-1, DOWN)], states[((HEIGHT-1, WIDTH-1, RIGHT))])

def solve_part_2():
    heat_map = [list(map(int, line)) for line in read_input_file_data().splitlines()]
    HEIGHT = len(heat_map)
    WIDTH = len(heat_map[0])
    UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
    MIN_STEPS, MAX_STEPS = 4, 10

    def get_heat_loss(row, col, steps, dir):
        heat_loss = 0
        if dir == UP:
            for i in range(1, steps+1):
                heat_loss += heat_map[row-i][col]
        elif dir == RIGHT:
            for i in range(1, steps+1):
                heat_loss += heat_map[row][col+i]
        elif dir == DOWN:
            for i in range(1, steps+1):
                heat_loss += heat_map[row+i][col]
        elif dir == LEFT:
            for i in range(1, steps+1):
                heat_loss += heat_map[row][col-i]
        else:
            raise Exception("Unknown direction")
        return heat_loss

    states = { (0, 0, None): 0 }
    frontier = set()
    for row in range(MIN_STEPS, MAX_STEPS+1):
        frontier.add((row, 0, DOWN, get_heat_loss(0, 0, row, DOWN)))
    for col in range(MIN_STEPS, MAX_STEPS+1):
        frontier.add((0, col, RIGHT, get_heat_loss(0, 0, col, RIGHT)))
    
    while frontier:
        new_frontier = set()
        for row, col, last_dir, heat_loss in frontier:
            # If visited with lower heat loss
            if ((row, col, last_dir) in states and heat_loss >= states[(row, col, last_dir)] or
                (row, col, (last_dir + 2) % 4) in states and heat_loss >= states[(row, col, (last_dir + 2) % 4)]):
                continue

            # Not visited or found path with lower heat loss
            states[(row, col, last_dir)] = heat_loss

            # Reached end, no longer need to branch
            if row == HEIGHT - 1 and col == WIDTH - 1:
                continue

            # Branching
            if last_dir in (UP, DOWN):
                for d in range(MIN_STEPS, MAX_STEPS+1):
                    if col - d >= 0:
                        new_frontier.add((row, col - d, LEFT, heat_loss + get_heat_loss(row, col, d, LEFT)))
                    if col + d < WIDTH:
                        new_frontier.add((row, col + d, RIGHT, heat_loss + get_heat_loss(row, col, d, RIGHT)))
            elif last_dir in (LEFT, RIGHT):
                for d in range(MIN_STEPS, MAX_STEPS+1):
                    if row - d >= 0:
                        new_frontier.add((row - d, col, UP, heat_loss + get_heat_loss(row, col, d, UP)))
                    if row + d < HEIGHT:
                        new_frontier.add((row + d, col, DOWN, heat_loss + get_heat_loss(row, col, d, DOWN)))
            
        frontier = new_frontier
    
    return min(states[(HEIGHT-1, WIDTH-1, DOWN)], states[((HEIGHT-1, WIDTH-1, RIGHT))])
    
print(solve_part_2())
