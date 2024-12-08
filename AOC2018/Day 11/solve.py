def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    SR = int(read_input_file_data())
    # initialize grids
    grids = [[0] * 300 for _ in range(300)]
    # find power levels
    for x in range(1, 301):
        for y in range(1, 301):
            rackID = x + 10
            grids[y-1][x-1] = ((((rackID * y + SR) * rackID) // 100) % 10) - 5
    # find largest power
    def grid_sum(x, y):
        return grids[y-1][x-1] + grids[y-1][x] + grids[y-1][x+1] + grids[y][x-1] + grids[y][x] + grids[y][x+1] + grids[y+1][x-1] + grids[y+1][x] + grids[y+1][x+1]
    max_power = grid_sum(0, 0)
    top_left = (0, 0)
    for x in range(1, 301 - 2):
        for y in range(1, 301 - 2):
            grid_power = grid_sum(x, y)
            if grid_power > max_power:
                max_power = grid_power
                top_left = (x, y)
    return top_left

def solve_part_2():
    SR = int(read_input_file_data())
    # initialize grids
    grids = [[0] * 300 for _ in range(300)]
    # find power levels
    for x in range(1, 301):
        for y in range(1, 301):
            rackID = x + 10
            grids[y-1][x-1] = ((((rackID * y + SR) * rackID) // 100) % 10) - 5
    # create grid sums
    sums = [[None] * 300 for _ in range(300)]
    def fill_sums(x, y):
        if x < 0 or y < 0:
            return 0
        if sums[y][x] != None:
            return sums[y][x]
        else:
            sums[y][x] = grids[y][x] + fill_sums(x-1, y) + fill_sums(x, y-1) - fill_sums(x-1, y-1)
            return sums[y][x]
    fill_sums(299, 299)
    # find max power grid
    def get_grid_sum(x, y):
        if x - 1 < 0 or y - 1 < 0:
            return 0
        return sums[y-1][x-1]
    max_power = grids[0][0]
    id = (0, 0, 1)
    for x in range(1, 301):
        for y in range(1, 301):
            for size in range(1, 301 - max(x, y)):
                x_limit = x + size - 1
                y_limit = y + size - 1
                grid_power = get_grid_sum(x_limit, y_limit) - get_grid_sum(x - 1, y_limit) - get_grid_sum(x_limit, y - 1) + get_grid_sum(x - 1, y - 1)
                if grid_power > max_power:
                    max_power = grid_power
                    id = (x, y, size)
    return id
    
print(solve_part_2())
