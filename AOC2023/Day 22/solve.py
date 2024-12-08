from functools import cmp_to_key
from queue import Queue

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    bricks = []
    for line in read_input_file_data().splitlines():
        left, right = line.split('~')
        left = tuple(map(int, left.split(',')))
        right = tuple(map(int, right.split(',')))
        bricks.append((left, right))

    def cmp(s1, s2):
        l1, r1 = s1
        l2, r2 = s2
        if l1[2] != l2[2]:
            return l1[2] - l2[2]
        elif l1[1] != l2[1]:
            return l1[1] - l2[1]
        else:
            return l1[0] - l2[0]
    bricks.sort(key=cmp_to_key(cmp))

    # 10 by 10 cross area
    top_view_height = [[0] * 10 for _ in range(10)]
    top_view_bricks = [[0] * 10 for _ in range(10)]
    unremovable_bricks = {0}
    can_remove_bricks = set()
    uncovered_bricks = set()
    for i, brick in enumerate(bricks, start=1):
        (lx, ly, lz), (rx, ry, rz) = brick
        if lz != rz: # Vertical brick: fixed x,y
            uncovered_bricks.discard(top_view_bricks[ly][lx]) # Supporting brick being covered
            unremovable_bricks.add(top_view_bricks[ly][lx]) # Supporting brick is sole support and cannot be removed
            top_view_height[ly][lx] += rz - lz + 1 # Update height
            top_view_bricks[ly][lx] = i # Update brick number
            uncovered_bricks.add(i) # Current brick uncovered
        else: # Horizontal brick: fixed z
            # Find height to rest on
            support_height = 0
            for y in range(ly, ry+1):
                for x in range(lx, rx+1):
                    support_height = max(top_view_height[y][x], support_height)
            # Find bricks being rested on
            support_bricks = set()
            for y in range(ly, ry+1):
                for x in range(lx, rx+1):
                    if top_view_height[y][x] == support_height:
                        uncovered_bricks.discard(top_view_bricks[y][x])  # Supporting brick being covered
                        support_bricks.add(top_view_bricks[y][x])
                    top_view_height[y][x] = support_height + 1  # Update height
                    top_view_bricks[y][x] = i  # Update brick number
            if len(support_bricks) > 1:
                can_remove_bricks.update(support_bricks) # More than 1 support brick, both can be removed
            elif len(support_bricks) == 1:
                unremovable_bricks.update(support_bricks) # Supporting brick is sole support and cannot be removed
            uncovered_bricks.add(i) # Current brick uncovered
    
    can_remove_bricks.update(uncovered_bricks)
    can_remove_bricks.difference_update(unremovable_bricks)
    return len(can_remove_bricks)

def solve_part_2():
    bricks = []
    for line in read_input_file_data().splitlines():
        left, right = line.split('~')
        left = tuple(map(int, left.split(',')))
        right = tuple(map(int, right.split(',')))
        bricks.append((left, right))

    def cmp(s1, s2):
        l1, r1 = s1
        l2, r2 = s2
        if l1[2] != l2[2]:
            return l1[2] - l2[2]
        elif l1[1] != l2[1]:
            return l1[1] - l2[1]
        else:
            return l1[0] - l2[0]
    bricks.sort(key=cmp_to_key(cmp))
    NUM_BRICKS = len(bricks)

    # 10 by 10 cross area
    top_view_height = [[0] * 10 for _ in range(10)]
    top_view_bricks = [[0] * 10 for _ in range(10)]
    bricks_on_top = {i: set() for i in range(NUM_BRICKS + 1)}
    bricks_below = {i: set() for i in range(NUM_BRICKS + 1)}
    for i, brick in enumerate(bricks, start=1):
        (lx, ly, lz), (rx, ry, rz) = brick
        if lz != rz: # Vertical brick: fixed x,y
            bricks_on_top[top_view_bricks[ly][lx]].add(i)
            bricks_below[i].add(top_view_bricks[ly][lx])
            top_view_height[ly][lx] += rz - lz + 1 # Update height
            top_view_bricks[ly][lx] = i # Update brick number
        else: # Horizontal brick: fixed z
            # Find height to rest on
            support_height = 0
            for y in range(ly, ry+1):
                for x in range(lx, rx+1):
                    support_height = max(top_view_height[y][x], support_height)
            # Find bricks being rested on
            for y in range(ly, ry+1):
                for x in range(lx, rx+1):
                    if top_view_height[y][x] == support_height:
                        bricks_on_top[top_view_bricks[y][x]].add(i)
                        bricks_below[i].add(top_view_bricks[y][x])
                    top_view_height[y][x] = support_height + 1  # Update height
                    top_view_bricks[y][x] = i  # Update brick number

    bricks_to_disintegrate = set()
    for i in range(1, NUM_BRICKS + 1):
        if len(bricks_below[i]) == 1:
            bricks_to_disintegrate.update(bricks_below[i])
    bricks_to_disintegrate.discard(0) # Discard ground if exists

    total_sum = 0
    for i in bricks_to_disintegrate:
        falling_bricks = {i}
        frontier = Queue()
        for brick in bricks_on_top[i]:
            frontier.put(brick)
        while not frontier.empty():
            new_frontier = Queue()
            while not frontier.empty():
                brick = frontier.get()
                unfell_supports = bricks_below[brick].difference(falling_bricks)
                if len(unfell_supports) == 0:
                    falling_bricks.add(brick)
                    for next_brick in bricks_on_top[brick]:
                        new_frontier.put(next_brick)
            frontier = new_frontier
        falling_bricks.discard(i)
        total_sum += len(falling_bricks)
    return total_sum
    
print(solve_part_2())
