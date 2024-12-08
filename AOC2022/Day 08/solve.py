def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def pre_process():
    file = read_input_file()
    lines = file.readlines()
    tree_map = []
    for line in lines:
        line_map = []
        for char in line[:-1]:
            line_map.append(int(char))
        tree_map.append(line_map)

    return tree_map

def solve_part_1():
    # initialization
    tree_map = pre_process()
    height = len(tree_map)
    width = len(tree_map[0])
    visibility_map = []
    UNKNOWN = 0
    HIDDEN = 1
    VISIBLE = 2

    for _ in range(height):
        line = [UNKNOWN] * width
        line[0] = VISIBLE
        line[-1] = VISIBLE
        visibility_map.append(line)
    visibility_map[0] = [VISIBLE] * width
    visibility_map[-1] = [VISIBLE] * width

    # solving
    # From top
    for col in range(1, width - 1):
        tallest = tree_map[0][col]
        for row in range(1, height - 1):
            if tree_map[row][col] > tallest:
                tallest = tree_map[row][col]
                visibility_map[row][col] = VISIBLE
            else:
                if visibility_map[row][col] != VISIBLE:
                    visibility_map[row][col] = HIDDEN

    # From bottom
    for col in range(1, width - 1):
        tallest = tree_map[height - 1][col]
        for row in range(height - 2, 0, -1):
            if tree_map[row][col] > tallest:
                tallest = tree_map[row][col]
                visibility_map[row][col] = VISIBLE
            else:
                if visibility_map[row][col] != VISIBLE:
                    visibility_map[row][col] = HIDDEN

    # From left
    for row in range(1, height - 1):
        tallest = tree_map[row][0]
        for col in range(1, width - 1):
            if tree_map[row][col] > tallest:
                tallest = tree_map[row][col]
                visibility_map[row][col] = VISIBLE
            else:
                if visibility_map[row][col] != VISIBLE:
                    visibility_map[row][col] = HIDDEN

    # From right
    for row in range(1, height - 1):
        tallest = tree_map[row][width - 1]
        for col in range(width - 2, 0, -1):
            if tree_map[row][col] > tallest:
                tallest = tree_map[row][col]
                visibility_map[row][col] = VISIBLE
            else:
                if visibility_map[row][col] != VISIBLE:
                    visibility_map[row][col] = HIDDEN

    # counting
    count = 0
    for row in range(height):
        count += visibility_map[row].count(VISIBLE)

    return count

def solve_part_2():
    tree_map = pre_process()
    height = len(tree_map)
    width = len(tree_map[0])
    max_score = 0
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            this_height = tree_map[row][col]
            
            up = 0
            for r in range(row - 1, -1, -1):
                up += 1
                if tree_map[r][col] >= this_height:
                    break
            
            down = 0
            for r in range(row + 1, height):
                down += 1
                if tree_map[r][col] >= this_height:
                    break

            left = 0
            for c in range(col - 1, -1, -1):
                left += 1
                if tree_map[row][c] >= this_height:
                    break

            right = 0
            for c in range(col + 1, width):
                right += 1
                if tree_map[row][c] >= this_height:
                    break

            score = up * down * left * right
            if score > max_score:
                max_score = score
    
    return max_score

print(solve_part_2())