def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    seafloor = read_input_file_data().splitlines()
    HEIGHT = len(seafloor)
    WIDTH = len(seafloor[0])

    east_cucumbers = set()
    south_cucumbers = set()
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if seafloor[i][j] == '>':
                east_cucumbers.add((i, j))
            elif seafloor[i][j] == 'v':
                south_cucumbers.add((i, j))
    
    steps = 0
    while True:
        is_move = False
        steps += 1

        new_east_cucumbers = set()
        for i, j in east_cucumbers:
            new_cucumber = (i, (j+1) % WIDTH)
            if new_cucumber not in east_cucumbers and new_cucumber not in south_cucumbers:
                is_move = True
                new_east_cucumbers.add(new_cucumber)
            else:
                new_east_cucumbers.add((i, j))
        east_cucumbers = new_east_cucumbers

        new_south_cucumbers = set()
        for i, j in south_cucumbers:
            new_cucumber = ((i+1) % HEIGHT, j)
            if new_cucumber not in east_cucumbers and new_cucumber not in south_cucumbers:
                is_move = True
                new_south_cucumbers.add(new_cucumber)
            else:
                new_south_cucumbers.add((i, j))
        south_cucumbers = new_south_cucumbers

        if not is_move:
            return steps

def solve_part_2():
    pass
    
print(solve_part_1())
