def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    garden_map = read_input_file_data().splitlines()
    HEIGHT = len(garden_map)
    WIDTH = len(garden_map[0])

    visited_regions = set()
    total_price = 0

    def visit_region(starting_pos):
        nonlocal visited_regions, total_price
        area = 0
        perimeter = 0

        frontier = set()
        frontier.add(starting_pos)
        REGION = garden_map[starting_pos[0]][starting_pos[1]]
        while len(frontier) != 0:
            new_frontier = set()
            for i, j in frontier:
                if (i, j) in visited_regions:
                    continue
                area += 1
                if i-1 >= 0 and garden_map[i-1][j] == REGION:
                    new_frontier.add((i-1, j))
                else:
                    perimeter += 1
                if i+1 < HEIGHT and garden_map[i+1][j] == REGION:
                    new_frontier.add((i+1, j))
                else:
                    perimeter += 1
                if j-1 >= 0 and garden_map[i][j-1] == REGION:
                    new_frontier.add((i, j-1))
                else:
                    perimeter += 1
                if j+1 < WIDTH and garden_map[i][j+1] == REGION:
                    new_frontier.add((i, j+1))
                else:
                    perimeter += 1

            visited_regions.update(frontier)
            frontier = new_frontier

        total_price += area * perimeter

    for i in range(HEIGHT):
        for j in range(WIDTH):
            if (i, j) not in visited_regions:
                visit_region((i, j))
            
    return total_price

def solve_part_2():
    garden_map = read_input_file_data().splitlines()
    HEIGHT = len(garden_map)
    WIDTH = len(garden_map[0])

    visited_regions = set()
    total_price = 0

    def visit_region(starting_pos):
        nonlocal visited_regions, total_price
        area = 0
        fences = set()

        frontier = set()
        frontier.add(starting_pos)
        REGION = garden_map[starting_pos[0]][starting_pos[1]]
        while len(frontier) != 0:
            new_frontier = set()
            for i, j in frontier:
                if (i, j) in visited_regions:
                    continue
                area += 1
                if i-1 >= 0 and garden_map[i-1][j] == REGION:
                    new_frontier.add((i-1, j))
                else:
                    fences.add((i-0.1, j, '-'))
                if i+1 < HEIGHT and garden_map[i+1][j] == REGION:
                    new_frontier.add((i+1, j))
                else:
                    fences.add((i+0.1, j, '-'))
                if j-1 >= 0 and garden_map[i][j-1] == REGION:
                    new_frontier.add((i, j-1))
                else:
                    fences.add((i, j-0.1, '|'))
                if j+1 < WIDTH and garden_map[i][j+1] == REGION:
                    new_frontier.add((i, j+1))
                else:
                    fences.add((i, j+0.1, '|'))

            visited_regions.update(frontier)
            frontier = new_frontier

        total_price += area * count_sides(fences)
        # perimeter = len(fences)
        # sides = count_sides(fences)
        # print(f"{REGION=} {area=} {sides=} {perimeter=}")
        # total_price += area * sides
    
    def count_sides(fences: set):
        sides = 0
        while len(fences) != 0:
            fence = fences.pop()
            sides += 1
            i, j, type = fence
            if type == '-':
                # remove left and right all the way
                left = j - 1
                while (i, left, type) in fences:
                    fences.remove((i, left, type))
                    left -= 1
                right = j + 1
                while (i, right, type) in fences:
                    fences.remove((i, right, type))
                    right += 1
            else:
                # remove up and down all the way
                up = i - 1
                while (up, j, type) in fences:
                    fences.remove((up, j, type))
                    up -= 1
                down = i + 1
                while (down, j, type) in fences:
                    fences.remove((down, j, type))
                    down += 1
        return sides

    for i in range(HEIGHT):
        for j in range(WIDTH):
            if (i, j) not in visited_regions:
                visit_region((i, j))
            
    return total_price
    
print(solve_part_2())
