import math

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    asteroids = []
    for y, line in enumerate(read_input_file_data().splitlines()):
        for x, char in enumerate(line):
            if char == '#':
                asteroids.append((x, y))

    max_detected = 0
    best_loc = None
    for (x1, y1) in asteroids:
        angles = set()
        for (x2, y2) in asteroids:
            if (x1, y1) == (x2, y2):
                continue
            angles.add(math.atan2(y2-y1, x2-x1))
        detected = len(angles)
        if detected > max_detected:
            best_loc = (x1, y1)
            max_detected = detected

    print(best_loc) # (29, 28)
    return max_detected

def solve_part_2():
    asteroids = []
    for y, line in enumerate(read_input_file_data().splitlines()):
        for x, char in enumerate(line):
            if char == '#':
                asteroids.append((x, y))

    LOCATION = (29, 28) # from part 1
    X, Y = LOCATION
    asteroids.remove(LOCATION)

    asteroid_angles = {}
    for (x, y) in asteroids:
        dx = x-X
        dy = y-Y
        angle = math.atan2(dx, -dy) % (2 * math.pi)
        if angle not in asteroid_angles:
            asteroid_angles[angle] = []
        asteroid_angles.get(angle).append((dx, dy))
    
    angles = list(asteroid_angles.keys())
    angles.sort()
    angled_list = [asteroid_angles[angle] for angle in angles]
    for ls in angled_list:
        ls.sort(key=lambda pt: abs(pt[0]) + abs(pt[1]))
    
    n = 200
    ptr = 0
    vaporized = None
    angled_list_size = len(angled_list)
    while n > 0 and angled_list:
        ls = angled_list[ptr]
        vaporized = ls.pop(0)
        n -= 1
        if not ls:
            angled_list.pop(ptr)
            angled_list_size -= 1
        else:
            ptr = (ptr + 1) % angled_list_size
    
    dx, dy = vaporized
    x = X + dx
    y = Y + dy
    return 100 * x + y
    
print(solve_part_2())
