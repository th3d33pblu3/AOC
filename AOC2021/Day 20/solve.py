def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

LIGHT = '#'
DARK = '.'

def solve_part_1():
    algorithm, image = read_input_file_data().split('\n\n')
    image = image.splitlines()
    WIDTH = len(image[0])
    HEIGHT = len(image)

    # Pixel tracking
    lit_pixels = set()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if image[y][x] == LIGHT:
                lit_pixels.add((x, y))
    unseen_pixels = DARK # Starts off as DARK

    # Borders of image
    x_min = 0
    y_min = 0
    x_max = WIDTH
    y_max = HEIGHT
    
    # Helper function
    def get_pixel_algo_value(x, y):
        nonlocal lit_pixels, unseen_pixels, x_min, y_min, x_max, y_max
        binary = ''
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                nx, ny = x+dx, y+dy
                if nx < x_min or nx >= x_max or ny < y_min or ny >= y_max: # Unseen pixel
                    binary += '1' if unseen_pixels == LIGHT else '0'
                else:
                    binary += '1' if (nx, ny) in lit_pixels else '0'
        return int(binary, 2)

    # Enhancement algorithm
    ENHANCEMENT_COUNT = 2
    for _ in range(ENHANCEMENT_COUNT):
        new_lit_pixels = set()
        for y in range(y_min-1, y_max+1): # Taking care of corner and edges
            for x in range(x_min-1, x_max+1): # Taking care of corner and edges
                enhanced = algorithm[get_pixel_algo_value(x, y)]
                if enhanced == LIGHT:
                    new_lit_pixels.add((x, y))

        # Update tracked pixels
        lit_pixels = new_lit_pixels

        # Update relevant range
        x_min -= 1
        y_min -= 1
        x_max += 1
        y_max += 1

        # Update unseen pixels
        if algorithm[0] == LIGHT and unseen_pixels == DARK:
            unseen_pixels = LIGHT
        elif algorithm[-1] == DARK and unseen_pixels == LIGHT:
            unseen_pixels = DARK
    
    assert unseen_pixels == DARK # Prevent infinite lit pixels
    return len(lit_pixels)

def solve_part_2():
    algorithm, image = read_input_file_data().split('\n\n')
    image = image.splitlines()
    WIDTH = len(image[0])
    HEIGHT = len(image)

    # Pixel tracking
    lit_pixels = set()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if image[y][x] == LIGHT:
                lit_pixels.add((x, y))
    unseen_pixels = DARK # Starts off as DARK

    # Borders of image
    x_min = 0
    y_min = 0
    x_max = WIDTH
    y_max = HEIGHT
    
    # Helper function
    def get_pixel_algo_value(x, y):
        nonlocal lit_pixels, unseen_pixels, x_min, y_min, x_max, y_max
        binary = ''
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                nx, ny = x+dx, y+dy
                if nx < x_min or nx >= x_max or ny < y_min or ny >= y_max: # Unseen pixel
                    binary += '1' if unseen_pixels == LIGHT else '0'
                else:
                    binary += '1' if (nx, ny) in lit_pixels else '0'
        return int(binary, 2)

    # Enhancement algorithm
    ENHANCEMENT_COUNT = 50
    for _ in range(ENHANCEMENT_COUNT):
        new_lit_pixels = set()
        for y in range(y_min-1, y_max+1): # Taking care of corner and edges
            for x in range(x_min-1, x_max+1): # Taking care of corner and edges
                enhanced = algorithm[get_pixel_algo_value(x, y)]
                if enhanced == LIGHT:
                    new_lit_pixels.add((x, y))

        # Update tracked pixels
        lit_pixels = new_lit_pixels

        # Update relevant range
        x_min -= 1
        y_min -= 1
        x_max += 1
        y_max += 1

        # Update unseen pixels
        if algorithm[0] == LIGHT and unseen_pixels == DARK:
            unseen_pixels = LIGHT
        elif algorithm[-1] == DARK and unseen_pixels == LIGHT:
            unseen_pixels = DARK
    
    assert unseen_pixels == DARK # Prevent infinite lit pixels
    return len(lit_pixels)
    
print(solve_part_2())
