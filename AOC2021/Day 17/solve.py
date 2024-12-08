target_x = (253, 280)
target_y = (-73, -46)

def can_reach_target(vx, vy):
    posx = 0
    posy = 0
    while posx <= target_x[1] and posy >= target_y[0]:
        if posx >= target_x[0] and posx <= target_x[1] and posy <= target_y[1] and posy >= target_y[0]:
            return True
        posx += vx
        posy += vy
        vx = max(0, vx - 1)
        vy -= 1
    return False

def get_highest(vx, vy):
    return (vy / 2) * (vy + 1)

def solve_part_1():
    max_h = 0
    for vx in range(1, target_x[1] + 1):
        for vy in range(target_y[0], abs(target_y[0])):
            if can_reach_target(vx, vy):
                max_h = max(max_h, get_highest(vx, vy))
    return max_h

def solve_part_2():
    can_reach = 0
    for vx in range(1, target_x[1] + 1):
        for vy in range(target_y[0], abs(target_y[0])):
            if can_reach_target(vx, vy):
                can_reach += 1
    return can_reach
    
print(solve_part_2())
