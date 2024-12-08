def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    trees = read_input_file_data().splitlines()
    height = len(trees)
    width = len(trees[0])
    checked_trees = 0
    for y in range(height):
        x = (3 * y) % width
        if trees[y][x] == "#":
            checked_trees += 1
    
    return checked_trees

def solve_part_2():
    trees = read_input_file_data().splitlines()
    height = len(trees)
    width = len(trees[0])

    def check_trees(x_jump, y_jump):
        checked_trees = 0
        x = 0
        y = 0
        while y < height:
            if trees[y][x] == "#":
                checked_trees += 1
            x = (x + x_jump) % width
            y += y_jump
        return checked_trees

    total_multiple = 1
    for x_jump, y_jump in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        t = check_trees(x_jump, y_jump)
        print(t)
        total_multiple *= t
    
    return total_multiple

print(solve_part_2())
