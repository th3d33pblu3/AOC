FAVOURITE_NUM = 1352

def is_wall(x, y):
    if x < 0 or y < 0:
        return True
    value = x*x + 3*x + 2*x*y + y + y*y + FAVOURITE_NUM
    return str(bin(value)).count('1') % 2 == 1

def solve_part_1():
    x_goal = 31
    y_goal = 39
    starting_x = 1
    starting_y = 1
    visited = set()
    current = {(starting_x, starting_y)}
    steps = 0
    while len(current) > 0:
        new_states = set()
        for x, y in current:
            if x == x_goal and y == y_goal:
                return steps
            if not is_wall(x - 1, y):
                new_states.add((x - 1, y))
            if not is_wall(x + 1, y):
                new_states.add((x + 1, y))
            if not is_wall(x, y - 1):
                new_states.add((x, y - 1))
            if not is_wall(x, y + 1):
                new_states.add((x, y + 1))
        
        visited = visited.union(current)
        current = new_states.difference(visited)
        steps += 1

def solve_part_2():
    STEP_LIMIT = 50
    starting_x = 1
    starting_y = 1
    visited = set()
    current = {(starting_x, starting_y)}
    steps = -1
    while steps < STEP_LIMIT:
        new_states = set()
        for x, y in current:
            if not is_wall(x - 1, y):
                new_states.add((x - 1, y))
            if not is_wall(x + 1, y):
                new_states.add((x + 1, y))
            if not is_wall(x, y - 1):
                new_states.add((x, y - 1))
            if not is_wall(x, y + 1):
                new_states.add((x, y + 1))
        steps += 1
        visited = visited.union(current)
        current = new_states.difference(visited)
        
    return len(visited)
                
    
print(solve_part_2())
